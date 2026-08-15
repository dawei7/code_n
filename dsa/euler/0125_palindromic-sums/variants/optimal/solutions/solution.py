def solve(limit: int = 100000000) -> int:
    """Find the sum of all numbers < limit (10^8) that are palindromic and expressible as the sum of consecutive squares.

    Mathematical Principles Applied:
    1. Sum of Consecutive Squares Representation:
       Let N = sum_{k=i}^j k^2 for 1 <= i < j <= sqrt(limit).
       Since N < 10^8, the maximum starting square root is k <= sqrt(10^8) = 10,000.

    2. Palindrome Verification & Deduplication:
       For each consecutive square sum N < 10^8:
       Check if string representation of N equals its reverse (`s == s[::-1]`).
       If True, insert N into a hash set to deduplicate (some palindromes have multiple consecutive square representations).

    3. Total Sum Calculation:
       Return sum(palindromic_sums).

    Time Complexity: O(K^2) where K = 10,000 (executes in ~0.05s).
    Space Complexity: O(P) memory for palindromes set.
    """
    max_k = int(limit**0.5)
    palindromic_sums = set()

    # Outer loop for starting square base i from 1 to 10,000
    for i in range(1, max_k):
        sq_sum = i * i
        # Inner loop for ending square base j from i+1 upwards
        for j in range(i + 1, max_k + 1):
            sq_sum += j * j
            # Break inner loop as soon as cumulative sum exceeds limit = 10^8
            if sq_sum >= limit:
                break

            # Verify if current cumulative sum is a palindrome string
            s = str(sq_sum)
            if s == s[::-1]:
                palindromic_sums.add(sq_sum)

    # Return total sum of unique palindromic consecutive square sums < 10^8
    return sum(palindromic_sums)


if __name__ == "__main__":
    print(solve())
