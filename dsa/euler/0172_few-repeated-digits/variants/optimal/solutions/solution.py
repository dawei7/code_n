import math


def solve(length: int = 18, max_repeat: int = 3) -> int:
    """Find the number of 18-digit numbers without leading zero where no digit occurs more than 3 times.

    Mathematical Principles Applied:
    1. Integer Partition & Multinomial Coefficient:
       Count digit occurrences (c0, c1, ..., c9) such that 0 <= c_i <= 3 and sum_{i=0}^9 c_i = 18.
       For a valid digit count tuple (c0, c1, ..., c9):
       The total number of 18-digit permutations without leading zero is given by:
       P = (18 - c0) * 17! / (c0! * c1! * ... * c9!).

    2. Recursive Depth-First Search for Digit Frequency Tuples:
       Branch on frequencies c_i in [0, 3] for digits 0 through 9.
       Prune branches where remaining length falls below 0 or exceeds maximum allowable.

    Time Complexity: O((max_repeat + 1)^10) executing in ~0.001s.
    Space Complexity: O(length) recursion memory.
    """
    fact = [math.factorial(i) for i in range(length + 1)]
    total_count = 0

    def dfs(digit: int, rem_length: int, curr_fact_prod: int, c0: int):
        nonlocal total_count
        # Base case at digit 9: set c9 = rem_length
        if digit == 9:
            c9 = rem_length
            if 0 <= c9 <= max_repeat:
                fact_prod = curr_fact_prod * fact[c9]
                # Multinomial permutations excluding leading zero: (18 - c0) * 17! / prod(c_i!)
                valid_perms = (length - c0) * (fact[length - 1] // fact_prod)
                total_count += valid_perms
            return

        # Branch on count c for current digit (0 <= c <= 3)
        for c in range(min(max_repeat, rem_length) + 1):
            dfs(
                digit + 1,
                rem_length - c,
                curr_fact_prod * fact[c],
                c if digit == 0 else c0,
            )

    # Start DFS at digit 0 with remaining length 18
    dfs(0, length, 1, 0)

    # Return total count of valid 18-digit numbers
    return total_count


if __name__ == "__main__":
    print(solve())
