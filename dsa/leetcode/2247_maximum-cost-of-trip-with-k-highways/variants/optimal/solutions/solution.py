from typing import List


class Solution:
    def maximumCost(self, n: int, highways: List[List[int]], k: int) -> int:
        if k >= n:
            return -1

        adjacency = [[] for _ in range(n)]
        for first, second, toll in highways:
            adjacency[first].append((second, toll))
            adjacency[second].append((first, toll))

        states = {(1 << city, city): 0 for city in range(n)}
        for _ in range(k):
            next_states = {}
            for (mask, city), cost in states.items():
                for neighbor, toll in adjacency[city]:
                    bit = 1 << neighbor
                    if mask & bit:
                        continue
                    state = (mask | bit, neighbor)
                    next_states[state] = max(next_states.get(state, -1), cost + toll)
            states = next_states
            if not states:
                return -1
        return max(states.values(), default=-1)
