class Solution:
    def minimumLevels(self, possible: List[int]) -> int:
        total = sum(1 if value else -1 for value in possible)
        alice = 0

        for levels in range(1, len(possible)):
            alice += 1 if possible[levels - 1] else -1
            if alice > total - alice:
                return levels

        return -1
