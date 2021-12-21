import typer
import CrabAligner1 as ca

input_location: str = "day7-input.txt"


def main():
    solution()


def solution():
    crab_aligner = ca.CrabAligner1(input_location)

    #typer.echo("Day 7 / Part 1")
    #crab_aligner.calculate_position_costs1()
    #print(crab_aligner)

    typer.echo("Day 7 / Part 2")
    crab_aligner.calculate_position_costs2()
    print(crab_aligner)


typer.run(main)
