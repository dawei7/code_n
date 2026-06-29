import sys

def possible(values: list[int], groups: int, mask: int) -> bool:
    count = len(values)
    if groups > count:
        return False
    prefix = [0] * (count + 1)
    for i, value in enumerate(values):
        prefix[i + 1] = prefix[i] + value
    dp = [0] * (groups + 1)
    dp[0] = 1
    for end in range(1, count + 1):
        next_dp = dp[:]
        bit = 1 << end
        for start in range(end):
            if prefix[end] - prefix[start] & mask != mask:
                continue
            start_bit = 1 << start
            upto = min(groups, end)
            for used in range(1, upto + 1):
                if dp[used - 1] & start_bit:
                    next_dp[used] |= bit
        dp = next_dp
    return bool(dp[groups] & 1 << count)

def best_and(values: list[int], groups: int) -> int:
    if groups <= 0:
        return 0
    values = [value for value in values if value]
    if groups > len(values):
        return 0
    answer = 0
    total = sum(values)
    for bit in range(total.bit_length() - 1, -1, -1):
        candidate = answer | 1 << bit
        if possible(values, groups, candidate):
            answer = candidate
    return answer

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n = data[0]
    idx = 1
    taste = data[idx:idx + n]
    idx += n
    q = data[idx]
    idx += 1
    out = []
    for _ in range(q):
        groups = data[idx]
        idx += 1
        toppings = data[idx:idx + n]
        idx += n
        values = [a * t for a, t in zip(taste, toppings) if t]
        out.append(str(best_and(values, groups)))
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
