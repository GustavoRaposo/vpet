import sys
import pygame
from libraries.animation import Animations


class Game:
    def __init__(self, screen_width, screen_height, title, version):
        super().__init__()
        pygame.init()
        pygame.display.set_caption(f"{title} {version}")
        pygame.mouse.set_visible(False)
        self.cursor = pygame.image.load("./assets/cursors/cursor.png")
        self.background = pygame.image.load("./assets/backgrounds/Background.png")
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.current_time = 0
        self.clock = pygame.time.Clock()
        self.running = True
        self.group = pygame.sprite.Group()
        self.animation = Animations("./assets/sprites/B_Morrigan",
                                    self.screen_width / 2, self.screen_height / 2,
                                    2,
                                    "right")
        self.group.add(self.animation)

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.animation.direction = "left"
                if event.key == pygame.K_LSHIFT:
                    self.animation.direction = "right"
                if event.key == pygame.K_q:
                    self.animation.change_state("idle")
                if event.key == pygame.K_w:
                    self.animation.change_state("walk")
                if event.key == pygame.K_e:
                    self.animation.change_state("eat")
                if event.key == pygame.K_r:
                    self.animation.change_state("grabbed")

    def draw(self):
        self.screen.blit(self.background, (0, 0))
        self.group.draw(self.screen)
        self.screen.blit(self.cursor, (pygame.mouse.get_pos()))

    def update(self):
        while self.running:
            self.event()
            self.draw()
            self.group.update()
            pygame.display.update()
            pygame.display.flip()
            self.clock.tick(60)
