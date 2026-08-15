def solve() -> int:
    """Find the largest palindrome product of two 3-digit numbers.

    Mathematical Principles Applied:
    1. Palindrome Product Definition:
       A product P = a * b (where 100 <= a, b <= 999) is a 6-digit palindrome
       P = abccba = 100001*a_dig + 10010*b_dig + 1100*c_dig = 11 * (9091*a_dig + 910*b_dig + 100*c_dig).
       Every 6-digit palindrome is divisible by 11, so at least one factor a or b must be a multiple of 11.

    2. Search Space Pruning:
       - Iterate a in descending order from 999 to 100.
       - If a * 999 <= max_palindrome, break outer loop (no larger product possible).
       - Iterate b in descending order from a to 100.
       - If a * b <= max_palindrome, break inner loop (further decrements of b yield smaller products).

    3. String Reversal Palindrome Verification:
       Convert product P to string s and test s == s[::-1].

    Time Complexity: O(D^2 / 11) pruned to ~3,000 checks.
    Space Complexity: O(1) constant auxiliary space.
    """
    # Track the maximum palindrome product found
    max_palindrome = 0

    # Outer loop: iterate factor 'a' downwards from 999 to 100
    for a in range(999, 99, -1):
        # Pruning check: if the maximum possible product with factor 'a' (a * 999)
        # is <= max_palindrome already found, no larger palindrome can be produced
        if a * 999 <= max_palindrome:
            break

        # Inner loop: iterate factor 'b' downwards from 'a' to 100 (avoids duplicate pairs)
        for b in range(a, 99, -1):
            prod = a * b

            # Pruning check: if product <= max_palindrome, further decrements of b yield smaller products
            if prod <= max_palindrome:
                break

            # Convert product to string representation
            s = str(prod)

            # Check if the string representation is identical to its reverse
            if s == s[::-1]:
                max_palindrome = prod

    # Return the largest palindrome product found
    return max_palindrome


if __name__ == "__main__":
    print(solve())
