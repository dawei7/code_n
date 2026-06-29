# cook your dish here


def solve():
    for _ in range(int(input())):
        n, k = map(int,input().split())
        d = list(map(int,input().split()))
        ans = ''
        for i in d:
            ans += str(int(i%k == 0))
        print(ans)


if __name__ == "__main__":
    solve()
