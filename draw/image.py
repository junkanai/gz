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
        super().__init__(xy, iwh, visible=visible, active=active, priority=priority)
        self.__original_image = pygame.image.load(path)
        self.__update()

    def __update(self):
        self.__image = pygame.transform.scale(self.__original_image, (self.w, self.h))

    def draw(self, screen, dx=0, dy=0):
        self._clicked = False
        if not self._updated: self.__update()
        if not self.visible: return
        screen.blit(self.__image, (self.x+dx, self.y+dy))
