def max_points_on_line(points):
    n = len(points)
    if n < 2:
        return n
    from math import gcd
    result = 0
    for i in range(n):
        slopes = {}
        overlap = 0
        cur_max = 0
        x1, y1 = points[i]
        for j in range(i + 1, n):
            x2, y2 = points[j]
            dx = x2 - x1
            dy = y2 - y1
            if dx == 0 and dy == 0:
                overlap += 1
                continue
            g = gcd(dx, dy)
            if g != 0:
                dx //= g
                dy //= g
            if dx < 0:
                dx = -dx
                dy = -dy
            elif dx == 0:
                dy = 1
            slope = (dx, dy)
            slopes[slope] = slopes.get(slope, 0) + 1
            cur_max = max(cur_max, slopes[slope])
        result = max(result, cur_max + overlap + 1)
    return result

def solve():
    import sys
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    t = int(input_data[0])
    index = 1
    results = []
    for _ in range(t):
        n = int(input_data[index])
        index += 1
        points = []
        for _ in range(n):
            x = int(input_data[index])
            y = int(input_data[index + 1])
            points.append((x, y))
            index += 2
        results.append(max_points_on_line(points))
    sys.stdout.write('\n'.join(map(str, results)) + '\n')


if __name__ == "__main__":
    solve()
