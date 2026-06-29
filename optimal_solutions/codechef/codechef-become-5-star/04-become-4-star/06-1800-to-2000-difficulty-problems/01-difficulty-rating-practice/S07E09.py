# cook your dish here


def solve():
    for _ in range(int(input())):
        n = int(input())
        a = list(map(int,input().split()))
        a.sort(reverse=True)

        ans = a[-1]
        print(ans*n + a.index(ans))


if __name__ == "__main__":
    solve()
