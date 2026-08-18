"""
Write a function that counts the number of valid consecutive digit pairs
in a string. A valid pair consists of two adjacent digits where the second
digit is exactly one greater than the first.
A 9 followed by a 0 is NOT a valid pair.

def pattern_tracker(text: str) -> int:
"""

def pattern_tracker(text: str) -> int:
    count = 0
    for i in range(len(text) - 1):
        a, b = text[i], text[i + 1]
        if a.isdigit() and b.isdigit() and int(b) == int(a) + 1:
            count += 1
    return count

"""
if __name__ == "__main__":
    print(pattern_tracker("123"))
    print(pattern_tracker("12a34"))
    print(pattern_tracker("987654321"))
    print(pattern_tracker("01234567"))
    print(pattern_tracker("abc"))
    print(pattern_tracker("1a2b3c4"))
    print(pattern_tracker("112233"))
"""
