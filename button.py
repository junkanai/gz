import pygame

class Rect:
    def __init__(self, x, y, w, h, color):
        self.x, self.y, self.w, self.h, self.color = x, y, w, h, color
        self.is_visible = True

class Text:
    def __init__(self, text, color, size, font, bold):
        self.text = text
        self.color = color
        self.size = size
        self.font = font
        self.bold = bold
        self.is_visible = True

class Image:
    def __init__(self, path, size):
        self.image = path
        self.size = size

class Button:
    def __init__(self, x = 0, y = 0, w = 200, h = 50, color = (255, 255, 255)):
        self.rect = Rect(x, y, w, h, color)
        self.text = None
        self.image = None
        self.__update()

    def __contains__(self, pos):
        if not (self.rect.x < pos[0] <= self.rect.x + self.rect.w): return False
        if not (self.rect.y < pos[1] <= self.rect.y + self.rect.h): return False
        return True

    def __update(self):
        self.__rect = pygame.Rect(self.rect.x, self.rect.y, self.rect.w, self.rect.h)

    def draw(self, screen):
        pygame.draw.rect(screen.surface, self.rect.color, self.__rect)

