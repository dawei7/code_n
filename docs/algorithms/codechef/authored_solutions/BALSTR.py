import sys


def additions_needed(s):
    open_count = 0
    missing_open = 0
    for ch in s:
        if ch == "(":
            open_count += 1
        elif open_count:
            open_count -= 1
        else:
            missing_open += 1
    return missing_open + open_count


def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    t = int(data[0])
    idx = 1
    out = []
    for _ in range(t):
        idx += 1
        s = data[idx].decode()
        idx += 1
        out.append(str(additions_needed(s)))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
