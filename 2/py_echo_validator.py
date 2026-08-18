"""
Write a function that checks if a string is a palindrome,
ignoring spaces and case, only consider alphabetic characters
for the comparison.

def echo_validator(text: str) -> bool:
"""

def echo_validator(text: str) -> bool:
    clean_text = ""

    for char in text:
        if char.isalpha():
            clean_text += char.lower()

    if not clean_text:
        return False

    return clean_text == clean_text[::-1]

"""
if __name__ == "__main__":
    print(echo_validator("racecar"))
    print(echo_validator("A man a plan a canal Panama"))
    print(echo_validator("race a car"))
    print(echo_validator("Was it a car or a cat I saw"))
    print(echo_validator("hello"))
    print(echo_validator("Madam Im Adam"))
    print(echo_validator(""))
"""
