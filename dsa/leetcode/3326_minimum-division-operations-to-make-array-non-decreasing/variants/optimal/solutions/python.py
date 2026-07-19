from functools import lru_cache


def _build_primes(limit: int = 1000) -> list[int]:
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for value in range(2, int(limit**0.5) + 1):
        if is_prime[value]:
            for multiple in range(value * value, limit + 1, value):
                is_prime[multiple] = False
    return [value for value in range(2, limit + 1) if is_prime[value]]


_PRIMES = _build_primes()


@lru_cache(maxsize=None)
def _smallest_prime_factor(value: int) -> int:
    if value < 4:
        return value
    for prime in _PRIMES:
        if prime * prime > value:
            return value
        if value % prime == 0:
            return prime
    return value


def solve(nums: list[int]) -> int:
    nums = nums[:]
    operations = 0

    for i in range(len(nums) - 2, -1, -1):
        if nums[i] <= nums[i + 1]:
            continue

        reduced = _smallest_prime_factor(nums[i])
        if reduced == nums[i] or reduced > nums[i + 1]:
            return -1

        nums[i] = reduced
        operations += 1

    return operations
