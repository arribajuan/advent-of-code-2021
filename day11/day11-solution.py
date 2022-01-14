import typer
import OctopusMatrix as om
import OctopusMatrix_inputs as omi
import typer

import OctopusMatrix as om
import OctopusMatrix_inputs as omi


def main():
    solution1()


def solution1():
    typer.echo("")
    typer.echo("Day 11 / Part 1")
    typer.echo("")

    octopi = om.OctopusMatrix(omi.input_test3_step0)
    for x in range(100):
        octopi.simulate_steps(5)
    typer.echo(octopi)
    typer.echo(f"Part 1 answer = {octopi.flashes_in_total - octopi.flashes_this_step}")


typer.run(main)
