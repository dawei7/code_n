## General

**Equalization is possible only within one remainder class**

Adding or subtracting exactly `k` never changes a value modulo `k`. Therefore all values in a query can become equal only if they have the same remainder.

This condition is also sufficient. If every value has remainder `r`, write

$$
\texttt{nums}[i]=r+kq_i.
$$

One operation changes `q_i` by exactly one. Equalizing original values is equivalent to choosing one integer target `q` and minimizing

$$
\sum_i|q_i-q|.
$$

Thus feasible queries reduce to the classic minimum absolute-deviation problem on normalized quotients `nums[i]//k`.

**Check remainder uniformity in constant time**

`remainder_changes[i]` is a prefix count of adjacent positions whose remainders differ. A query `[l,r]` has one remainder throughout exactly when no change occurs across edges `l+1..r`, tested by

`remainder_changes[r] == remainder_changes[l]`.

If they differ, the source appends `-1` immediately.

**The median minimizes total absolute distance**

For feasible normalized values, any median minimizes the sum of absolute differences. The source selects order

`(length+1)//2`,

the lower median in one-based order for even lengths.

To answer many arbitrary ranges, it needs both the range median and sums below/above it. Persistent segment-tree prefix versions provide these without sorting every query.

**Coordinate-compress normalized values**

`coordinates` is the sorted set of all quotients. `rank[value]` maps each quotient to a compact leaf index. Ordering is preserved, so selecting by rank selects by numeric value.

The persistent tree stores at every node:

- `counts`: number of inserted prefix values in its rank interval.
- `totals`: sum of those normalized values.
- Child indices.

`roots[t]` represents the first `t` normalized array values. Query range `[l,r]` is represented by subtracting fields of `roots[l]` from `roots[r+1]`.

**Build persistent versions by path copying**

`add(previous,...)` creates a new node copying the previous version's children, then increments count and total. It recursively creates new nodes only along the inserted rank's root-to-leaf path; untouched subtrees are shared.

Each prefix root therefore adds one value while preserving every older root for future range subtraction.

**Descend to the range median**

At a tree interval, subtracting older-left count from newer-left count gives how many query values lie in the left half.

If the desired order is within that count, descend left.

Otherwise, all left-half values are strictly below the eventual median. Add their count and sum to `below_count` and `below_sum`, subtract their count from `order`, and descend right.

At the leaf, `coordinates[low]` is the median. The difference between leaf-node versions gives how many query values equal it and their total.

The source defines the left group as every value at or below the median:

`left_count = below_count + median_count`

and analogously `left_sum`. The remaining values form the strictly greater right group.

**Compute absolute deviations from counts and sums**

For values `x<=median`,

$$
|x-median|=median-x.
$$

Their total cost is

$$
median\cdot left\_count-left\_sum.
$$

For greater values, the cost is

$$
right\_sum-median\cdot right\_count.
$$

Adding these expressions gives the minimum number of quotient unit moves, which equals the number of original ±`k` operations.

For `[1,4,7]` with `k=3`, all remainders are one and normalized values are zero, one, two. Median one yields distances one, zero, one, totaling two.

**Why every query answer is exact**

Different remainders prove impossibility by invariance. Equal remainders make every quotient target reachable. Median optimality supplies the best target, and root subtraction returns exact range frequencies and sums. The final formula counts every required unit operation once.

Queries are hypothetical: persistent roots and prefix arrays are immutable, so one answer never changes another.

## Complexity detail

Let `U` be the number of distinct normalized values, with `U<=n`. Compression sorting takes $O(n\log n)$. Each of `n` persistent insertions creates $O(\log U)$ nodes, taking $O(n\log U)$ time and space.

Each feasible query descends $O(\log U)$ levels; infeasible queries are $O(1)$. Total time is

$$
O((n+q)\log n),
$$

and persistent-tree space is $O(n\log n)$, matching the manifest. Prefix roots, remainder changes, and compression maps add $O(n)$.

## Alternatives and edge cases

- **Sort every query subarray:** This costs up to $O(qn\log n)$. Persistence reuses global preprocessing.
- **Use the mean:** Absolute deviation is minimized by a median, not an average.
- **Ignore remainders:** Values in different modulo classes can never meet using ±`k` operations.
- **Check only endpoint remainders:** An interior change could make the query impossible; the prefix change count checks the whole interval.
- **Persistent counts without sums:** They locate the median but cannot compute total deviation in logarithmic time. Node totals are essential.
- **Single-element query:** Remainders are uniform, the sole value is its median, and cost is zero.
- **Even length:** Either middle value minimizes the L1 cost. The chosen lower median is valid.
- **Duplicate medians:** `median_count` groups all equal occurrences, each with zero deviation.
- **Large original values:** Normalization keeps exact quotient distances; arithmetic sums should use wide integers.
- **Independent queries:** No operation mutates `nums` or the persistent versions.
- **Coordinate compression:** It preserves ordering while allowing a compact segment-tree domain.
- **All query values equal:** The median formula returns zero.
