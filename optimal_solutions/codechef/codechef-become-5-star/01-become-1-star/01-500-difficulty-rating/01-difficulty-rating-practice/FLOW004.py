


def solve():
    T = int(input())
    for _ in range(T):
        N = int(input())

        last_digit = N % 10

        first_digit = N
        while first_digit >= 10:
            first_digit //= 10

        print(first_digit + last_digit)


if __name__ == "__main__":
    solve()
