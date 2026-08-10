## General

**Replace gas and cost by one net change**

At station `k`, the tank changes by:

$$
d_k=\texttt{gas[k]}-\texttt{cost[k]}.
$$

A chosen start is feasible exactly when every running sum along the clockwise circuit is nonnegative. The tank begins at zero, so a negative running sum means the car cannot pay for that outgoing leg.

The selected solution builds one contiguous circular block of stations and tries to make that block traversable from its left endpoint. It begins with station `n - 1`. The variable meanings are:

- `i`: the current proposed starting station, or left endpoint;
- `j`: the next station to append at the clockwise right endpoint;
- `cnt`: how many distinct stations have entered the block;
- `s`: the total net gas across the current block.

Initially the block is empty, with both endpoints positioned at `n - 1`. Every station is added exactly once, either by advancing `j` clockwise or by moving `i` backward.

**Grow clockwise while the route remains possible**

The outer loop appends station `j` by adding its net change to `s`. It increments `cnt` and advances `j` with modulo `n`, so after station `n - 1` the forward endpoint wraps to station `0`.

Suppose the existing block was traversable from `i` and had nonnegative total fuel. Appending one station at its end does not change any earlier running balance. Only the new final balance can become negative.

If `s` stays nonnegative, the enlarged block remains traversable from the same `i`. The algorithm can safely continue appending clockwise stations.

If `s` becomes negative, starting at `i` cannot finish the enlarged block. The inner loop then moves `i` one station backward and adds that station’s net gas. It keeps prepending stations until the total becomes nonnegative or all $n$ stations have been included.

**Why prepending until nonnegative repairs every prefix**

It is not generally true that a segment with nonnegative total is traversable from its first position; an early deficit could still occur. The particular order used here supplies the stronger guarantee.

Before the failed forward append, the old block was traversable. Therefore all of its old prefixes were nonnegative. Adding the new rightmost station makes only the complete enlarged block negative.

Call that negative sum $S_0$. As the algorithm prepends stations in reverse order, let $S_1,S_2,\ldots$ be the successive whole-block sums. The inner loop continues while each of those sums is negative and stops at the first $S_k \ge 0$.

In forward travel order, the newly prepended stations appear in the reverse of the order in which they were added. The fuel after traversing the first newly prepended station is $S_k-S_{k-1}$, which is nonnegative because $S_k \ge 0$ and $S_{k-1}<0$. After the next one, it is $S_k-S_{k-2}$, also nonnegative. The same reasoning covers every prefix of the prepended portion.

When the car reaches the old block, it carries the total contribution of the prepended portion. Every prefix of the old block except its newly appended last station was already feasible. At the final station, the balance is exactly $S_k$, which is nonnegative. Thus the whole enlarged block is traversable from the new `i`.

This proves the maintained fact: whenever an iteration finishes with `s >= 0`, every running balance from `i` across the current circular block is nonnegative.

**Why the final check decides existence**

`cnt` increases once for each station added at either endpoint. The two endpoints grow toward one another and the loops stop after exactly $n$ additions, so the final `s` is:

$$
\sum_{k=0}^{n-1}(\texttt{gas[k]}-\texttt{cost[k]}).
$$

If this total is negative, the circuit consumes more gas than all stations provide. No starting position can change that total, so the answer must be `-1`.

If the total is nonnegative, the maintained traversal property says the complete $n$-station block can be driven clockwise from `i` without a negative tank. The code therefore returns `i`.

For a one-station input, that station is added once. A nonnegative net returns index zero; a negative net returns `-1`.

## Complexity detail

Let $n$ be the common length of `gas` and `cost`.

Although the code has a nested `while`, it is not quadratic. Both loops share `cnt`, and every pass through either station-adding body increments it. No station is inserted twice, and `cnt` stops at $n$. The total number of net-change additions is exactly $n$, so time is $O(n)$.

The algorithm stores only four integers and computes each net value directly from the input arrays. It allocates no proportional container, so auxiliary space is $O(1)$.

Modulo is used only for the forward pointer `j`. The backward pointer `i` does not need modulo because it starts at `n - 1` and can be decremented at most `n - 1` times before `cnt` reaches $n$; it therefore never needs to move below index zero.

## Alternatives and edge cases

- **Standard forward greedy reset:** Accumulate a candidate’s tank from left to right. When it becomes negative at `k`, eliminate every start in the current segment and restart at `k + 1`. A separate total sum decides whether any start exists.
- **Brute force every station:** Simulate up to $n$ legs from each of $n$ starts. It is easy to understand but takes $O(n^2)$ time.
- **Prefix-sum minimum:** A valid circular start can be chosen immediately after a minimum prefix sum when total net gas is nonnegative. This gives another $O(n)$ proof and implementation.
- **One station:** Return zero exactly when `gas[0] >= cost[0]`; otherwise return `-1`.
- **Total gas equals total cost:** Feasibility is still possible because the final tank may be exactly zero. The code correctly rejects only `s < 0`, not `s <= 0`.
- **Temporary negative segment:** The inner loop is required even if a later station would eventually compensate. A car cannot borrow gas from a future station it cannot yet reach.
- **Large values:** Python integers do not overflow. In fixed-width languages, the total can be as large as roughly $10^9$ under the given limits and should use a safe integer type.
- **Unique-answer guarantee:** The source returns the `i` constructed by its deterministic growth order. The Reference guarantees uniqueness when a feasible answer exists, so no tie policy is needed.
- **Nonempty arrays:** The contract has $n \ge 1$. With empty arrays, modulo by `n` would be invalid.
- **Runtime dependency:** The selected source uses `List` in type annotations without importing it. A standalone module needs `from typing import List` unless the harness supplies that name.
