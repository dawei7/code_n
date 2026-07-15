class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        if month < 3:
            month += 12
            year -= 1

        century = year // 100
        year_in_century = year % 100
        weekday = (
            century // 4
            - 2 * century
            + year_in_century
            + year_in_century // 4
            + 13 * (month + 1) // 5
            + day
            - 1
        ) % 7
        names = [
            "Sunday",
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
        ]
        return names[weekday]
