


def solve():
    for _ in range(int(input())):
        n, k = map(int, input().split())
        s = input()
        t = [0]*n
        for i in range(n):
            if s[i] == '0':
                continue
            t[i] = 0
            if i > 0 and s[i-1] == '0':
                t[i-1] = 1
            if i+1 < n and s[i+1] == '0':
                t[i+1] = 1
        k -= 1
        dist = [n+1]*n
        prv = -1
        for i in range(n):
            if t[i] == 1:
                prv = i
            if prv != -1:
                dist[i] = i - prv
        prv = -1
        for i in reversed(range(n)):
            if t[i] == 1:
                prv = i
            if prv != -1:
                dist[i] = min(dist[i], prv - i)
        ans = ''
        for i in range(n):
            first = dist[i]
            if first == n+1 or first > k:
                ans += '0'
            else:
                if (k-first)%2 == 0:
                    ans += '1'
                else:
                    ans += '0'
        print(ans)


if __name__ == "__main__":
    solve()
