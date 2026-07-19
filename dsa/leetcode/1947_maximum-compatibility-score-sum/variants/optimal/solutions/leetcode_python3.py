from typing import List


class Solution:
    def maxCompatibilitySum(
        self,
        students: List[List[int]],
        mentors: List[List[int]],
    ) -> int:
        count = len(students)
        scores = [
            [
                sum(a == b for a, b in zip(student, mentor))
                for mentor in mentors
            ]
            for student in students
        ]

        dp = [-1] * (1 << count)
        dp[0] = 0

        for mask in range(1 << count):
            student = mask.bit_count()
            if student == count:
                continue

            for mentor in range(count):
                bit = 1 << mentor
                if not mask & bit:
                    next_mask = mask | bit
                    dp[next_mask] = max(
                        dp[next_mask],
                        dp[mask] + scores[student][mentor],
                    )

        return dp[-1]
