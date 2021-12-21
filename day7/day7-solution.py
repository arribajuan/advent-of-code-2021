import CrabAligner1 as ca1
import typer

input_location: str = "day7-input.txt"


def main():
    typer.echo("Day 7 - main")
    solution1()


def solution1():
    typer.echo("Day 7 / Part 1 - Solution 1!")
    crab_aligner = ca1.CrabAligner1(input_location)
    crab_aligner.calculate_position_costs()
    print(crab_aligner)


typer.run(main)
