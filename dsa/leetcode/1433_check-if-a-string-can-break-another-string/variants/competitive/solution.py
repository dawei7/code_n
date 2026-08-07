class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        counts1 = [0] * 26
        counts2 = [0] * 26
        for left, right in zip(s1, s2):
            counts1[ord(left) - ord("a")] += 1
            counts2[ord(right) - ord("a")] += 1

        balance = 0
        saw_positive = False
        saw_negative = False
        for left_count, right_count in zip(counts1, counts2):
            balance += left_count - right_count
            saw_positive |= balance > 0
            saw_negative |= balance < 0
            if saw_positive and saw_negative:
                return False
        return True
