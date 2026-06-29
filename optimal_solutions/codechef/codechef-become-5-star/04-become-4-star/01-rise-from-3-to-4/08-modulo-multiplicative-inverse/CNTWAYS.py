import sys
MOD = 1000000007

def build_factorials(limit: int) -> tuple[list[int], list[int]]:
    fact = [1] * (limit + 1)
    for i in range(1, limit + 1):
        fact[i] = fact[i - 1] * i % MOD
    inv_fact = [1] * (limit + 1)
    inv_fact[limit] = pow(fact[limit], MOD - 2, MOD)
    for i in range(limit, 0, -1):
        inv_fact[i - 1] = inv_fact[i] * i % MOD
    return (fact, inv_fact)

def comb(n: int, k: int, fact: list[int], inv_fact: list[int]) -> int:
    if k < 0 or k > n:
        return 0
    return fact[n] * inv_fact[k] % MOD * inv_fact[n - k] % MOD

def valid_paths(width: int, height: int, cut_width: int, cut_height: int, fact: list[int], inv_fact: list[int]) -> int:
    total = comb(width + height, width, fact, inv_fact)
    invalid = 0
    left_x = width - cut_width
    for y in range(cut_height):
        before = comb(left_x + y, left_x, fact, inv_fact)
        after = comb(cut_width - 1 + (height - y), cut_width - 1, fact, inv_fact)
        invalid = (invalid + before * after) % MOD
    return (total - invalid) % MOD

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    r = data[0]
    cases = []
    idx = 1
    max_sum = 0
    for _ in range(r):
        n, m, a, b = (data[idx], data[idx + 1], data[idx + 2], data[idx + 3])
        idx += 4
        cases.append((n, m, a, b))
        max_sum = max(max_sum, n + m)
    fact, inv_fact = build_factorials(max_sum)
    out = [str(valid_paths(n, m, a, b, fact, inv_fact)) for n, m, a, b in cases]
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
