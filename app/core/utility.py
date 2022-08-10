import sys


def atoi():
    input_str = input("Entrer you desired str: ")
    result = ""
    is_positive = True
    for char in input_str:
        if check_is_white_space(char):
            continue

        if check_is_character(char):
            if len(result) > 0:
                break

            if char == "-":
                is_positive = False
            elif char == "+":
                is_positive = True
            else:
                break

        if check_is_number(char):
            if check_is_zero(char) and len(result) == 0:
                continue
            result += char

    if is_positive:
        result = check_overflow(result)
    else:
        result = check_underflow(result)

    print(result if is_positive else f"-{result}")


def check_is_white_space(char):
    return ord(char) == 32


def check_is_character(char):
    return ord(char) < 48 or ord(char) > 57


def check_is_number(char):
    return 48 <= ord(char) <= 57


def check_is_zero(char):
    return ord(char) == 48


def check_overflow(result):
    max_int = str(sys.maxsize)
    max_int_length = len(max_int)

    if len(result) > max_int_length:
        return max_int

    if len(result) == max_int_length:
        for idx, char in enumerate(result):
            if ord(char) > ord(max_int[idx]):
                return max_int

    return result


def check_underflow(result):
    min_int = str(-sys.maxsize - 1)[1:]
    min_int_length = len(min_int)

    if len(result) > min_int_length:
        return min_int

    if len(result) == min_int_length:
        for idx, char in enumerate(result):
            if ord(char) < ord(min_int[idx]):
                return min_int

    return result


atoi()
