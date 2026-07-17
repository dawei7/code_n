from typing import List


class Solution:
    def maximumBeauty(self, flowers: List[int]) -> int:
        positive_sum = 0
        best_start = {}
        answer = float("-inf")

        for beauty in flowers:
            if beauty in best_start:
                answer = max(
                    answer,
                    beauty + positive_sum + best_start[beauty],
                )

            positive_sum += max(beauty, 0)
            start_score = beauty - positive_sum
            if beauty not in best_start:
                best_start[beauty] = start_score
            else:
                best_start[beauty] = max(
                    best_start[beauty],
                    start_score,
                )

        return answer
