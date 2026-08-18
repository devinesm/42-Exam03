"""
Write a function that checks if two strings are anagrams.
They must contain exactly the same letters with the same quantity,
ignoring case and spaces.

def anagram(s1: str, s2: str) -> bool:
"""

def anagram(s1: str, s2: str) -> bool:
    s1_sorted = sorted(s1.lower().replace(" ", ""))
    s2_sorted = sorted(s2.lower().replace(" ", ""))
    return s1_sorted == s2_sorted

"""
if __name__ == "__main__":
    print(anagram("listen", "silent"))
    print(anagram("Triangle", "Integral"))
    print(anagram("Dormitory", "Dirty Room"))
    print(anagram("hello", "world"))
    print(anagram("", ""))
    print(anagram("abc", "abcc"))
"""
