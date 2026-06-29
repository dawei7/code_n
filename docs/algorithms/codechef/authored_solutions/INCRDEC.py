import sys
from collections import Counter


def build_sequence(values: list[int]) -> list[int] | None:
    counts = Counter(values)
    if any(freq > 2 for freq in counts.values()):
        return None

    unique = sorted(counts)
    duplicates = [value for value in unique if counts[value] == 2]
    if duplicates and duplicates[-1] == unique[-1]:
        return None

    return unique + duplicates[::-1]


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    t = data[0]
    idx = 1
    out: list[str] = []
    for _ in range(t):
        n = data[idx]
        idx += 1
        values = data[idx : idx + n]
        idx += n
        sequence = build_sequence(values)
        if sequence is None:
            out.append("NO")
        else:
            out.append("YES")
            out.append(" ".join(map(str, sequence)))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
