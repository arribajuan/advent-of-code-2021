import typer


class CrabAligner1:
    crabs: list[int] = []
    cost: list[int] = []
    min_position: int = 0
    min_cost: int = 0
    position_cost_cache = {0: 0}

    def __init__(self, input_location: str):
        self.load_input(input_location)

    def __str__(self):
        result = "   Crab aligner\n"
        result += f"   - total crab: {len(self.crabs)}\n"
        result += f"   - minimal cost {self.min_cost} at position {self.min_position}\n"
        return result

    def load_input(self, input_location: str):
        with open(input_location, "r") as f:
            lines = f.readlines()
        self.crabs = [int(i) for i in lines[0].strip().split(",")]

    def calculate_position_costs1(self):
        typer.echo("Calculating position costs1")

        with typer.progressbar(range(len(self.crabs))) as progress:
            for i in progress:
                positions_moved = 0
                cost_of_move = 0

                for j in range(len(self.crabs)):
                    positions_moved += abs(i - self.crabs[j])
                    cost_of_move = self.calculate_move_cost1(positions_moved)

                self.cost.append(cost_of_move)

        self.min_cost = min(self.cost)
        self.min_position = self.cost.index(self.min_cost)

    def calculate_move_cost1(self, positions_moved: int):
        return positions_moved

    def calculate_position_costs2(self):
        typer.echo("Calculating position costs2")

        with typer.progressbar(range(len(self.crabs))) as progress:
            for i in progress:
                cost_total = 0

                for j in range(len(self.crabs)):
                    positions_moved_now = abs(i - self.crabs[j])
                    cost_now = self.calculate_move_cost2(positions_moved_now)
                    cost_total += cost_now

                self.cost.append(cost_total)

        self.min_cost = min(self.cost)
        self.min_position = self.cost.index(self.min_cost)

    def calculate_move_cost2(self, positions_moved: int):
        cost = 0
        for i in range(positions_moved):
            cost += i + 1
        return cost
