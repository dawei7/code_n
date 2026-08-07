from collections import Counter
from typing import List


class Solution:
    def distinctNumbers(self, nums: List[int], k: int) -> List[int]:
        frequencies = Counter(nums[:k])
        answer = [len(frequencies)]

        for right in range(k, len(nums)):
            outgoing = nums[right - k]
            frequencies[outgoing] -= 1
            if frequencies[outgoing] == 0:
                del frequencies[outgoing]

            frequencies[nums[right]] += 1
            answer.append(len(frequencies))

        return answer
