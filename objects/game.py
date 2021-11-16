import sys
import pygame
from objects.pet import Pet


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
        self.pet = Pet(self.screen_width / 2, self.screen_height / 2,
                       "./meta/B_Morrigan_meta.json")

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.pet.is_clicked():
                    self.pet.state = "grabbed"
            if event.type == pygame.MOUSEBUTTONUP:
                if self.pet.state == "grabbed":
                    self.pet.state = "idle"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_SPACE:
                    self.pet.direction = 1
                if event.key == pygame.K_LSHIFT:
                    self.pet.direction = -1
                if event.key == pygame.K_q:
                    self.pet.state = "idle"
                if event.key == pygame.K_w:
                    self.pet.state = "walk"
                if event.key == pygame.K_e:
                    self.pet.state = "eat"
                if event.key == pygame.K_r:
                    self.pet.state = "grabbed"

    def draw(self):
        self.screen.blit(self.background, (0, 0))
        self.pet.draw(self.screen)
        self.screen.blit(self.cursor, (pygame.mouse.get_pos()))

    def update(self):
        while self.running:
            self.event()
            self.draw()
            self.pet.update()
            pygame.display.update()
            pygame.display.flip()
            self.clock.tick(60)
