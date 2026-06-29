


def solve():
    T = int(input())

    for _ in range(T):
        N = int(input())
        S = input()

        n = S.count('1')

        ans = ((n * (n + 1)) // 2)

        print(ans)


if __name__ == "__main__":
    solve()
