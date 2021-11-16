import sys

import pygame


class GameState:
    def __init__(self):
        super().__init__()
        self.state = 'intro'
        self.clock = pygame.time.Clock()

    def intro(self, screen):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.state = 'main'
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        screen.fill(000)
        screen.blit(pygame.image.load("./assets/cursors/cursor.png"), (pygame.mouse.get_pos()))
        pygame.display.update()
        pygame.display.flip()
        self.clock.tick(60)

    def main(self, screen, pet):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pet.is_clicked():
                    pet.state = "grabbed"
            if event.type == pygame.MOUSEBUTTONUP:
                if pet.state == "grabbed":
                    pet.state = "idle"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_SPACE:
                    pet.direction = 1
                if event.key == pygame.K_LSHIFT:
                    pet.direction = -1
                if event.key == pygame.K_q:
                    pet.state = "idle"
                if event.key == pygame.K_w:
                    pet.state = "walk"
                if event.key == pygame.K_e:
                    pet.state = "eat"
                if event.key == pygame.K_r:
                    pet.state = "grabbed"

        screen.blit(pygame.image.load("./assets/backgrounds/Background.png"), (0, 0))
        pet.draw(screen)
        screen.blit(pygame.image.load("./assets/cursors/cursor.png"), (pygame.mouse.get_pos()))
        pet.update()
        pygame.display.update()
        pygame.display.flip()
        self.clock.tick(60)

    def state_manager(self, screen, pet):
        if self.state == "intro":
            self.intro(screen)
        if self.state == "main":
            self.main(screen, pet)
