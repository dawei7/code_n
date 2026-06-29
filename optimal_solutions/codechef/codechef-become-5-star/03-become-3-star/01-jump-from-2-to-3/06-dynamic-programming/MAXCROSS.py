


def solve():
    def maximal_crosses(mat):
        n = len(mat)

        # Horizontal prefix and suffix
        horizontal_prefix = [[0] * n for _ in range(n)]
        horizontal_suffix = [[0] * n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                if mat[i][j] == '.':
                    horizontal_prefix[i][j] = 0
                else:
                    horizontal_prefix[i][j] = (horizontal_prefix[i][j-1] if j >= 1 else 0) + 1

            mx = 0
            for j in range(n-1, -1, -1):
                if mat[i][j] == '.':
                    horizontal_suffix[i][j] = 0
                    mx = 0
                else:
                    horizontal_suffix[i][j] = mx
                    mx += 1

        # Vertical prefix and suffix
        vertical_prefix = [[0] * n for _ in range(n)]
        vertical_suffix = [[0] * n for _ in range(n)]

        for j in range(n):
            for i in range(n):
                if mat[i][j] == '.':
                    vertical_prefix[i][j] = 0
                else:
                    vertical_prefix[i][j] = (vertical_prefix[i-1][j] if i >= 1 else 0) + 1

            mx = 0
            for i in range(n-1, -1, -1):
                if mat[i][j] == '.':
                    vertical_suffix[i][j] = 0
                    mx = 0
                else:
                    vertical_suffix[i][j] = mx
                    mx += 1

        # Right diagonal prefix and suffix
        right_diagonal_prefix = [[0] * n for _ in range(n)]
        right_diagonal_suffix = [[0] * n for _ in range(n)]

        for i in range(n):
            k, j = i, 0
            while k < n and j < n:
                if mat[k][j] == '.':
                    right_diagonal_prefix[k][j] = 0
                else:
                    right_diagonal_prefix[k][j] = (right_diagonal_prefix[k-1][j-1] if k >= 1 and j >= 1 else 0) + 1
                k += 1
                j += 1

            k -= 1
            j -= 1
            mx = 0
            while k >= 0 and j >= 0:
                if mat[k][j] == '.':
                    right_diagonal_suffix[k][j] = 0
                    mx = 0
                else:
                    right_diagonal_suffix[k][j] = mx
                    mx += 1
                k -= 1
                j -= 1

        for i in range(n):
            k, j = 0, i
            while k < n and j < n:
                if mat[k][j] == '.':
                    right_diagonal_prefix[k][j] = 0
                else:
                    right_diagonal_prefix[k][j] = (right_diagonal_prefix[k-1][j-1] if k >= 1 and j >= 1 else 0) + 1
                k += 1
                j += 1

            k -= 1
            j -= 1
            mx = 0
            while k >= 0 and j >= 0:
                if mat[k][j] == '.':
                    right_diagonal_suffix[k][j] = 0
                    mx = 0
                else:
                    right_diagonal_suffix[k][j] = mx
                    mx += 1
                k -= 1
                j -= 1

        # Left diagonal prefix and suffix
        left_diagonal_prefix = [[0] * n for _ in range(n)]
        left_diagonal_suffix = [[0] * n for _ in range(n)]

        for i in range(n):
            k, j = i, n-1
            while k < n and j >= 0:
                if mat[k][j] == '.':
                    left_diagonal_prefix[k][j] = 0
                else:
                    left_diagonal_prefix[k][j] = (left_diagonal_prefix[k-1][j+1] if k >= 1 and j+1 < n else 0) + 1
                k += 1
                j -= 1

            k -= 1
            j += 1
            mx = 0
            while k >= 0 and j < n:
                if mat[k][j] == '.':
                    left_diagonal_suffix[k][j] = 0
                    mx = 0
                else:
                    left_diagonal_suffix[k][j] = mx
                    mx += 1
                k -= 1
                j += 1

        for i in range(n):
            k, j = 0, i
            while k < n and j >= 0:
                if mat[k][j] == '.':
                    left_diagonal_prefix[k][j] = 0
                else:
                    left_diagonal_prefix[k][j] = (left_diagonal_prefix[k-1][j+1] if k >= 1 and j+1 < n else 0) + 1
                k += 1
                j -= 1

            k -= 1
            j += 1
            mx = 0
            while k >= 0 and j < n:
                if mat[k][j] == '.':
                    left_diagonal_suffix[k][j] = 0
                    mx = 0
                else:
                    left_diagonal_suffix[k][j] = mx
                    mx += 1
                k -= 1
                j += 1

        # Calculate maximal crosses
        for i in range(n):
            for j in range(n):
                mx = max(
                    horizontal_prefix[i][j] + horizontal_suffix[i][j],
                    vertical_prefix[i][j] + vertical_suffix[i][j],
                    right_diagonal_prefix[i][j] + right_diagonal_suffix[i][j],
                    left_diagonal_prefix[i][j] + left_diagonal_suffix[i][j]
                )
                print(mx, end=' ')
            print()


    # Input reading and function call
    if __name__ == "__main__":
        n = int(input().strip())
        A = []
        for _ in range(n):
            A.append(list(input().strip()))
        maximal_crosses(A)


if __name__ == "__main__":
    solve()
