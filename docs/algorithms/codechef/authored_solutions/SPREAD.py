import sys


def main() -> None:
    tokens = sys.stdin.buffer.read().split()
    if not tokens:
        return
    n = int(tokens[0])
    operations = int(tokens[1])
    initial = int(tokens[2])
    idx = 3
    bit = [0] * (n + 2)

    def add(pos: int, value: int) -> None:
        while pos <= n + 1:
            bit[pos] += value
            pos += pos & -pos

    def prefix(pos: int) -> int:
        total = 0
        while pos:
            total += bit[pos]
            pos -= pos & -pos
        return total

    out: list[str] = []
    for _ in range(operations):
        op = tokens[idx]
        idx += 1
        if op == b"S":
            left = int(tokens[idx])
            right = int(tokens[idx + 1])
            value = int(tokens[idx + 2])
            idx += 3
            add(left, value)
            add(right + 1, -value)
        else:
            pos = int(tokens[idx])
            idx += 1
            out.append(str(initial + prefix(pos)))

    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
