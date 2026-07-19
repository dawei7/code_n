"""Optimal app-local solution for LeetCode 1518."""


def solve(numBottles, numExchange):
    """Return the maximum number of full bottles that can be consumed."""
    return numBottles + (numBottles - 1) // (numExchange - 1)
