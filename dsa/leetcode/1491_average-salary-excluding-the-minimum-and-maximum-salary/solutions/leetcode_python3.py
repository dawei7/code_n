from typing import List


class Solution:
    def average(self, salary: List[int]) -> float:
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

