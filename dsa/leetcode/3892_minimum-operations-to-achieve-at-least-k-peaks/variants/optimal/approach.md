## General

The circular shape is the main difficulty. A peak cannot be adjacent to another peak, including across the boundary between the last and first indices. Once that restriction is recognized, the problem becomes a minimum-weight independent-set problem with an exact number of selected vertices.

The source first computes the cost of making any one index a peak, then uses dynamic programming to select $k$ nonadjacent indices. It removes the cycle by considering separately whether index 0 is excluded or included.

**The exact cost of choosing one peak**

For index $i$, circular indexing makes its neighbors

$$
(i-1)\bmod n
\quad\text{and}\quad
(i+1)\bmod n.
$$

To be strictly greater than both, `nums[i]` must reach

$$
\max\!\left(
\texttt{nums}[(i-1)\bmod n],
\texttt{nums}[(i+1)\bmod n]
\right)+1.
$$

The function `peak_cost(i)` therefore returns

$$
w_i=
\max\!\left(
0,\,
\max(\text{two neighbors})+1-\texttt{nums}[i]
\right).
$$

If $i$ is already a peak, $w_i=0$. Otherwise, $w_i$ is exactly the number of unit increments needed to raise it just above the larger neighbor.

**Why selected peak costs are independent**

Adjacent indices cannot both be peaks. If $i$ and $i+1$ were both peaks, each would have to be strictly greater than the other, which is impossible. Hence every feasible peak set is an independent set on the cycle.

For two selected nonadjacent indices, raising one does not change either neighbor of the other. There is no reason to increase an unselected position because that could only raise the threshold of a nearby selected peak. Therefore a selected set $P$ can be realized at minimum cost

$$
\sum_{i\in P} w_i.
$$

This additive property is what permits a weighted dynamic program. Without it, choosing one peak could change the cost of another.

**Why “at least \(k\)” can be solved as “exactly \(k\)”**

All weights are nonnegative. Suppose some construction creates more than $k$ peaks. Choose any $k$ of those peak indices; they remain pairwise nonadjacent. Starting from the original array, raise only those chosen positions to their individual required values. Each is still greater than its unchanged neighbors, and omitting other increments cannot increase the cost.

Thus an optimum for at least $k$ peaks exists with exactly $k$ deliberately selected peaks. The algorithm may minimize over exact-$k$ independent sets.

**The immediate impossibility test**

A cycle of length $n$ contains at most

$$
\left\lfloor\frac n2\right\rfloor
$$

pairwise nonadjacent vertices. Alternating indices reaches this bound for even $n$; for odd $n$, the wraparound edge prevents selecting both ends of a would-be alternating sequence.

The source returns `-1` when `k > n // 2`. It returns zero immediately for `k == 0` because no modifications are required to satisfy an empty quota.

**The path dynamic-programming states**

The helper `path_cost(left, right, picks)` solves a linear subproblem: select exactly `picks` nonadjacent indices from the inclusive path `left..right`.

Two arrays hold the state after a processed prefix:

- `skip[count]` is the minimum cost of selecting exactly `count` positions when the most recently processed position is not selected.
- `take[count]` is the minimum cost of selecting exactly `count` positions when the most recently processed position is selected.

Initially, before processing any position, selecting zero and ending in the skipped state costs zero. Every other state is impossible and receives `infinity`.

When processing a position with weight $w$:

$$
\text{newTake}[c]
=
\text{oldSkip}[c-1]+w,
$$

because taking the current position requires skipping its predecessor, and

$$
\text{newSkip}[c]
=
\min(\text{oldSkip}[c],\text{oldTake}[c]),
$$

because skipping the current position permits either previous state.

The source performs these transitions in place while iterating `count` downward. This direction is crucial. When computing `take[count]`, `skip[count - 1]` must still describe the previous prefix rather than the current position. Descending counts ensure that the lower-count cell has not yet been updated.

The temporary `old_take` preserves the old `take[count]` before that array entry is overwritten. It is then used to update `skip[count]`. At the end, the requested answer is the smaller of the states that skip or take the final path position.

