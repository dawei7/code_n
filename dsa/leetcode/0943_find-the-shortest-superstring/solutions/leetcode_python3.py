from typing import List


class Solution:
    def shortestSuperstring(self, words: List[str]) -> str:
        n = len(words)
        overlap = [[0] * n for _ in range(n)]
        for left in range(n):
            for right in range(n):
                if left == right:
                    continue
                limit = min(len(words[left]), len(words[right]))
                for length in range(limit, 0, -1):
                    if words[left].endswith(words[right][:length]):
                        overlap[left][right] = length
                        break

        state_count = 1 << n
        dp = [[-1] * n for _ in range(state_count)]
        parent = [[-1] * n for _ in range(state_count)]
        for index in range(n):
            dp[1 << index][index] = 0

        for mask in range(1, state_count):
            for last in range(n):
                if not mask & (1 << last):
                    continue
                previous_mask = mask ^ (1 << last)
                if previous_mask == 0:
                    continue
                for previous in range(n):
                    if dp[previous_mask][previous] < 0:
                        continue
                    candidate = dp[previous_mask][previous] + overlap[previous][last]
                    if candidate > dp[mask][last]:
                        dp[mask][last] = candidate
                        parent[mask][last] = previous

        full_mask = state_count - 1
        last = max(range(n), key=lambda index: dp[full_mask][index])
        order = []
        mask = full_mask
        while last != -1:
            order.append(last)
            previous = parent[mask][last]
            mask ^= 1 << last
            last = previous
        order.reverse()

        result = words[order[0]]
        for left, right in zip(order, order[1:]):
            result += words[right][overlap[left][right]:]
        return result
