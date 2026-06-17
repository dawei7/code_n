"""Solution for dc_02: Majority Element.

The setup always generates a list with a majority element
(occurs strictly more than n/2 times). Find and return that
value. Boyer-Moore: track a candidate and counter; promote on
counter=0, increment on match, decrement on mismatch. The
final candidate is the majority if one exists.
Requirement: O(n) time, O(1) space.
Source: https://www.geeksforgeeks.org/majority-element/

Inputs passed to solve():
    arr: list of n integers (always has a majority).
    n: length of arr.

Goal:
    the majority element (the one that appears > n/2 times).

Samples:
Sample 1 input:  arr = [3, 1, 3, 3, 2], n = 5
Sample 1 output: 3

Sample 2 input:  arr = [1], n = 1
Sample 2 output: 1


"""

def solve(arr, n):
    # Write your code here.
    return None
