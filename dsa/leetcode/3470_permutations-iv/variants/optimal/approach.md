## General

An alternating permutation has a fixed parity pattern once its first value is chosen. When $n$ is odd, there is one more odd value than even value, so the first value must be odd. When $n$ is even, either parity can start. Every later position must use the parity opposite the preceding value.

Suppose a candidate is placed and $o$ odd values and $e$ even values remain. First verify that these counts match the forced parity slots in the remaining suffix. If the next slot is odd, it contains $\lceil(o+e)/2\rceil$ positions and the even slots contain $\lfloor(o+e)/2\rfloor$ positions; the roles reverse when the next slot is even. An incompatible candidate contributes no valid completions.

For compatible counts, the odd values may be assigned to their odd slots in $o!$ orders and the even values to their even slots in $e!$ orders. Interleaving is already fixed by parity, so the candidate owns exactly

$$
o!\,e!
$$

consecutive permutations in lexicographical order.

Convert `k` to a zero-based rank. At each position, inspect unused values from smallest to largest, skipping candidates with the wrong parity or incompatible remaining counts. If a candidate's block is no larger than the rank, subtract the whole block. Otherwise, select that candidate and continue inside its block. If every candidate is skipped, the requested rank exceeds the total number of alternating permutations and the result is empty. Because each selected prefix fixes the next parity, this block subtraction is standard lexicographical unranking specialized to the alternating constraint.

## Complexity detail

Let $n$ be the requested permutation length. Factorials take $O(n)$ time to precompute. Up to $O(n)$ unused values are inspected at each of $n$ positions, and removing a value from the array-backed available list may also shift $O(n)$ entries, so time is $O(n^2)$. The factorial table, available values, and answer use $O(n)$ space. Python's arbitrary-precision integers safely represent the factorial products; other languages may cap counts above $10^{15}$ because larger exact values cannot affect `k`.

## Alternatives and edge cases

- **Generate and sort every permutation:** This takes factorial time and becomes impossible long before $n=100$.
- **Ordinary factoradic unranking:** Treating all remaining values as interchangeable ignores that candidates of the wrong parity have zero valid completions.
- **Capped factorial counts:** Replacing any count above $10^{15}$ with a sentinel is safe and avoids overflow in fixed-width languages.
- **Odd length:** The first value must be odd because odd values occupy both ends of the alternating pattern.
- **Even length:** Odd-starting and even-starting permutations both participate in the same lexicographical ordering.
- **`n = 1`:** `[1]` is the only valid permutation, so every larger rank returns `[]`.
- **Rank beyond the total:** Exhausting all candidate blocks at any position proves that no requested permutation exists.
