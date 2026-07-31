from collections import defaultdict
from typing import List


class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        totals = defaultdict(int)
        best = {}

        for creator, video_id, view_count in zip(creators, ids, views):
            totals[creator] += view_count
            if (
                creator not in best
                or view_count > best[creator][0]
                or (view_count == best[creator][0] and video_id < best[creator][1])
            ):
                best[creator] = (view_count, video_id)

        maximum = max(totals.values())
        return [[creator, best[creator][1]] for creator, total in totals.items() if total == maximum]
