


def solve():
    def f1():
        dp1 = [[False, False] for _ in range(n // 2 + 2)]
        dp1[n // 2 + 1][0] = dp1[n // 2 + 1][1] = True

        for idx in range(n // 2, -1, -1):
            for flag in range(2):
                ans = False
                if not flag:
                    ans = ans or dp1[idx + 1][1]
                if n // 2 + idx + 1 - flag < n:
                    ans = ans or (s[idx] == s[n // 2 + idx + 1 - flag] and dp1[idx + 1][flag])
                dp1[idx][flag] = ans

        return dp1[0][0]

    def f2():
        dp2 = [[False, False] for _ in range(n)]
        dp2[n // 2 - 1][0] = dp2[n // 2 - 1][1] = True

        for idx in range(n // 2, n):
            for flag in range(2):
                ans = False
                if not flag:
                    ans = ans or dp2[idx - 1][1]
                if idx - n // 2 - 1 + flag >= 0:
                    ans = ans or (s[idx] == s[idx - n // 2 - 1 + flag] and dp2[idx - 1][flag])
                dp2[idx][flag] = ans

        return dp2[n - 1][0]

    t = int(input())
    for _ in range(t):
        s = input().strip()
        n = len(s)

        if n == 1:
            print("NO")
            continue

        if n % 2 == 0:
            for i in range(n // 2):
                if s[i] != s[n // 2 + i]:
                    print("NO")
                    break
            else:
                print("YES")
        else:
            for i in range(n // 2):
                if s[i] != s[n // 2 + i + 1]:
                    break
            else:
                print("YES")
                continue

            if f1():
                print("YES")
            elif f2():
                print("YES")
            else:
                print("NO")


if __name__ == "__main__":
    solve()
