


def solve():
    for _ in range(int(input())):
        n = int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        c = sorted(a + b)
        print(min(c[i] - c[i-n+1] for i in range(n-1, 2*n)))


if __name__ == "__main__":
    solve()
