import pygame
from .draw.image import Image

def sort_priority(unit): return unit.priority

class Window:
    def __init__(self, caption="gz window", wh=(600, 400), color=(0, 0, 0)):
        pygame.init()
        self.__screen = pygame.display.set_mode(wh)
        pygame.display.set_caption(caption)

        (self.__w, self.__h) = wh
        self.color = color
        self.__working = True
        self.__units = []

    def add(self, unit, priority=None):
        try:
            if not unit._is_GzObject: return
            if priority != None: unit.priority = priority
            self.__units.append(unit)
            self.__units.sort(key=sort_priority)
            self.__units.reverse()
        except AttributeError:
            raise AttributeError("Cannot add this type of object")

    @property
    def update(self):
        if not self.__working: return False
        self.__screen.fill(self.color)

        for unit in self.__units: unit.draw(self.__screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT: return False

            if event.type == pygame.MOUSEBUTTONDOWN:
                for unit in reversed(self.__units):
                    if unit._click_check(event.pos): break

        pygame.display.update()
        return True

    @update.setter
    def update(self, b):
        if b == False:
            self.__working = False
            return
        else:
            raise ValueError

    def __del__(self):
        pygame.quit()

    @property
    def mouse_xy(self):
        return pygame.mouse.get_pos()

    @property
    def on_display(self):
        return pygame.mouse.get_pressed()

    @property
    def w(self): return self.__w

    @property
    def h(self): return self.__h

    @property
    def wh(self): return (self.__w, self.__h)

    @property
    def xc(self): return self.__w//2

    @property
    def yc(self): return self.__h//2

    @property
    def xyc(self): return (self.__w//2, self.__h//2)
