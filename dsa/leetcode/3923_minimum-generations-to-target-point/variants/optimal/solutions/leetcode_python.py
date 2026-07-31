from typing import List


class Solution:
    def minGenerations(
        self, points: List[List[int]], target: List[int]
    ) -> int:
        target_point = tuple(target)
        known = {tuple(point) for point in points}
        if target_point in known:
            return 0

        frontier = set(known)
        generation = 1

        while frontier:
            available = tuple(known)
            produced = set()

            for a in frontier:
                for b in available:
                    if a == b or (b in frontier and b < a):
                        continue

                    midpoint = (
                        (a[0] + b[0]) // 2,
                        (a[1] + b[1]) // 2,
                        (a[2] + b[2]) // 2,
                    )
                    if midpoint not in known:
                        produced.add(midpoint)

            if target_point in produced:
                return generation
            if not produced:
                return -1

            known.update(produced)
            frontier = produced
            generation += 1

        return -1
