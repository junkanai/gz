import pygame
from .draw.gzgroup import GzGroup


class Window(GzGroup):
    def __init__(self, caption="gz window", wh=(600, 400), color=(0, 0, 0)):
        pygame.init()
        self.__screen = pygame.display.set_mode(wh)
        pygame.display.set_caption(caption)

        super().__init__()

        (self.__w, self.__h) = wh
        self.color = color
        self.__working = True

    @property
    def update(self):
        if not self.__working: return False
        self.__screen.fill(self.color)

        self.draw(self.__screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT: return False

            if event.type == pygame.MOUSEBUTTONDOWN:
                self._click_check(event.pos)

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

    @property
    def x(self): return pygame.mouse.get_pos()[0]

    @property
    def y(self): return pygame.mouse.get_pos()[1]

    @property
    def xy(self): return pygame.mouse.get_pos()

