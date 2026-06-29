


def solve():
    N, H, x = map(int, input().split())
    T = list(map(int, input().split()))

    if any(T[i] + x == H for i in range(N)):
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    solve()
