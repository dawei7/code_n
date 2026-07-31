## General

Consider the first $i+1$ values. An allowed operation inside this prefix preserves its sum, while an operation crossing into it from index $i+1$ can only increase that sum. The original prefix sum can therefore never decrease. If every final value were at most $M$, that prefix could hold at most $(i+1)M$, so necessarily

$$
M \ge \left\lceil
\frac{\texttt{nums[0]}+\cdots+\texttt{nums[i]}}{i+1}
\right\rceil.
$$

The answer must be at least the largest such ceiling over all prefixes.

That lower bound is also attainable. Process the array conceptually from left to right while allowing a later position's excess to move into unused capacity in earlier positions. For a candidate bound equal to the largest prefix ceiling, every prefix has total mass at most its number of slots times the bound. Thus, whenever a position exceeds the bound, the preceding positions collectively have enough unused capacity to receive its excess through repeated leftward moves. No element needs to exceed the bound.

A single scan maintains the prefix sum and the maximum ceiling average seen so far. Compute the ceiling with integer arithmetic as `(prefix_sum + index) // (index + 1)`, avoiding floating-point rounding.

## Complexity detail

Let $n=\lvert\texttt{nums}\rvert$. The algorithm visits each value once, taking $O(n)$ time. The running prefix sum and answer use $O(1)$ auxiliary space.

Python integers safely hold a prefix sum up to $10^{14}$. In fixed-width languages, the prefix sum must use a 64-bit integer even though the returned answer fits the input-value range.

## Alternatives and edge cases

- **Binary search on the answer:** Testing whether every prefix fits under a proposed maximum is correct, but it takes $O(n\log V)$ time for $V=\max(\texttt{nums})$.
- **Recompute every prefix sum:** Applying the same ceiling formula with a fresh sum for each prefix is correct but costs $O(n^2)$ time.
- **Simulate individual transfers:** Unit-by-unit balancing can require an enormous number of operations because values reach $10^9$.
- **All zeros:** Every prefix ceiling is zero, so the minimum maximum is zero.
- **Large first value:** `nums[0]` cannot move right; it is an unavoidable lower bound.
- **Large trailing value:** Its mass can spread across every earlier position, and the full-array ceiling may determine the answer.
- **Already uniform:** Every prefix average equals the existing value, so no operation improves the maximum.
- **Integer ceiling:** Use exact integer arithmetic; floating-point division is unnecessary and can lose precision in other language runtimes.
