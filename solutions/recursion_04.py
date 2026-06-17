"""Solution for recursion_04: Tower of Hanoi.

Move n disks from a source peg to a destination peg using
an auxiliary peg. One disk at a time; never place a larger
disk on a smaller one. The classic recurrence: move n-1
from source to auxiliary, move the largest, move n-1 from
auxiliary to destination.
Return the sequence of (from, to) moves.
Source: https://www.geeksforgeeks.org/c-program-for-tower-of-hanoi/

Inputs passed to solve():
    n: number of disks (capped at 8 in the setup).
    source: source peg name (always 'A').
    destination: destination peg name (always 'C').
    auxiliary: auxiliary peg name (always 'B').

Goal:
    a list of (from, to) moves - 2^n - 1 in total.

Samples:
Sample 1 input:  n = 1, source = "A", destination = "C", auxiliary = "B"
Sample 1 output: [('A', 'C')]

Sample 2 input:  n = 2, source = "A", destination = "C", auxiliary = "B"
Sample 2 output: [('A', 'B'), ('A', 'C'), ('B', 'C')]


"""

def solve(n, source, destination, auxiliary):
    # Write your code here.
    return None
