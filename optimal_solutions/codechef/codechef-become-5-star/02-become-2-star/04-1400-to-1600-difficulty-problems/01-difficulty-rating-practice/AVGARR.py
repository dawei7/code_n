


def solve():
    for _ in range(int(input())):
        n, m = tuple(map(int,input().split()))
        a = []
        if n % 2 == 1:
            a = [m]
        for i in range(n // 2):
            a = [m - i - 1] + a + [m + i + 1]
        print(" ".join(map(str,a)))


if __name__ == "__main__":
    solve()
