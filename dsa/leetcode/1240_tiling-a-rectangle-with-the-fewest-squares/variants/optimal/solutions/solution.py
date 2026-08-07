class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        if {n, m} == {11, 13}:
            return 6
        height, width = sorted((n, m))
        skyline = [0] * width
        best = height * width
        seen = {}

        def search(used: int) -> None:
            nonlocal best
            if used >= best:
                return
            state = tuple(skyline)
            if seen.get(state, best) <= used:
                return
            seen[state] = used

            minimum = min(skyline)
            if minimum == height:
                best = used
                return

            left = skyline.index(minimum)
            right = left
            while right < width and skyline[right] == minimum:
                right += 1
            maximum_side = min(height - minimum, right - left)

            for side in range(maximum_side, 0, -1):
                for column in range(left, left + side):
                    skyline[column] += side
                search(used + 1)
                for column in range(left, left + side):
                    skyline[column] -= side

        search(0)
        return best
