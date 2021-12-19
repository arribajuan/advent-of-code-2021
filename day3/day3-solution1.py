from enum import Enum

input_location: str = "day3-input.txt"


class FilterTypeEnum(Enum):
    MOST_COMMON = 1
    LEAST_COMMON = 2


def solution1_1():
    b1_count = 0
    b2_count = 0
    b3_count = 0
    b4_count = 0
    b5_count = 0
    b6_count = 0
    b7_count = 0
    b8_count = 0
    b9_count = 0
    b10_count = 0
    b11_count = 0
    b12_count = 0
    input_count = 0

    with open(input_location, "r") as f:
        for line in f:
            b1_count = b1_count + int(line[0])
            b2_count = b2_count + int(line[1])
            b3_count = b3_count + int(line[2])
            b4_count = b4_count + int(line[3])
            b5_count = b5_count + int(line[4])
            b6_count = b6_count + int(line[5])
            b7_count = b7_count + int(line[6])
            b8_count = b8_count + int(line[7])
            b9_count = b9_count + int(line[8])
            b10_count = b10_count + int(line[9])
            b11_count = b11_count + int(line[10])
            b12_count = b12_count + int(line[11])

            input_count = input_count + 1

    # If the bit count is greater than  half the total, means 1 is majority
    gamma_b1 = int(b1_count > (input_count / 2))
    gamma_b2 = int(b2_count > (input_count / 2))
    gamma_b3 = int(b3_count > (input_count / 2))
    gamma_b4 = int(b4_count > (input_count / 2))
    gamma_b5 = int(b5_count > (input_count / 2))
    gamma_b6 = int(b6_count > (input_count / 2))
    gamma_b7 = int(b7_count > (input_count / 2))
    gamma_b8 = int(b8_count > (input_count / 2))
    gamma_b9 = int(b9_count > (input_count / 2))
    gamma_b10 = int(b10_count > (input_count / 2))
    gamma_b11 = int(b11_count > (input_count / 2))
    gamma_b12 = int(b12_count > (input_count / 2))

    epsilon_b1 = abs(gamma_b1 - 1)
    epsilon_b2 = abs(gamma_b2 - 1)
    epsilon_b3 = abs(gamma_b3 - 1)
    epsilon_b4 = abs(gamma_b4 - 1)
    epsilon_b5 = abs(gamma_b5 - 1)
    epsilon_b6 = abs(gamma_b6 - 1)
    epsilon_b7 = abs(gamma_b7 - 1)
    epsilon_b8 = abs(gamma_b8 - 1)
    epsilon_b9 = abs(gamma_b9 - 1)
    epsilon_b10 = abs(gamma_b10 - 1)
    epsilon_b11 = abs(gamma_b11 - 1)
    epsilon_b12 = abs(gamma_b12 - 1)

    gamma_binary_string = str(gamma_b1) + str(gamma_b2) + str(gamma_b3) + str(gamma_b4) + str(gamma_b5) + str(
        gamma_b6) + str(gamma_b7) + str(gamma_b8) + str(gamma_b9) + str(gamma_b10) + str(gamma_b11) + str(gamma_b12)
    gamma_decimal = int(gamma_binary_string, 2)
    epsilon_binary_string = str(epsilon_b1) + str(epsilon_b2) + str(epsilon_b3) + str(epsilon_b4) + str(
        epsilon_b5) + str(epsilon_b6) + str(epsilon_b7) + str(epsilon_b8) + str(epsilon_b9) + str(epsilon_b10) + str(
        epsilon_b11) + str(epsilon_b12)
    epsilon_decimal = int(epsilon_binary_string, 2)

    power_consumption = gamma_decimal * epsilon_decimal

    # Print debug messages
    #print(f"Total items = {input_count}")

    #print("")

    #print("Counts")
    #print(f"b1 = {b1_count}")
    #print(f"b2 = {b2_count}")
    #print(f"b3 = {b3_count}")
    #print(f"b4 = {b4_count}")
    #print(f"b5 = {b5_count}")
    #print(f"b6 = {b6_count}")
    #print(f"b7 = {b7_count}")
    #print(f"b8 = {b8_count}")
    #print(f"b9 = {b9_count}")
    #print(f"b10 = {b10_count}")
    #print(f"b11 = {b11_count}")
    #print(f"b12 = {b12_count}")

    #print("")

    #print("Gamma")
    #print(f"b1 = {gamma_b1}")
    #print(f"b2 = {gamma_b2}")
    #print(f"b3 = {gamma_b3}")
    #print(f"b4 = {gamma_b4}")
    #print(f"b5 = {gamma_b5}")
    #print(f"b6 = {gamma_b6}")
    #print(f"b7 = {gamma_b7}")
    #print(f"b8 = {gamma_b8}")
    #print(f"b9 = {gamma_b9}")
    #print(f"b10 = {gamma_b10}")
    #print(f"b11 = {gamma_b11}")
    #print(f"b12 = {gamma_b12}")

    #print("")

    #print("Epsilon")
    #print(f"b1 = {epsilon_b1}")
    #print(f"b2 = {epsilon_b2}")
    #print(f"b3 = {epsilon_b3}")
    #print(f"b4 = {epsilon_b4}")
    #print(f"b5 = {epsilon_b5}")
    #print(f"b6 = {epsilon_b6}")
    #print(f"b7 = {epsilon_b7}")
    #print(f"b8 = {epsilon_b8}")
    #print(f"b9 = {epsilon_b9}")
    #print(f"b10 = {epsilon_b10}")
    #print(f"b11 = {epsilon_b11}")
    #print(f"b12 = {epsilon_b12}")

    #print("")

    #print(f"Gamma binary: {gamma_binary_string}")
    #print(f"Gamma decimal: {gamma_decimal}")
    #print(f"Epsilon binary: {epsilon_binary_string}")
    #print(f"Epsilon decimal: {epsilon_decimal}")

    #print("")

    print(f"Day 3 part 1 solution: {power_consumption}")


