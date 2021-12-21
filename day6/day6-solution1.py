import day6.LanternfishSimulator as ls

input_location: str = "day6-input.txt"


def solution():
    my_sim = ls.LanternfishSimulator(input_location)
    my_sim.sim_turns(80)
    print(my_sim)


solution()
