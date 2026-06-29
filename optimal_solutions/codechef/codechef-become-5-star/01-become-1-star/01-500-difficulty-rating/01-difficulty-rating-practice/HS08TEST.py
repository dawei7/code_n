


def solve():
    X, Y = map(float, input().split())

    if X % 5 == 0 and X + 0.50 <= Y:
        Y -= (X + 0.50)

    print(f"{Y:.2f}")


if __name__ == "__main__":
    solve()
