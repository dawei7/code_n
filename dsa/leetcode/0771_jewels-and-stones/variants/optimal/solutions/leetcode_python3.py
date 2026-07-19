class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewel_types = set(jewels)
        return sum(stone in jewel_types for stone in stones)
