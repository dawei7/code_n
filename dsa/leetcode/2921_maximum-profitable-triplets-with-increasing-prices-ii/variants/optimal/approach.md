## General

Fix an item $j$ as the middle of the triplet. We need the greatest profit from an earlier item with a smaller price and the greatest profit from a later item with a larger price. If both exist, their independent maxima plus `profits[j]` give the best triplet using this middle.

Version II cannot scan both sides for every $j$. The source precomputes the two side maxima with Fenwick trees that store prefix maximum profit rather than prefix sums.

**Fenwick prefix-maximum operations**

`update(x,v)` visits Fenwick ancestors of price coordinate $x$ and replaces their stored values with the larger of the old value and $v$. `query(x)` walks Fenwick prefixes downward and returns the greatest profit recorded at any coordinate from $1$ through $x$.

Maximum works here because updates never need to be undone during either one-directional sweep. All profits are positive, so zero safely means no qualifying item has been inserted.

**Forward sweep for the left choice**

For item $i$ with price $x$, the solution first runs `tree1.query(x - 1)` and stores it in `left[i]`. This query includes only strictly smaller price coordinates.

Only afterward does it call `tree1.update(x, profits[i])`. Since the tree contains exactly earlier indices before the update, `left[i]` is

$$
\max\{\texttt{profits}[p]\mid p<i,\ \texttt{prices}[p]<\texttt{prices}[i]\}.
$$

Querying before updating prevents the current item from selecting itself. Querying $x-1$ instead of $x$ excludes equal prices.

**Reverse price coordinates for the right choice**

A Fenwick query naturally asks for smaller coordinates, but on the right we need original prices larger than the current one. Let $m$ be the maximum price and transform original price $p$ to

$$
q=m+1-p.
$$

Larger original prices produce smaller transformed coordinates. The reverse index sweep contains exactly later array positions. For current transformed coordinate $q$, `tree2.query(q - 1)` therefore returns the greatest profit among later items with strictly larger original price.

After querying, the current profit is inserted at $q$. This gives the exact `right[i]` side maximum.

**Combine valid middle positions**

The final generator examines corresponding `left`, current profit, and `right` values. It includes a middle only when both side values are nonzero, then maximizes `l + x + r`. If no middle qualifies, `max(..., default=-1)` returns the required `-1`.

For any valid triplet $(i,j,k)$, the forward tree value at $j$ is at least `profits[i]`, and the reverse tree value is at least `profits[k]`. Thus the candidate for $j$ is at least that triplet's profit. Conversely, every nonzero tree result came from a real index on the correct side with the required strict price relation. Each candidate is a real valid triplet. These two directions prove global optimality.

**Why the transformed coordinate has an extra one**

With `q = m + 1 - p`, original maximum price $m$ maps to coordinate $1$, never zero. Fenwick trees are one-indexed, so every update is legal. The allocated size $m+1$ is sufficient for all transformed and original price coordinates.

## Complexity detail

Let $n$ be item count and $P=\max(\texttt{prices})$. Each query or update takes $O(\log P)$ time. There are two queries and two updates per item across the two sweeps, so total time is $O(n\log P)$.

Arrays `left` and `right` use $O(n)$ space. The two Fenwick arrays use $O(P)$ space. Total auxiliary space is $O(n+P)$.

The final zip and maximum scan is $O(n)$ time and does not change the dominant bound.

## Alternatives and edge cases

- **Quadratic side scans:** Version I fixes each middle and scans both sides in $O(n^2)$ time, which is too slow for $n=50000$.
- **Segment tree:** Range-maximum queries also work in $O(n\log P)$ but require more storage and code than Fenwick prefix maxima.
- **Coordinate compression:** It can replace direct price coordinates when prices are huge, reducing tree space to $O(n)$. Here $P\le5000$, so direct coordinates are simple.
- **Equal prices:** `query(x-1)` excludes them on the left, and the reversed `query(q-1)` excludes them on the right.
- **Zero sentinel:** It is safe because all profits are at least one. With nonpositive profits, existence would need separate tracking.
- **Maximum price on the left sweep:** It can query every lower price normally.
- **Maximum price as a right candidate:** It maps to transformed coordinate one and is included for every smaller current price.
- **No valid triplet:** The filtered generator is empty and `default=-1` handles it without an exception.
- **Duplicate price coordinates:** Fenwick update keeps only the greatest profit seen at that coordinate, which is all future queries need.
- **Index order comes from sweep direction:** The price tree does not store indices, but the forward tree contains only earlier positions and the reverse tree only later positions when each query occurs.
- **Independent side choices:** Once the middle is fixed, selecting the best left profit cannot invalidate the best right choice because their index ranges are disjoint.
