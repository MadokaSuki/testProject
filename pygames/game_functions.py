import sys
import pygame
from pygames.alien import Alien

from bullet import Bullet


# 空格开火
def fire_bullet(ai_settings, screen, ship, bullets):
    new_bullet = Bullet(ai_settings, screen, ship)  # 传入屏幕和飞船位置以确认新的子弹位置
    if len(bullets) < new_bullet.bullet_max:
        bullets.add(new_bullet)


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
def check_down_events(event, ai_settings, screen, ship, bullets):
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
        fire_bullet(ai_settings, screen, ship, bullets)
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


def check_events(ai_settings, screen, ship, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # 按x退出
        elif event.type == pygame.KEYDOWN:  # 按下按键
            check_down_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:  # 松开按键
            check_up_events(event, ai_settings, screen, ship, bullets)


def update_screen(ai_settings, screen, aliens, ship, bullets):
    screen.fill(ai_settings.bg_color)  # 背景颜色填充
    for bullet in bullets:
        bullet.draw_bullet()  # 根据所有子弹的坐标绘制子弹
    ship.blitme()  # 绘制飞船
    aliens.draw(screen)
    pygame.display.flip()  # 刷新屏幕进行绘制


def update_bullets(bullets):  # 去除掉屏幕边缘外子弹
    bullets.update()  # 继承group中的方法 相当于update每一个元素
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    print(len(bullets))


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
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def get_number_rows(ai_settings, ship_height, alien_height):
    available_space_y = (ai_settings.screen_height
                         - 3 * alien_height
                         - ship_height)  # 可用的从上到下外星人间距
    number_rows = int(available_space_y / (2 * alien_height))  # 可容纳外星人行数
    return number_rows

