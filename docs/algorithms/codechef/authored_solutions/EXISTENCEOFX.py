import sys


def exists(a: int, b: int, c: int) -> bool:
    states = {0}
    for bit in range(62):
        abit = (a >> bit) & 1
        bbit = (b >> bit) & 1
        cbit = (c >> bit) & 1
        nxt = set()
        for carry in states:
            for xbit in (0, 1):
                total = (abit ^ xbit) + (bbit ^ xbit) + carry
                if (total & 1) == (cbit ^ xbit):
                    nxt.add(total >> 1)
        states = nxt
        if not states:
            return False
    return 0 in states


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        a, b, c = data[idx:idx + 3]
        idx += 3
        out.append("YES" if exists(a, b, c) else "NO")
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
