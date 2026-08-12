import datetime


def solve() -> int:
    """Count how many Sundays fell on the 1st of the month from 1901 to 2000.
    
    Time Complexity: O(Y * M)
    Space Complexity: O(1)
    """
    sundays = 0
    for year in range(1901, 2001):
        for month in range(1, 13):
            if datetime.date(year, month, 1).weekday() == 6:
                sundays += 1
    return sundays
