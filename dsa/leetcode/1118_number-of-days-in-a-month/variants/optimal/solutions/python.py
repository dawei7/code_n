"""Optimal app-local solution for LeetCode 1118."""


def solve(year, month):
    if month == 2:
        leap = year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)
        return 29 if leap else 28
    return 30 if month in {4, 6, 9, 11} else 31
