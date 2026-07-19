from typing import List


class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        net_right = sum(
            amount if direction == 1 else -amount
            for direction, amount in shift
        )
        net_right %= len(s)
        if net_right == 0:
            return s
        return s[-net_right:] + s[:-net_right]
