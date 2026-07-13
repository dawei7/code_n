from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        path = []

        def search(start: int, remaining: int) -> None:
            if remaining == 0:
                result.append(path[:])
                return
            for index in range(start, len(candidates)):
                if index > start and candidates[index] == candidates[index - 1]:
                    continue
                value = candidates[index]
                if value > remaining:
                    break
                path.append(value)
                search(index + 1, remaining - value)
                path.pop()

        search(0, target)
        return result
