import sys


def required_bit(left, right):
    bit = (left ^ right).bit_length() - 1
    left_bit = (left >> bit) & 1
    right_bit = (right >> bit) & 1
    return bit, 0 if left_bit < right_bit else 1


def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        a, b, c = data[idx:idx + 3]
        idx += 3
        requirements = {}
        ok = True
        for bit, value in (required_bit(a, b), required_bit(b, c)):
            if bit in requirements and requirements[bit] != value:
                ok = False
            requirements[bit] = value
        if not ok:
            out.append("-1")
            continue
        x = 0
        for bit, value in requirements.items():
            if value:
                x |= 1 << bit
        out.append(str(x if (a ^ x) < (b ^ x) < (c ^ x) else -1))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
