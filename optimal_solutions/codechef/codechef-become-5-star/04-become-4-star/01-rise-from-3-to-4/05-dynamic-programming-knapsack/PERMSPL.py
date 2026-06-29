import sys

def possible(values: list[int]) -> bool:
    n = len(values)
    degree = [0] * n
    for i in range(n):
        vi = values[i]
        for j in range(i + 1, n):
            if vi > values[j]:
                degree[i] += 1
                degree[j] += 1
    target_twice = sum(degree)
    if target_twice & 1:
        return False
    target = target_twice // 2
    bits = 1
    mask = (1 << target + 1) - 1
    for value in degree:
        bits |= bits << value
        bits &= mask
    return bits >> target & 1 == 1

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
        out.append('YES' if possible(values) else 'NO')
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
