import sys
import pygame

from objects.game_state import GameState
from objects.pet import Pet


class Game:
    def __init__(self, screen_width, screen_height, title, version):
        super().__init__()
        pygame.init()
        pygame.display.set_caption(f"{title} {version}")
        pygame.mouse.set_visible(False)
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.pet = Pet(self.screen_width / 2, self.screen_height / 2, "#000")
        self.game_state = GameState()

    def update(self):
        while True:
            self.game_state.state_manager(self.screen, self.pet)
