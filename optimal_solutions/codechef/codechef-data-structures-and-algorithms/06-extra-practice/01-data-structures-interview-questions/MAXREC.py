import sys

def maxHistogramArea(heights):
    stack = []
    max_area = 0
    index = 0
    n = len(heights)
    while index < n:
        if not stack or heights[stack[-1]] <= heights[index]:
            stack.append(index)
            index += 1
        else:
            top = stack.pop()
            area = heights[top] * (index if not stack else index - stack[-1] - 1)
            if area > max_area:
                max_area = area
    while stack:
        top = stack.pop()
        area = heights[top] * (index if not stack else index - stack[-1] - 1)
        if area > max_area:
            max_area = area
    return max_area

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    N, M = (int(data[0]), int(data[1]))
    grid = []
    idx = 2
    for _ in range(N):
        row = list(map(int, data[idx:idx + M]))
        grid.append(row)
        idx += M
    max_area = 0
    heights = [0] * M
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 1:
                heights[j] += 1
            else:
                heights[j] = 0
        max_area = max(max_area, maxHistogramArea(heights))
    sys.stdout.write(str(max_area))


if __name__ == "__main__":
    solve()
