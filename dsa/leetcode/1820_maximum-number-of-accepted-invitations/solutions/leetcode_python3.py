from typing import List


class Solution:
    def maximumInvitations(self, grid: List[List[int]]) -> int:
        matched_boy = [-1] * len(grid[0])

        def augment(boy: int, seen: list[bool]) -> bool:
            for girl, acceptable in enumerate(grid[boy]):
                if not acceptable or seen[girl]:
                    continue
                seen[girl] = True
                if matched_boy[girl] == -1 or augment(
                    matched_boy[girl], seen
                ):
                    matched_boy[girl] = boy
                    return True
            return False

        answer = 0
        for boy in range(len(grid)):
            if augment(boy, [False] * len(grid[0])):
                answer += 1
        return answer
