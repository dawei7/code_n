class Solution:
    def maximumBags(
        self,
        capacity: List[int],
        rocks: List[int],
        additionalRocks: int,
    ) -> int:
        deficits = sorted(
            maximum - current
            for maximum, current in zip(capacity, rocks)
        )
        full_bags = 0

        for deficit in deficits:
            if deficit > additionalRocks:
                break
            additionalRocks -= deficit
            full_bags += 1

        return full_bags
