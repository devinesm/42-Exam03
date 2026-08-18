"""
Write a function that sorts a list of strings according to multiple criteria:
1. Primary sort: By string length (shortest first)
2. Secondary sort: ASCII order, except letters are compared case-insensitively
   (for strings of same length)
3. Tertiary sort: By number of vowels (ascending, for same length and lexically equal)
4. Equal strings will appear in the same order as in the input list.

Forbidden functions: sorted(), list.sort()

def cryptic_sorter(strings: list[str]) -> list[str]:
"""

def count_vowels(word: str) -> int:
    vowels = 'aeiouAEIOU'
    i = 0
    for c in word:
        if c in vowels:
            i += 1
    return i


def should_swap(word1: str, word2: str) -> bool:
    # First Rule
    if len(word1) != len(word2):
        return len(word1) > len(word2)

    # Seconde Rule
    lower1 = word1.lower()
    lower2 = word2.lower()

    if lower1 != lower2:
        return lower1 > lower2

    # Third Rule
    vowels1 = count_vowels(word1)
    vowels2 = count_vowels(word2)

    if vowels1 != vowels2:
        return vowels1 > vowels2

    # Forth Rule
    return False


def cryptic_sorter(strings: list[str]) -> list[str]:
    result = strings[:]
    n = len(result)

    for i in range(n):
        for j in range(0, n - i - 1):
            if should_swap(result[j], result[j + 1]):
                result[j], result[j + 1] = result[j + 1], result[j]
    return result

"""
if __name__ == "__main__":
    print(cryptic_sorter(["apple","cat","banana","dog","elephant"]))
    print(cryptic_sorter(["aaa","bbb","AAA","BBB"]))
    print(cryptic_sorter(["hello","world","hi","test"]))
    print(cryptic_sorter([]))
    print(cryptic_sorter([""]))
"""
