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

    octopi = om.OctopusMatrix(omi.input_test1_step0)
    for x in range(50):
        octopi.simulate_steps(5)
        typer.echo(octopi)

    # m = omi.input_test1_step0.copy()
    # typer.echo(m)
    # m = m + 1
    # typer.echo(m)

    # typer.echo(type(omi.input_test0_step0))
    # typer.echo(omi.input_test0_step0)
    # typer.echo(omi.input_test0_step0.item((0, 0)))
    # typer.echo(omi.input_test0_step0.item((0, 1)))
    # typer.echo(omi.input_test0_step0.item((1, 1)))

    # typer.echo(omi.input_test0_step0.item((1, 2)))
    # omi.input_test0_step0[1, 2] = 100
    # typer.echo(omi.input_test0_step0.item((1, 2)))


typer.run(main)
