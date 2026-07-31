## General

Every final piece must contain exactly one `1`, so the pieces correspond in order to the `1` positions in the array. Leading zeros must join the piece containing the first `1`, and trailing zeros must join the piece containing the last `1`; neither region creates a choice.

Consider consecutive `1` values at indices $p$ and $q$. Exactly one split boundary must separate them. It may be placed after index $p$, after any intervening zero, but not after index $q$. This gives $q-p$ possible boundary positions. Choices in distinct gaps do not interfere, so the total number of splits is the product of these index differences.

Scan from left to right while remembering the previous `1` index. On each later `1`, multiply the answer by its distance from the previous one and reduce modulo $10^9+7$. Every valid split chooses exactly one boundary in each gap, and every such combination yields pieces containing exactly one `1`, establishing the product bijection. If no `1` occurs, return zero; otherwise a single `1` yields the empty product, which is one.

## Complexity detail

Let $n$ be the array length. The scan visits each element once, taking $O(n)$ time. Only the previous `1` index and running product are stored, so auxiliary space is $O(1)$.

## Alternatives and edge cases

- **Dynamic programming over prefixes:** Testing every possible previous cut can count valid partitions but takes $O(n^2)$ time unless simplified to the same gap product.
- **Store every one position:** Multiplying consecutive differences afterward is correct but uses $O(n)$ space unnecessarily.
- **Enumerate split subsets:** There are $2^{n-1}$ possible boundary sets, making direct enumeration impractical.
- An all-zero array has no good subarray covering it and therefore has answer zero.
- With exactly one `1`, the entire array is the only valid piece regardless of outer zeros.
- Adjacent `1` values have distance one, forcing their separating boundary.
- Leading and trailing zeros never change the number of splits.
- Apply the modulus after every multiplication to keep the running value bounded.
