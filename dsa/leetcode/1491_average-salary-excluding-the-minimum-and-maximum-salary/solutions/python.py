"""Optimal app-local solution for LeetCode 1491."""


def solve(salary):
    """Return the mean after excluding one minimum and one maximum."""
    total = 0
    minimum = salary[0]
    maximum = salary[0]

    for value in salary:
        total += value
        if value < minimum:
            minimum = value
        if value > maximum:
            maximum = value

    return (total - minimum - maximum) / (len(salary) - 2)
