import pygame

class Window:
    def __init__(self, caption="gz window", size=(600, 400), color=(0, 0, 0)):
        pygame.init()
        self.__screen = pygame.display.set_mode(size)
        pygame.display.set_caption(caption)

        self.__h = size[1]
        self.__w = size[0]
        self.color = color
        self.__working = True
        self.__units = []

    def add(self, unit, priority=None):
        if priority != None: unit.priority = priority

        self.__units.append(unit)
    
    @property
    def w(self): return self.__w

    @property
    def h(self): return self.__h

    @property
    def update(self):
        if not self.__working: return False
        self.__screen.fill(self.color)

        for unit in self.__units: unit.draw(self.__screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT: return False

            if event.type == pygame.MOUSEBUTTONDOWN:
                for unit in reversed(self.__units):
                    if unit._press_check(event.pos): break

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
    
