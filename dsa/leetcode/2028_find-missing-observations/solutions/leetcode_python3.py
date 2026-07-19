from typing import List


class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        missing_sum = mean * (len(rolls) + n) - sum(rolls)
        if missing_sum < n or missing_sum > 6 * n:
            return []

        quotient, remainder = divmod(missing_sum, n)
        return [quotient + 1] * remainder + [quotient] * (n - remainder)
