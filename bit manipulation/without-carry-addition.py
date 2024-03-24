import math


def addition_without_carry(first_num: int, second_num: int):
    bit_sum, result = 0, 0
    multiplier = 1

    while first_num or second_num:
        bit_sum = ((first_num % 10) + (second_num % 10))
        bit_sum = bit_sum % 10

        result = (bit_sum * multiplier) + result

        multiplier = multiplier * 10

        first_num = math.floor(first_num / 10)
        second_num = math.floor(second_num / 10)

    return result


if __name__ == "__main__":
    print(addition_without_carry(8458, 8732))
