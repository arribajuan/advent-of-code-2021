
def solution1():
    prevNum = 0
    currNum = 0
    counter = 0

    with open('day1/day1-input.txt', 'r')as f:

        for line in f:
            currNum = int(line)

            if prevNum > 0 and currNum > prevNum:
                counter = counter + 1

            prevNum = currNum

    print(f"Solution 1 counter = {counter}")


def solution2():
    print("Solution 2 not implemented")


solution1()
solution2()
