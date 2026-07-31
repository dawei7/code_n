## General

**Make each finalized value as small as possible.** Process `nums` from left to right. If the previous finalized value is `previous`, the current result must exceed it. Subtracting the largest prime strictly smaller than `number - previous` produces the smallest legal current result. If no such prime exists, leave the number unchanged.

Precompute every prime through $M = \max(\texttt{nums})$ with the sieve of Eratosthenes. A binary search finds the largest prime below each current difference limit. If the resulting number is not greater than `previous`, no valid choice exists.

Choosing the smallest feasible current value leaves at least as much room as any other choice for every later element. Given any successful sequence, replacing its current value with the greedy value preserves strictness with the predecessor and cannot invalidate its relation to the next value. Applying this exchange at each position proves that a failure of the greedy scan means every possible sequence fails, while completing the scan constructs a valid one.

## Complexity detail

Let $n$ be the array length and $M$ its maximum value. The sieve costs $O(M \log\log M)$ time. Each of the $n$ binary searches costs $O(\log M)$, for total time $O(M \log\log M + n \log M)$. The sieve and prime list use $O(M)$ auxiliary space.

## Alternatives and edge cases

- **Scan every prime per element:** The same greedy rule can linearly inspect the prime list, but this costs up to $O(nM / \log M)$ after sieving.
- **Trial division for each candidate:** Repeated primality checks avoid a sieve but duplicate number-theory work and have a worse bound.
- **No subtraction:** Leaving a value unchanged is necessary when no eligible prime exists and is valid when it already exceeds the predecessor.
- **Strict inequality:** The selected prime must be strictly below `number - previous`; equality would make the result equal to the predecessor.
- **Value one:** No prime can be subtracted, so it remains one and can only occupy a position whose predecessor is below one.
