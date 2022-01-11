import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    def __init__(self, ai_settings, screen):
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载外星人图像并设置为rect属性
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # 每个外星人最初都在屏幕左上角附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # x,y 为矩形左上角坐标

        # 存储外星人准确位置
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def blitme(self):
        self.screen.blit(self.image, self.rect)