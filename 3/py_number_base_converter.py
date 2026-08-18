"""
Write a function that converts a number from one base to another.
Support bases from 2 to 36 inclusive.
Use digits 0-9 and letters A-Z for values 10-35.
Return "ERROR" for invalid inputs.

def number_base_converter(number: str, from_base: int, to_base: int) -> str:
"""

def number_base_converter(number: str, from_base: int, to_base: int) -> str:
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if from_base < 2 or from_base > 36:
        return "ERROR"
    elif to_base < 2 or to_base > 36:
        return "ERROR"
    elif number == "":
        return "ERROR"

    value = 0
    for c in number.upper():
        pos = digits.find(c)
        if pos == -1 or pos >= from_base:
            return "ERROR"
        value = value * from_base + pos
    if value == 0:
        return "0"
    result = ""
    while value > 0:
        result = digits[value % to_base] + result
        value //= to_base
    return result

"""
if __name__ == "__main__":
    print(number_base_converter("1010", 2, 10))
    print(number_base_converter("FF", 16, 10))
    print(number_base_converter("255", 10, 16))
    print(number_base_converter("123", 10, 2))
    print(number_base_converter("Z", 36, 10))
    print(number_base_converter("35", 10, 36))
    print(number_base_converter("123", 1, 10))
    print(number_base_converter("G", 16, 10))
"""
