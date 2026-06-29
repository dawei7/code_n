


def solve():
    def hasPairWithDifference(A: list[int], N: int, B: int) -> int:
        A.sort()
        i = 0
        j = 1

        while i < N and j < N:
            if i != j and A[j] - A[i] == B:
                return 1
            elif A[j] - A[i] < B:
                j += 1
            else:
                i += 1

        return 0


if __name__ == "__main__":
    solve()
