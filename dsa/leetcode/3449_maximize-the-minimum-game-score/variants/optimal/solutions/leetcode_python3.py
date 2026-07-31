from typing import List


class Solution:
    def maxScore(self, points: List[int], m: int) -> int:
        n = len(points)

        def feasible(target: int) -> bool:
            if target == 0:
                return True

            moves = 1
            incoming = 1

            for index in range(n - 1):
                required = (target + points[index] - 1) // points[index]

                if index == n - 2:
                    last_required = (target + points[index + 1] - 1) // points[index + 1]
                    need_current = max(0, required - incoming)

                    continue_moves = moves + 2 * need_current + 1
                    last_incoming = need_current + 1
                    continue_moves += 2 * max(0, last_required - last_incoming)

                    stop_moves = moves + 2 * max(need_current, last_required)
                    return min(continue_moves, stop_moves) <= m

                bounces = max(0, required - incoming)
                moves += 2 * bounces + 1
                if moves > m:
                    return False
                incoming = bounces + 1

            return False

        low = 0
        high = min(points) * m
        while low <= high:
            middle = (low + high) // 2
            if feasible(middle):
                low = middle + 1
            else:
                high = middle - 1

        return high
