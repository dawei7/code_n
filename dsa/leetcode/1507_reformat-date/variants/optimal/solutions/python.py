"""Optimal app-local solution for LeetCode 1507."""


def solve(date: str) -> str:
    """Convert an ordinal English date to YYYY-MM-DD."""
    day, month, year = date.split()
    months = {
        "Jan": "01",
        "Feb": "02",
        "Mar": "03",
        "Apr": "04",
        "May": "05",
        "Jun": "06",
        "Jul": "07",
        "Aug": "08",
        "Sep": "09",
        "Oct": "10",
        "Nov": "11",
        "Dec": "12",
    }
    return f"{year}-{months[month]}-{int(day[:-2]):02d}"
