input_location: str = "day2-input.txt"


def solution1_1():
    move_up = 0
    move_down = 0
    move_forward = 0

    with open(input_location, "r") as f:
        for line in f:
            lineItems = line.split()
            direction = lineItems[0]
            magnitude = int(lineItems[1])

            if direction == "up":
                move_up = move_up + magnitude
            if direction == "down":
                move_down = move_down + magnitude
            if direction == "forward":
                move_forward = move_forward + magnitude

        depth = move_down - move_up
        result = depth * move_forward

    print(f"Day 2 part 2 solution: {result}")


solution1_1()