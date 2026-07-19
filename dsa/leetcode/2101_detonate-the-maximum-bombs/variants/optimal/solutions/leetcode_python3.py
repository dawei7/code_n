from typing import List


class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        adjacency = [[] for _ in range(n)]

        for source, (x_source, y_source, radius) in enumerate(bombs):
            radius_squared = radius * radius
            for target, (x_target, y_target, _) in enumerate(bombs):
                if source == target:
                    continue
                dx = x_source - x_target
                dy = y_source - y_target
                if dx * dx + dy * dy <= radius_squared:
                    adjacency[source].append(target)

        maximum = 1
        for start in range(n):
            seen = {start}
            stack = [start]
            while stack:
                bomb = stack.pop()
                for neighbor in adjacency[bomb]:
                    if neighbor not in seen:
                        seen.add(neighbor)
                        stack.append(neighbor)
            maximum = max(maximum, len(seen))
        return maximum
