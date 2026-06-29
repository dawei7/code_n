


def solve():
    def spiralmatValues(mat):
        top, bottom, left, right = 0, len(mat) - 1, 0, len(mat[0]) - 1
        direction = 1

        while top <= bottom and left <= right:
            if direction == 1:
                for i in range(left, right + 1):
                    print(mat[top][i], end=" ")
                direction = 2
                top += 1
            elif direction == 2:
                for i in range(top, bottom + 1):
                    print(mat[i][right], end=" ")
                direction = 3
                right -= 1
            elif direction == 3:
                for i in range(right, left - 1, -1):
                    print(mat[bottom][i], end=" ")
                direction = 4
                bottom -= 1
            elif direction == 4:
                for i in range(bottom, top - 1, -1):
                    print(mat[i][left], end=" ")
                direction = 1
                left += 1

    if __name__ == "__main__":
        n, m = map(int, input().split())

        assert 1 <= n <= 100
        assert 1 <= m <= 100

        mat = [list(map(int, input().split())) for _ in range(n)]

        spiralmatValues(mat)


if __name__ == "__main__":
    solve()
