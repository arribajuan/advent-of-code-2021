import LanternfishSimulator as ls1
import LanternfishSimulator2 as ls2
import typer

input_location: str = "day6-input.txt"


def solution1():
    typer.echo("Hello from typer!")
    my_sim = ls1.LanternfishSimulator(input_location)
    my_sim.sim_turns(150)
    # print(my_sim)


def solution2():
    my_sim = ls2.LanternfishSimulator2(input_location)
    my_sim.sim_turns(7)
    print(my_sim)


typer.run(solution1())
