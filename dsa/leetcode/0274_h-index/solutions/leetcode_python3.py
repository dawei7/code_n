from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        paper_count = len(citations)
        buckets = [0] * (paper_count + 1)
        for citation_count in citations:
            buckets[min(citation_count, paper_count)] += 1
        qualifying = 0
        for h in range(paper_count, -1, -1):
            qualifying += buckets[h]
            if qualifying >= h:
                return h
        return 0
