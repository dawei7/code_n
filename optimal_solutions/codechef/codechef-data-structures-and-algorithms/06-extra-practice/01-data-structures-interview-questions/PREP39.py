


def solve():
    def powerModulo(N, X, M):
        # Edge cases
        if X == 0:
            return 1
        if M == 1:
            return 0

        val = pow(abs(N), X, M)

        # If result should be negative
        if N < 0 and X % 2 == 1:
            if val == 0:
                return 0
            return -val
        else:
            return val


if __name__ == "__main__":
    solve()
