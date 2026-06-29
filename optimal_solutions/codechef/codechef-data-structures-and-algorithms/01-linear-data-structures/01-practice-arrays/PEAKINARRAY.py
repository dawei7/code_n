


def solve():
    def findPeaks(A, n):
        hasPeak = False

        for i in range(n):
            if (i == 0 or A[i] > A[i - 1]) and (i == n - 1 or A[i] > A[i + 1]):
                print(A[i], end=" ")
                hasPeak = True

        if not hasPeak:
            print(-1)


if __name__ == "__main__":
    solve()
