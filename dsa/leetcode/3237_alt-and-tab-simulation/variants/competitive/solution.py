from typing import List


class Solution:
    def simulationResult(
        self,
        windows: List[int],
        queries: List[int],
    ) -> List[int]:
        seen = set()
        result = []

        for window in reversed(queries):
            if window not in seen:
                seen.add(window)
                result.append(window)

        result.extend(window for window in windows if window not in seen)
        return result
