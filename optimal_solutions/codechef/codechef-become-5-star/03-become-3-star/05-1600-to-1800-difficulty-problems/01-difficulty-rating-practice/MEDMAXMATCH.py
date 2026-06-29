


def solve():
    def med(A, B, N):
        A.sort()
        B.sort()

        median = float('inf')

        i = N // 2
        j = N - 1

        while i < N:
            median = min(median, A[i] + B[j])
            i += 1
            j -= 1

        return median


    t = int(input())

    for _ in range(t):
        n = int(input())

        A = list(map(int, input().split()))
        B = list(map(int, input().split()))

        print(med(A, B, n))


if __name__ == "__main__":
    solve()
