
def solution1_1():
    prevNum = 0
    currNum = 0
    counter = 0

    with open("./day1/day1-input.txt", "r") as f:

        for line in f:
            currNum = int(line)

            if prevNum > 0 and currNum > prevNum:
                counter = counter + 1

            prevNum = currNum

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
