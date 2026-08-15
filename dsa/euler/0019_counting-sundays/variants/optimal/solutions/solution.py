def solve() -> int:
    """Count how many Sundays fell on the 1st of the month during the 20th century (1901 to 2000).

    Problem Context & Mathematical Principles:
    -------------------------------------------
    1. Gregorian Calendar Leap Year Rules:
       A year is a leap year (366 days) if it is divisible by 4, except end-of-century
       years which must also be divisible by 400:
           is_leap(y) = (y % 4 == 0) and (y % 100 != 0 or y % 400 == 0)

    2. Day-of-Week Modular Progression:
       Represent days of the week modulo 7 where:
           0: Monday, 1: Tuesday, ..., 5: Saturday, 6: Sunday.
       - Jan 1, 1900 was a Monday (day 0).
       - 1900 was not a leap year (365 days, 365 = 52 * 7 + 1), so Jan 1, 1901 was day 1 (Tuesday).
       - Advancing from month m to m + 1 increments the 1st day of the week by (days_in_month % 7).

    3. Pure Arithmetic Counting:
       Stepping through each of the 1200 months in [1901, 2000], we count months where day % 7 == 6.

    Complexity:
    -----------
    - Time Complexity: O(Y * M) across 100 years and 12 months (1,200 steps, ~0.0001s).
    - Space Complexity: O(1) constant auxiliary space.
    """
    # Standard month lengths (index 1 to 12)
    month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Jan 1, 1900 was Monday (0). Jan 1, 1901 was Tuesday (1)
    day = 1
    sunday_count = 0

    for year in range(1901, 2001):
        is_leap = (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0)
        for month in range(1, 13):
            # Check if 1st day of current month is Sunday (6 mod 7)
            if day % 7 == 6:
                sunday_count += 1

            # Advance day by number of days in current month
            days = 29 if (month == 2 and is_leap) else month_days[month]
            day += days

    return sunday_count


if __name__ == "__main__":
    print(solve())
