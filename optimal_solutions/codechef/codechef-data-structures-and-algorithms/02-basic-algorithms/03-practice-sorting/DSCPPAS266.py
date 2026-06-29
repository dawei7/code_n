


def solve():
    def canReduce(N: int, arr: list[int]) -> bool:
        arr.sort()

        for i in range(1, N):
            if arr[i] - arr[i - 1] > 1:
                return False

        return True


if __name__ == "__main__":
    solve()
