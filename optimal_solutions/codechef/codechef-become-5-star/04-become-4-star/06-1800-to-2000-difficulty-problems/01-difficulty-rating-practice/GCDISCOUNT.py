from math import gcd


def solve():
    for t in range(int(input())):
        n = int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        prefix = [a[0]]
        for i in range(1, n):
            prefix.append(gcd(prefix[i - 1], a[i]))

        suffix = [a[-1]]
        for i in range(n - 2, -1, -1):
            suffix.append(gcd(suffix[-1], a[i]))

        suffix = suffix[::-1]
        if n == 1:
            print(max(a[0], b[0]))
            continue
        maxi = prefix[-1]  # Without discount is bare minimum
        for i in range(n):
            if i == 0:
                maxi = max(maxi, gcd(b[0], suffix[1]))
            elif i == n - 1:
                maxi = max(maxi, gcd(b[-1], prefix[n - 2]))
            else:
                maxi = max(maxi, gcd(b[i], gcd(prefix[i - 1], suffix[i + 1])))

        print(maxi)


if __name__ == "__main__":
    solve()
