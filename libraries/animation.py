import pygame


class Animations(pygame.sprite.Sprite):
    def __init__(self, paths, x, y):
        super().__init__()
        self.idle = [pygame.image.load(path) for path in paths[0]]
        self.walk = [pygame.image.load(path) for path in paths[1]]
        self.grabbed = [pygame.image.load(path) for path in paths[2]]
        self.eat = [pygame.image.load(path) for path in paths[3]]
        self.speed = 0.15
        self.scale = 2
        self.direction = "right"
        self.current_sate = self.idle
        self.current_frame = 0
        self.image = self.current_sate[self.current_frame]
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.topleft = [self.x, self.y]
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def update(self):
        self.current_frame += self.speed
        if self.current_frame >= len(self.current_sate):
            self.current_frame = 0
        self.image = self.current_sate[int(self.current_frame)]
        self.image = pygame.transform.scale(self.image,
                                            (self.width * self.scale,
                                             self.height * self.scale))
        if self.direction == "right":
            self.image = pygame.transform.flip(self.image, flip_x=True, flip_y=False)
        if self.direction == "left":
            self.image = pygame.transform.flip(self.image, flip_x=False, flip_y=False)
        self.rect.center = [self.x, self.y]

    def change_state(self, state):
        if state == "idle":
            self.current_sate = self.idle
            self.speed = 0.15
        if state == "walk":
            self.current_sate = self.walk
            self.speed = 0.1
        if state == "eat":
            self.current_sate = self.eat
            self.speed = 0.1
        if state == "grabbed":
            self.current_sate = self.grabbed
            self.speed = 0.1
