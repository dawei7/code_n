from typing import List


class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        flips = []
        for target in range(len(arr), 1, -1):
            index = arr.index(target, 0, target)
            if index == target - 1:
                continue
            if index != 0:
                arr[: index + 1] = reversed(arr[: index + 1])
                flips.append(index + 1)
            arr[:target] = reversed(arr[:target])
            flips.append(target)
        return flips
