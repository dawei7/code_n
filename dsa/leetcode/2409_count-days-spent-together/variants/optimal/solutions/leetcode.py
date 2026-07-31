class Solution:
    def countDaysTogether(
        self,
        arriveAlice: str,
        leaveAlice: str,
        arriveBob: str,
        leaveBob: str,
    ) -> int:
        days_before_month = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]

        def ordinal(date: str) -> int:
            month = int(date[:2])
            day = int(date[3:])
            return days_before_month[month - 1] + day

        overlap_start = max(ordinal(arriveAlice), ordinal(arriveBob))
        overlap_end = min(ordinal(leaveAlice), ordinal(leaveBob))
        return max(0, overlap_end - overlap_start + 1)
