class Solution:
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        reachable = 1

        for value in sorted(set(rewardValues)):
            reachable |= (reachable & ((1 << value) - 1)) << value

        return reachable.bit_length() - 1
