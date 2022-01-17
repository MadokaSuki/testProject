import sys
import pygame
from pygames.alien import Alien
from time import sleep

from bullet import Bullet


# 空格开火
def fire_bullet(ai_settings, screen, ship, bullets, stats):
    new_bullet = Bullet(ai_settings, screen, ship)  # 传入屏幕和飞船位置以确认新的子弹位置
    if len(bullets) < new_bullet.bullet_max:
        bullets.add(new_bullet)
        stats.shoot_times += 1


# 改变速度("," ".")
def change_speed(event, ship):
    if event.key == pygame.K_COMMA:
        if ship.ship_speed_factor <= 2.5:
            ship.ship_speed_factor += 0.5
    if event.key == pygame.K_PERIOD:
        if ship.ship_speed_factor >= 1:
            ship.ship_speed_factor -= 0.5
    # 加减速


# 按下按键
def check_down_events(event, ai_settings, screen, ship, bullets, stats):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_h:
        ship.return_center = True
    # 飞船移动控制（按键检测函数） h回到原位
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets, stats)
        # print(stats.shoot_times)
    elif event.key == pygame.K_ESCAPE:
        sys.exit()
    # 开火函数
    change_speed(event, ship)
    # 改变速度函数


# 抬起按键
def check_up_events(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False
    elif event.key == pygame.K_h:
        ship.return_center = False
    # 飞船移动控制（按键检测函数）


def check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets, sb):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # 按x退出
        elif event.type == pygame.MOUSEBUTTONDOWN:  # 按下鼠标
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, play_button, ship, aliens, bullets, mouse_x, mouse_y, sb)
        elif event.type == pygame.KEYDOWN:  # 按下按键
            check_down_events(event, ai_settings, screen, ship, bullets, stats)
        elif event.type == pygame.KEYUP:  # 松开按键
            check_up_events(event, ai_settings, screen, ship, bullets)


def check_play_button(ai_settings, screen, stats, play_button, ship, aliens, bullets, mouse_x, mouse_y, sb):
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)  # 检查鼠标位置是否在play_button内
    if button_clicked and not stats.game_active:  # 游戏未激活并且点击按钮才启用
        pygame.mouse.set_visible(False)  # 隐藏鼠标
        ai_settings.initialize_dynamic_settings()
        stats.reset_stats()  # 重置最大游玩次数
        stats.game_active = True

        sb.prep_level()  # 重置分数和等级
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_ships()

        aliens.empty()
        bullets.empty()

        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()


def update_screen(ai_settings, screen, stats, aliens, ship, bullets, play_button, sb):
    screen.fill(ai_settings.bg_color)  # 背景颜色填充
    for bullet in bullets:
        bullet.draw_bullet()  # 根据所有子弹的坐标绘制子弹
    ship.blitme()  # 绘制飞船
    aliens.draw(screen)
    sb.show_score()
    if not stats.game_active:
        play_button.draw_button()
    pygame.display.flip()  # 刷新屏幕进行绘制


def update_bullets(ai_settings, screen, ship, aliens, bullets, stats, sb):  # 去除掉屏幕边缘外子弹, 并进行碰撞检测
    bullets.update()  # 继承group中的方法 相当于update每一个元素
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
            update_shoot_accuracy(stats)
            sb.prep_score()
    check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets, stats, sb)


def update_shoot_accuracy(stats):  # 更新准确率
    if stats.shoot_times != 0:
        stats.shoot_accuracy = stats.hit_times / stats.shoot_times * 100
        # print(stats.shoot_accuracy)


def check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets, stats, sb):
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        for aliens in collisions.values():
            stats.hit_times += len(aliens)
            stats.score += ai_settings.alien_points * len(aliens)
            update_shoot_accuracy(stats)
            sb.prep_score()
        # print("%.2f %" % (stats.hit_times / stats.shoot_times * 100))
    check_high_score(stats, sb)
    if len(aliens) == 0:
        bullets.empty()
        # ai_settings.alien_speed_factor += 0.2  # 难度增加机制
        ai_settings.increase_speed()
        stats.level += 1
        sb.prep_level()
        create_fleet(ai_settings, screen, ship, aliens)
    # print(len(bullets))


def check_fleet_edges(ai_settings, aliens):
    for alien in aliens.sprites():
        # print(alien.rect.x, alien.rect.y)
        if alien.check_edges():  # 如果外星人到达边界，则改变方向
            change_fleet_direction(ai_settings, aliens)
            break  # 注意break缩进位置！


def change_fleet_direction(ai_settings, aliens):
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def update_aliens(ai_settings, stats, screen, ship, aliens, bullets, sb):
    check_fleet_edges(ai_settings, aliens)  # 外星人边缘碰撞以改变方向和下移
    aliens.update()  # 平滑移动外星人
    check_ship_collide(ai_settings, stats, screen, ship, aliens, bullets, sb)  # 检测飞船碰撞
    check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets, sb)  # 检测外星人到屏幕底
    # print(stats.ships_left)


def check_ship_collide(ai_settings, stats, screen, ship, aliens, bullets, sb):  # 如果飞船外星人碰撞调用ship_hit函数
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets, sb)
        # print(stats.ships_left)


def create_fleet(ai_settings, screen, ship, aliens):
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)


def get_number_aliens_x(ai_settings, alien_width):
    available_space_x = ai_settings.screen_width - 2 * alien_width  # 可用的最左到最右端外星人间距
    number_aliens_x = int(available_space_x / (2 * alien_width))  # 可容纳外星人数量
    return number_aliens_x


def create_alien(ai_settings, screen, aliens, alien_number, row_number):  # 根据可容纳外星人数量
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = 2 * alien.rect.height + 2 * alien.rect.height * row_number # 初始外星人高度
    aliens.add(alien)


def get_number_rows(ai_settings, ship_height, alien_height):
    available_space_y = (ai_settings.screen_height
                         - 3 * alien_height
                         - ship_height)  # 可用的从上到下外星人间距
    number_rows = int(available_space_y / (2 * alien_height))  # 可容纳外星人行数
    return number_rows


def ship_hit(ai_settings, stats, screen, ship, aliens, bullets, sb):
    if stats.ships_left > 0:
        stats.ships_left -= 1

        sb.prep_ships()

        # 清空屏幕
        aliens.empty()
        bullets.empty()

        create_fleet(ai_settings, screen, ship, aliens)  # 重新创建外星人
        ship.center_ship()  # 飞船重新置中
        sleep(0.5)

    else:  # 把游戏重置成未激活状态
        stats.game_active = False
        pygame.mouse.set_visible(True)


def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets, sb):  # 如果外星人到屏幕底则调用ship_hit函数
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets, sb)
            break


def check_high_score(stats, sb):
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()

