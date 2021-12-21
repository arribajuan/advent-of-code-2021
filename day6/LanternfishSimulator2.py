class LanternfishSimulator2:
    lanternfish: list[int] = []
    fish_in_timer8 = 0
    fish_in_timer7 = 0
    fish_in_timer6 = 0
    fish_in_timer5 = 0
    fish_in_timer4 = 0
    fish_in_timer3 = 0
    fish_in_timer2 = 0
    fish_in_timer1 = 0
    turns: int = 0

    def __init__(self, input_location: str):
        self.load_input(input_location)
        self.initialize_fish_counts()

    def __str__(self):
        result = "Simulation\n"
        result += f" - turns: {self.turns}\n"
        result += f" - total fish: {self.fish_in_timer1 + self.fish_in_timer2 + self.fish_in_timer3 + self.fish_in_timer4 + self.fish_in_timer5 + self.fish_in_timer6 + self.fish_in_timer7 + self.fish_in_timer8}\n"
        result += f"  -  in timer 8: {self.fish_in_timer8}\n"
        result += f"   - in timer 7: {self.fish_in_timer7}\n"
        result += f"   - in timer 6: {self.fish_in_timer6}\n"
        result += f"   - in timer 5: {self.fish_in_timer5}\n"
        result += f"   - in timer 4: {self.fish_in_timer4}\n"
        result += f"   - in timer 3: {self.fish_in_timer3}\n"
        result += f"   - in timer 2: {self.fish_in_timer2}\n"
        result += f"   - in timer 1: {self.fish_in_timer1}\n"
        return result

    def load_input(self, input_location: str):
        with open(input_location, "r") as f:
            lines = f.readlines()
        self.lanternfish = [int(i) for i in lines[0].strip().split(",")]

    def initialize_fish_counts(self):
        for fish_timer in self.lanternfish:
            if fish_timer == 6:
                self.fish_in_timer6 += 1
            if fish_timer == 5:
                self.fish_in_timer5 += 1
            if fish_timer == 4:
                self.fish_in_timer4 += 1
            if fish_timer == 3:
                self.fish_in_timer3 += 1
            if fish_timer == 2:
                self.fish_in_timer2 += 1
            if fish_timer == 1:
                self.fish_in_timer1 += 1

        pass

    def sim_turn(self):
        self.turns += 1

        offspring = self.fish_in_timer1

        self.fish_in_timer1 = self.fish_in_timer2
        self.fish_in_timer2 = self.fish_in_timer3
        self.fish_in_timer3 = self.fish_in_timer4
        self.fish_in_timer4 = self.fish_in_timer5
        self.fish_in_timer5 = self.fish_in_timer6
        self.fish_in_timer6 = self.fish_in_timer7 + offspring
        self.fish_in_timer7 = self.fish_in_timer8
        self.fish_in_timer8 = offspring

    def sim_turns(self, turns_to_simulate: int):
        for i in range(turns_to_simulate):
            #print(f"Sim turn: {i}")
            #print(self)
            self.sim_turn()
