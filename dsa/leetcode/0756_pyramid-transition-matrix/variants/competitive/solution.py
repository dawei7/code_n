from collections import defaultdict
from functools import cache
from typing import List


class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        transitions = defaultdict(list)
        for rule in allowed:
            transitions[rule[:2]].append(rule[2])

        @cache
        def can_build(row: str) -> bool:
            if len(row) == 1:
                return True

            next_row = []

            def build(position: int) -> bool:
                if position == len(row) - 1:
                    return can_build("".join(next_row))

                for top in transitions.get(row[position : position + 2], ()):
                    next_row.append(top)
                    if build(position + 1):
                        return True
                    next_row.pop()
                return False

            return build(0)

        return can_build(bottom)
