"""Last-balloon interval dynamic programming for LeetCode 312."""


def _max_coins(nums: list[int]) -> int:
    values = [1, *nums, 1]
    size = len(values)
    best = [[0] * size for _ in range(size)]
    for width in range(2, size):
        for left in range(size - width):
            right = left + width
            boundary_product = values[left] * values[right]
            best[left][right] = max(
                best[left][last]
                + boundary_product * values[last]
                + best[last][right]
                for last in range(left + 1, right)
            )
    return best[0][size - 1]


def solve(nums: list[int]) -> int:
    return _max_coins(nums)
