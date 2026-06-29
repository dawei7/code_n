from collections import Counter


def solve():
    for _ in range(int(input())):
        n, k = [int(i) for i in input().split()]
        s = input()
        tot1 = tot = 0
        if len(set(s)) == 1:
            print(0)
            continue
        ch = True
        for i in range(k):
            x = s[i::k]
            c = Counter(x)
            if ch:
                if c["1"]:
                    tot += c["0"]
                else:
                    tot = float('inf')
                    ch = False
            xx = c["1"]
            tot1 += xx//2
            if xx % 2:
                tot1 += 2
        print(min(tot, tot1))


if __name__ == "__main__":
    solve()
