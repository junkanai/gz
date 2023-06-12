import pygame


class Rect:
    def __init__(self, x, y, w, h, color):
        self.x, self.y, self.w, self.h, self.color = x, y, w, h, color
        self.is_visible = True

    def __contains__(self, pos):
        if not (self.x < pos[0] <= self.x + self.w): return False
        if not (self.y < pos[1] <= self.y + self.h): return False
        return True

    def _update(self):
        self.__rect = pygame.Rect(self.x, self.y, self.w, self.h)

    def draw(self, screen):
        pygame.draw.rect(screen.surface, self.color, self.__rect)

    def get_center(self):
        return (self.x + self.w // 2, self.y + self.h // 2)

    def set_position(self, *pos):
        self.x = pos[0]
        self.y = pos[1]
        self._update()

    def set_size(self, *size):
        self.w = size[0]
        self.h = size[1]
        self._udpate()


