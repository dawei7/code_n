import sys
MOD = 1000000007
INV2 = (MOD + 1) // 2

def build_answer(box_size: int, max_count: int, freq_prefix: list[int], fact: list[int], inv_fact: list[int]) -> int:
    total_boxes = 0
    arrangements = 1
    half_arrangements = 1
    half_boxes = 0
    odd = 0
    left = 1
    while left <= max_count:
        boxes = (left + box_size - 1) // box_size
        right = min(max_count, boxes * box_size)
        amount = freq_prefix[right] - freq_prefix[left - 1]
        if amount:
            total_boxes += boxes * amount
            arrangements = arrangements * pow(inv_fact[boxes], amount, MOD) % MOD
            half = boxes // 2
            half_boxes += half * amount
            half_arrangements = half_arrangements * pow(inv_fact[half], amount, MOD) % MOD
            if boxes & 1:
                odd += amount
        left = right + 1
    arrangements = arrangements * fact[total_boxes] % MOD
    if odd <= 1:
        palindrome = fact[half_boxes] * half_arrangements % MOD
    else:
        palindrome = 0
    return (arrangements + palindrome) * INV2 % MOD

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n = data[0]
    counts = data[1:1 + n]
    q_idx = 1 + n
    q = data[q_idx]
    queries = data[q_idx + 1:q_idx + 1 + q]
    max_count = max(counts, default=0)
    total_count = sum(counts)
    fact = [1] * (total_count + n + 1)
    for i in range(1, len(fact)):
        fact[i] = fact[i - 1] * i % MOD
    inv_fact = [1] * len(fact)
    inv_fact[-1] = pow(fact[-1], MOD - 2, MOD)
    for i in range(len(fact) - 1, 0, -1):
        inv_fact[i - 1] = inv_fact[i] * i % MOD
    freq = [0] * (max_count + 1)
    for value in counts:
        freq[value] += 1
    freq_prefix = [0] * (max_count + 1)
    for i in range(1, max_count + 1):
        freq_prefix[i] = freq_prefix[i - 1] + freq[i]
    cache: dict[int, int] = {}
    out: list[str] = []
    for size in queries:
        if size not in cache:
            if size > max_count:
                palindrome = 1 if n <= 1 else 0
                cache[size] = (fact[n] + palindrome) * INV2 % MOD
            else:
                cache[size] = build_answer(size, max_count, freq_prefix, fact, inv_fact)
        out.append(str(cache[size]))
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
