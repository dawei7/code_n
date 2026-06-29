import sys


def solve():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    idx = 1
    out = []
    for _ in range(t):
        idx += 1
        s = data[idx].decode()
        idx += 1
        charged = [i for i, ch in enumerate(s) if ch != "0"]
        if not charged:
            out.append(str(len(s)))
            continue
        neutral = 0
        for left, right in zip(charged, charged[1:]):
            gap = right - left - 1
            if gap > 0 and s[left] != s[right] and gap % 2 == 1:
                neutral += 1
        out.append(str(neutral))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
