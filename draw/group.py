import pygame
from .gzobject import GzObject
from .gzgroup import GzGroup

class Group(GzObject, GzGroup):
    def __init__(self,
                 xy=(0, 0),
                 visible=True,
                 active=False,
                 priority=90):
        GzObject.__init__(self, xy, (100, 100), (0, 0), 1, visible, active, priority)
        GzGroup.__init__(self)

    def _click_check(self, pos):
        return GzGroup._click_check(self, pos)

    def draw(self, screen, dx=0, dy=0):
        if not self._updated:
            GzGroup._update(self)
        GzGroup.draw(self, screen)
