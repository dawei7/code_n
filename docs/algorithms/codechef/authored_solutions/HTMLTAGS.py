import sys


def valid(tag):
    if not (tag.startswith("</") and tag.endswith(">")):
        return False
    body = tag[2:-1]
    return bool(body) and all(ch.isdigit() or ("a" <= ch <= "z") for ch in body)


def solve():
    lines = sys.stdin.read().splitlines()
    if not lines:
        return
    t = int(lines[0].strip())
    out = []
    for line in lines[1:1 + t]:
        out.append("Success" if valid(line.strip()) else "Error")
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
