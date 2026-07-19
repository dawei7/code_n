class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        days_before_month = (0, 0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334)

        def ordinal(date: str) -> int:
            year, month, day = map(int, date.split("-"))
            previous_year = year - 1
            days = (
                365 * previous_year
                + previous_year // 4
                - previous_year // 100
                + previous_year // 400
            )
            days += days_before_month[month] + day
            if month > 2 and (
                year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)
            ):
                days += 1
            return days

        return abs(ordinal(date1) - ordinal(date2))
