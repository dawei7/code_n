from typing import List


class Solution:
    def canEat(
        self, candiesCount: List[int], queries: List[List[int]]
    ) -> List[bool]:
        prefix = [0]
        for count in candiesCount:
            prefix.append(prefix[-1] + count)

        answer = []
        for favorite_type, favorite_day, daily_cap in queries:
            minimum_eaten = favorite_day + 1
            maximum_eaten = minimum_eaten * daily_cap
            before = prefix[favorite_type]
            through = prefix[favorite_type + 1]
            answer.append(before < maximum_eaten and minimum_eaten <= through)

        return answer
