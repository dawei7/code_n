from typing import List


class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        first = second = third = 0
        intersection = []
        while first < len(arr1) and second < len(arr2) and third < len(arr3):
            left, middle, right = arr1[first], arr2[second], arr3[third]
            if left == middle == right:
                intersection.append(left)
                first += 1
                second += 1
                third += 1
                continue
            current_maximum = max(left, middle, right)
            if left < current_maximum:
                first += 1
            if middle < current_maximum:
                second += 1
            if right < current_maximum:
                third += 1
        return intersection
