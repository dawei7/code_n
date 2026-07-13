class Solution:
    def maxA(self, n: int) -> int:
        best = [0] * (n + 1)
        for presses in range(1, n + 1):
            best[presses] = best[presses - 1] + 1
            for multiplier in range(2, 6):
                phase_cost = multiplier + 1
                if phase_cost <= presses:
                    best[presses] = max(
                        best[presses],
                        best[presses - phase_cost] * multiplier,
                    )
        return best[n]
