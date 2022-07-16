import pygame


class GzObject:
    def __init__(self, x=0, y=0, w=100, h=100, visible=True, active=False, priority=90):
        self.__x = x
        self.__y = y
        self.__w = w
        self.__h = h
        self.__visible = visible    # draw or not
        self.__active = active      # can press or not
        self.__priority = priority
        self.__active = 
        self._updated = True


    def _press_check(self, pos):
        if not self.active: return False
        if not self.__x < pos[0] <= self.__x + self.__w: return False
        if not self.__y < pos[1] <= self.__y + self.__h: return False
        return True

    @property
    def x(self): return self.__x

    @x.setter
    def x(self, n):
        self.__x = n
        self._updated = False

    @property
    def y(self): return self.__y

    @y.setter
    def y(self, n):
        self.__y = n
        self._updated = False

    @property
    def w(self): return self.__w

    @w.setter
    def w(self, n):
        self.__w = n
        self._updated = False

    @property
    def h(self): return self.__h

    @h.setter
    def h(self, n):
        self.__h = n
        self._updated = False

    @property
    def visible(self): return self.__visible

    @visible.setter
    def visible(self, n):
        self.__visible = n
        self._updated = False

    @property
    def priority(self): return self.__priority

    @priority.setter
    def priority(self, n):
        self.__priority = n
        self._updated = False

    @property
    def xc(self): return self.x + self.w//2

    @xc.setter
    def xc(self, n):
        self.x = n - self.w//2
        self._updated = False

    @property
    def yc(self): return self.y + self.h//2

    @yc.setter
    def yc(self, n):
        self.y = n - self.h//2
        self._updated = False
