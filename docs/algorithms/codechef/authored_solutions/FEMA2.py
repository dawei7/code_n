import sys
from collections import deque


def matched_pairs(row: str, power: int) -> int:
    sheets = [0] * (len(row) + 1)
    for i, ch in enumerate(row):
        sheets[i + 1] = sheets[i] + (1 if ch == ":" else 0)

    magnets: deque[int] = deque()
    irons: deque[int] = deque()
    answer = 0

    for i, ch in enumerate(row):
        if ch == "X":
            magnets.clear()
            irons.clear()
            continue
        if ch == "M":
            magnets.append(i)
        elif ch == "I":
            irons.append(i)
        else:
            continue

        while magnets and irons:
            m = magnets[0]
            iron = irons[0]
            lo, hi = sorted((m, iron))
            sheet_count = sheets[hi] - sheets[lo + 1]
            attraction = power + 1 - abs(m - iron) - sheet_count
            if attraction > 0:
                answer += 1
                magnets.popleft()
                irons.popleft()
            elif m < iron:
                magnets.popleft()
            else:
                irons.popleft()

    return answer


def main() -> None:
    tokens = sys.stdin.buffer.read().split()
    if not tokens:
        return
    t = int(tokens[0])
    idx = 1
    out: list[str] = []
    for _ in range(t):
        n = int(tokens[idx])
        power = int(tokens[idx + 1])
        row = tokens[idx + 2].decode()
        idx += 3
        out.append(str(matched_pairs(row, power)))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
