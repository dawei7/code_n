## General

For index `i`, only elements at later indices matter. A left-to-right scan does not yet know those values, but a right-to-left scan has already processed exactly the suffix to the right. The source maintains frequency counts for that processed suffix in a Fenwick tree.

For each value, it asks how many stored suffix values are strictly smaller, records that count, and then ensures the current value is available when processing positions farther left.

**Compressing values into ranks**

Fenwick tree positions must be small positive integers, while `nums` can contain negative values and gaps. The source creates

`alls = sorted(set(nums))`.

The set removes duplicate values, and sorting puts the remaining values in increasing numeric order. It then maps them to one-based ranks:

`m = {v: i for i, v in enumerate(alls, 1)}`.

If value $a<b$, then `m[a] < m[b]`. Equal values receive the same rank. Therefore, comparing ranks preserves every ordering fact needed by the problem while discarding irrelevant numeric gaps.

One-based ranks are especially convenient because Fenwick position zero is reserved as the stopping boundary. If there are $u$ distinct values, valid ranks are 1 through $u$.

**What the Fenwick tree stores**

After some suffix has been processed, the logical frequency at rank $r$ equals the number of occurrences in that suffix whose value has rank $r$. Duplicates increase the same frequency rather than creating separate positions.

For positive index $x$, `lowbit(x) = x & -x` isolates its least significant set bit. Fenwick entry `c[x]` stores the total frequency over the rank interval

$$
[x-\operatorname{lowbit}(x)+1,\ x].
$$

These overlapping blocks allow a point frequency increment and a prefix-frequency query in logarithmic time.

**Adding one occurrence**

`tree.update(x, 1)` increments the frequency of the current rank. It updates `c[x]`, then repeatedly advances with

`x += lowbit(x)`.

Each next position represents a larger Fenwick interval containing the original rank. Updating all such entries preserves every prefix summary affected by the new occurrence.

**Counting all strictly smaller ranks**

`tree.query(t)` returns the total frequency at ranks 1 through `t`. It adds `c[t]`, then repeatedly removes the trailing represented block with

`t -= lowbit(t)`.

The visited blocks are disjoint and exactly cover the requested rank prefix.

If the current value has rank `x`, strictly smaller values have ranks 1 through `x - 1`. Therefore,

`tree.query(x - 1)`

is precisely the number of smaller values currently represented in the tree.

Using `query(x)` would be wrong because it would include equal values. The problem requires `<`, not `<=`.

**The right-to-left invariant**

Before processing original index `i`, the tree contains occurrences from indices greater than `i` and no occurrences from indices less than `i`. This is initially true for the rightmost element because no later value exists.

The source obtains reverse order with `nums[::-1]`. For current value `v`, it finds rank `x`, updates that rank, and appends `query(x - 1)`.

Although the update happens before the query, the newly inserted current value has rank exactly `x`, outside queried ranks 1 through `x - 1`. It contributes nothing. Thus, the query still counts only strictly smaller elements from the earlier represented suffix.

After the iteration, the tree contains the old suffix plus the current occurrence. That is exactly the suffix that should be visible to the next index on the left, preserving the invariant.

**Why duplicates are handled correctly**

All equal values share one rank. Every occurrence increments that rank's frequency, but a query for rank `x - 1` stops before it. Therefore, neither the current inserted occurrence nor any equal occurrence to its right is counted as smaller.

For `[-1, -1]`, both values have rank 1. Each query asks for prefix zero, which returns zero, producing `[0, 0]`.

**Tracing the main example**

For `nums = [5,2,6,1]`, sorted distinct values are `[1,2,5,6]`, with ranks 1, 2, 3, and 4.

| Processed value | Rank | Smaller stored ranks | Appended count |
| --- | --- | --- | --- |
| 1 | 1 | none | 0 |
| 6 | 4 | rank 1 contains one value | 1 |
| 2 | 2 | rank 1 contains one value | 1 |
| 5 | 3 | ranks 1 and 2 contain two values | 2 |

Counts are produced in reverse original order as `[0,1,1,2]`. The final `ans[::-1]` restores index order and returns `[2,1,1,0]`.

**Why the result is exact**

At each index, the suffix invariant guarantees that every stored occurrence comes from the right and every right-side occurrence is stored. Rank order guarantees that querying through `x - 1` includes exactly values smaller than the current one. Frequency totals count repeated smaller occurrences individually.

The appended number is therefore correct for that index. Reversing the collected answers changes only their presentation order, not their association with positions.

## Complexity detail

Let $n$ be the input length and $u$ the number of distinct values, where $u\le n$.

Building the set costs $O(n)$ expected time, and sorting its $u$ values costs $O(u\log u)$. Creating the map costs $O(u)$. Each of the $n$ iterations performs one Fenwick update and one query, each costing $O(\log u)$.

Total time is

$$
O(n+u\log u+n\log u)=O(n\log n).
$$

The distinct-value list, rank map, Fenwick array, reversed input slice, and answer list each use at most linear storage. Total auxiliary space is $O(n)$.

The slices `nums[::-1]` and `ans[::-1]` create lists rather than lazy views, which is included in the linear bound.

## Alternatives and edge cases

- **Modified merge sort:** Sort `(value, original_index)` pairs and count how many right-half elements move before each left-half element during merging. This also gives $O(n\log n)$ time and $O(n)$ space.
- **Segment tree over ranks:** Store frequencies and query the rank interval below the current value. It has the same asymptotic bounds but uses a larger and more general structure.
- **Fixed value-offset Fenwick tree:** The constraints permit shifting values by $10^4$. It avoids sorting but allocates for the entire value range; compression adapts to actual distinct values.
- **Balanced ordered multiset with rank queries:** Insert suffix values and ask how many are below the current one. A suitable augmented tree works in $O(n\log n)$ but is not built into Python.
- **Compare every later pair:** This directly follows the definition but costs $O(n^2)$ time.
- **Scan left to right:** The maintained values would lie to the left, answering the wrong directional question.
- **Query through rank `x`:** Equal values would be counted, violating strict comparison.
- **Update before query:** It is safe only because the query ends at `x - 1`. If querying `x`, insertion order would introduce an additional error from the current element.
- **Smallest value:** Its rank is 1, so `query(0)` returns zero without entering the loop.
- **Largest value:** Its query includes every stored rank except equal largest values, exactly as required.
- **All values equal:** Every query prefix is below their shared rank and contains no occurrences, so all answers are zero.
- **Strictly increasing input:** Every later value is larger, so all counts are zero.
- **Strictly decreasing input:** At index `i`, every later value is smaller, producing counts `n-1, n-2, ..., 0`.
- **Negative values:** Compression orders them numerically and needs no special array indexing.
- **One element:** The reverse scan inserts it, queries below it as zero, and returns `[0]`.
