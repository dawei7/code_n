class Solution:
    def minLights(self, lights: list[int]) -> int:
        n = len(lights)
        difference = [0] * (n + 1)

        for position, radius in enumerate(lights):
            if radius:
                left = max(0, position - radius)
                right = min(n - 1, position + radius)
                difference[left] += 1
                difference[right + 1] -= 1

        visible = [False] * n
        active = 0
        for position in range(n):
            active += difference[position]
            visible[position] = active > 0

        additional = 0
        position = 0
        while position < n:
            if visible[position]:
                position += 1
            else:
                additional += 1
                position += 3

        return additional
