from typing import List


class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        state_count = 1 << len(tasks)
        best = [(len(tasks) + 1, 0)] * state_count
        best[0] = (1, 0)

        for mask in range(state_count):
            sessions, used = best[mask]
            for index, duration in enumerate(tasks):
                if mask >> index & 1:
                    continue
                next_mask = mask | 1 << index
                if used + duration <= sessionTime:
                    candidate = (sessions, used + duration)
                else:
                    candidate = (sessions + 1, duration)
                if candidate < best[next_mask]:
                    best[next_mask] = candidate

        return best[-1][0]
