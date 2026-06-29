


def solve():
    def equalPairs(mat):
        ans = 0
        mp = {}

        for row in mat:
            row_tuple = tuple(row)
            mp[row_tuple] = mp.get(row_tuple, 0) + 1

        for i in range(len(mat[0])):
            col_list = [mat[j][i] for j in range(len(mat))]
            ans += mp.get(tuple(col_list), 0)

        return ans

    if __name__ == "__main__":
        n = int(input())
        assert 1 <= n <= 100

        mat = [list(map(int, input().split())) for _ in range(n)]

        print(equalPairs(mat))


if __name__ == "__main__":
    solve()
