"""Reference solution for LeetCode 1360."""


DAYS_BEFORE_MONTH = (0, 0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334)


def _ordinal(date):
    year, month, day = map(int, date.split("-"))
    previous_year = year - 1
    days = (
        365 * previous_year
        + previous_year // 4
        - previous_year // 100
        + previous_year // 400
    )
    days += DAYS_BEFORE_MONTH[month] + day
    if month > 2 and (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)):
        days += 1
    return days


def solve(date1, date2):
    return abs(_ordinal(date1) - _ordinal(date2))
