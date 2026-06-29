


def solve():
    def getPascalElement(N, M):
        # Base cases
        if M == 0 or M == N:
            return 1

        # Recursive relation
        return getPascalElement(N - 1, M - 1) + getPascalElement(N - 1, M)


if __name__ == "__main__":
    solve()
