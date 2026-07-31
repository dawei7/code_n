from math import gcd


class Solution:
    def countGoodSubseq(
        self, nums: list[int], p: int, queries: list[list[int]]
    ) -> int:
        n = len(nums)
        factor_limit = 1
        for value in nums:
            if value % p == 0:
                factor_limit = max(factor_limit, value // p)
        for _, value in queries:
            if value % p == 0:
                factor_limit = max(factor_limit, value // p)

        smallest_prime = list(range(factor_limit + 1))
        for prime in range(2, int(factor_limit**0.5) + 1):
            if smallest_prime[prime] != prime:
                continue
            for multiple in range(prime * prime, factor_limit + 1, prime):
                if smallest_prime[multiple] == multiple:
                    smallest_prime[multiple] = prime

        factor_cache: list[tuple[int, ...] | None] = [None] * (factor_limit + 1)
        factor_cache[1] = ()

        def distinct_factors(value: int) -> tuple[int, ...]:
            cached = factor_cache[value]
            if cached is not None:
                return cached
            original = value
            factors: list[int] = []
            while value > 1:
                prime = smallest_prime[value]
                factors.append(prime)
                while value % prime == 0:
                    value //= prime
            result = tuple(factors)
            factor_cache[original] = result
            return result

        scaled = [value // p if value % p == 0 else 0 for value in nums]
        active_count = sum(value > 0 for value in scaled)

        size = 1
        while size < n:
            size *= 2
        tree = [0] * (2 * size)
        tree[size : size + n] = scaled
        for node in range(size - 1, 0, -1):
            tree[node] = gcd(tree[2 * node], tree[2 * node + 1])

        factor_counts = [0] * (factor_limit + 1)
        factor_index_xors = [0] * (factor_limit + 1)
        all_indices_xor = 0
        for index, value in enumerate(scaled):
            all_indices_xor ^= index
            if value == 0:
                continue
            for prime in distinct_factors(value):
                factor_counts[prime] += 1
                factor_index_xors[prime] ^= index

        critical_indices: dict[int, int] = {}
        for prime in range(2, factor_limit + 1):
            if factor_counts[prime] == n - 1:
                missing = all_indices_xor ^ factor_index_xors[prime]
                critical_indices[missing] = critical_indices.get(missing, 0) + 1

        def detach_critical(prime: int) -> None:
            if factor_counts[prime] != n - 1:
                return
            missing = all_indices_xor ^ factor_index_xors[prime]
            remaining = critical_indices[missing] - 1
            if remaining:
                critical_indices[missing] = remaining
            else:
                del critical_indices[missing]

        def attach_critical(prime: int) -> None:
            if factor_counts[prime] != n - 1:
                return
            missing = all_indices_xor ^ factor_index_xors[prime]
            critical_indices[missing] = critical_indices.get(missing, 0) + 1

        answer = 0
        for index, value in queries:
            old_scaled = scaled[index]
            new_scaled = value // p if value % p == 0 else 0

            old_factors = set(distinct_factors(old_scaled)) if old_scaled else set()
            new_factors = set(distinct_factors(new_scaled)) if new_scaled else set()

            for prime in old_factors ^ new_factors:
                detach_critical(prime)
                if prime in old_factors:
                    factor_counts[prime] -= 1
                else:
                    factor_counts[prime] += 1
                factor_index_xors[prime] ^= index
                attach_critical(prime)

            if bool(old_scaled) != bool(new_scaled):
                active_count += 1 if new_scaled else -1

            scaled[index] = new_scaled
            node = size + index
            tree[node] = new_scaled
            node //= 2
            while node:
                tree[node] = gcd(tree[2 * node], tree[2 * node + 1])
                node //= 2

            if tree[1] == 1 and (
                active_count < n or len(critical_indices) < n
            ):
                answer += 1

        return answer
