import pygame


class GzObject:
    def __init__(self, xy, wh, dxy, scale, visible, active, priority):
        (self.__x, self.__y) = xy
        (self.__w, self.__h) = wh
        (self._dx, self._dy) = dxy
        self.__scale = scale
        self.__visible = visible    # draw or not
        self.__active = active      # can press or not
        self.__priority = priority

        self._clicked= False
        self._updated = True

    def _click_check(self, pos):
        self._clicked = False
        if not self.__active: return False
        if not (self.__x + self._dx < pos[0]): return False
        if not (pos[0] <= self.__x + self._dx + self.__w): return False
        if not (self.__y + self._dy < pos[1]): return False
        if not (pos[1] <= self.__y + self._dy + self.__h): return False
        self._clicked = True
        return True

    def scale(self, rate):
        if rate < 0: rate = 0
        self.__w = int(self.__w * rate)
        self.__h = int(self.__h * rate)
        self._updated = False

    def _dxy(self, dx, dy):
        self._dx = dx
        self._dy = dy
        self._updated = False

    @property
    def clicked(self): return self._clicked

    @property
    def touched(self):
        if not self.__active: return False
        pos = pygame.mouse.get_pos()
        if not (self.__x + self._dx < pos[0]): return False
        if not (pos[0] <= self.__x + self._dx + self.__w): return False
        if not (self.__y + self._dy < pos[1]): return False
        if not (pos[1] <= self.__y + self._dy + self.__h): return False
        return True

    @property
    def x(self): return self.__x

    @x.setter
    def x(self, n):
        if n < 0: n = 0
        self.__x = n
        self._updated = False

    @property
    def y(self): return self.__y

    @y.setter
    def y(self, n):
        if n < 0: n = 0
        self.__y = n
        self._updated = False

    @property
    def xy(self): return (self.__x, self.__h)

    @xy.setter
    def xy(self, n):
        self.x = n[0]
        self.y = n[1]
        self._updated = False

    @property
    def w(self): return self.__w

    @w.setter
    def w(self, n):
        if n < 0: n = 0
        self.__w = n
        self._updated = False

    @property
    def h(self): return self.__h

    @h.setter
    def h(self, n):
        if n < 0: n = 0
        self.__h = n
        self._updated = False

    @property
    def wh(self): return (self.__w, self.__h)

    @wh.setter
    def wh(self, n):
        self.w = n[0]
        self.h = n[1]
        self._updated = False

    @property
    def visible(self): return self.__visible

    @visible.setter
    def visible(self, n):
        self.__visible = n
        self._updated = False

    @property
    def active(self): return self.__active

    @active.setter
    def active(self, n):
        self.__active = n
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

    @property
    def xyc(self): return (self.xc, self.yc)

    @xyc.setter
    def xyc(self, n):
        self.xc = n[0]
        self.yc = n[1]

    @property
    def _is_GzObject(self): return True
