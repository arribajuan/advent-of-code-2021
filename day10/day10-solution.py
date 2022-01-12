import typer
import SyntaxResult as sr
import SyntaxChecker as sc

input_location: str = "day10-input.txt"

def main():
    #solution1_check_syntax()
    solution1()




def solution1_check_syntax():
    typer.echo("Day 10 / Part 1")
    checkResult = sc.SyntaxChecker().check_syntax("(>")
    typer.echo(checkResult)


def solution1():
    typer.echo("Day 10 / Part 1")

    with open(input_location, "r") as f:
        input_lines = f.readlines()

    total = 0
    for line in input_lines:
        checkResult = sc.SyntaxChecker().check_syntax(line.strip())
        total += checkResult.invalid_character_points
        typer.echo(checkResult)

    typer.echo("")
    typer.echo(f"Total points = {total}")
    typer.echo("")

typer.run(main)
