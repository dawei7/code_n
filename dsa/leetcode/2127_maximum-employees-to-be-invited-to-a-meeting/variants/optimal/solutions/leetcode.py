from collections import deque
from typing import List


class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        n = len(favorite)
        indegree = [0] * n
        for person in favorite:
            indegree[person] += 1

        depth = [1] * n
        queue = deque(i for i, degree in enumerate(indegree) if degree == 0)
        while queue:
            employee = queue.popleft()
            person = favorite[employee]
            depth[person] = max(depth[person], depth[employee] + 1)
            indegree[person] -= 1
            if indegree[person] == 0:
                queue.append(person)

        longest_cycle = 0
        extended_pairs = 0
        for start in range(n):
            if indegree[start] == 0:
                continue

            cycle_length = 0
            employee = start
            while indegree[employee] > 0:
                indegree[employee] = 0
                cycle_length += 1
                employee = favorite[employee]

            if cycle_length == 2:
                extended_pairs += depth[start] + depth[favorite[start]]
            else:
                longest_cycle = max(longest_cycle, cycle_length)

        return max(longest_cycle, extended_pairs)
