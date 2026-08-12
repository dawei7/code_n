import bisect
import math


def solve(limit: int = 190, mod: int = 10**16) -> int:
    """Find PSR(p) mod 10^16 where p is the product of primes < limit.
    
    Time Complexity: O(2^(N/2) * log(2^(N/2))) Meet-in-the-Middle for N primes
    Space Complexity: O(2^(N/2))
    """
    if limit <= 2:
        return 1

    def get_primes(n: int):
        sieve = [True] * (n + 1)
        sieve[0] = sieve[1] = False
        for i in range(2, int(n**0.5) + 1):
            if sieve[i]:
                for j in range(i * i, n + 1, i):
                    sieve[j] = False
        return [i for i in range(n + 1) if sieve[i]]

    primes = get_primes(limit - 1)
    N = len(primes)
    if N == 0:
        return 1

    log_primes = [math.log(p) for p in primes]
    half_log_sum = sum(log_primes) / 2.0

    mid = N // 2
    p1 = primes[:mid]
    log1 = log_primes[:mid]

    p2 = primes[mid:]
    log2 = log_primes[mid:]

    left_subsets = []

    def gen_left(idx: int, curr_log: float, curr_val: int):
        if idx == len(p1):
            left_subsets.append((curr_log, curr_val))
            return
        gen_left(idx + 1, curr_log, curr_val)
        gen_left(idx + 1, curr_log + log1[idx], (curr_val * p1[idx]) % mod)

    gen_left(0, 0.0, 1)

    left_subsets.sort(key=lambda x: x[0])
    left_logs = [x[0] for x in left_subsets]

    best_log = -1.0
    best_val_mod = 0

    def gen_right_and_match(idx: int, curr_log: float, curr_val: int):
        nonlocal best_log, best_val_mod
        if idx == len(p2):
            rem_log = half_log_sum - curr_log
            if rem_log >= 0:
                pos = bisect.bisect_right(left_logs, rem_log) - 1
                if pos >= 0:
                    matched_log = curr_log + left_logs[pos]
                    if matched_log > best_log:
                        best_log = matched_log
                        best_val_mod = (curr_val * left_subsets[pos][1]) % mod
            return

        gen_right_and_match(idx + 1, curr_log, curr_val)
        gen_right_and_match(idx + 1, curr_log + log2[idx], (curr_val * p2[idx]) % mod)

    gen_right_and_match(0, 0.0, 1)

    return best_val_mod

