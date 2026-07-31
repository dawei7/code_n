def solve(nums: list[int], maxVal: int) -> int:
    limit = max(maxVal, max(nums))
    frequency = [0] * (limit + 1)
    for value in nums:
        frequency[value] += 1
    divisible_count = [0] * (limit + 1)
    for divisor in range(1, limit + 1):
        divisible_count[divisor] = sum((frequency[multiple] for multiple in range(divisor, limit + 1, divisor)))
    smallest_prime = list(range(limit + 1))
    factor = 2
    while factor * factor <= limit:
        if smallest_prime[factor] == factor:
            for multiple in range(factor * factor, limit + 1, factor):
                if smallest_prime[multiple] == multiple:
                    smallest_prime[multiple] = factor
        factor += 1
    best_score = 0
    for selected_value in range(1, limit + 1):
        if selected_value > maxVal and frequency[selected_value] == 0:
            continue
        remaining = selected_value
        prime_factors = []
        while remaining > 1:
            prime = smallest_prime[remaining]
            prime_factors.append(prime)
            while remaining % prime == 0:
                remaining //= prime
        signed_products = [(1, -1)]
        for prime in prime_factors:
            signed_products += [(product * prime, -sign) for product, sign in signed_products]
        shared_factor_count = sum((sign * divisible_count[product] for product, sign in signed_products[1:]))
        if frequency[selected_value] > 0:
            modification_cost = shared_factor_count
            if selected_value > 1:
                modification_cost -= 1
        elif shared_factor_count > 0:
            modification_cost = shared_factor_count
        else:
            modification_cost = 1
        best_score = max(best_score, selected_value - modification_cost)
    return best_score
