class Settings():

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.fleet_drop_speed = 10
        self.ship_limit = 3
        self.speed_up_scale = 1.1
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.alien_speed_factor = 0.5
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.fleet_direction = 1

    def increase_speed(self):
        self.ship_speed_factor *= self.speed_up_scale
        self.bullet_speed_factor *= self.speed_up_scale
        self.alien_speed_factor *= self.speed_up_scale


