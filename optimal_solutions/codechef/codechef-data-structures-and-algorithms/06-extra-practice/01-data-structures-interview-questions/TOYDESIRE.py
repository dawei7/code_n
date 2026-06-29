def solve():
    import sys
    data = sys.stdin.read().strip().split()
    t = int(data[0])
    index = 1
    out = []
    for _ in range(t):
        n = int(data[index])
        x = int(data[index + 1])
        index += 2
        coins = list(map(int, data[index:index + n]))
        index += n
        coins.sort(reverse=True)
        s = 0
        count = 0
        for coin in coins:
            s += coin
            count += 1
            if s >= x:
                break
        if s >= x:
            out.append(str(count))
        else:
            out.append('-1')
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
