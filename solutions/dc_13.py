"""Solution for dc_13: Allocate Minimum Number of Pages.


            Given an array arr[] of n book page counts and m
            students, allocate contiguous page blocks to each
            student so that the maximum pages any one student
            gets is minimised. Binary search on the answer:
            for a candidate max `mx`, greedily assign pages to
            students, count how many are needed, and check if
            m is achievable. The minimum feasible `mx` is the
            answer.
            Source: https://www.geeksforgeeks.org/dsa/allocate-minimum-number-pages/
            

Inputs passed to solve():
    arr: list of n positive page counts.
    n: number of books (capped at 12 in tests).
    m: number of students (1 <= m <= n).

Goal:
    the minimum possible value of the maximum pages any student receives, as a non-negative int.

Samples:
Sample 1 input:  arr = [10, 20, 30, 40], n = 4, m = 2
Sample 1 output: 60

Sample 2 input:  arr = [10, 20, 30], n = 3, m = 1
Sample 2 output: 60

Sample 3 input:  arr = [10, 20, 30], n = 3, m = 3
Sample 3 output: 30

"""

def solve(arr, n, m):
    # Write your code here.
    return None
