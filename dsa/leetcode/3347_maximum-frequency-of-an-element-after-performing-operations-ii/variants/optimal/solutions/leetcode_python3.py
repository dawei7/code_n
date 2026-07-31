from collections import Counter, defaultdict


class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        counts = Counter(nums)
        events = defaultdict(int)

        for value in nums:
            events[value - k] += 1
            events[value + k + 1] -= 1

        for value in counts:
            events[value] += 0

        reachable = 0
        best = 0
        for target in sorted(events):
            reachable += events[target]
            unchanged = counts[target]
            best = max(
                best,
                unchanged + min(numOperations, reachable - unchanged),
            )

        return best
