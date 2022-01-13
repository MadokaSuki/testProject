import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(self, ai_settings, screen, ship):
        super().__init__()
        self.ai_settings = ai_settings
        self.bullet_height = 15
        self.bullet_width = 300
        self.bullet_color = 60, 60, 60
        self.bullet_max = 5
        self.screen = screen
        self.speed_factor = ai_settings.bullet_speed_factor

        self.rect = pygame.Rect(0, 0, self.bullet_width, self.bullet_height) # 设置子弹的矩形形状
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.y = float(self.rect.y)  # 浮点化使其更精确

    def update(self):
        self.y -= self.speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.bullet_color, self.rect)
