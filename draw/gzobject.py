import pygame


class GzObject:
    def __init__(self, x=0, y=0, w=100, h=100, visible=True, priority=90):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.visible = visible
        self.priority = priority

    @property
    def xc(self):
        return self.x + self.w//2

    @xc.setter
    def xc(self, n):
        self.x = n - self.w//2

    @property
    def yc(self):
        return self.y + self.h//2

    @yc.setter
    def yc(self, n):
        self.y = n - self.h//2
