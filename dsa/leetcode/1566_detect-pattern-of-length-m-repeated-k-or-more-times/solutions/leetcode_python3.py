from typing import List


class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        equal_offset_run = 0

        for index in range(len(arr) - m):
            if arr[index] == arr[index + m]:
                equal_offset_run += 1
                if equal_offset_run == m * (k - 1):
                    return True
            else:
                equal_offset_run = 0

        return False
