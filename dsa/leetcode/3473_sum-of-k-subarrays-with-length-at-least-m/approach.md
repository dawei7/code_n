## General

**Build the answer one chosen subarray at a time.** The non-overlap condition suggests a prefix dynamic program. After finishing one layer, `previous[p]` represents the maximum sum obtainable by choosing exactly `chosen - 1` valid non-overlapping subarrays entirely within the first $p$ elements, `nums[0..p-1]`.

Before choosing any subarray, the best sum in every prefix is zero, so `previous` starts as an all-zero array. This does not mean later layers may choose fewer than the requested number: each outer iteration creates exactly one additional subarray and replaces `previous` with that exact-count layer.

The prefix-sum array satisfies

$$
\texttt{prefix}[r]-\texttt{prefix}[l]
=
\sum_{i=l}^{r-1}\texttt{nums}[i].
$$

It lets the code evaluate a proposed final subarray $[l,r)$ in constant time.

**Express a transition ending at one boundary.** Suppose the new, `chosen`-th subarray ends at exclusive boundary `end` and begins at `start`. Its length must be at least $m$, so `start <= end - m`. Everything chosen earlier must lie within the prefix ending at `start` to avoid overlap. The total is

$$
\texttt{previous}[start]
+\texttt{prefix}[end]
-\texttt{prefix}[start].
$$

For fixed `end`, `prefix[end]` is constant. The best legal beginning is therefore determined by

$$
\max_{start\le end-m}
\bigl(
\texttt{previous}[start]-\texttt{prefix}[start]
\bigr).
$$

The source stores this running maximum in `best_start`.

**Update the running maximum incrementally.** When `end` advances by one, exactly one new starting boundary becomes eligible: `start = end - m`. The assignment

`best_start = max(best_start, previous[start] - prefix[start])`

adds that candidate while retaining every earlier eligible start. Therefore, after the update, `prefix[end] + best_start` is the best solution whose last selected subarray ends exactly at `end` and has length at least $m$.

This algebra is the key optimization. A direct DP would scan every possible `start` for every `end` and cost an extra factor of $n$. Pulling `prefix[end]` outside the maximum turns that scan into one running value.

**Allow the last subarray to end earlier.** `current[end]` is the best sum for exactly `chosen` subarrays inside the first `end` elements, not necessarily using element `end - 1`. It is the maximum of:

- `current[end - 1]`, which leaves the new last array element unused; and
- `prefix[end] + best_start`, which ends the final chosen subarray at `end`.

Thus the update

`current[end] = max(current[end - 1], prefix[end] + best_start)`

captures both possibilities.

The inner loop starts at `chosen * m` because choosing `chosen` subarrays of minimum length $m$ requires at least that many elements. Entries before that boundary remain at `negative_infinity`, marking impossible exact-count states. The chosen sentinel $-10^{30}$ is far below any legal sum under the constraints, so it cannot be mistaken for a real optimum.

For the first example with $k=2,m=2$, the first layer computes the best single length-at-least-two subarray in every prefix. The second layer considers a final subarray and combines it only with a first-layer value ending no later than that subarray's start. The transition can select `[0,2)` with sum $3$ and `[3,6)` with sum $10$, giving $13$ while leaving index two unused.

**Negative values require exact-count states.** It would be wrong to initialize every layer to zero or allow skipping an entire required subarray, because the problem asks for exactly $k$. In the second example, $k=n$ and $m=1$, so every element must be its own selected subarray even though several values are negative. The layer construction forces all four choices and returns $-10$ rather than an invalid nonnegative result.

**Why the recurrence is correct.** Consider an optimal selection of exactly `chosen` subarrays in the first `end` elements. If no selected subarray ends at `end`, the selection is represented by `current[end-1]`. Otherwise, let its final subarray be $[start,end)$. The earlier subarrays form an optimal or suboptimal feasible solution inside the first `start` elements, and replacing them with `previous[start]` cannot reduce the total. The running maximum considers this `start` because its length is at least $m$. Hence one transition attains the optimum. Conversely, every transition joins a valid previous exact-count selection with a non-overlapping length-at-least-$m$ subarray, so it never creates an illegal solution. Induction over layers and prefix length proves `previous[n]` is the requested maximum.

## Complexity detail

Prefix construction takes $O(n)$ time. Each of the $k$ DP layers scans at most $n$ ending boundaries and performs constant work per boundary, so total time is $O(nk)$.

The prefix, previous, and current arrays each contain $n+1$ values. Only two DP layers coexist; earlier layers are discarded after `previous = current`. Auxiliary space is $O(n)$, matching the manifest.

The mathematical sum can be as low as roughly $-2\cdot10^7$ under the declared limits, so `-10**30` is a safe unreachable-state sentinel. Python integer arithmetic also avoids overflow for positive totals.

Without the `best_start` transformation, scanning all starts would cost $O(kn^2)$. The running maximum is what achieves the stated optimal layer-by-prefix bound.

## Alternatives and edge cases

- **Enumerate all sets of subarrays:** The number of boundary combinations grows combinatorially.
- **Try every start for every end:** This produces $O(kn^2)$ time; algebraically maintaining `previous[start] - prefix[start]` removes that extra scan.
- **Use ordinary Kadane's algorithm:** Kadane handles one subarray and does not enforce exactly $k$ non-overlapping selections or a minimum length.
- **Initialize each layer with zero:** That would silently allow fewer than `k` subarrays and fail on all-negative inputs.
- **Exactly enough elements \(n=km\):** Every selected subarray must have length exactly $m$ and together they cover the array.
- **\(m=1\):** Every single element is a legal subarray, and the same recurrence applies without special handling.
- **Longer-than-\(m\) subarray:** Earlier start boundaries remain in `best_start`, so the transition is not limited to exact length $m$.
- **Gaps between subarrays:** `previous[start]` may leave unused elements in its prefix, and `current[end-1]` may leave unused suffix elements.
- **Adjacent subarrays:** Ending an earlier subarray at `start` and beginning the next there is non-overlapping and correctly allowed.
- **All values negative:** Exact-count negative-infinity states force the least harmful legal $k$ subarrays instead of choosing none.
- **Prefix indexing:** Subarray $[start,end)$ includes `start` through `end-1`; using exclusive boundaries avoids off-by-one ambiguity.
- **Feasibility guarantee:** The constraint `k <= floor(n/m)` ensures `previous[n]` is reachable after the final layer.
