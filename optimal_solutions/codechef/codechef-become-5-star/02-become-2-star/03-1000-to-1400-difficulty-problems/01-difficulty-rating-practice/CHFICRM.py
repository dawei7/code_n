import sys

def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        n = data[idx]
        idx += 1
        five = ten = 0
        ok = True
        for coin in data[idx:idx + n]:
            if coin == 5:
                five += 1
            elif coin == 10:
                if five == 0:
                    ok = False
                else:
                    five -= 1
                    ten += 1
            elif ten:
                ten -= 1
            elif five >= 2:
                five -= 2
            else:
                ok = False
        idx += n
        out.append('YES' if ok else 'NO')
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
