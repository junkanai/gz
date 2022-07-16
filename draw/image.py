import pygame
from .gzobject import GzObject

class Image(GzObject):
    def __init__(self, path, size=(150, 150), priority=90):
        super().__init__(w=size[0], h=size[1], priority=priority)
        self.__original_image = pygame.image.load(path)
        self.__update()

    def __update(self):
        self.__image = pygame.transform.scale(self.__original_image, (self.w, self.h))
        self._updated = True


    def draw(self, screen, dx=0, dy=0):
        if not self._updated: self.__update()
        if not self.visible: return
        screen.blit(self.__image, (self.x+dx, self.y+dy))
