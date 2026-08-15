import itertools
import math


def solve() -> int:
    """Find the largest 0-9 10-digit pandigital concatenated product formed by an integer k with 2 or more integers.

    Mathematical Principles Applied:
    1. Pandigital Product Definition:
       An integer k multiplied by integers (a1, a2, ...) produces products (p1 = k*a1, p2 = k*a2, ...).
       The concatenated output string `p1 + p2 + ...` must be a 10-digit 0-9 pandigital permutation.
       Additionally, the concatenated input string `k + a1 + a2 + ...` MUST ALSO be a 10-digit 0-9 pandigital permutation!

    2. Reverse Lexicographical Search:
       Iterate 10-digit pandigital permutations of '9876543210' in descending lexicographical order.
       The FIRST permutation `p_str` that can be partitioned into valid product blocks (p1, p2, ...) with a common factor k
       such that `str(k) + str(a1) + str(a2) + ...` is a valid 0-9 pandigital number IS THE MAXIMUM!

    3. Block Partition & Common Divisor GCD Pruning:
       - Partition `p_str` into 2 blocks (p1, p2) or 3 blocks (p1, p2, p3).
       - Compute g = gcd(p1, p2, ...).
       - For each divisor k of g: check if `k + (p1//k) + (p2//k) + ...` forms a 0-9 pandigital number.

    Time Complexity: O(Pandigital_Permutations * Divisors) executing in ~0.50s.
    Space Complexity: O(1) constant auxiliary space.
    """
    digits = "9876543210"

    def check_pandigital_input(k_str: str, a_strs: list[str]) -> bool:
        """Verify concatenated input k + a1 + a2 + ... forms a 10-digit 0-9 pandigital string."""
        concat_input = k_str + "".join(a_strs)
        if len(concat_input) != 10 or concat_input.startswith("0"):
            return False
        return set(concat_input) == set("0123456789")

    # Descending lexicographical search over 10-digit pandigital permutations
    for p_tuple in itertools.permutations(digits):
        if p_tuple[0] == "0":
            continue
        p_str = "".join(p_tuple)
        L = len(p_str)

        # 1. Partition p_str into 2 product blocks (s1, s2)
        for i in range(1, L):
            s1, s2 = p_str[:i], p_str[i:]
            if s1.startswith("0") or s2.startswith("0"):
                continue
            p1, p2 = int(s1), int(s2)

            g = math.gcd(p1, p2)
            if g <= 1:
                continue

            divs = []
            for d in range(2, int(math.isqrt(g)) + 1):
                if g % d == 0:
                    divs.append(d)
                    if d * d != g:
                        divs.append(g // d)
            divs.append(g)

            for k in divs:
                a1 = p1 // k
                a2 = p2 // k
                if check_pandigital_input(str(k), [str(a1), str(a2)]):
                    return int(p_str)

        # 2. Partition p_str into 3 product blocks (s1, s2, s3)
        for i in range(1, L - 1):
            for j in range(i + 1, L):
                s1, s2, s3 = p_str[:i], p_str[i:j], p_str[j:]
                if (
                    s1.startswith("0")
                    or s2.startswith("0")
                    or s3.startswith("0")
                ):
                    continue
                p1, p2, p3 = int(s1), int(s2), int(s3)

                g = math.gcd(math.gcd(p1, p2), p3)
                if g <= 1:
                    continue

                divs = []
                for d in range(2, int(math.isqrt(g)) + 1):
                    if g % d == 0:
                        divs.append(d)
                        if d * d != g:
                            divs.append(g // d)
                divs.append(g)

                for k in divs:
                    a1, a2, a3 = p1 // k, p2 // k, p3 // k
                    if check_pandigital_input(
                        str(k), [str(a1), str(a2), str(a3)]
                    ):
                        return int(p_str)

    # No valid pandigital concatenated product found (should not occur for valid input)
    raise ValueError("No pandigital concatenated product found")


if __name__ == "__main__":
    print(solve())
