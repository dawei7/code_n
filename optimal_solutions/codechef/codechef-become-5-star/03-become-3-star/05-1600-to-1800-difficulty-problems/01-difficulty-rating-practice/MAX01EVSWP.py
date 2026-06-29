import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    idx = 1
    out = []
    for _ in range(t):
        n = int(data[idx])
        s = data[idx + 1]
        idx += 2
        odd_count = (n + 1) // 2
        even_count = n // 2
        odd = s[0::2]
        even = s[1::2]
        z_odd = odd.count(48)
        o_odd = odd_count - z_odd
        z_even = even.count(48)
        o_even = even_count - z_even
        best = 0
        max_internal = min(z_odd, o_even)
        for internal in range(max_internal + 1):
            remaining_odd_zero = z_odd - internal
            first_loss = 0 if remaining_odd_zero > 0 else min(1, o_odd)
            cross_targets = max(0, o_odd - first_loss)
            cross = min(z_even, cross_targets)
            best = max(best, internal + cross)
        out.append(str(best))
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
