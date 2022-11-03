class Settings:
    """"Класс для хранения всех настроек игры Alien Invasion."""

    def __init__(self):
        """Инициализирует статические настройки игры."""
        # Параметры экрана
        self.screen_width = 1000
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Настройка корабля
        self.ship_limit = 0

        # Параметры снаряда
        self.bullet_width = 600
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 5

        # Настройки пришельцев
        self.fleet_drop_speed = 15

        # Темп ускорения игры
        self.speedcup_scale = 2

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self, ship_speed=4.0, bullet_speed=6.0, alien_speed=1.75):
        """Инициализирует настройки, изменяющиеся в ходе игры."""
        self.ship_speed = ship_speed
        self.bullet_speed = bullet_speed
        self.alien_speed = alien_speed
        self.fleet_direction = 1  # 1 - движение вправо, -1 - влево

    def increase_speed(self):
        """Увеличение настройки скорости."""
        self.ship_speed *= self.speedcup_scale
        self.bullet_speed *= self.speedcup_scale
        self.alien_speed *= self.speedcup_scale
