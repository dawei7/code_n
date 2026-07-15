from typing import List


class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        job_count = len(jobDifficulty)
        if job_count < d:
            return -1

        dp = [0] * job_count
        hardest = 0
        for index in range(job_count - 1, -1, -1):
            hardest = max(hardest, jobDifficulty[index])
            dp[index] = hardest

        for day_count in range(2, d + 1):
            next_dp = [float("inf")] * job_count
            for start in range(job_count - day_count + 1):
                hardest = 0
                last_cut = job_count - day_count
                for cut in range(start, last_cut + 1):
                    hardest = max(hardest, jobDifficulty[cut])
                    next_dp[start] = min(
                        next_dp[start], hardest + dp[cut + 1]
                    )
            dp = next_dp

        return dp[0]
