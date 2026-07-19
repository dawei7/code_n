## General
**View the operation as an index permutation**

The transformation never changes values; it only moves them between positions. Indices $0$ and $n-1$ stay fixed. For an internal position $i$, the source position selected by one operation is `i // 2` when $i$ is even and `n // 2 + (i - 1) // 2` when $i$ is odd.

**Track one representative internal index**

Start at position $1$ and repeatedly apply that even-or-odd source map. Count the steps until it returns to $1$. This follows one integer rather than allocating and transforming the entire permutation.

**Why one cycle determines the whole return**

For every internal index, the source map is multiplication by the inverse of $2$ modulo $n-1$: doubling the mapped index is congruent to the original index. After $k$ steps, index $1$ returns exactly when this modular multiplier has become $1$. The same multiplier then fixes every internal index, while the two endpoints were always fixed. Thus the whole permutation returns at precisely the same first positive step.

## Complexity detail
The loop performs one constant-time index update for each of the $k$ operations in the answer, taking $O(k)$ time. It stores only the current position and counter, requiring $O(1)$ space.

## Alternatives and edge cases
- **Simulate the entire permutation:** It is straightforward and correct but performs $O(n)$ work and uses $O(n)$ storage for every transformation.
- **Compute a multiplicative order directly:** Number-theoretic factorization can derive the order of two modulo $n-1$, but the bounded cycle simulation is simpler and already follows the exact transformation.
- **Smallest length:** For `n = 2`, both positions are fixed and the minimum positive answer is `1`.
- **Positive operation count:** Check for the return only after applying one step; the initial identity must not produce answer zero.
- **Fixed endpoints:** Tracking index `0` or `n - 1` would always return one and reveal nothing about internal cycles.
- **Even input guarantee:** The two halves and all transformation indices are integral because `n` is even.
