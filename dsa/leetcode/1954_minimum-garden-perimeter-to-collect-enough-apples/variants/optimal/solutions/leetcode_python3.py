class Solution:
    def minimumPerimeter(self, neededApples: int) -> int:
        def apples(half_side: int) -> int:
            return 2 * half_side * (half_side + 1) * (2 * half_side + 1)

        low, high = 1, 1
        while apples(high) < neededApples:
            high *= 2

        while low < high:
            middle = (low + high) // 2
            if apples(middle) >= neededApples:
                high = middle
            else:
                low = middle + 1

        return 8 * low
