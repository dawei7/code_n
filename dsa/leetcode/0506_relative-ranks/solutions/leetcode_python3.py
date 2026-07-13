from typing import List


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        order = sorted(range(len(score)), key=score.__getitem__, reverse=True)
        answer = [""] * len(score)
        medals = ("Gold Medal", "Silver Medal", "Bronze Medal")
        for rank, index in enumerate(order, start=1):
            answer[index] = medals[rank - 1] if rank <= 3 else str(rank)
        return answer
