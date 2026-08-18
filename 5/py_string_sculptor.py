"""
Write a function that transforms a string by alternating the case of
alphabetic characters only.
Non-alphabetic characters remain unchanged and are NOT counted in the
alternation index.
The first alphabetic character should be lowercase, the second uppercase, etc.
Spaces reset the alternation (next alpha after a space is lowercase again).

def string_sculptor(text: str) -> str:
"""

def string_sculptor(text: str) -> str:
    alternation_index = 0
    result = ""
    for c in text:
        if c == " ":
            result += " "
            alternation_index = 0
        elif c.isalpha():
            if alternation_index % 2 == 0:
                result += c.lower()
            else:
                result += c.upper()
            alternation_index += 1
        else:
            result += c
    return result

"""
if __name__ == "__main__":
    print(string_sculptor("hello"))
    print(string_sculptor("Hello World"))
    print(string_sculptor("abc123def"))
    print(string_sculptor("Python3.9!"))
    print(string_sculptor(""))
"""
