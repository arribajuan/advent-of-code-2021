from typing import List

input_location: str = "day4-input.txt"


def bingo_load_input():
    game: list[str] = []
    tables: list[list[list[str]]] = []

    with open(input_location, "r") as f:
        lines = f.readlines()

        game = lines[0].strip().split()

        row = 1
        while row < len(lines):
            r1 = lines[row + 1].strip().split()
            r2 = lines[row + 2].strip().split()
            r3 = lines[row + 3].strip().split()
            r4 = lines[row + 4].strip().split()
            r5 = lines[row + 5].strip().split()
            table = [r1, r2, r3, r4, r5]
            tables.append(table)

            row = row + 6

    return game, tables


def solution1_1():
    game, tables = bingo_load_input()

    print(game)
    print(tables)


solution1_1()
