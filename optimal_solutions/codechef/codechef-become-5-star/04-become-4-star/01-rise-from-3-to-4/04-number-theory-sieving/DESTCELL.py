import sys

def destroyed_counts(rows: int, cols: int) -> list[int]:
    total = rows * cols
    answer: list[str] = []
    for step in range(1, total + 1):
        row_order_hits = (total + step - 1) // step
        intersection = 0
        for pos in range(0, total, step):
            r, c = divmod(pos, cols)
            if (c * rows + r) % step == 0:
                intersection += 1
        answer.append(str(2 * row_order_hits - intersection))
    return answer

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    t = data[0]
    idx = 1
    out: list[str] = []
    for _ in range(t):
        rows, cols = (data[idx], data[idx + 1])
        idx += 2
        out.append(' '.join(destroyed_counts(rows, cols)))
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
