from math import gcd


def solve(nums: list[int], p: int, queries: list[list[int]]) -> int:
    n = len(nums)

    maximum_reduced = 1
    for value in nums:
        if value % p == 0:
            maximum_reduced = max(maximum_reduced, value // p)
    for _, value in queries:
        if value % p == 0:
            maximum_reduced = max(maximum_reduced, value // p)

    smallest_factor = list(range(maximum_reduced + 1))
    for candidate in range(2, int(maximum_reduced**0.5) + 1):
        if smallest_factor[candidate] != candidate:
            continue
        for multiple in range(candidate * candidate, maximum_reduced + 1, candidate):
            if smallest_factor[multiple] == multiple:
                smallest_factor[multiple] = candidate

    factor_cache: list[tuple[int, ...] | None] = [None] * (maximum_reduced + 1)
    factor_cache[1] = ()

    def prime_memberships(value: int) -> tuple[int, ...]:
        cached = factor_cache[value]
        if cached is not None:
            return cached

        original = value
        factors: list[int] = []
        while value > 1:
            prime = smallest_factor[value]
            factors.append(prime)
            while value % prime == 0:
                value //= prime
        factor_cache[original] = tuple(factors)
        return factor_cache[original]

    reduced = [value // p if value % p == 0 else 0 for value in nums]
    eligible_count = sum(value != 0 for value in reduced)

    leaf_count = 1
    while leaf_count < n:
        leaf_count *= 2
    gcd_tree = [0] * (2 * leaf_count)
    gcd_tree[leaf_count : leaf_count + n] = reduced
    for node in range(leaf_count - 1, 0, -1):
        gcd_tree[node] = gcd(gcd_tree[node * 2], gcd_tree[node * 2 + 1])

    membership_count = [0] * (maximum_reduced + 1)
    membership_xor = [0] * (maximum_reduced + 1)
    every_index_xor = 0
    for index, value in enumerate(reduced):
        every_index_xor ^= index
        if value:
            for prime in prime_memberships(value):
                membership_count[prime] += 1
                membership_xor[prime] ^= index

    critical_multiplicity: dict[int, int] = {}

    def add_critical_prime(prime: int) -> None:
        if membership_count[prime] == n - 1:
            missing_index = every_index_xor ^ membership_xor[prime]
            critical_multiplicity[missing_index] = (
                critical_multiplicity.get(missing_index, 0) + 1
            )

    def remove_critical_prime(prime: int) -> None:
        if membership_count[prime] != n - 1:
            return
        missing_index = every_index_xor ^ membership_xor[prime]
        remaining = critical_multiplicity[missing_index] - 1
        if remaining:
            critical_multiplicity[missing_index] = remaining
        else:
            del critical_multiplicity[missing_index]

    for prime in range(2, maximum_reduced + 1):
        add_critical_prime(prime)

    successful_queries = 0
    for index, new_value in queries:
        old_reduced = reduced[index]
        new_reduced = new_value // p if new_value % p == 0 else 0
        old_primes = set(prime_memberships(old_reduced)) if old_reduced else set()
        new_primes = set(prime_memberships(new_reduced)) if new_reduced else set()

        for prime in old_primes ^ new_primes:
            remove_critical_prime(prime)
            if prime in old_primes:
                membership_count[prime] -= 1
            else:
                membership_count[prime] += 1
            membership_xor[prime] ^= index
            add_critical_prime(prime)

        if bool(old_reduced) != bool(new_reduced):
            eligible_count += 1 if new_reduced else -1
        reduced[index] = new_reduced

        node = leaf_count + index
        gcd_tree[node] = new_reduced
        node //= 2
        while node:
            gcd_tree[node] = gcd(gcd_tree[node * 2], gcd_tree[node * 2 + 1])
            node //= 2

        if gcd_tree[1] == 1 and (
            eligible_count < n or len(critical_multiplicity) < n
        ):
            successful_queries += 1

    return successful_queries
