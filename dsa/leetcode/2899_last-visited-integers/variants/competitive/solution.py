from typing import List


class Solution:
    def lastVisitedIntegers(self, nums: List[int]) -> List[int]:
        seen = []
        answer = []
        consecutive_queries = 0

        for value in nums:
            if value == -1:
                consecutive_queries += 1
                if consecutive_queries <= len(seen):
                    answer.append(seen[-consecutive_queries])
                else:
                    answer.append(-1)
            else:
                seen.append(value)
                consecutive_queries = 0

        return answer
