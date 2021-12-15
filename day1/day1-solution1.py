
def solution1_1():
    prev_num = 0
    counter = 0

    with open("./day1/day1-input.txt", "r") as f:

        for line in f:
            curr_num = int(line)

            if 0 < prev_num < curr_num:
                counter = counter + 1

            prev_num = curr_num

    print(f"Day 1 part 1 solution: counter = {counter}")


def solution1_2():
    counter = 0

    with open("./day1/day1-input.txt", "r") as f:
        num1 = f.readline()
        num2 = f.readline()

        while num2:
            if int(num2) > int(num1):
                counter = counter + 1

            num1 = num2
            num2 = f.readline()

    print(f"Day 1 part 1 solution: counter = {counter}")


def solution2():
    counter = 0

    with open("./day1/day1-input.txt", "r") as f:
        num1 = f.readline()
        num2 = f.readline()
        num3 = f.readline()
        num4 = f.readline()

        while num4:
            sum1 = int(num1) + int(num2) + int(num3)
            sum2 = int(num2) + int(num3) + int(num4)

            if sum2 > sum1:
                counter = counter + 1

            num1 = num2
            num2 = num3
            num3 = num4
            num4 = f.readline()

    print(f"Day 1 part 2 solution: counter = {counter}")


solution1_1()
solution1_2()
solution2()
