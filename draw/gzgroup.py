def sort_priority(unit): return unit.priority

class GzGroup:
    def __init__(self):
        self.__units = []

    def draw(self, screen):
        for unit in self.__units:
            unit.draw(screen)

    def _click_check(self, pos):
        for unit in reversed(self.__units):
            if unit._click_check(pos):
                return True
        else:
            return False

    def _update(self):
        for unit in self.__units:
            unit._dxy(self.x, self.y)
            unit._update()

    def __add__(self, unit):
        try:
            if not unit._is_GzObject: return
            self.__units.append(unit)
            self.__units.sort(key=sort_priority)
            self.__units.reverse()
        except AttributeError:
            raise AttributeError("Cannot add this type of object")
        return self

    def __sub__(self, unit):
        for i in range(len(self.__units)):
            if self.__units[i] is unit:
                self.__units[i]._clicked = False
                self.__units.pop(i)
                return self
        return self
