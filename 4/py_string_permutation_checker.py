"""
Write a function that determines if two strings are permutations of each other.
Case sensitive. Whitespace and punctuation count as regular characters.
Empty strings are permutations of each other.

def string_permutation_checker(s1: str, s2: str) -> bool:
"""

def string_permutation_checker(s1: str, s2: str) -> bool:
    s1_sorted = sorted(s1)
    s2_sorted = sorted(s2)
    return s1_sorted == s2_sorted

"""
if __name__ == "__main__":
    print(string_permutation_checker("abc", "bca"))
    print(string_permutation_checker("abc", "def"))
    print(string_permutation_checker("listen", "silent"))
    print(string_permutation_checker("hello", "bello"))
    print(string_permutation_checker("", ""))
    print(string_permutation_checker("a", ""))
    print(string_permutation_checker("Abc", "abc"))
    print(string_permutation_checker("a gentleman","elegant man"))
"""
