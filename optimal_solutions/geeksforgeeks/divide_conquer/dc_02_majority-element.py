"""Optimal solution for dc_02: Majority Element.

Boyer-Moore: track a candidate and a counter. Walk the array;
on each new element, if the counter is zero, promote it to
candidate. Increment on a match, decrement otherwise. The
candidate at the end is the majority element if one exists.
The setup always produces a list with a majority, so the
candidate is the answer.
"""


def solve(arr, n):
    if n == 0:
        return -1
    candidate = None
    count = 0
    for value in arr:
        if count == 0:
            candidate = value
        count += 1 if value == candidate else -1
    return candidate
