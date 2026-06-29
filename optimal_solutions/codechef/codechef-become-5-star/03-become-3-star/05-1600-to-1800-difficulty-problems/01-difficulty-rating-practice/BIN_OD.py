


def solve():
    for _ in range(int(input())):
        n, q = map(int, input().split())
        a = list(map(int, input().split()))
        pref = [[0 for i in range(60)] for _ in range(n+1)]
        for i in range(n):
            for k in range(60):
                pref[i+1][k] = pref[i][k] + ((a[i] >> k) & 1)
        for i in range(q):
            k, l1, r1, l2, r2 = map(int, input().split())
            on1, on2 = pref[r1][k] - pref[l1-1][k], pref[r2][k] - pref[l2-1][k]
            off1, off2 = r1-l1+1 - on1, r2-l2+1 - on2
            print(on1*off2 + on2*off1)


if __name__ == "__main__":
    solve()
