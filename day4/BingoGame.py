import day4.BingoTable as bt
import copy


class BingoGame:
    game_numbers: list[int] = []
    tables: list[bt.BingoTable] = []
    game_winners: list[bt.BingoTable]

    def __init__(self, input_location: str):
        self.load_input(input_location)
        self.game_winners = []

    def load_input(self, input_location: str):
        with open(input_location, "r") as f:
            lines = f.readlines()

            self.game_numbers = [int(i) for i in lines[0].strip().split(",")]

            row = 1
            table_count = 1
            while row < len(lines):
                r1 = [int(i) for i in lines[row + 1].strip().split()]
                r2 = [int(i) for i in lines[row + 2].strip().split()]
                r3 = [int(i) for i in lines[row + 3].strip().split()]
                r4 = [int(i) for i in lines[row + 4].strip().split()]
                r5 = [int(i) for i in lines[row + 5].strip().split()]
                self.tables.append(bt.BingoTable(table_count, [r1, r2, r3, r4, r5]))
                row += 6
                table_count += 1

    def play_number(self, game_number: int):
        for i, t in enumerate(self.tables):
            if t.play_number(game_number):
                if not self.table_found((t.table_number)):
                    self.game_winners.append(copy.deepcopy(t))

    def table_found(self, table_number: int):
        for t in self.game_winners:
            if t.table_number == table_number:
                return True
        return False
