


def solve():
    def collatz_steps(n):
        if n == 1:
            return 0
        elif n % 2 == 0:
            return 1 + collatz_steps(n // 2)
        else:
            return 1 + collatz_steps(3 * n + 1)

    if __name__ == "__main__":
        n = int(input())
        print(collatz_steps(n))


if __name__ == "__main__":
    solve()
