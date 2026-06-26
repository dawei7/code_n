"""Optimal solution for recursion_04: Tower of Hanoi.

Move n disks from source to destination using an auxiliary
peg. The optimal recurrence is: move n-1 disks from source
to auxiliary, move the largest disk, move n-1 disks from
auxiliary to destination. Returns the sequence of moves as
a list of (from, to) tuples.
"""


def solve(n, source, destination, auxiliary):
    moves = []

    def helper(count, src, dst, aux):
        if count == 0:
            return
        helper(count - 1, src, aux, dst)
        moves.append((src, dst))
        helper(count - 1, aux, dst, src)

    helper(n, source, destination, auxiliary)
    return moves
