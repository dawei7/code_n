import bisect
import sys
MOD = 1000000007

def solve_case(intervals: list[tuple[int, int]]) -> tuple[int, str]:
    n = len(intervals)
    diff = [0] * (n + 2)
    for left, right in intervals:
        diff[left] += 1
        diff[right + 1] -= 1
    valid = []
    current = 0
    for k in range(n + 1):
        current += diff[k]
        if current == k:
            valid.append(k)
    candidates = valid[:]
    for left, right in intervals:
        if len(candidates) <= 1:
            break
        first_inside = bisect.bisect_left(candidates, left)
        first_after = bisect.bisect_right(candidates, right)
        inside_count = first_after - first_inside
        if inside_count == len(candidates):
            continue
        if inside_count:
            candidates = candidates[:first_inside] + candidates[first_after:]
    chosen = candidates[0]
    assignment = ''.join(('1' if left <= chosen <= right else '0' for left, right in intervals))
    return (len(valid) % MOD, assignment)

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
        intervals = []
        for _ in range(n):
            intervals.append((data[idx], data[idx + 1]))
            idx += 2
        count, assignment = solve_case(intervals)
        out.append(str(count))
        out.append(assignment)
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
