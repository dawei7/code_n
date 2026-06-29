# cook your dish here


def solve():
    t = int(input())
    ans = ''

    for i in range(t):
        s = list(input())
        t = list(input())
        for j in range(len(s)):
                if s[j] == t[j]:
                    ans += 'G'
                else:
                    ans += 'B'
        print(ans)
        ans = ''


if __name__ == "__main__":
    solve()
