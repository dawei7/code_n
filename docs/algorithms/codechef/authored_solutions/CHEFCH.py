import sys


def solve():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for s in data[1:1 + t]:
        changes_a = changes_b = 0
        for i, ch in enumerate(s):
            expected_a = ord("-") if i % 2 == 0 else ord("+")
            expected_b = ord("+") if i % 2 == 0 else ord("-")
            changes_a += ch != expected_a
            changes_b += ch != expected_b
        out.append(str(min(changes_a, changes_b)))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
