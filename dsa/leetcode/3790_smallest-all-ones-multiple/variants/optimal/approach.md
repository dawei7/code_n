## General

An all-ones integer always ends in `1`. It can therefore never be divisible by `2` or `5`; if `k` contains either factor, return `-1` immediately.

Otherwise, construct only remainders. If an $L$-digit repunit has remainder `r`, appending another `1` changes it to `10 * r + 1` modulo `k`. Starting from zero and applying this update visits candidate lengths in increasing order, so the first zero remainder gives the smallest all-ones multiple.

At most `k` lengths need examination. When `k` is coprime to ten, suppose none of the first `k` repunits had remainder zero. Two would share a nonzero remainder. Subtracting the shorter from the longer yields a power of ten times a smaller repunit divisible by `k`; because that power of ten is invertible modulo `k`, the smaller repunit would also be divisible, a contradiction. Thus a valid length appears by `k` whenever the initial factor test passes.

## Complexity detail

The loop performs at most $K=k$ constant-size remainder updates, taking $O(K)$ time. It stores only the current remainder and length, so auxiliary space is $O(1)$. No potentially enormous repunit is materialized.

## Alternatives and edge cases

- **Construct each integer:** Repeatedly compute `value = value * 10 + 1` using arbitrary-precision integers. It finds the same answer but arithmetic becomes progressively more expensive as the digit count grows.
- **Visited remainder set:** Track remainders until zero or repetition. This is valid but uses $O(K)$ space; the number-theory bound makes the set unnecessary.
- **Factor two or five:** These are exactly the divisibility obstructions because every candidate ends in `1`.
- **Composite divisors:** The same remainder recurrence and `k`-step bound apply; primality is irrelevant.
- **Return length:** The required result is the number of digits, not the repunit itself.
