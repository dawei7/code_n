from typing import List


class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        prefix = [0]
        for value in skill:
            prefix.append(prefix[-1] + value)

        start = 0
        previous_mana = mana[0]
        for current_mana in mana[1:]:
            start = max(
                start + previous_mana * prefix[wizard + 1]
                - current_mana * prefix[wizard]
                for wizard in range(len(skill))
            )
            previous_mana = current_mana

        return start + previous_mana * prefix[-1]
