## General

**Separate peak status from array values.** Define an indicator $p_i$ that is 1 exactly when $0<i<n-1$ and `nums[i]` is strictly greater than both neighbors. Then a type-1 query `[1, l, r]` asks for

$$
\sum_{i=l+1}^{r-1} p_i.
$$

Excluding $l$ and $r$ is essential: the first and last elements of the requested subarray cannot be peaks for that query, even if they are peaks in the full array.

**Store the indicators in a Fenwick tree.** A Fenwick tree supports the required indicator-range sum using two prefix sums in $O(\log n)$ time. Initialize it with every peak in the original array.

**Repair only locally after an update.** Changing `nums[index]` can affect the peak tests only at `index - 1`, `index`, and `index + 1`; every other test reads unchanged values. Remove the old indicators for the valid positions in that three-element neighborhood, assign the new value, recompute those indicators, and add the new ones back to the tree.

The Fenwick tree therefore equals the current peak-indicator array before every query. This is true after initialization. A type-1 query does not alter either structure and returns exactly the sum over its legal interior. A type-2 query removes and recomputes every indicator whose defining comparison can change, while leaving all unaffected indicators intact. Induction over the query sequence proves that every reported count matches the current array.

## Complexity detail

Let $n$ be the length of `nums` and $q$ the number of queries. Building the indicators with Fenwick updates costs $O(n\log n)$. Each type-1 query performs two prefix sums, and each type-2 query performs only a constant number of Fenwick updates, so all queries cost $O(q\log n)$. The total time is $O((n+q)\log n)$, and the copied array, indicator list, and Fenwick tree use $O(n)$ space.

## Alternatives and edge cases

- **Segment tree:** It provides the same $O(\log n)$ point updates and range sums, but a Fenwick tree is smaller and sufficient because the maintained operation is addition.
- **Sorted set of peak indices:** Counting peaks in an interval is possible with an order-statistics structure, but ordinary language-level sorted lists can make insertion or deletion $O(n)$.
- **Rescan every query range:** Directly checking all interior positions is simple and correct, but it can cost $O(nq)$ across many full-range queries.
- **Short ranges:** If $r-l<2$, there is no interior position and the answer is zero.
- **Strict comparison:** Equal adjacent values prevent a peak; use `>` on both sides, not `>=`.
- **Subarray endpoints:** Query positions $l$ and $r$ are always excluded from the sum.
- **Array endpoints:** Indices 0 and $n-1$ can never be peaks and must never be inserted into the tree.
- **Boundary updates:** Updating index 0 or $n-1$ can still change the status of its sole interior neighbor.
- **No-op updates:** Assigning the existing value remains correct because removing and restoring the same local indicators leaves the tree unchanged.
- **Answer order:** Append a value only for type-1 queries; update queries do not create output entries.
