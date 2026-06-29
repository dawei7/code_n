


def solve():
    for i in range(int(input())):
        n = int(input())
        a = list(map(int,input().split()))
        c = 0
        for i in range(n):
            if a[i] == i + 1 + c:
                c = c + 1
        print(c)


if __name__ == "__main__":
    solve()
