from collections import deque


def solve():
    def minTimeToRot(grid):
        rows, cols = len(grid), len(grid[0])
        visited = [row[:] for row in grid]

        rottenQueue = deque()
        freshOrangeCount = 0

        for i in range(rows):
            for j in range(cols):
                if visited[i][j] == 2:
                    rottenQueue.append((i, j))
                if visited[i][j] == 1:
                    freshOrangeCount += 1

        if freshOrangeCount == 0:
            return 0
        if not rottenQueue:
            return -1

        minutes = -1
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]

        while rottenQueue:
            size = len(rottenQueue)
            for _ in range(size):
                x, y = rottenQueue.popleft()
                for dx, dy in directions:
                    i, j = x + dx, y + dy
                    if 0 <= i < rows and 0 <= j < cols and visited[i][j] == 1:
                        visited[i][j] = 2
                        freshOrangeCount -= 1
                        rottenQueue.append((i, j))
            minutes += 1

        if freshOrangeCount == 0:
            return minutes
        return -1

    if __name__ == "__main__":
        n, m = map(int, input().split())

        assert 1 <= n <= 100
        assert 1 <= m <= 100

        mat = [list(map(int, input().split())) for _ in range(n)]

        print(minTimeToRot(mat))


if __name__ == "__main__":
    solve()
