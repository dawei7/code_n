def solve(max_k: int = 12000) -> int:
    """Find sum of all minimal product-sum numbers for 2 <= k <= max_k.
    
    Time Complexity: O(Factorizations)
    Space Complexity: O(max_k)
    """
    max_val = 2 * max_k
    min_k = [float('inf')] * (max_k + 1)

    def get_factors(prod: int, sum_f: int, num_f: int, start_f: int):
        k = prod - sum_f + num_f
        if k <= max_k:
            if prod < min_k[k]:
                min_k[k] = prod

        for f in range(start_f, max_val // prod + 1):
            get_factors(prod * f, sum_f + f, num_f + 1, f)

    get_factors(1, 0, 0, 2)

    return sum(set(min_k[2:]))