def solution2_1():
    with open(input_location, "r") as f:
        diagnostic_report = f.readlines()

    ogr_data = diagnostic_report.copy()  # Oxygen generator rating
    ogr_decimal = solution2_1_process(ogr_data, FilterTypeEnum.MOST_COMMON)

    co2sr_data = diagnostic_report.copy()  # CO2 Scrubber rating
    co2sr_decimal = solution2_1_process(co2sr_data, FilterTypeEnum.LEAST_COMMON)

    result = ogr_decimal * co2sr_decimal

    #print(f"OGR = {ogr_decimal}")
    #print(f"CO2SR = {co2sr_decimal}")
    #print(f"RESUKT = {result}")

    print(f"Day 3 part 2 solution: {result}")


def solution2_1_process(diagnostic_report, filter_type: FilterTypeEnum):
    for bit_position in range(12):
        common_bit = solution2_1_most_common_bit(bit_position, diagnostic_report)
        diagnostic_report = solution2_1_filter(bit_position, diagnostic_report, common_bit, filter_type)

        #print(f"Position = {bit_position}")
        #print(f"Common bit = {common_bit}")
        #print(f"Remaining items in list = {len(diagnostic_report)}")

        if len(diagnostic_report) == 1:
            processed_line = diagnostic_report[0]
            processed_decimal = int(processed_line, 2)
            #print(" -- we have an answer!")
            #print(f" -- {processed_line}")
            #print(f" -- {processed_decimal}")
            return processed_decimal

        #print("----")


def solution2_1_filter(bit_position, diagnostic_report, common_bit, filter_type: FilterTypeEnum):
    if filter_type is FilterTypeEnum.MOST_COMMON:
        return [line for line in diagnostic_report if int(line[bit_position]) == common_bit]
    elif filter_type is FilterTypeEnum.LEAST_COMMON:
        return [line for line in diagnostic_report if int(line[bit_position]) != common_bit]


def solution2_1_most_common_bit(bit_position, diagnostic_report):
    bit_count = 0

    for line in diagnostic_report:
        bit_count = bit_count + int(line[bit_position])

    return int(bit_count >= len(diagnostic_report) / 2)


solution1_1()
solution2_1()
