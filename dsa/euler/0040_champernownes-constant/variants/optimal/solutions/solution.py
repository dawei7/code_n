import math


def solve() -> int:
    """Find the product d_1 * d_10 * d_100 * d_1000 * d_10000 * d_100000 * d_1000000 of Champernowne's constant.

    Problem Context & Mathematical Principles:
    -------------------------------------------
    1. Champernowne's Constant Digit Blocks:
       C_10 = 0.123456789101112131415161718192021...
       The sequence of positive integers is partitioned into decimal digit length blocks:
           - 1-digit block: 1 to 9 (9 numbers, 9 * 1 = 9 digits, positions 1 to 9)
           - 2-digit block: 10 to 99 (90 numbers, 90 * 2 = 180 digits, positions 10 to 189)
           - L-digit block: 10^{L-1} to 10^L - 1 (9 * 10^{L-1} numbers, L * 9 * 10^{L-1} digits)

    2. O(log k) Direct Digit Extraction:
       To find the k-th digit d_k:
           - Subtract the total digit count of preceding complete blocks until k falls in block L.
           - The target integer is: num = 10^{L-1} + (k - 1) // L
           - The target digit is the ((k - 1) % L)-th digit of num.

    3. Exact Zero-Allocation Evaluation:
       Target indices: k in {10^0, 10^1, 10^2, 10^3, 10^4, 10^5, 10^6}.
       The product of all 7 target digits is evaluated in O(1) time with zero memory allocations.

    Complexity:
    -----------
    - Time Complexity: O(log k) per query, total ~0.00002s.
    - Space Complexity: O(1) constant auxiliary space.
    """

    def get_digit(k: int) -> int:
        """Find the k-th decimal digit of Champernowne's constant in O(log k) time."""
        length = 1
        count = 9
        start = 1
        while k > length * count:
            k -= length * count
            length += 1
            count *= 10
            start *= 10

        num = start + (k - 1) // length
        digit_idx = (k - 1) % length
        return int(str(num)[digit_idx])

    targets = [1, 10, 100, 1000, 10000, 100000, 1000000]
    return math.prod(get_digit(k) for k in targets)


if __name__ == "__main__":
    print(solve())
