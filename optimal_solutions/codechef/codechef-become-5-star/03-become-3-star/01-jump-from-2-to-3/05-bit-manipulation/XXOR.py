import sys
MAX_BITS = 31

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n, q = (data[0], data[1])
    arr = data[2:2 + n]
    idx = 2 + n
    prefix = [[0] * (n + 1) for _ in range(MAX_BITS)]
    for i, value in enumerate(arr, 1):
        for bit in range(MAX_BITS):
            prefix[bit][i] = prefix[bit][i - 1] + (value >> bit & 1)
    out: list[str] = []
    for _ in range(q):
        left, right = (data[idx], data[idx + 1])
        idx += 2
        length = right - left + 1
        x = 0
        for bit in range(MAX_BITS):
            ones = prefix[bit][right] - prefix[bit][left - 1]
            if ones < length - ones:
                x |= 1 << bit
        out.append(str(x))
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
