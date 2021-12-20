class BingoTable:
    table_number: int
    table_numbers: list[list[int]]
    positions_marked: list[list[int]]
    numbers_played: list[int]
    is_winner: bool
    winner_row: int
    winner_column: int

    def __init__(self, table_number, table_numbers):
        self.table_number = table_number
        self.table_numbers = table_numbers
        self.positions_marked = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
        self.numbers_played = []
        self.is_winner = False
        self.winner_row = -1
        self.winner_column = -1

    def __str__(self):
        result = ""
        result += f"Table {self.table_number}\n"
        for i in self.table_numbers:
            for j in i:
                result += str(j) + " - "
            result += "\n"

        result += "\n"
        result += "Positions marked\n"
        for i in self.positions_marked:
            for j in i:
                result += str(j) + " - "
            result += "\n"

        result += "\n"
        result += "Numbers played\n"
        for i in self.numbers_played:
            result += str(i) + " - "
        result += "\n"

        result += "\n"
        result += f"Is winner? {self.is_winner}\n"
        if self.winner_row > 0:
            result += f" - Winner row {self.winner_row}\n"
        if self.winner_column > 0:
            result += f" - Winner column {self.winner_column}\n"

        return result

    def play_number(self, game_number: int) -> bool:
        # Add to list of numbers played
        self.numbers_played.append(game_number)

        # Update marked positions
        for i in range(len(self.table_numbers)):
            for j in range(len(self.table_numbers[i])):
                if self.table_numbers[i][j] == game_number:
                    self.positions_marked[i][j] = 1

        # Search for full rows
        for i in range(len(self.positions_marked)):
            count = 0
            for j in range(len(self.positions_marked[i])):
                count += self.positions_marked[i][j]
            if count == len(self.positions_marked[i]):
                self.is_winner = True
                self.winner_row = i
                return True

        # Search for full column
        for i in range(len(self.positions_marked)):
            count = 0
            for j in range(len(self.positions_marked[i])):
                count += self.positions_marked[j][i]
            if count == len(self.positions_marked[j]):
                self.is_winner = True
                self.winner_column = i
                return True

        return False
