from config.config import Config
from objects.position import Position
import copy
import uuid


def _set_life_length() -> int:
    return Config.get_settings('organism.life_length_start')


class Organism:
    def __init__(self):
        self._id: uuid = self.generate_id()
        self._position: Position = self.generate_position()
        self._previous_position: Position = None
        self._life_length: int = _set_life_length()
        self._age: int = 0
        self._should_be_killed: bool = False

    def __str__(self):
        return f'Id: {self.id}'

    def move_random(self) -> None:
        self._previous_position = copy.deepcopy(self._position)
        self._position.move_random()

    @staticmethod
    def new_position_attempts() -> int:
        for i in range(10):
            yield i

    @property
    def id(self) -> uuid:
        return self._id

    @property
    def position(self) -> Position:
        return self._position

    @property
    def life_length(self) -> int:
        return self._life_length

    @property
    def should_be_killed (self) -> bool:
        return self._should_be_killed

    @staticmethod
    def generate_id() -> uuid:
        return uuid.uuid4()

    @staticmethod
    def generate_position() -> Position:
        return Position()

    def update(self) -> None:
        """
        Each cycle iteration organism properties are updated. Properties like age, position etc.
        :return: None
        """
        self._update_age()
        self.move_random()

    def _update_age(self) -> None:
        """
        Function updates the age and kills the organism when it's higher or equal life length
        :return:
        """
        self._age += 1

        if self._age >= self._life_length:
            self._kill()

    def _kill(self) -> None:
        self._should_be_killed = True
