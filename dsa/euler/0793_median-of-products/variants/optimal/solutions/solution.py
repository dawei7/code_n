"""Project Euler Problem 793: Median of Products.

Find M(1000003), the median of pairwise products S_i * S_j for 0 <= i < j < n,
where S_0 = 290797, S_{i+1} = S_i^2 mod 50515093.
"""

from typing import List


def _generate_sorted_s(n: int) -> List[int]:
    s0 = 290797
    array = []
    for _ in range(n):
        array.append(s0)
        s0 = (s0 * s0) % 50515093
    return sorted(array)


def _count_products_at_most(values: List[int], threshold: int) -> int:
    count = 0
    right = len(values) - 1

    for left, value in enumerate(values):
        while right > left and value * values[right] > threshold:
            right -= 1
        if right <= left:
            break
        count += right - left

    return count


def solve(n: int = 1_000_003) -> int:
    """Compute M(n) using binary search over candidate products with two-pointer predicate."""
    values = _generate_sorted_s(n)
    lo = values[0] * values[1]
    hi = values[-1] * values[-2]
    target = ((n * (n - 1)) // 2 + 1) // 2

    while lo < hi:
        mid = (lo + hi) // 2
        if _count_products_at_most(values, mid) >= target:
            hi = mid
        else:
            lo = mid + 1

    return lo


if __name__ == "__main__":
    print(solve())
