class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        ordered_happiness = sorted(happiness, reverse=True)
        total = 0

        for turn in range(k):
            contribution = ordered_happiness[turn] - turn
            if contribution <= 0:
                break
            total += contribution

        return total
