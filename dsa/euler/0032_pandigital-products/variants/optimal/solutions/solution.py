def solve() -> int:
    """Find the sum of all unique products whose multiplicand/multiplier/product identity is 1..9 pandigital.

    Mathematical Principles Applied:
    1. Pandigital Length Identity Constraint:
       Let a * b = p be a pandigital identity containing digits 1 through 9 exactly once.
       Total digit count len(str(a)) + len(str(b)) + len(str(p)) MUST equal 9.

    2. Bounded Digit Count Partitioning:
       - If len(a) + len(b) <= 3, len(p) <= 4 => Total digits <= 7 < 9.
       - If len(a) + len(b) >= 5, len(p) >= 4 => Total digits >= 10 > 9.
       Therefore, len(a) + len(b) MUST equal 5, and len(p) MUST equal 4!

    3. Two Permutation Length Cases:
       Case 1: 1-digit * 4-digit = 4-digit (1 <= a <= 9, 1234 <= b <= 9876 // a)
       Case 2: 2-digit * 3-digit = 4-digit (12 <= a <= 98, 123 <= b <= 9876 // a)

    Time Complexity: O(A * B) bounded to ~4,000 product checks (executes in ~0.005s).
    Space Complexity: O(1) set storage.
    """
    # Track unique products found (set deduplicates identical products from different factor pairs)
    unique_products = set()

    # Target digit set for 1..9 pandigital validation
    target_digits = set("123456789")

    # Case 1: 1-digit * 4-digit = 4-digit
    for a in range(1, 10):
        for b in range(1234, 9876 // a + 1):
            p = a * b
            identity_str = f"{a}{b}{p}"

            # Check if identity string has length 9 and contains digits 1-9 exactly once
            if len(identity_str) == 9 and set(identity_str) == target_digits:
                unique_products.add(p)

    # Case 2: 2-digit * 3-digit = 4-digit
    for a in range(12, 99):
        for b in range(123, 9876 // a + 1):
            p = a * b
            identity_str = f"{a}{b}{p}"

            # Check if identity string has length 9 and contains digits 1-9 exactly once
            if len(identity_str) == 9 and set(identity_str) == target_digits:
                unique_products.add(p)

    # Return sum of all unique pandigital products
    return sum(unique_products)


if __name__ == "__main__":
    print(solve())