**Feasibility and the loop bound**

A path containing $L$ positions can select at most $\lceil L/2\rceil$ nonadjacent positions. With

$$
L=\texttt{right}-\texttt{left}+1,
$$

the source writes this limit as

```text
(right - left + 2) // 2
```

and returns `infinity` if `picks` exceeds it. The per-position `upper` bound similarly avoids updating selection counts that cannot yet be reached.

**Turning the cycle into two paths**

Every valid solution belongs to exactly one of two broad cases.

In the first case, index 0 is not selected. Removing it breaks both wraparound edges, leaving the ordinary path $1$ through $n-1$. The source evaluates

```text
path_cost(1, n - 1, k)
```

In the second case, index 0 is selected. Its two circular neighbors, indices 1 and $n-1$, must be excluded. The remaining candidates form the path $2$ through $n-2$, from which the algorithm selects $k-1$ positions:

```text
peak_cost(0) + path_cost(2, n - 2, k - 1)
```

Taking the smaller result covers every exact-$k$ independent set on the cycle. Any such set either contains index 0 or it does not; there is no third case. Within each case, the path recurrence evaluates all legal sets and sums their exact independent weights.

## Complexity detail

Let $n$ be the array length. A call to `path_cost` processes $O(n)$ positions. For each position, it may update counts from 1 through `picks`, so one call costs $O(nk)$ time in the worst case.

The source makes two path calls. Their path lengths differ, but their combined asymptotic cost remains

$$
O(nk).
$$

Computing `peak_cost` is constant time. It is called once for each processed path position and once separately for index 0, adding only $O(n)$ work, which is absorbed by $O(nk)$ when $k>0. The special $k=0$ case returns in $O(1)$ time.

Each path call allocates two arrays of length `picks + 1`. The calls execute sequentially, so their storage is not added together. The auxiliary space is

$$
O(k).
$$

The source does not store an $n\times k$ table. Its rolling `skip` and `take` arrays retain only the previous-prefix information needed for the next transition. The manifest's $O(nk)$ time and $O(k)$ space therefore match the checked-in implementation.

The sentinel `10**30` is safely larger than any real answer under the stated constraints. One chosen index needs at most about $2\cdot10^5+1$ increments, and at most 2500 indices can be selected, far below the sentinel.

## Alternatives and edge cases

- **Full two-dimensional DP:** Storing a value for every position and count makes reconstruction easier but uses $O(nk)$ space instead of the source's $O(k)$ rolling storage.
- **Generic cycle DP:** A state that remembers whether index 0 and the previous index were selected can process the circle in one larger table. Splitting on index 0 yields simpler path transitions.
- **Greedy by cheapest individual weights:** Choosing the $k$ smallest `peak_cost` values can select adjacent indices and is therefore invalid; the independent-set constraint must be enforced.
- **Zero requested peaks:** The answer is zero regardless of the existing array, and the source handles this before allocating DP arrays.
- **Impossible quota:** More than $\lfloor n/2\rfloor$ peaks cannot coexist on a cycle, even after arbitrarily many increments.
- **Two-element circle:** Each index sees the other element as both its previous and next neighbor. At most one peak is possible, and the two cycle cases correctly compare which index is cheaper to raise.
- **Odd cycle:** Alternating choices cannot include both ends because index $n-1$ is adjacent to index 0; the include/exclude split preserves this wraparound restriction.
- **Already-existing peaks:** Their weights are zero, so the DP can select them for free while still respecting adjacency.
- **Negative values:** The cost formula depends only on comparisons and differences, so negative starting entries need no special handling.
- **Strict comparison:** The required value is one more than the larger neighbor. Omitting the `+1` would create a tie rather than a peak.
- **In-place update direction:** Counts must be processed from high to low. An ascending loop could reuse a state created for the current index and effectively select that same position more than once.
- **Empty residual path:** When index 0 is selected in a very short array, `left > right` is valid only if zero further picks are required; `path_cost` checks `picks == 0` first and returns zero.
