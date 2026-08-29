def solve(n: int = 10000000) -> int:
    """Find S(10^7): sum_{k=1}^n d_n(1/k) for n = 10^7.

    Modular exponentiation power residue reciprocal digit summation loop.

    Time Complexity: O(n log n)
    Space Complexity: O(1)
    """
    total_sum = 0
    n_minus_1 = n - 1

    for k in range(1, n + 1):
        rem = pow(10, n_minus_1, k)
        digit = (10 * rem) // k
        total_sum += digit

    return total_sum


if __name__ == "__main__":
    print(solve())
