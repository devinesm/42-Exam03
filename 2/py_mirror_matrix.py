"""
Given a 2D matrix (list of lists), return a new matrix where each row
is reversed.

def mirror_matrix(matrix: list[list[int]]) -> list[list[int]]:
"""

def mirror_matrix(matrix: list[list[int]]) -> list[list[int]]:
    return [row[::-1] for row in matrix]

"""
if __name__ == "__main__":
    print(mirror_matrix([[1,2,3],[4,5,6]]))
    print(mirror_matrix([[1,2],[3,4],[5,6]]))
    print(mirror_matrix([[7]]))
    print(mirror_matrix([[1,2,3,4]]))
    print(mirror_matrix([[-1,-2],[-3,-4]]))
"""
