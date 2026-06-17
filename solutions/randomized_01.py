"""Solution for randomized_01: Randomized Quicksort.

Quicksort with a random pivot. Each partition picks a
random index in [lo, hi] and uses that as the pivot; this
breaks the pathological O(n^2) cases of deterministic
quicksort on sorted / reverse-sorted / all-equal input.
Expected O(n log n) regardless of input order.
Source: https://www.geeksforgeeks.org/quicksort-using-random-pivoting/

Inputs passed to solve():
    data: list of n random integers.
    n: length of data.

Goal:
    the sorted list.

Samples:
Sample 1 input:  data = [10, 7, 8, 9, 1, 5], n = 6
Sample 1 output: [1, 5, 7, 8, 9, 10]

Sample 2 input:  data = [1, 2, 3, 4, 5], n = 5
Sample 2 output: [1, 2, 3, 4, 5]


"""

def solve(data, n):
    # Write your code here.
    return None
