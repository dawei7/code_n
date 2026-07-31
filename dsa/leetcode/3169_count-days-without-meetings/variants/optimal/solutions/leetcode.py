class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        covered = 0
        current_end = 0

        for start, end in sorted(meetings):
            if end > current_end:
                covered += end - max(start, current_end + 1) + 1
                current_end = end

        return days - covered
