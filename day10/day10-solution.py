import typer
import SyntaxResult as sr
import SyntaxChecker as sc

input_location: str = "day10-input.txt"


def main():
    solution()


def solution():
    typer.echo("Day 10 / Part 1")
    checkResult = sc.SyntaxChecker().check_syntax("[({(<(())[]>[[{[]{<()<>>")
    typer.echo(checkResult)


typer.run(main)
