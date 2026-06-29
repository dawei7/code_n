


def solve():
    MAXN = 10**7 + 10
    prm = [i for i in range(MAXN)]
    for i in range(2, MAXN):
        if i*i >= MAXN: break
        if prm[i] < i: continue
        for j in range(i*i, MAXN, i): prm[j] = i

    import sys
    input = sys.stdin.readline

    for _ in range(int(input())):
        n = int(input())
        a = list(map(int, input().split()))
        freq = {}
        freq[1] = 0
        for x in a:
            sqf = 1
            while x > 1:
                p, ct = prm[x], 0
                while x%p == 0:
                    x //= p
                    ct ^= 1
                if ct == 1: sqf *= p
            if sqf == 1: continue
            if sqf not in freq: freq[sqf] = 0
            freq[sqf] += 1
        print(max(freq.values()))


if __name__ == "__main__":
    solve()
