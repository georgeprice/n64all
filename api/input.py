class Input:

    def __init__(self):
        self._hold_time = 0
        self._active = False

    def get_active(self) -> bool:
        return self._active

    def get_held_time(self) -> int:
        return self._hold_time

    def toggle(self) -> None:
        self._active = not self._active

    def set_active(self, new_active) -> None:
        self._active = new_active

    def set_hold_time(self, new_hold_time) -> None:
        if not isinstance(new_hold_time, int):
            raise TypeError("New hold time needs to be an int dude")
        elif new_hold_time is None:
            raise ValueError("New hold time can't be None you dingus")
        self._hold_time = new_hold_time

    def get_state(self):
        return {'active' : self.get_active()}


class Analog(Input):

    def __init__(self):
        super().__init__()
        self._x, self._y = 0, 0

    def get_x(self) -> int:
        return self._x

    def get_y(self) -> int:
        return self._y

    def set_x(self, x) -> None:
        if not isinstance(x, int):
            raise TypeError("New x needs to be a float dude")
        elif x is None:
            raise ValueError("New x can't be None you dingus")
        elif x < -80:
            raise ValueError("New x is a little boi")
        elif x > 80:
            raise ValueError("New x is a big boi")
        self._x = x

    def set_y(self, y) -> None:
        if not isinstance(y, int):
            raise TypeError("New y needs to be a float dude")
        elif y is None:
            raise ValueError("New y can't be None you dingus")
        elif y < -80:
            raise ValueError("New y is a little boi")
        elif y > 80:
            raise ValueError("New y is a big boi")
        self._y = y

    def get_state(self):
        s = {
            'x': self.get_x(),
            'y': self.get_y()
        }
        s.update(super().get_state())
        return s
