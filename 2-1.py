import fileinput
import logging
from dataclasses import dataclass


@dataclass
class Set:
    red: int = 0
    green: int = 0
    blue: int = 0

    def __le__(self, other):
        return (
            self.red <= other.red
            and self.green <= other.green
            and self.blue <= other.blue
        )


@dataclass
class Game:
    id: int
    sets: list[Set]

    def is_possible(self, bag: Set):
        return all((s <= bag for s in self.sets))


def parse_sets(line: str) -> list[Set]:
    # Example input: "1 blue, 5 red; 3 blue, 5 green, 13 red; 6 red, 1 blue, 4 green; 16 red, 12 green"
    result = []
    set_strs = line.split(";")
    for set_str in set_strs:
        curr_set = Set()
        for color_str in set_str.split(","):
            color_info = color_str.lstrip().split(" ")
            num = int(color_info[0])
            color = color_info[1]
            setattr(curr_set, color, num)
        result.append(curr_set)
    return result


def parse_game(line: str) -> Game:
    # Example input: "Game 1: 1 blue, 5 red; 3 blue, 5 green, 13 red; 6 red, 1 blue, 4 green; 16 red, 12 green"
    game_info = line.split(":")
    id_str, sets_str = game_info[0], game_info[1]
    game_id = int(id_str.split(" ")[1])
    sets = parse_sets(sets_str)
    game = Game(game_id, sets)
    logging.debug(f"parse_game('{line}') -> {game}")
    return game


bag = Set(12, 13, 14)
sum = 0
for line in fileinput.input():
    game = parse_game(line.strip())
    if game.is_possible(bag):
        sum += game.id

print(f"Result: {sum}")
