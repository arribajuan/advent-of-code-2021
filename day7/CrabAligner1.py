import typer


class CrabAligner1:
    crabs: list[int] = []
    cost: list[int] = []
    min_position: int = 0
    min_cost: int = 0
    max_position: int = 0
    max_cost: int = 0
    position_cost_cache = {0: 0}

    def __init__(self, input_location: str):
        self.load_input(input_location)

    def __str__(self):
        result = "Crab aligner\n"
        result += f" - total crab: {len(self.crabs)}\n"
        result += f" - minimal cost {self.min_cost} at position {self.min_position}\n"
        result += f" - max cost {self.max_cost} at position {self.max_position}\n"
        return result

    def load_input(self, input_location: str):
        with open(input_location, "r") as f:
            lines = f.readlines()
        self.crabs = [int(i) for i in lines[0].strip().split(",")]

    def calculate_position_costs(self):
        typer.echo("Calculating position costs")

        for i in range(len(self.crabs)):
            positions_moved = 0
            for j in range(len(self.crabs)):
                positions_moved += abs(i - self.crabs[j])
                cost_of_move = self.calculate_move_cost(positions_moved)
            self.cost.append(cost_of_move)
            typer.echo(f" - position {i}, cost {cost_of_move}")

        self.min_cost = min(self.cost)
        self.min_position = self.cost.index(self.min_cost)

        self.max_cost = max(self.cost)
        self.max_position = self.cost.index(self.max_cost)

    def calculate_move_cost(self, positions_moved: int):
        return positions_moved

