import pygame
from .gzobject import GzObject

class Image(GzObject):
    def __init__(self, path,
                 xy=(0, 0),
                 wh=(150, 150),
                 scale=1,
                 visible=True,
                 active=False,
                 priority=90):
        iwh = (int(wh[0] * scale), int(wh[1] * scale))
        super().__init__(xy, iwh, (0, 0), 1, visible, active, priority)
        self.__path = path
        self.__original_image = pygame.image.load(path)
        self._update()

    def copy(self):
        return Image(self.__path, self.xy, self.wh, 1,
                     self.visible, self.active, self.priority)

    def _update(self):
        self.__image = pygame.transform.scale(self.__original_image, (self.w, self.h))

    def draw(self, screen):
        self._clicked = False
        if not self._updated: self._update()
        if not self.visible: return
        screen.blit(self.__image, (self.x+self._dx, self.y+self._dy))
