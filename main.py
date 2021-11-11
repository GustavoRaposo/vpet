import pygame

from objects.pet import Pet

pygame.init()

display = pygame.display.set_mode([480, 640])
pygame.display.set_caption("Vpet 0.0.0")

player = Pet(0, 0, 64, 64)

gameLoop = True

if __name__ == '__main__':

    while gameLoop:
        pygame.display.update()