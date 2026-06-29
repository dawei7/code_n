def solve():
    import sys, math
    data = sys.stdin.read().split()
    t = int(data[0])
    index = 1
    results = []
    for _ in range(t):
        n = int(data[index])
        s = data[index + 1]
        index += 2
        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1
        g = 0
        for count in freq.values():
            g = count if g == 0 else math.gcd(g, count)
        results.append(str(g))
    sys.stdout.write('\n'.join(results))


if __name__ == "__main__":
    solve()
