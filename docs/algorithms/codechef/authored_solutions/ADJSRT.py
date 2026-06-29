import sys
from collections import defaultdict, deque


def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n = data[0]
    values = data[1:1 + n]

    occurrence: dict[int, int] = defaultdict(int)
    current = []
    for value in values:
        occurrence[value] += 1
        current.append((value, occurrence[value]))

    occurrence.clear()
    target = []
    for value in sorted(values):
        occurrence[value] += 1
        target.append((value, occurrence[value]))

    pos = {label: i for i, label in enumerate(current)}
    swaps = []
    for i, needed in enumerate(target):
        j = pos[needed]
        while j > i:
            left = current[j - 1]
            right = current[j]
            current[j - 1], current[j] = right, left
            pos[right] = j - 1
            pos[left] = j
            swaps.append(j - 1)
            j -= 1

    out = [str(len(swaps))]
    out.append(" ".join(map(str, swaps)))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
