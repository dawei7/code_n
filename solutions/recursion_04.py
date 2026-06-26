"""
Description
-----------
Move n disks from a source peg to a destination peg using
an auxiliary peg. One disk at a time; never place a larger
disk on a smaller one. The classic recurrence: move n-1
from source to auxiliary, move the largest, move n-1 from
auxiliary to destination.
Return the sequence of (from, to) moves.
Source: https://www.geeksforgeeks.org/c-program-for-tower-of-hanoi/

Examples
--------
Example 1:
Input:  n = 1, source = "A", destination = "C", auxiliary = "B"
Output: [('A', 'C')]

Example 2:
Input:  n = 2, source = "A", destination = "C", auxiliary = "B"
Output: [('A', 'B'), ('A', 'C'), ('B', 'C')]
"""

def solve(n, source, destination, auxiliary):
    # Write your code here.
    return None
