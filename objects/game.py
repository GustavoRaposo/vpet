import sys

import pygame


class Game:
    def __init__(self, screen_width, screen_height, title, version):
        super().__init__()
        pygame.init()
        pygame.display.set_caption(f"{title} {version}")
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.current_time = 0
        self.clock = pygame.time.Clock()
        self.running = True

    def update(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()

            self.current_time = pygame.time.get_ticks()
            self.clock.tick(60)
