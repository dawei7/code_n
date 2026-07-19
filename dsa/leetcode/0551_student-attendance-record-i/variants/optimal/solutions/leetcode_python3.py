class Solution:
    def checkRecord(self, s: str) -> bool:
        absences = 0
        late_streak = 0

        for status in s:
            if status == "A":
                absences += 1

            if status == "L":
                late_streak += 1
            else:
                late_streak = 0

            if absences >= 2 or late_streak >= 3:
                return False

        return True

