class Solution:
    def maxArea(self, coords: List[List[int]]) -> int:
        min_x = min(x for x, _ in coords)
        max_x = max(x for x, _ in coords)
        min_y = min(y for _, y in coords)
        max_y = max(y for _, y in coords)

        vertical = {}
        horizontal = {}

        for x, y in coords:
            if x not in vertical:
                vertical[x] = [y, y]
            else:
                vertical[x][0] = min(vertical[x][0], y)
                vertical[x][1] = max(vertical[x][1], y)

            if y not in horizontal:
                horizontal[y] = [x, x]
            else:
                horizontal[y][0] = min(horizontal[y][0], x)
                horizontal[y][1] = max(horizontal[y][1], x)

        best = 0

        for x, (low_y, high_y) in vertical.items():
            base = high_y - low_y
            height = max(x - min_x, max_x - x)
            best = max(best, base * height)

        for y, (low_x, high_x) in horizontal.items():
            base = high_x - low_x
            height = max(y - min_y, max_y - y)
            best = max(best, base * height)

        return best if best > 0 else -1
