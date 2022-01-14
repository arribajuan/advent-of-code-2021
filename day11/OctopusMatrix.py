import numpy as np


class OctopusMatrix:
    matrix_octopi: np.matrix
    matrix_flashes: np.matrix
    current_step: int = 0
    flashes_this_step: int = 0
    flashes_in_total: int = 0

    def __init__(self, octopus_matrix):
        self.matrix_octopi = octopus_matrix
        self.matrix_flashes = np.asmatrix(np.zeros(self.matrix_octopi.shape, int))

    def __str__(self):
        result = "Octopus Matrix\n"
        result += f"{self.matrix_octopi}"
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

    def sim_flash_point(self, idx):
        x = idx[0]  # = row
        y = idx[1]  # = column

        #  - Add to self.matrix_flashes
        self.matrix_flashes[x, y] = 1

        #  - Reset point to 0
        self.matrix_octopi[x, y] = 0

        #  - Update stats
        self.flashes_this_step += 1
        self.flashes_in_total += 1

        #  - Add 1 energy to surrounding points
        x_size = self.matrix_octopi.shape[0]
        y_size = self.matrix_octopi.shape[1]

        if x > 0 and y > 0 and self.matrix_flashes.item((x - 1, y - 1)) == 0:
            self.matrix_octopi[x - 1, y - 1] += 1  # top left

        if x > 0 and self.matrix_flashes.item((x - 1, y)) == 0:
            self.matrix_octopi[x - 1, y] += 1  # top

        if x > 0 and y < y_size and self.matrix_flashes.item((x - 1, y + 1)) == 0:
            self.matrix_octopi[x - 1, y + 1] += 1  # top right

        if y > 0 and self.matrix_flashes.item((x, y - 1)) == 0:
            self.matrix_octopi[x, y - 1] += 1  # mid left

        if y < y_size and self.matrix_flashes.item((x, y + 1)) == 0:
            self.matrix_octopi[x, y + 1] += 1  # mid right

        if x < x_size and y > 0 and self.matrix_flashes.item((x + 1, y - 1)) == 0:
            self.matrix_octopi[x + 1, y - 1] += 1  # bottom left

        if x < x_size and self.matrix_flashes.item((x + 1, y)) == 0:
            self.matrix_octopi[x + 1, y] += 1  # bottom

        if x < x_size and y < y_size and self.matrix_flashes.item((x + 1, y + 1)) == 0:
            self.matrix_octopi[x + 1, y + 1] += 1  # bottom right

    def sim_flashes(self):
        # self.log(f"\n")
        # self.log(f"---------------------\n")
        # self.log(f"SIM FLASHES?\n")
        # self.log(f"Octopi Matrix - {type(self.matrix_octopi)}\n")
        # self.log(self.matrix_octopi)
        # self.log(f"\n")
        # self.log(f"Flash matrix - {type(self.matrix_flashes)}\n")
        # self.log(self.matrix_flashes)
        # self.log(f"\n")

        # self.log(f"Check matrix\n")
        for idx, item in np.ndenumerate(self.matrix_octopi):
            has_flashed_already = self.matrix_flashes.item(idx)
            # self.log(f" - point {idx}, value {item}, has flashed? {has_flashed_already}")

            if item > 9 and has_flashed_already == 0:
                # self.log(f"    -> Process flash at {idx}")
                self.sim_flash_point(idx)

        # self.log(f"---------------------\n")

    def sim_is_flash_imminent(self):
        # self.log(f"\n")
        # self.log(f"---------------------\n")
        # self.log(f"IS FLASH IMMINENT?\n")
        # self.log(f"Octopi Matrix - {type(self.matrix_octopi)}\n")
        # self.log(self.matrix_octopi)
        # self.log(f"\n")
        # self.log(f"Flash matrix - {type(self.matrix_flashes)}\n")
        # self.log(self.matrix_flashes)
        # self.log(f"\n")

        # self.log(f"Check matrix\n")
        for idx, item in np.ndenumerate(self.matrix_octopi):
            has_flashed_already = self.matrix_flashes.item(idx)
            # self.log(f" - point {idx}, value {item}, has flashed? {has_flashed_already}")

            if item > 9 and has_flashed_already == 0:
                # self.log(f"    -> flash imminent\n")
                # self.log(f"---------------------\n")
                return True
        return False

    def simulate_steps(self, max_rounds):
        self.current_step += 1
        self.flashes_this_step = 0

        self.log(f"")
        self.log(f"Simulating step {self.current_step}")

        self.log(f"Increase energy!!")
        self.sim_increase_energy_to_matrix()

        sim_round_count = 1
        while self.sim_is_flash_imminent() and sim_round_count < max_rounds:
            self.log(f"Sim flashes round {sim_round_count}!!")
            self.sim_flashes()
            sim_round_count += 1
