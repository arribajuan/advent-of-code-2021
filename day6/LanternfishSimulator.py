import typer


class LanternfishSimulator:
    lanternfish: list[int] = []
    turns: int = 0

    def __init__(self, input_location: str):
        self.load_input(input_location)

    def __str__(self):
        result = "Simulation\n"
        result += f" - turns: {self.turns}\n"
        result += f" - total fish: {len(self.lanternfish)}"
        return result

    def load_input(self, input_location: str):
        with open(input_location, "r") as f:
            lines = f.readlines()
        self.lanternfish = [int(i) for i in lines[0].strip().split(",")]

    def sim_turn(self):
        self.turns += 1

        fish_to_process = len(self.lanternfish)
        offspring = 0

        typer.echo(f" ... {fish_to_process} fish to simulate")

        with typer.progressbar(range(fish_to_process)) as progress:
            for i in progress:
                if self.lanternfish[i] == 0:
                    offspring += 1
                    self.lanternfish[i] = 6
                else:
                    self.lanternfish[i] -= 1

        for i in range(offspring):
            self.lanternfish.append((8))

    def sim_turns(self, turns_to_simulate: int):
        for i in range(turns_to_simulate):
            print(f"Sim turn: {i}")
            self.sim_turn()
