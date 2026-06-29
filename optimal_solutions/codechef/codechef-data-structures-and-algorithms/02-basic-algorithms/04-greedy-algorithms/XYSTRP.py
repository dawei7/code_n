


def solve():
    t = int(input())
    for _ in range(t):
        ans1 = 0
        s = input()
        n = len(s)
        i = 1
        while i < n:
            if s[i] != s[i - 1]:
                ans1 += 1
                i += 1
            i += 1
        print(ans1)


if __name__ == "__main__":
    solve()
