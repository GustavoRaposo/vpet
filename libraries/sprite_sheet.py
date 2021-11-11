import pygame


class SpriteSheet:
    def __init__(self, sprite_sheet_image, width, height):
        super().__init__()
        self.sprite_sheet_image = sprite_sheet_image
        self.width = width
        self.height = height
