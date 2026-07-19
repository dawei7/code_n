## General
**Count the complementary set:** Every positive integer either has a repeated digit or has all distinct digits. Count distinct-digit values no greater than `n`, then subtract that count from `n`.

**Count shorter lengths with permutations:** For a length $L<D$, the first digit has nine choices because it cannot be zero. Each later position chooses a different digit from the remaining pool, giving `9 * permutations(9, L - 1)` distinct-digit numbers.

**Follow the prefix of n:** Scan `n` left to right. At position `i`, try every smaller digit that is legal there and has not appeared in the fixed prefix. After choosing it, fill the remaining positions with ordered selections from unused digits. Then add the actual digit of `n` to the used set and continue. If that digit is already used, stop because no number with the exact prefix can remain distinct; if the entire scan succeeds, include `n` itself.

Every distinct-digit number is counted either in a shorter-length group or at the first position where it is smaller than `n`. These groups are disjoint, and the permutation factor fills every legal suffix exactly once. Subtracting their total therefore leaves precisely the numbers with a repeated digit.

## Complexity detail
There are $D$ positions, at most ten candidate digits per position, and a permutation product over at most $D$ factors, giving $O(D^2)$ time. The used-digit set stores at most $D$ entries, so auxiliary space is $O(D)$.

## Alternatives and edge cases
- **Digit dynamic programming:** Memoizing position, used-digit mask, and tightness is a general solution with $O(D2^{10})$ states.
- **Enumerate every integer:** Testing each decimal representation is correct but costs $O(nD)$ time.
- **Single-digit bound:** No positive one-digit number contains a repeated digit.
- **Repeated digit in n:** Stop the equal-prefix scan at its first repetition; smaller branches were already counted.
- **Leading zeroes:** They are not digits of a shorter number and must not consume the digit zero.
