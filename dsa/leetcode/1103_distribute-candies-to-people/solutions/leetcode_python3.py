from math import isqrt
from typing import List


class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        complete_gifts = (isqrt(8 * candies + 1) - 1) // 2
        remaining = candies - complete_gifts * (complete_gifts + 1) // 2
        distribution = [0] * num_people

        for person in range(num_people):
            if person >= complete_gifts:
                break
            gift_count = (complete_gifts - 1 - person) // num_people + 1
            distribution[person] = gift_count * (
                2 * (person + 1) + (gift_count - 1) * num_people
            ) // 2

        if remaining:
            distribution[complete_gifts % num_people] += remaining
        return distribution
