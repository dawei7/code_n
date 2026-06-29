import sys


def main() -> None:
    tokens = sys.stdin.buffer.read().split()
    t = int(tokens[0])
    out = []
    transitions = {
        1: (1, 2),
        2: (3, 2),
        3: (4, 2),
        4: (5, 2),
        5: (1, 2),
    }
    for raw in tokens[1:1 + t]:
        state = 1
        for ch in raw:
            state = transitions[state][ch - 48]
        out.append("YES" if state == 5 else "NO")
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
