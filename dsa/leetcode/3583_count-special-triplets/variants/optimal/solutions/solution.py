from collections import Counter


class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        modulo = 1_000_000_007
        left = Counter()
        right = Counter(nums)
        answer = 0

        for value in nums:
            right[value] -= 1
            target = value * 2
            answer = (answer + left[target] * right[target]) % modulo
            left[value] += 1

        return answer
