


def solve():
    for _ in range(int(input())):
        n, x, k = map(int, input().split())
        if n * x > k:
            print("NO")
        else:
            print("YES")


if __name__ == "__main__":
    solve()
