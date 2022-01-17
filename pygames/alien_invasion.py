import pygame
from game_stats import GameStats
from settings import Settings
from ship import Ship
from pygame.sprite import Group
import game_functions as gf
from button import Button
from scoreboard import Scoreboard


def run_game():
    pygame.init()  # 初始化
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,
                                      ai_settings.screen_height))  # 设置屏幕大小
    pygame.display.set_caption("Alien Invasion")  # 设置标题
    play_button = Button(ai_settings, screen, 'Play')

    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    ship = Ship(ai_settings, screen)  # 创建飞船
    bullets = Group()  # 创建一个空的bullets组
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)  # 创建多行外星人
    # alien = Alien(ai_settings, screen)
    while True:  # 进入游戏循环
        gf.check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets, sb)  # 通过按键控制飞船和子弹发射

        if stats.game_active:
            ship.update()  # 更新飞船位置
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets, stats, sb)  # 更新子弹位置 并附加上限条件
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets, sb)
        gf.update_screen(ai_settings, screen, stats, aliens, ship, bullets, play_button, sb)  # 把飞船和子弹在屏幕上画出来


# 总体逻辑：先创建飞船和子弹本体（存在初始位置），
# 进入循环，
# 根据按键改变飞船的位置和子弹开火的创建（add新的子弹进入bullets列表，子弹的起始位置为飞船的当前位置），
# （根据按键的True False判定）更新飞船的位置，
# 遍历子弹列表的位置并且一直追踪到离开屏幕为止，
# 把子弹和飞船根据当前位置绘画显示出来
run_game()

