import pygame
from .gzobject import GzObject

class Rect(GzObject):
    def __init__(self,
                 xy=(0, 0),
                 wh=(200, 100),
                 color=(100, 100, 100),
                 visible=True,
                 active=False,
                 priority=90):
        super().__init__(xy, wh, (0, 0), 1, visible, active, priority)
        self.color = color
        self._update()

    def copy(self):
        return Rect(self.xy, self.wh, self.color,
                    self.visible, self.active, self.priority)

    def _update(self):
        self.__rect = pygame.Rect(self.x+self._dx, self.y+self._dy, self.w, self.h)

    def draw(self, screen):
        self._clicked = False
        if not self._updated: self._update()
        if not self.visible: return
        pygame.draw.rect(screen, self.color, self.__rect)
