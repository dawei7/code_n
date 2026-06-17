"""Solution for bit_05: Single Number III.

Every element in the input array appears exactly
twice except for TWO elements, which each appear
once. Return those two unique values (sorted).
XOR everything to find a bit that differs between
the two uniques, then split the array by that bit
and XOR each half to recover each unique value.
O(n) time, O(1) extra space.
Source: https://www.geeksforgeeks.org/find-two-non-repeating-elements-given-array/

Inputs passed to solve():
    arr: list of integers; two unique values, others appear twice.

Goal:
    a sorted list [a, b] of the two unique elements.

Samples:
Sample 1 input:  arr = [1, 2, 3, 2, 1, 4]
Sample 1 output: [3, 4]

Sample 2 input:  arr = [1, 1, 2, 3]
Sample 2 output: [2, 3]


"""

def solve(arr):
    # Write your code here.
    return None
