from objects.organism import Organism
from objects.world import World
from config.config import Config


def main():
    world = get_start_stage()
    simulate(world)


def simulate(world: World) -> None:
    for _ in range(0, Config.get_settings('simulation.iterations')):
        world.update()


def get_start_stage() -> World:
    world = World()
    beginning_organisms_count = Config.get_settings('simulation.beginning_organisms_count')

    for _ in range(beginning_organisms_count):
        new_organism = Organism()
        number_of_creation_attempts: int = 0

        position_is_correct = world.space_is_free(new_organism.position)

        while not position_is_correct or number_of_creation_attempts > 9:
            new_organism.generate_position()
            position_is_correct = world.space_is_free(new_organism.position)
            number_of_creation_attempts += 1

        world.add_organism(new_organism)

    return world


if __name__ == '__main__':
    main()
