from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(index):
            x, y = points[index]
            return x * x + y * y

        left = 0
        right = len(points) - 1
        target = k - 1

        while left <= right:
            pivot = distance((left + right) // 2)
            i = left
            j = right

            while i <= j:
                while distance(i) < pivot:
                    i += 1
                while distance(j) > pivot:
                    j -= 1
                if i <= j:
                    points[i], points[j] = points[j], points[i]
                    i += 1
                    j -= 1

            if target <= j:
                right = j
            elif target >= i:
                left = i
            else:
                break

        return points[:k]
