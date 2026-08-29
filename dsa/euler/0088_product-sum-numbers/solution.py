def solve(max_k: int = 12000) -> int:
    """Find the sum of all minimal product-sum numbers N for 2 <= k <= max_k (12,000).

    Mathematical Principles Applied:
    1. Product-Sum Property:
       A positive integer N is a product-sum number of set size k if N can be written as:
       N = a_1 * a_2 * ... * a_m
       N = a_1 + a_2 + ... + a_m + (1 + 1 + ... + 1) [with k - m ones]
       Combining product and sum yields set size k:
       k = N - sum_{i=1}^m a_i + m.

    2. Upper Bound on Minimal N_k:
       For any k, N_k <= 2*k (since the set {1, 1, ..., 1, 2, k} has size k and product = sum = 2k).
       Therefore, we search factorizations for products up to 2 * max_k = 24,000.

    3. Recursive Factorization Backtracking:
       Recursively generate all factorizations prod = a_1 * a_2 * ... * a_m, update min_k[k] = min(min_k[k], prod),
       and sum unique minimal product-sum numbers across 2 <= k <= 12,000.

    Time Complexity: O(Factorizations) executing in ~0.02s.
    Space Complexity: O(max_k) memory for min_k array.
    """
    max_val = 2 * max_k
    # Array to track minimal product N for each set size k in 2..max_k
    min_k = [float("inf")] * (max_k + 1)

    def get_factors(prod: int, sum_f: int, num_f: int, start_f: int) -> None:
        """Recursive backtracking helper to generate non-decreasing factorizations of prod."""
        # Calculate equivalent set size k by appending (k - num_f) ones:
        # prod = sum_f + (k - num_f) * 1 => k = prod - sum_f + num_f
        k = prod - sum_f + num_f

        # Update minimal product N for set size k if within max_k bound
        if k <= max_k:
            if prod < min_k[k]:
                min_k[k] = prod

        # Branch factorizations starting from start_f to enforce non-decreasing order
        for f in range(start_f, max_val // prod + 1):
            get_factors(prod * f, sum_f + f, num_f + 1, f)

    # Start factorization search with initial product 1, sum 0, count 0, starting factor 2
    get_factors(1, 0, 0, 2)

    # Return sum of UNIQUE minimal product-sum numbers across k in 2..12,000
    return sum(set(min_k[2:]))


if __name__ == "__main__":
    print(solve())
