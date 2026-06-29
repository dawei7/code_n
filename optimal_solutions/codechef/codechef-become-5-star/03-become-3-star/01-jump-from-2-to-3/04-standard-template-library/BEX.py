import sys

def solve() -> None:
    buffer = sys.stdin.buffer
    line = buffer.readline()
    if not line:
        return
    actions = int(line)
    pile: list[tuple[int, bytes]] = []
    minima: list[int] = []
    out: list[str] = []
    for _ in range(actions):
        parts = buffer.readline().split()
        value = int(parts[0])
        if value == -1:
            idx = minima.pop()
            above = len(pile) - idx - 1
            _exercises, name = pile[idx]
            out.append(f'{above} {name.decode()}')
            del pile[idx:]
            continue
        if value > 0:
            pile.append((value, parts[1]))
            if not minima or value <= pile[minima[-1]][0]:
                minima.append(len(pile) - 1)
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
