import pygame


class Ship():

    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        # 初始化飞船图片
        self.screen_rect = screen.get_rect()
        self.ship_speed_factor = ai_settings.ship_speed_factor
        # 获得屏幕位置

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        self.return_center = False
        # 设置飞船自身的位置

        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)
        self.bottom = float(self.rect.bottom)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        # 触及边缘停止移动
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.centerx -= self.ship_speed_factor
        if self.moving_up and self.rect.top > 0:
            self.centery -= self.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.ship_speed_factor
        if self.return_center:
            self.centerx = self.screen_rect.centerx
            self.centery = self.screen_rect.bottom - self.rect.height / 2
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

    def center_ship(self):
        self.centerx = self.screen_rect.centerx
        self.centery = self.screen_rect.bottom - self.rect.height / 2



