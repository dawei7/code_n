from collections import Counter, defaultdict
from itertools import combinations


class Solution:
    def mostVisitedPattern(
        self, username: List[str], timestamp: List[int], website: List[str]
    ) -> List[str]:
        histories = defaultdict(list)
        for _, user, site in sorted(zip(timestamp, username, website)):
            histories[user].append(site)

        scores = Counter()
        for sites in histories.values():
            scores.update(set(combinations(sites, 3)))

        best = min(scores, key=lambda pattern: (-scores[pattern], pattern))
        return list(best)
