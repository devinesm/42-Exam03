"""
Write a function that checks if the string 'small' is a subsequence
of 'big'. A subsequence means all characters of 'small' appear in 'big'
in the same order, but not necessarily consecutively.
Function is case-sensitive.

def hidenp(small: str, big: str) -> bool:
"""

def hidenp(small: str, big: str) -> bool:
    i = 0
    for c in big:
        if i < len(small) and small[i] == c:
            i += 1
    return i == len(small)

"""
if __name__ == "__main__":
    print(hidenp("abc", "a1b2c3"))
    print(hidenp("ace", "abcde"))
    print(hidenp("aec", "abcde"))
    print(hidenp("", "abc"))
    print(hidenp("abc", "ab"))
    print(hidenp("aaaa", "aaa"))
    print(hidenp("sing","subsequence testing"))
"""
