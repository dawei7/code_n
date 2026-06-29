


def solve():
    t = int(input())

    for _ in range(t):
        s = input().strip()
        n = len(s)

        b = [0] * n
        ans = 0

        for i in range(1, n + 1):
            val = i * (n - i + 1)

            if s[i - 1] == '0':
                b[i - 1] = val
            else:
                b[i - 1] = -val
                ans += abs(b[i - 1])

        curr_sum = 0
        mx = 0

        for x in b:
            curr_sum += x

            if curr_sum < 0:
                curr_sum = 0

            mx = max(mx, curr_sum)

        print(mx + ans)


if __name__ == "__main__":
    solve()
