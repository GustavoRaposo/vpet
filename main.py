import pygame

from objects.game import Game

game = Game(480, 640, "Vpet", "0.0.0")

if __name__ == '__main__':
    game.update()
