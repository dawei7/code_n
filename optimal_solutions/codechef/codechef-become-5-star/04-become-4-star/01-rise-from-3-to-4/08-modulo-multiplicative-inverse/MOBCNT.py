import sys
from collections import Counter
MOD = 1000000007

def build_factorials(limit: int):
    fact = [1] * (limit + 1)
    for i in range(1, limit + 1):
        fact[i] = fact[i - 1] * i % MOD
    inv_fact = [1] * (limit + 1)
    inv_fact[limit] = pow(fact[limit], MOD - 2, MOD)
    for i in range(limit, 0, -1):
        inv_fact[i - 1] = inv_fact[i] * i % MOD
    return (fact, inv_fact)

def choose(n: int, r: int, fact: list[int], inv_fact: list[int]) -> int:
    if r < 0 or r > n:
        return 0
    return fact[n] * inv_fact[r] % MOD * inv_fact[n - r] % MOD

def solve_case(weights: list[int], fact: list[int], inv_fact: list[int]) -> int:
    total = sum(weights)
    by_depth = Counter()
    for weight in weights:
        if total % weight:
            return 0
        ratio = total // weight
        if ratio & ratio - 1:
            return 0
        by_depth[ratio.bit_length() - 1] += 1
    answer = 1
    slots = 1
    max_depth = max(by_depth)
    for depth in range(max_depth + 1):
        leaves = by_depth.get(depth, 0)
        if leaves > slots:
            return 0
        answer = answer * choose(slots, leaves, fact, inv_fact) % MOD
        slots = (slots - leaves) * 2
    return answer if slots == 0 else 0

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    t = data[0]
    idx = 1
    cases = []
    max_n = 0
    for _ in range(t):
        n = data[idx]
        idx += 1
        weights = data[idx:idx + n]
        idx += n
        cases.append(weights)
        if n > max_n:
            max_n = n
    fact, inv_fact = build_factorials(max_n)
    sys.stdout.write('\n'.join((str(solve_case(case, fact, inv_fact)) for case in cases)))


if __name__ == "__main__":
    solve()
