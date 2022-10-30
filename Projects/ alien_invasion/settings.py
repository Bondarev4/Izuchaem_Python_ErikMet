class Settings:
    """"Класс для хранения всех настроек игры Alien Invasion."""

    def __init__(self):
        """Инициализирует настройки игры."""
        # Параметры экрана
        self.screen_width = 1000
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Настройка корабля
        self.ship_speed = 1.5
        self.ship_limit = 1

        # Параметры снаряда
        self.bullet_speed = 2
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 5

        # Настройки пришельцев
        self.alien_speed = 10.0
        self.fleet_drop_speed = 5
        self.fleet_direction = 1  # 1 - движение вправо, -1 - влево
