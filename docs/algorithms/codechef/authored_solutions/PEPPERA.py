import sys


def balance_grid(grid: list[str]) -> list[str]:
    n = len(grid)
    half = n // 2
    diffs = [row[:half].count("1") - row[half:].count("1") for row in grid]
    total_abs = sum(abs(value) for value in diffs)
    offset = total_abs

    possible = {0}
    parents: list[dict[int, tuple[int, bool]]] = []
    for diff in diffs:
        parent: dict[int, tuple[int, bool]] = {}
        new_possible = set()
        for value in possible:
            keep = value + diff
            rev = value - diff
            if keep not in parent:
                parent[keep] = (value, False)
            if rev not in parent:
                parent[rev] = (value, True)
            new_possible.add(keep)
            new_possible.add(rev)
        parents.append(parent)
        possible = new_possible

    best = min(possible, key=abs)
    reverse = [False] * n
    current = best
    for i in range(n - 1, -1, -1):
        previous, reversed_row = parents[i][current]
        reverse[i] = reversed_row
        current = previous

    return [row[::-1] if reverse[i] else row for i, row in enumerate(grid)]


def main() -> None:
    tokens = sys.stdin.buffer.read().split()
    if not tokens:
        return
    t = int(tokens[0])
    idx = 1
    out: list[str] = []
    for _ in range(t):
        n = int(tokens[idx])
        idx += 1
        grid = [tokens[idx + i].decode() for i in range(n)]
        idx += n
        out.extend(balance_grid(grid))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
