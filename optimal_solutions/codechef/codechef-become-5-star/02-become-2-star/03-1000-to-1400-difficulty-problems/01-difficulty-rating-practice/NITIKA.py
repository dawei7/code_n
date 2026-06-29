import sys

def pretty(part):
    lower = part.lower()
    return lower[:1].upper() + lower[1:]

def solve():
    lines = sys.stdin.read().splitlines()
    if not lines:
        return
    t = int(lines[0])
    out = []
    for line in lines[1:1 + t]:
        parts = line.split()
        last = pretty(parts[-1])
        initials = [pretty(part)[0] + '.' for part in parts[:-1]]
        out.append(' '.join(initials + [last]))
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
