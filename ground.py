import pygame
import math


class Ground:
    def __init__(self, y, screen_width) -> None:
        self.sprite = pygame.image.load("grass.png")
        self.rect = pygame.Rect(0, y, screen_width, self.sprite.get_height())

    def render(self, screen:pygame.Surface):
        # I didn't want to scale the image so I do this instead
        for x in range(math.ceil(screen.get_width() / self.sprite.get_width())):
            screen.blit(self.sprite, (x * self.sprite.get_width(), self.rect.top))