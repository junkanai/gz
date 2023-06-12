import pygame


class Text:
    def __init__(self, text, color, size, font, bold):
        self.text = text
        self.color = color
        self.size = size
        self.font = font
        self.bold = bold
        self.is_visible = True

    def _update(self):
        pass

    def draw(self, screen):
        pass
