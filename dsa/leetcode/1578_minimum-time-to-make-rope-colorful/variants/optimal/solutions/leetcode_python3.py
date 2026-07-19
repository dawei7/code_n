class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        total = 0
        previous_color = ""
        kept_time = 0

        for color, removal_time in zip(colors, neededTime):
            if color == previous_color:
                total += min(kept_time, removal_time)
                kept_time = max(kept_time, removal_time)
            else:
                previous_color = color
                kept_time = removal_time

        return total
