import sys

def current_or(bit_counts):
    ans = 0
    for bit, count in enumerate(bit_counts):
        if count:
            ans |= 1 << bit
    return ans

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        n = data[idx]
        q = data[idx + 1]
        idx += 2
        arr = data[idx:idx + n]
        idx += n
        bit_counts = [0] * 31
        for value in arr:
            for bit in range(31):
                if value >> bit & 1:
                    bit_counts[bit] += 1
        out.append(str(current_or(bit_counts)))
        for _ in range(q):
            pos = data[idx] - 1
            value = data[idx + 1]
            idx += 2
            old = arr[pos]
            if old != value:
                for bit in range(31):
                    if old >> bit & 1:
                        bit_counts[bit] -= 1
                    if value >> bit & 1:
                        bit_counts[bit] += 1
                arr[pos] = value
            out.append(str(current_or(bit_counts)))
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
