from config.config import Config
import random


class Position:
    def __init__(self):
        self._x: int = self._generate_ramdom_x()
        self._y: int = self._generate_ramdom_y()

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value

    def _generate_ramdom_x(self) -> int:
        max_size = Config.get_settings('world.size.x_axis')
        return self.generate_ramdom_n(max_size)

    def _generate_ramdom_y(self) -> int:
        max_size = Config.get_settings('world.size.y_axis')
        return self.generate_ramdom_n(max_size)

    def move_random(self) -> None:
        x = -1
        y = -1

        while (x < 1 or y < 1) or (x > Config.get_settings('world.size.x_axis') or y > Config.get_settings('world.size.y_axis')):
            x_move = random.choice([-1, 0, 1])
            y_move = random.choice([-1, 0, 1])
            x = self.x + x_move
            y = self.y + y_move

        self.x = x
        self.y = y

    @staticmethod
    def generate_ramdom_n(max_size: int) -> int:
        return random.randint(1, max_size + 1)
