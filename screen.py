import pygame

class Screen:
    def __init__(self, size = (1600, 900), c = (0, 0, 0), caption = "gz screen"):
        pygame.init()
        self.surface = pygame.display.set_mode(size)
        pygame.display.set_caption(caption)
        self.c = c
        self.working = True

    def draw(self):
        if self.working:
            self.surface.fill(self.c)
            return True
        return False

    def update(self):
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.working = False
                return
            event.clicked = event.type == pygame.MOUSEBUTTONDOWN
            yield event
