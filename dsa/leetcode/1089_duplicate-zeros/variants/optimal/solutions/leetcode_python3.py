from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        duplicates = 0
        last = len(arr) - 1
        source = 0

        while source <= last - duplicates:
            if arr[source] == 0:
                if source == last - duplicates:
                    arr[last] = 0
                    last -= 1
                    break
                duplicates += 1
            source += 1

        for source in range(last - duplicates, -1, -1):
            if arr[source] == 0:
                arr[source + duplicates] = 0
                duplicates -= 1
                arr[source + duplicates] = 0
            else:
                arr[source + duplicates] = arr[source]
