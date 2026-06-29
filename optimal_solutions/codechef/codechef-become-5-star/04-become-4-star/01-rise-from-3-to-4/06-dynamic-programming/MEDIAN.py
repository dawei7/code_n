import sys

def operations_needed(values: list[int]) -> int:
    n = len(values)
    maximum = max(values)
    start = 0
    for i, value in enumerate(values):
        if value == maximum:
            start |= 1 << i
    full = (1 << n) - 1
    if start == full:
        return 0
    interval_masks: list[tuple[int, int]] = []
    for left in range(n):
        mask = 0
        for right in range(left, n):
            mask |= 1 << right
            length = right - left + 1
            need = (length + 1) // 2
            interval_masks.append((mask, need))
    memo: dict[tuple[int, int], bool] = {}

    def can_finish(mask: int, depth: int) -> bool:
        if mask == full:
            return True
        if depth == 0:
            return False
        key = (mask, depth)
        if key in memo:
            return memo[key]
        current_count = mask.bit_count()
        if current_count << depth < n:
            memo[key] = False
            return False
        next_masks = []
        for interval, need in interval_masks:
            missing = interval & ~mask
            if missing and (mask & interval).bit_count() >= need:
                next_masks.append(mask | interval)
        next_masks.sort(key=int.bit_count, reverse=True)
        last = -1
        for nxt in next_masks:
            if nxt == last:
                continue
            last = nxt
            if can_finish(nxt, depth - 1):
                memo[key] = True
                return True
        memo[key] = False
        return False
    for depth in range(1, 7):
        memo.clear()
        if can_finish(start, depth):
            return depth
    return 7

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    t = data[0]
    idx = 1
    out: list[str] = []
    for _ in range(t):
        n = data[idx]
        idx += 1
        values = data[idx:idx + n]
        idx += n
        out.append(str(operations_needed(values)))
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
