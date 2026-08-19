"""
Write a function that rotates an array to the right by k positions.
Rotating right by k means the last k elements move to the front.

def twist_sequence(arr: list[int], k: int) -> list[int]:
"""

def twist_sequence(arr: list[int], k: int) -> list[int]:
    if not arr:
        return []
    k = k % len(arr)

    new = []
    cut_point = start = len(arr) - k

    while start < (len(arr)):
        new.append(arr[start])
        start += 1

    i = 0
    while i < cut_point:
        new.append(arr[i])
        i += 1
    return new

"""
if __name__ == "__main__":
    print(twist_sequence([1,2,3,4,5], 2))
    print(twist_sequence([1,2,3], 1))
    print(twist_sequence([1,2,3,4], 0))
    print(twist_sequence([1,2,3], 5))
    print(twist_sequence([], 3))
"""
