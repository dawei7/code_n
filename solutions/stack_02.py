"""Solution for stack_02: Next Greater Element.

For each index i, return the next value to the right that's
strictly greater than arr[i], or -1 if none. Monotonic stack
of indices: pop while arr[i] > arr[top], record arr[i] as the
answer for the popped index.
Requirement: O(n) time.
Source: https://www.geeksforgeeks.org/next-greater-element/

Inputs passed to solve():
    arr: list of n random integers.
    n: length of arr.

Goal:
    a list of n values (each the next greater to the right, or -1).

Samples:
Sample 1 input:  arr = [4, 5, 2, 25], n = 4
Sample 1 output: [5, 25, 25, -1]

Sample 2 input:  arr = [13, 7, 6, 12], n = 4
Sample 2 output: [-1, 12, 12, -1]


"""

def solve(arr, n):
    # Write your code here.
    return None
