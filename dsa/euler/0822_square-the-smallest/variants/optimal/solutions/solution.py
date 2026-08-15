import heapq
import math


def solve(n: int = 10000, m: int = 10**16) -> int:
    """Find S(10^4, 10^16) mod 1234567891 for sum of numbers after m squarings.

    Log-scale heap equilibrium simulation and modular double-exponentiation loop.

    Time Complexity: O(n log n + log m)
    Space Complexity: O(n)
    """
    MOD = 1234567891

    # Exact simulation for small m
    if m <= 1000:
        heap = [i for i in range(2, n + 1)]
        heapq.heapify(heap)
        for _ in range(m):
            val = heapq.heappop(heap)
            heapq.heappush(heap, val * val)
        return sum(heap) % MOD

    # Log-scale heap simulation for large m
    heap = [(math.log(math.log(i)), i, 0) for i in range(2, n + 1)]
    heapq.heapify(heap)

    rounds = 0
    max_loglog = math.log(math.log(n))

    # Equilibrium phase: square elements until log-log values exceed max_loglog
    while rounds < m:
        loglog, init, cnt = heapq.heappop(heap)
        if loglog > max_loglog:
            heapq.heappush(heap, (loglog, init, cnt))
            break

        # Compute next log-log value
        cnt += 1
        new_loglog = loglog + math.log(2)
        heapq.heappush(heap, (new_loglog, init, cnt))
        rounds += 1

    rem_m = m - rounds
    q = rem_m // (n - 1)
    r = rem_m % (n - 1)

    sorted_heap = sorted(heap, key=lambda item: item[0])
    total_sum = 0

    for idx, (loglog, init, cnt) in enumerate(sorted_heap):
        extra = q + (1 if idx < r else 0)
        final_cnt = cnt + extra
        # Double modular exponentiation: init^(2^final_cnt) mod MOD
        exp2 = pow(2, final_cnt, MOD - 1)
        val = pow(init, exp2, MOD)
        total_sum = (total_sum + val) % MOD

    return total_sum


if __name__ == "__main__":
    print(solve())
