from collections import deque
from typing import List


class Solution:
    def maximumSum(
        self, nums: List[int], m: int, l: int, r: int
    ) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)
        for index, value in enumerate(nums):
            prefix[index + 1] = prefix[index] + value

        negative_infinity = float("-inf")
        previous = [0] * (n + 1)
        answer = negative_infinity

        for _ in range(min(m, n // l)):
            current = [negative_infinity] * (n + 1)
            candidates = deque()

            for end in range(1, n + 1):
                start = end - l
                if start >= 0 and previous[start] != negative_infinity:
                    candidate = previous[start] - prefix[start]
                    while (
                        candidates
                        and previous[candidates[-1]] - prefix[candidates[-1]]
                        <= candidate
                    ):
                        candidates.pop()
                    candidates.append(start)

                while candidates and candidates[0] < end - r:
                    candidates.popleft()

                current[end] = current[end - 1]
                if candidates:
                    current[end] = max(
                        current[end],
                        prefix[end]
                        + previous[candidates[0]]
                        - prefix[candidates[0]],
                    )

            answer = max(answer, current[n])
            previous = current

        return answer
