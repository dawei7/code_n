from typing import List


class Solution:
    def digArtifacts(self, n: int, artifacts: List[List[int]], dig: List[List[int]]) -> int:
        dug = {(row, column) for row, column in dig}
        extracted = 0

        for top, left, bottom, right in artifacts:
            complete = True
            for row in range(top, bottom + 1):
                for column in range(left, right + 1):
                    if (row, column) not in dug:
                        complete = False
                        break
                if not complete:
                    break
            if complete:
                extracted += 1

        return extracted
