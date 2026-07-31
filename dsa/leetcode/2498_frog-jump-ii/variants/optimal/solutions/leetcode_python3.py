class Solution:
    def maxJump(self, stones: List[int]) -> int:
        if len(stones) == 2:
            return stones[1] - stones[0]

        return max(
            stones[index] - stones[index - 2]
            for index in range(2, len(stones))
        )
