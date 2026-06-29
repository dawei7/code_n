import sys

def can_sort_once(arr):
    n = len(arr)
    values = sorted(set(arr))
    rank = {v: i for i, v in enumerate(values)}
    k = len(values)
    ranks = [rank[v] for v in arr]
    low_mark = [False] * (k + 1)
    high_mark = [False] * k
    bit = [0] * (k + 1)

    def add(pos: int) -> None:
        pos += 1
        while pos <= k:
            bit[pos] += 1
            pos += pos & -pos

    def prefix(pos: int) -> int:
        pos += 1
        total = 0
        while pos:
            total += bit[pos]
            pos -= pos & -pos
        return total

    def kth(target: int) -> int:
        pos = 0
        step = 1 << k.bit_length() - 1
        while step:
            nxt = pos + step
            if nxt <= k and bit[nxt] < target:
                target -= bit[nxt]
                pos = nxt
            step >>= 1
        return pos
    for r in ranks:
        seen_le = prefix(r)
        seen_total = prefix(k - 1)
        if seen_total > seen_le:
            successor = kth(seen_le + 1)
            low_mark[successor + 1] = True
            high_mark[r] = True
        add(r)
    low_bad = [False] * (k + 1)
    cur = False
    for i in range(k + 1):
        cur = cur or low_mark[i]
        low_bad[i] = cur
    high_bad = [False] * k
    cur = False
    for i in range(k - 1, -1, -1):
        high_bad[i] = cur
        cur = cur or high_mark[i]
    if not low_bad[k]:
        return True
    last_less = [-1] * k
    seen_last = -1
    for i, r in enumerate(ranks):
        if r > 0:
            pass
        seen_last = max(seen_last, i if r == 0 else seen_last)
    last_pos = [-1] * k
    first_pos = [n] * k
    positions = [[] for _ in range(k)]
    for i, r in enumerate(ranks):
        last_pos[r] = i
        first_pos[r] = min(first_pos[r], i)
        positions[r].append(i)
    running = -1
    for r in range(k):
        last_less[r] = running
        running = max(running, last_pos[r])
    first_greater = [n] * k
    running = n
    for r in range(k - 1, -1, -1):
        first_greater[r] = running
        running = min(running, first_pos[r])
    for r in range(k):
        if low_bad[r] or high_bad[r]:
            continue
        lo = last_less[r]
        hi = first_greater[r]
        if all((pos >= lo or pos <= hi for pos in positions[r])):
            return True
    return False

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        n = data[idx]
        idx += 1
        arr = data[idx:idx + n]
        idx += n
        out.append('YES' if can_sort_once(arr) else 'NO')
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
