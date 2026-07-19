import math
from typing import List

def solve(coins: List[int], k: int) -> int:
    """
    Finds the k-th smallest multiple using binary search and inclusion-exclusion.
    """
    coins = sorted(set(coins))
    reduced: list[int] = []
    for coin in coins:
        if not any(coin % existing == 0 for existing in reduced):
            reduced.append(coin)
    coins = reduced

    def get_lcm(a, b):
        return abs(a * b) // math.gcd(a, b)

    high = min(coins) * k
    terms: list[tuple[int, int]] = []

    def build_terms(index: int, current_lcm: int, parity: int) -> None:
        for pos in range(index, len(coins)):
            next_lcm = get_lcm(current_lcm, coins[pos])
            if next_lcm > high:
                continue
            terms.append((next_lcm, parity))
            build_terms(pos + 1, next_lcm, -parity)

    build_terms(0, 1, 1)

    def count_multiples(mid: int) -> int:
        count = 0
        for lcm_val, sign in terms:
            count += sign * (mid // lcm_val)
        return count

    low = min(coins)
    ans = high

    while low <= high:
        mid = (low + high) // 2
        if count_multiples(mid) >= k:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    return ans
