import pygame


class Animations(pygame.sprite.Sprite):
    def __init__(self, path, x, y, scale, direction):
        super().__init__()
        self.idle = [pygame.image.load(f"{path}/idle_1.png"),
                     pygame.image.load(f"{path}/idle_2.png"),
                     pygame.image.load(f"{path}/idle_3.png"),
                     pygame.image.load(f"{path}/idle_2.png"),
                     pygame.image.load(f"{path}/idle_4.png"),
                     pygame.image.load(f"{path}/idle_5.png"),
                     pygame.image.load(f"{path}/idle_6.png"),
                     pygame.image.load(f"{path}/idle_7.png")]
        self.walk = [pygame.image.load(f"{path}/walk_1.png"),
                     pygame.image.load(f"{path}/walk_2.png"),
                     pygame.image.load(f"{path}/walk_3.png"),
                     pygame.image.load(f"{path}/walk_2.png")]
        self.grabbed = [pygame.image.load(f"{path}/grab_1.png"),
                        pygame.image.load(f"{path}/grab_2.png"),
                        pygame.image.load(f"{path}/grab_3.png")]
        self.eat = [pygame.image.load(f"{path}/eat_1.png"),
                    pygame.image.load(f"{path}/eat_2.png"),
                    pygame.image.load(f"{path}/eat_3.png")]
        self.speed = 0.15
        self.scale = scale
        self.direction = direction
        self.current_sate = self.idle
        self.current_frame = 0
        self.image = self.current_sate[self.current_frame]
        self.rect = self.image.get_rect()
        self.rect.topleft = [x, y]

    def update(self):
        self.current_frame += self.speed
        if self.current_frame >= len(self.current_sate):
            self.current_frame = 0
        self.image = self.current_sate[int(self.current_frame)]
        self.image = pygame.transform.scale(self.image,
                                            (self.image.get_width() * self.scale,
                                             self.image.get_height() * self.scale))
        if self.direction == "right":
            self.image = pygame.transform.flip(self.image, flip_x=True, flip_y=False)
        if self.direction == "left":
            self.image = pygame.transform.flip(self.image, flip_x=False, flip_y=False)

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
