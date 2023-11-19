from config.config import Config
from objects.organism import Organism
from objects.position import Position
from typing import List, Tuple


class World:
    def __init__(self):
        self._max_x: int = Config.get_settings('world.size.x_axis')
        self._max_y: int = Config.get_settings('world.size.y_axis')
        self._organisms: [Organism] = list()
        self._points: List[Tuple[int, int]] = list()
        self._interation: int = 0

    def __del__(self):
        self._organisms = None

    @property
    def organisms(self) -> [Organism]:
        return self._organisms

    @property
    def iteration(self) -> int:
        return self._interation

    def update(self) -> None:
        self._interation += 1

        for organism in self._organisms:
            organism.update()

    def add_organism(self, new_organism: Organism) -> None:
        self._organisms.append(new_organism)

    def organisms_count(self) -> int:
        return len(self._organisms)

    def space_is_free(self, position: Position) -> bool:
        for organism in self._organisms:
            if organism.position == position:
                return False
        return True
