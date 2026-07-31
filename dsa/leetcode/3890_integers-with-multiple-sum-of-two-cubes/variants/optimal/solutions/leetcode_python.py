class Solution:
    def findGoodIntegers(self, n: int) -> list[int]:
        cubes = []
        value = 1
        while value * value * value + 1 <= n:
            cubes.append(value * value * value)
            value += 1

        representations = {}
        for right in range(len(cubes)):
            right_cube = cubes[right]
            for left in range(right + 1):
                total = cubes[left] + right_cube
                if total > n:
                    break
                representations[total] = representations.get(total, 0) + 1

        return sorted(
            total
            for total, count in representations.items()
            if count >= 2
        )
