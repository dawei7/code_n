class Solution:
    def minCostSetTime(
        self,
        startAt: int,
        moveCost: int,
        pushCost: int,
        targetSeconds: int,
    ) -> int:
        def entry_cost(minutes: int, seconds: int) -> int:
            digits = f"{minutes:02d}{seconds:02d}".lstrip("0")
            finger = str(startAt)
            cost = 0

            for digit in digits:
                if digit != finger:
                    cost += moveCost
                    finger = digit
                cost += pushCost

            return cost

        best = float("inf")
        for minutes in range(100):
            seconds = targetSeconds - 60 * minutes
            if 0 <= seconds <= 99:
                best = min(best, entry_cost(minutes, seconds))

        return int(best)
