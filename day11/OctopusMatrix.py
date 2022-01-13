import numpy as np


class OctopusMatrix:
    matrix_octopi: np.matrix
    matrix_flashes: np.matrix
    current_step: int = 0
    flashes_this_step: int = 0
    flashes_in_total: int = 0

    def __init__(self, octopus_matrix):
        self.matrix_octopi = octopus_matrix
        self.matrix_flashes = np.zeros(self.matrix_octopi.shape, int)

    def __str__(self):
        result = "Octopus Matrix\n"
        result += self.matrix_octopi
        result += "\n"
        result += f" - Step: {self.current_step}\n"
        result += f" - Flashes in this step: {self.flashes_this_step}\n"
        result += f" - Total flashes: {self.flashes_in_total}\n"
        return result

    def log(self, text_to_log):
        if True:
            print(text_to_log)

    def sim_increase_energy_to_matrix(self):
        self.matrix_octopi = self.matrix_octopi + 1

    def sim_flash_point(self, x, y):
        # If this point has not flashed in this step (self.matrix_flashes)
        if self.matrix_flashes[x][y] == 0:
            #  - Add to self.matrix_flashes
            self.matrix_flashes[x][y] = 1

            #  - Reset point to 0
            self.matrix_octopi[x][y] = 0

            #  - Update stats
            self.flashes_this_step += 1
            self.flashes_in_total += 1

            #  - Add 1 energy to surrounding points
            # tl
            # l
            # bl
            # t
            # b
            # tr
            # r
            # br

    def sim_flashes(self):
        for idx, item in np.ndenumerate(self.matrix_octopi):
            if item > 9:
                self.log(f" - Flash at {idx}")
                self.sim_flash_point(idx[0], idx[1])

    def sim_is_flash_imminent(self):
        for item in np.nditer(self.matrix_octopi):
            if item > 9:
                return True
        return False

    def simulate_step(self):
        self.log(f"")
        self.log(f"Simulating step {self.current_step + 1}")

        self.current_step += 1
        self.flashes_this_step = 0

        self.sim_increase_energy_to_matrix()
        while self.sim_is_flash_imminent():
            self.sim_flashes()
