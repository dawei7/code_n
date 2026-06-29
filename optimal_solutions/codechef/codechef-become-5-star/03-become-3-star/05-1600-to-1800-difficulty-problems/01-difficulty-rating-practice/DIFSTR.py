


def solve():
    for _ in range(int(input())):
        n = int(input())
        ans = ''
        for i in range(n):
            st = input()
            ans += str(1-int(st[i]))

        print(ans)


if __name__ == "__main__":
    solve()
