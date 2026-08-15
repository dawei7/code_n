def is_lychrel(n: int) -> bool:
    """Test if n is a Lychrel candidate by applying 50 iterations of reverse-and-add.

    Mathematical Principles Applied:
    1. Reverse-and-Add Process (196-algorithm):
       Given integer n, form n_{k+1} = n_k + reverse(n_k).
       If n_k becomes palindromic within 50 iterations, n is NOT a Lychrel number.

    2. Lychrel Candidate Boundary:
       If no palindrome is produced after 50 iterations for numbers n < 10,000,
       n is assumed to be a Lychrel number (per Problem 55 specification).
    """
    curr = n
    # Perform up to 49 additions (50 iterations total)
    for _ in range(49):
        # Reverse digits of curr and add to curr
        curr += int(str(curr)[::-1])

        # Test if new sum is palindromic
        s = str(curr)
        if s == s[::-1]:
            # Palindrome formed => NOT a Lychrel number
            return False

    # No palindrome formed after 50 iterations => Lychrel candidate
    return True


def solve(limit: int = 10000) -> int:
    """Find the number of Lychrel numbers strictly below limit (10,000).

    Time Complexity: O(limit * 50) executing in ~0.04s.
    Space Complexity: O(1) constant auxiliary space.
    """
    # Count Lychrel candidates for integers 1 <= i < 10000
    lychrel_count = sum(1 for i in range(1, limit) if is_lychrel(i))

    # Return total count of Lychrel numbers below limit
    return lychrel_count


if __name__ == "__main__":
    print(solve())
