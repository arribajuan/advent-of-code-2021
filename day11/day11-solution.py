import numpy as np
import typer
import OctopusMatrix as om
import OctopusMatrix_inputs as omi



def main():
    solution1()


def solution1():
    typer.echo("")
    typer.echo("Day 11 / Part 1")

    m = omi.input_test1_step0.copy()
    typer.echo(m)
    m = m + 1
    typer.echo(m)





typer.run(main)
