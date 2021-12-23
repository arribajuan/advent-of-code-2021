import typer
import RiskDetector as rd

input_location: str = "day9-input.txt"


def main():
    solution()


def solution():
    typer.echo("Day 9 / Part 1")
    risk_detector = rd.RiskDetector(input_location)
    risk_detector.find_lowest_points()
    typer.echo(risk_detector)


typer.run(main)
