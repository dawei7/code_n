import sys


def can_sort(s):
    target = "".join(sorted(s))
    n = len(s)
    for i in range(n // 2):
        if sorted((s[i], s[n - 1 - i])) != sorted((target[i], target[n - 1 - i])):
            return False
    return n % 2 == 0 or s[n // 2] == target[n // 2]


def solve():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    idx = 1
    out = []
    for _ in range(t):
        idx += 1
        s = data[idx].decode()
        idx += 1
        out.append("YES" if can_sort(s) else "NO")
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
