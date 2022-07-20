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

    def _update(self, dx, dy):
        for unit in self.__units:
            unit._dxy(dx, dy)
            unit._update()

    def __add__(self, *units):
        try:
            if type(units[0]) is tuple or type(units[0]) is list:
                for unit in units[0]:
                    if not unit._is_GzObject: return
                    self.__units.append(unit)
                    self.__units.sort(key=sort_priority)
                    self.__units.reverse()
            else:
                if not units[0]._is_GzObject: return
                self.__units.append(units[0])
                self.__units.sort(key=sort_priority)
                self.__units.reverse()
        except AttributeError:
            raise AttributeError("Cannot add this type of object")
        return self

    def __sub__(self, *units):
        if type(units[0]) is tuple or type(units[0]) is list:
            for unit in units[0]:
                for i in range(len(self.__units)):
                    if self.__units[i] is unit:
                        self.__units[i]._clicked = False
                        self.__units.pop(i)
                        break
        else:
            for i in range(len(self.__units)):
                if self.__units[i] is units[0]:
                    self.__units[i]._clicked = False
                    self.__units.pop(i)
                    break
        return self

    """
    def draw(self, screen):
        for key, value in self.__dict__.items():
            if key.startswith("_Window__"): continue
            print(key, value)
    """
