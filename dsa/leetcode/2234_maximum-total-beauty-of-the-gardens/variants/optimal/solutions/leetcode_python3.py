from bisect import bisect_left
from typing import List


class Solution:
    def maximumBeauty(
        self,
        flowers: List[int],
        newFlowers: int,
        target: int,
        full: int,
        partial: int,
    ) -> int:
        flowers = sorted(min(value, target) for value in flowers)
        count = len(flowers)
        prefix = [0]
        for value in flowers:
            prefix.append(prefix[-1] + value)

        already_complete = count - bisect_left(flowers, target)
        answer = 0

        for complete_count in range(already_complete, count + 1):
            incomplete_count = count - complete_count
            completion_cost = (
                complete_count * target
                - (prefix[count] - prefix[incomplete_count])
            )
            if completion_cost > newFlowers:
                break

            beauty = complete_count * full
            if incomplete_count:
                remaining = newFlowers - completion_cost
                low = flowers[0]
                high = target - 1
                while low <= high:
                    level = (low + high) // 2
                    raised_count = bisect_left(
                        flowers,
                        level,
                        0,
                        incomplete_count,
                    )
                    cost = level * raised_count - prefix[raised_count]
                    if cost <= remaining:
                        low = level + 1
                    else:
                        high = level - 1
                beauty += high * partial

            answer = max(answer, beauty)

        return answer
