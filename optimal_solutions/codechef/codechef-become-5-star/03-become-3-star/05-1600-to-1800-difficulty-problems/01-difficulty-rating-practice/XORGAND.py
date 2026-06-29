def get_hsb(x):
    for bit in range(31, -1, -1):
        if x & 1 << bit:
            return bit
    return 32

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    index = 0
    t = int(data[index])
    index += 1
    results = []
    for _ in range(t):
        n = int(data[index])
        index += 1
        a = list(map(int, data[index:index + n]))
        index += n
        pref_hsb = [[0] * 33 for _ in range(n)]
        for i in range(n):
            if i > 0:
                pref_hsb[i] = pref_hsb[i - 1][:]
            pref_hsb[i][get_hsb(a[i])] += 1
        q = int(data[index])
        index += 1
        for _ in range(q):
            L = int(data[index]) - 1
            R = int(data[index + 1]) - 1
            x = int(data[index + 2])
            index += 3
            total = R - L + 1
            hsb_x = get_hsb(x)
            count_hsb_x = pref_hsb[R][hsb_x]
            if L > 0:
                count_hsb_x -= pref_hsb[L - 1][hsb_x]
            results.append(total - count_hsb_x)
    print('\n'.join(map(str, results)))


if __name__ == "__main__":
    solve()
