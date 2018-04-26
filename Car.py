import pygame
from Shared import BLACK, RED, WINDOW_WIDTH, WINDOW_HIEGHT

class Car:
    def __init__(self, x=0, y=0, dx=4, dy=0, car_width=30, car_height=30, color=RED):
        self.image = ""
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.width = car_width
        self.height = car_height
        self.color = color

    def load_image(self, img):
        self.image = pygame.image.load(img).convert()
        self.image.set_colorkey(BLACK)

    def draw_image(self, window):
        window.blit(self.image, [self.x, self.y])

    def move_x(self):
        self.x += self.dx

    def move_y(self):
        self.y += self.dy

    # def draw_rect(self):
    #     pygame.draw.rect(screen, self.color, [self.x, self.y, self.width, self.height], 0)

    def check_out_of_window(self):
        if self.x + self.width > WINDOW_WIDTH or self.x < 0:
            self.x -= self.dx
        if self.y + self.height > WINDOW_HIEGHT or self.y < 0:
            self.y -= self.dy
