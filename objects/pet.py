import pygame.sprite
import json
from libraries.animation import Animations


class Pet:

    def __init__(self, x, y, metadata_path):
        super().__init__()
        self.x = x
        self.y = y
        with open(metadata_path) as f:
            self.meta_data = json.load(f)
        self.animation = Animations(self.meta_data['sprites'], self.x, self.y)
        self.base_health_points = self.meta_data['base_stats'][0]
        self.base_attack = self.meta_data['base_stats'][1]
        self.base_intelligence = self.meta_data['base_stats'][2]
        self.base_defense = self.meta_data['base_stats'][3]
        self.base_speed = self.meta_data['base_stats'][4]
        f.close()
        self.group = pygame.sprite.Group()
        self.group.add(self.animation)
        self.walk_speed = 1
        self.direction = 1
        self.state = "idle"
        self.drag_x = 0
        self.drag_y = 0
        self.hungry = 100
        self.happiness = 100
        self.energy = 100
        self.weight = 5
        self.experience = 0
        self.level = 1
        self.experience = 0
        self.experience_to_level = int(self.level * 100 * 1.25)

    def update(self):
        self.animation.x = self.x
        self.animation.y = self.y
        if self.direction == 1:
            self.animation.direction = "right"
        if self.direction == -1:
            self.animation.direction = "left"
        self.idle()
        self.walk()
        self.eat()
        self.grab()
        self.animation.update()

    def draw(self, screen):
        self.group.draw(screen)

    def change_direction(self):
        self.direction = self.direction * -1

    def walk(self):
        if self.state == "walk":
            screen_width, screen_height = pygame.display.get_window_size()
            if self.x <= 0:
                self.direction = 1
            if self.x >= screen_width - self.animation.width:
                self.direction = -1
            self.x = self.x + self.walk_speed * self.direction
            self.animation.change_state("walk")

    def eat(self):
        if self.state == "eat":
            self.animation.change_state("eat")

    def idle(self):
        if self.state == "idle":
            self.animation.change_state("idle")

    def grab(self):
        if self.state == "grabbed":
            self.animation.change_state("grabbed")
            mouse_x, mouse_y = pygame.mouse.get_pos()
            self.x = mouse_x - self.drag_x

    def is_clicked(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        self.drag_x = mouse_x - self.x
        self.drag_y = mouse_y - self.y
        return pygame.mouse.get_pressed()[0] and self.x <= mouse_x <= self.x + self.animation.width and self.y <= mouse_y <= self.y + self.animation.height
