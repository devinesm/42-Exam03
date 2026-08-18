"""
Write a function that checks if the brackets in a string are valid.

A string is valid if every opening bracket has a matching closing bracket
in the correct order.

Allowed brackets: (), [], {}

def bracket_validator(s: str) -> bool:
"""

def bracket_validator(s: str) -> bool:
    pairs = {
        ")" : "(",
        "]" : "[",
        "}" : "{"
    }

    stack = []
    for c in s:
        if c in '([{':
            stack.append(c)
        elif c in ')]}':
            if not stack or stack.pop() != pairs[c]:
                return False
    return len(stack) == 0

"""
if __name__ == "__main__":
    print(bracket_validator("()"))
    print(bracket_validator("()[]{}"))
    print(bracket_validator("(]"))
    print(bracket_validator("([)]"))
    print(bracket_validator("{[]}"))
    print(bracket_validator("hello(world)"))
    print(bracket_validator("((())"))
    print(bracket_validator(""))
"""
