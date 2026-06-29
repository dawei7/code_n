


def solve():
    def check(arr, d, n, c):
        c -= 1
        prev = arr[0]

        for i in range(1, n):
            if arr[i] - prev >= d:
                c -= 1
                prev = arr[i]
            if c == 0:
                return True
        return False


if __name__ == "__main__":
    solve()
