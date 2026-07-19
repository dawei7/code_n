## General
**Remove complete rounds**

Let $S$ be the sum of all values in `chalk`. Every full pass through the class consumes exactly $S$ pieces and returns to student `0`, so complete passes do not affect which student eventually replaces the chalk. Replace `k` with `k % S`.

This remainder is strictly smaller than the cost of one full round, guaranteeing that the replacement occurs during the next single pass. A zero remainder means earlier rounds consumed the chalk exactly and student `0` replaces it.

**Scan the final partial round**

Visit students in order. If the remainder is less than the current requirement, return that index. Otherwise subtract the requirement and continue. Equality must take the subtraction branch because the student has enough chalk to complete the turn.

Modulo removes only whole sequences with identical state before and after, so it preserves the eventual replacement student. During the final pass, each successful subtraction exactly mirrors one real turn; the first failed comparison is therefore the required student.

## Complexity detail
Summing the $N$ requirements and scanning at most one further pass both take $O(N)$ time. The total, remainder, index, and current requirement use $O(1)$ auxiliary space. Fixed-width implementations should sum in a type wide enough for as much as $10^{10}$ chalk per round.

## Alternatives and edge cases
- **Literal cyclic simulation:** It follows the process directly but may take work proportional to `k` when requirements are small.
- **Prefix sums and binary search:** After reducing by the round sum, search the first prefix sum strictly greater than the remainder in $O(N+\log N)$ time and $O(N)$ space.
- **Exact round multiple:** A zero remainder means student `0` replaces the chalk.
- **Exact student requirement:** That student completes the turn; the following student may replace it.
- **One student:** The only possible result is index `0`.
- **Large `k`:** Reduce before simulating to avoid billions of turns.
