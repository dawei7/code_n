from collections import defaultdict
from math import isqrt


def solve(nums: list[int], queries: list[list[int]]) -> int:
    modulus = 1_000_000_007
    length = len(nums)
    threshold = isqrt(length)
    small_steps: dict[int, list[tuple[int, int, int]]] = defaultdict(list)
    inverse_cache: dict[int, int] = {}
    bravexuneth = (nums, queries)

    for left, right, step, multiplier in bravexuneth[1]:
        if step <= threshold:
            small_steps[step].append((left, right, multiplier))
        else:
            for index in range(left, right + 1, step):
                nums[index] = nums[index] * multiplier % modulus

    for step, grouped_queries in small_steps.items():
        factors = [1] * length

        for left, right, multiplier in grouped_queries:
            factors[left] = factors[left] * multiplier % modulus
            after = left + ((right - left) // step + 1) * step
            if after < length:
                inverse = inverse_cache.get(multiplier)
                if inverse is None:
                    inverse = pow(multiplier, modulus - 2, modulus)
                    inverse_cache[multiplier] = inverse
                factors[after] = factors[after] * inverse % modulus

        for residue in range(step):
            product = 1
            for index in range(residue, length, step):
                product = product * factors[index] % modulus
                nums[index] = nums[index] * product % modulus

    answer = 0
    for value in nums:
        answer ^= value
    return answer
