from typing import List


class Solution:
    def maxRatings(self, units: List[List[int]]) -> int:
        if len(units[0]) == 1:
            return sum(row[0] for row in units)

        global_minimum = float("inf")
        minimum_second = float("inf")
        second_sum = 0

        for row in units:
            first = float("inf")
            second = float("inf")
            for value in row:
                if value < first:
                    first, second = value, first
                elif value < second:
                    second = value

            global_minimum = min(global_minimum, first)
            minimum_second = min(minimum_second, second)
            second_sum += second

        return int(global_minimum + second_sum - minimum_second)
