import day6.LanternfishSimulator as ls1
import day6.LanternfishSimulator2 as ls2

input_location: str = "day6-input.txt"


def solution1():
    my_sim = ls1.LanternfishSimulator(input_location)
    my_sim.sim_turns(100)
    #print(my_sim)

def solution2():
    my_sim = ls2.LanternfishSimulator2(input_location)
    my_sim.sim_turns(7)
    print(my_sim)

solution1()
#solution2()
