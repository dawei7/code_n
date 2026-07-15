from bisect import bisect_right
from typing import List


class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        candidates = sorted(set(arr2))
        states = {-1: 0}

        for value in arr1:
            next_states = {}
            for previous, operations in states.items():
                if value > previous:
                    next_states[value] = min(
                        next_states.get(value, float("inf")), operations
                    )

                replacement_index = bisect_right(candidates, previous)
                if replacement_index < len(candidates):
                    replacement = candidates[replacement_index]
                    next_states[replacement] = min(
                        next_states.get(replacement, float("inf")), operations + 1
                    )

            best_cost = float("inf")
            states = {}
            for previous, operations in sorted(next_states.items()):
                if operations < best_cost:
                    states[previous] = operations
                    best_cost = operations

            if not states:
                return -1

        return min(states.values())
