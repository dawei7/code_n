from collections import deque
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def updateMatrix(matrix):
    rows, cols = (len(matrix), len(matrix[0]))
    queue = deque()
    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] == 0:
                queue.append((row, col))
            else:
                matrix[row][col] = -1
    while queue:
        row, col = queue.popleft()
        for dr, dc in directions:
            new_row, new_col = (row + dr, col + dc)
            if 0 <= new_row < rows and 0 <= new_col < cols and (matrix[new_row][new_col] == -1):
                matrix[new_row][new_col] = matrix[row][col] + 1
                queue.append((new_row, new_col))

def solve():
    n, m = map(int, input().split())
    assert 1 <= n <= 100
    assert 1 <= m <= 100
    mat = [list(map(int, input().split())) for _ in range(n)]
    for row in mat:
        for x in row:
            assert x == 0 or x == 1
    updateMatrix(mat)
    for row in mat:
        print(' '.join(map(str, row)))


if __name__ == "__main__":
    solve()
