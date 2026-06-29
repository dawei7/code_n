


def solve():
    t = int(input())
    for tc in range(t):
        N, X = map(int, input().split())
        if X<N:
            print(-1)
        else:
            div = (X-N) + 1
            print(div, end=" ")
            for i in range(1, N+1):
                print(i if i!=div else "", end=" ")
            print()


if __name__ == "__main__":
    solve()
