import pygame

from .rect import Rect
from .text import Text
from .image import Image


class Button:
    def __init__(self, x = 0, y = 0, w = 200, h = 50, color = (255, 255, 255)):
        self.rect = Rect(x, y, w, h, color)
        self.text = None
        self.image = None
        self._update()

    def __contains__(self, pos):
        return pos in self.rect

    def _update(self):
        self.rect._update()

    def draw(self, screen):
        self.rect.draw(screen)

    def get_center(self):
        return self.rect.get_center()
