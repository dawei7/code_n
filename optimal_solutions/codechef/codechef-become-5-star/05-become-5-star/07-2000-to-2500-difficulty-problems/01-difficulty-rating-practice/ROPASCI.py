# cook your dish here


def solve():
    n = 10000001
    t = int(input())

    for _ in range(t):
        n = int(input())
        s = input()
        dp = [0] * n
        dp[n - 1] = n - 1

        p, r, sc = -1, -1, -1

        if s[n - 1] == 'P':
            p = n - 1
        elif s[n - 1] == 'R':
            r = n - 1
        else:
            sc = n - 1

        for i in range(n - 2, -1, -1):
            if s[i] == 'P':
                dp[i] = dp[sc] if sc != -1 else i
                p = i
            elif s[i] == 'R':
                dp[i] = dp[p] if p != -1 else i
                r = i
            else:
                dp[i] = dp[r] if r != -1 else i
                sc = i

        res = ''.join([s[dp[i]] for i in range(n)])
        print(res)


if __name__ == "__main__":
    solve()
