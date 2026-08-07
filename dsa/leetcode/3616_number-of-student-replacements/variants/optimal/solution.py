from typing import List


class Solution:
    def totalReplacements(self, ranks: List[int]) -> int:
        best_rank = ranks[0]
        replacements = 0

        for rank in ranks:
            if rank < best_rank:
                best_rank = rank
                replacements += 1

        return replacements
