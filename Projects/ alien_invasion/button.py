import pygame.font


flag_difficulty_game = 0  # 1 - difficult set/ 0 - difficulty unset


class ButtonStart:
    def __init__(self, surface, main_rect, ai):
        """Инициализирует кнопку старта игры."""
        self.ai = ai
        self.stats = ai.stats
        self.settings = ai.settings

        self.screen = surface
        self.screen_rect = main_rect

        self.width, self.height = 170, 60
        self.button_color = 'GREY'
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont('Comic Sans MS', 40)

        self.rect = pygame.Rect(0, 0, self.width, self.height)

        self.rect.midtop = self.screen_rect.midtop
        self.rect.y += 25

        self._button_create()

    def _button_create(self):
        """Преобразует msg в прямоугольник и выравнивает текст по центру."""
        self.msg_image = self.font.render('Start', True, self.text_color,
                                          self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def button_func(self):
        global flag_difficulty_game
        if not flag_difficulty_game:
            self.settings.initialize_dynamic_settings()
        flag_difficulty_game = False
        self.ai._start_game()

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)


class ButtonEasy(ButtonStart):
    """Инициализирует кнопку выбора легкой сложности игры."""
    def __init__(self, surface, main_rect, ai):
        super().__init__(surface, main_rect, ai)
        self.width, self.height = 160, 50
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.button_color = 'GREEN'
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont('Comic Sans MS', 30)

        self.rect.bottomleft = self.screen_rect.bottomleft
        self.rect.x += 15
        self.rect.y -= 20

        self._button_create()

    def _button_create(self):
        super()._button_create()
        self.msg_image = self.font.render('Easy', True, self.text_color,
                                          self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def button_func(self):
        global flag_difficulty_game
        flag_difficulty_game = True
        self.settings.initialize_dynamic_settings(ship_speed=5,
                                                  bullet_speed=8.0,
                                                  alien_speed=0.6)


class ButtonMedium(ButtonEasy):
    """Инициализирует кнопку выбора средней сложности игры."""
    def __init__(self, surface, main_rect, ai):
        super().__init__(surface, main_rect, ai)
        self.button_color = (232, 192, 12)

        self.rect.midbottom = self.screen_rect.midbottom
        self.rect.y -= 20

        self._button_create()

    def _button_create(self):
        super()._button_create()
        self.msg_image = self.font.render('Medium', True, self.text_color,
                                          self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def button_func(self):
        global flag_difficulty_game
        flag_difficulty_game = True
        self.settings.initialize_dynamic_settings(ship_speed=4.0,
                                                  bullet_speed=6.0,
                                                  alien_speed=1)


class ButtonHard(ButtonEasy):
    """Инициализирует кнопку выбора высокой сложности игры."""
    def __init__(self, surface, main_rect, ai):
        super().__init__(surface, main_rect, ai)
        self.button_color = 'RED'

        self.rect.bottomright = main_rect.bottomright
        self.rect.x -= 15
        self.rect.y -= 20

        self._button_create()

    def _button_create(self):
        super()._button_create()
        self.msg_image = self.font.render('Hard', True, self.text_color,
                                          self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def button_func(self):
        global flag_difficulty_game
        flag_difficulty_game = True
        self.settings.initialize_dynamic_settings(ship_speed=2.0,
                                                  bullet_speed=3.0,
                                                  alien_speed=1.5)


class GameMenu:
    """Инициализирует игровое меню."""
    def __init__(self, ai_game):
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.width, self.height = 600, 170
        self.button_color = 'BLACK'

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        self._button_initialization()

    def show_menu(self):
        self.screen.fill(self.button_color, self.rect)
        self.button_start.draw_button()
        self.button_easy.draw_button()
        self.button_medium.draw_button()
        self.button_hard.draw_button()

    def _button_initialization(self):
        def check_collide(obj, obj_predicate):
            def set_point(mouse_pos):
                if obj.collidepoint(mouse_pos):
                    obj_predicate()
                else:
                    return None
            return set_point
        ai_game = self.ai_game
        self.button_start = ButtonStart(self.screen, self.rect, ai_game)
        self.button_easy = ButtonEasy(self.screen, self.rect, ai_game)
        self.button_medium = ButtonMedium(self.screen, self.rect, ai_game)
        self.button_hard = ButtonHard(self.screen, self.rect, ai_game)
        self.button_action = [
            check_collide(self.button_start.rect, self.button_start.button_func),
            check_collide(self.button_easy.rect, self.button_easy.button_func),
            check_collide(self.button_medium.rect, self.button_medium.button_func),
            check_collide(self.button_hard.rect, self.button_hard.button_func)
        ]
