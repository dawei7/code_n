def solve():
    import sys
    data = sys.stdin.read().split()
    if not data:
        return
    t = int(data[0])
    pos = 1
    result = []
    for _ in range(t):
        n = int(data[pos])
        pos += 1
        arr = list(map(int, data[pos:pos + n]))
        pos += n
        if n == 0:
            result.append('0')
            continue
        left = [1] * n
        for i in range(1, n):
            if arr[i] > arr[i - 1]:
                left[i] = left[i - 1] + 1
            else:
                left[i] = 1
        right = [1] * n
        for i in range(n - 2, -1, -1):
            if arr[i] > arr[i + 1]:
                right[i] = right[i + 1] + 1
            else:
                right[i] = 1
        max_peak = 0
        for i in range(n):
            peak_len = left[i] + right[i] - 1
            if peak_len > max_peak:
                max_peak = peak_len
        result.append(str(max_peak))
    sys.stdout.write('\n'.join(result))


if __name__ == "__main__":
    solve()
