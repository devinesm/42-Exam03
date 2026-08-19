"""
Write a function that creates a Caesar cipher by shifting letters in a
string by a given amount.
Non-alphabetic characters should remain unchanged.
The shift can be negative (shift left).

def whisper_cipher(text: str, shift: int) -> str:
"""

def whisper_cipher(text: str, shift: int) -> str:
    result = []
    for c in text:
        if c.isupper():
            result.append(chr((ord(c) - ord('A') + shift) % 26 + ord('A')))
        elif c.islower():
            result.append(chr((ord(c) - ord('a') + shift) % 26 + ord('a')))
        else:
            result.append(c)
    return "".join(result)

"""
if __name__ == "__main__":
    print(whisper_cipher("hello", 3))
    print(whisper_cipher("Hello World!", 1))
    print(whisper_cipher("xyz", 3))
    print(whisper_cipher("ABC123def", 5))
    print(whisper_cipher("", 10))
    print(whisper_cipher("abc", -3))
"""
