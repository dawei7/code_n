## General

**The original positions do not constrain the chain**

The definition tests a chosen subsequence only after sorting it. Consequently, the task is to determine which values are available, not to preserve a square-chain order in the original array. Because every value is at least $2$, squaring strictly increases it; duplicate copies of one value cannot extend a chain. Store the distinct values in a hash set.

For each distinct starting value $x$, repeatedly test $x$, $x^2$, $x^4$, and so on in the set. Every successful membership test contributes one element to that start's streak. The first missing value ends the chain. Record a length only when it is at least two, leaving the answer at `-1` if no square relation exists.

This enumerates every possible chain start. For any valid square streak, starting the traversal at its smallest selected value follows every later value in exactly the required order, so the traversal reaches its full length. Starting from an interior value can repeat part of the work but cannot hide a longer answer.

## Complexity detail

Let $n$ be the array length and let $M=\max(\texttt{nums})$. Constructing the hash set costs $O(n)$ expected time and space. Starting from a value at least $2$, repeated squaring exceeds $M$ after $O(\log\log M)$ successful steps. Across at most $n$ distinct starts, the expected time is $O(n\log\log M)$ and the space is $O(n)$.

The expected-time qualification comes from hash-set membership. Under the stated $M\le 10^5$ bound, a chain contains at most five present values, but the bound above keeps the dependence explicit.

## Alternatives and edge cases

- **Sorted dynamic programming:** Sort distinct values and set a value's chain length from its integer square root when present. This costs $O(n\log n)$ time and $O(n)$ space.
- **Repeated list searches:** Following the same chains directly in `nums` is correct, but each membership test can be linear, producing $O(n^2\log\log M)$ time.
- **Duplicate values:** Since $x^2>x$ for every allowed value, equal copies never occupy consecutive positions in a valid chain; converting to a set is safe.
- **Several chains:** Every distinct value is considered as a start, so the maximum is found even when shorter chains overlap or appear earlier.
- **No squared pair:** A maximum traversal length of one is not a square streak, and the required result is `-1`.
