def solve():
    import sys
    input_data = sys.stdin.read().strip().split()
    t = int(input_data[0])
    idx = 1
    out_lines = []
    import bisect
    for _ in range(t):
        n = int(input_data[idx])
        q = int(input_data[idx + 1])
        idx += 2
        A = list(map(int, input_data[idx:idx + n]))
        idx += n
        B = list(map(int, input_data[idx:idx + n]))
        idx += n
        queries = list(map(int, input_data[idx:idx + q]))
        idx += q
        AB = list(zip(A, B))
        AB.sort(key=lambda x: x[0])
        sorted_A = [pair[0] for pair in AB]
        prefix = []
        curr = 0
        for a, b in AB:
            curr += b
            prefix.append(curr)
        res = []
        for x in queries:
            pos = bisect.bisect_right(sorted_A, x)
            if pos == 0:
                res.append('0')
            else:
                res.append(str(prefix[pos - 1]))
        out_lines.append(' '.join(res))
    sys.stdout.write('\n'.join(out_lines))


if __name__ == "__main__":
    solve()
