import typer
import SyntaxChecker as sc

input_location: str = "day10-input.txt"


def main():
    # solution_check_syntax()
    # solution_complete_invalid_syntax()
    # solution_calculate_invalid_syntax_points()
    solution1()
    solution2()


def solution_check_syntax():
    typer.echo("Day 10 / Syntax Check")

    # result = sc.SyntaxChecker().check_syntax("(>")
    result = sc.SyntaxChecker().check_syntax("[({(<(())[]>[[{[]{<()<>>")
    # result = sc.SyntaxChecker().check_syntax("[(()[<>])]({[<{<<[]>>(")
    # result = sc.SyntaxChecker().check_syntax("(((({<>}<{<{<>}{[]{[]{}")
    # result = sc.SyntaxChecker().check_syntax("{<[[]]>}<{[{[{[]{()[[[]")
    # result = sc.SyntaxChecker().check_syntax("<{([{{}}[<[[[<>{}]]]>[]]")

    typer.echo(result)


def solution_complete_invalid_syntax():
    typer.echo("Day 10 / Incomplete syntax")
    input_string = "[({([[{{"
    result = sc.SyntaxChecker().complete_invalid_syntax_string(input_string)
    typer.echo(f"Remaining syntax: {input_string}, fix it by appending: {result}")


def solution_calculate_invalid_syntax_points():
    typer.echo("Day 10 / Incomplete syntax points")
    input_string = "}}]])})]"
    result = sc.SyntaxChecker().calculate_invalid_syntax_points(input_string)
    typer.echo(f"Text to fix syntax: {input_string}, points: {result}")


def solution1():
    typer.echo("")
    typer.echo("Day 10 / Part 1")

    with open(input_location, "r") as f:
        input_lines = f.readlines()

    total = 0
    for line in input_lines:
        result = sc.SyntaxChecker().check_syntax(line.strip())
        total += result.invalid_character_points
        typer.echo(result)

    typer.echo("")
    typer.echo(f"Total points = {total}")
    typer.echo("")


def solution2():
    typer.echo("")
    typer.echo("Day 10 / Part 2")

    with open(input_location, "r") as f:
        input_lines = f.readlines()

    point_list = []
    for line in input_lines:
        result = sc.SyntaxChecker().check_syntax(line.strip())
        if result.incomplete_syntax_fix_points > 0:
            point_list.append(result.incomplete_syntax_fix_points)

    sorted_point_list = sorted(point_list)
    middle_point = int(len(sorted_point_list) / 2)

    typer.echo("")
    typer.echo(f"Total entries = {len(sorted_point_list)}")
    typer.echo(f"Middle point = {middle_point}")
    typer.echo(f"Points for the middle entry = {sorted_point_list[middle_point]}")
    typer.echo("")


typer.run(main)
