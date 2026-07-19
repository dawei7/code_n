class Solution:
    def dayOfYear(self, date: str) -> int:
        year, month, day = (int(part) for part in date.split("-"))
        month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            month_days[1] = 29
        return sum(month_days[: month - 1]) + day
