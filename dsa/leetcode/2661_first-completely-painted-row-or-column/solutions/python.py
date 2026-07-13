from typing import List

def solve(arr: List[int], mat: List[List[int]]) -> int:
    m = len(mat)
    n = len(mat[0])

    # Step 1: Pre-process mat to store the position of each number
    # pos_map[value] = (row_index, col_index)
    pos_map = {}
    for r in range(m):
        for c in range(n):
            pos_map[mat[r][c]] = (r, c)

    # Step 2: Initialize counters for each row and column
    # row_counts[r] stores how many numbers are left to paint in row r
    # col_counts[c] stores how many numbers are left to paint in column c
    row_counts = [n] * m  # Each row initially needs 'n' numbers to be painted
    col_counts = [m] * n  # Each column initially needs 'm' numbers to be painted

    # Step 3: Iterate through arr, painting numbers and checking for completion
    for k, num in enumerate(arr):
        r, c = pos_map[num]

        # Decrement the count for the corresponding row and column
        row_counts[r] -= 1
        col_counts[c] -= 1

        # Check if this painting completed a row or a column
        if row_counts[r] == 0 or col_counts[c] == 0:
            return k
    
    # This line should theoretically not be reached given problem constraints
    # as a row or column must eventually be completed.
    return -1
