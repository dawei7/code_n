## General

**Rewrite every range sum as a difference of prefixes.**

Let the prefix sequence be

$$
P_0=0,
\qquad
P_t=\text{nums}[0]+\cdots+\text{nums}[t-1]
\quad\text{for }1\le t\le n.
$$

Then the inclusive range from original index $i$ through $j$ has sum

$$
S(i,j)=P_{j+1}-P_i.
$$

The source constructs exactly these $n+1$ values with `accumulate(nums, initial=0)`. The initial zero is not optional: it represents the prefix before the array and lets ranges that begin at index zero use the same formula as every other range.

Suppose the scan's current prefix is $x=P_{j+1}$ and an earlier prefix is $y=P_i$. The range sum is $x-y$. It is valid when

$$
\text{lower}\le x-y\le\text{upper}.
$$

Solving both inequalities for $y$ gives

$$
x-\text{upper}\le y\le x-\text{lower}.
$$

So, for each current prefix $x$, the task is to count earlier prefix values in one inclusive numeric interval. The exact source answers those dynamic interval-count queries with coordinate compression and a Binary Indexed Tree, also called a Fenwick tree.

**Why values need coordinate compression.**

Prefix sums can be negative, positive, repeated, and much larger in magnitude than the input bounds. A Fenwick tree indexes a compact positive integer range, not arbitrary signed values. Coordinate compression sorts all values that may be used as stored points or query boundaries and replaces each with its rank.

The source builds `arr` from three values for every prefix sum $x$:

- $x$, because that prefix will later be inserted;
- $x-\text{lower}$, the inclusive right query boundary;
- $x-\text{upper}$, the inclusive left query boundary.

It removes duplicate numeric values with `set` and sorts the remainder. If `arr[a] < arr[b]`, then rank `a` is also smaller than rank `b`, so interval order is preserved. At most $3(n+1)$ values are considered before duplicates are removed, making the compressed coordinate set linear in size.

Including both boundary expressions is a useful exact-code detail. The source uses `bisect_left` for both ends. Because each queried endpoint is guaranteed to occur in `arr`, `bisect_left` returns that endpoint's precise zero-based position. Adding one converts it to the Fenwick tree's one-based index. A prefix query through the right endpoint then includes all values equal to that endpoint, as required by the inclusive bounds.

**What the Fenwick tree stores.**

At any point in the left-to-right scan, the tree stores the frequency of every prefix sum processed earlier. It stores counts, not merely presence. If the same cumulative sum occurs at several earlier indices, each occurrence represents a different possible start boundary and must be counted separately.

The internal array `c` is one-based. `update(rank, 1)` adds one occurrence at a compressed rank. It then repeatedly advances by `x & -x`, the lowest set bit. Each visited tree cell represents a block of ranks containing the updated point.

`query(rank)` returns the total frequency in compressed ranks `1` through `rank`. It adds the current tree cell and repeatedly subtracts the lowest set bit, moving through disjoint blocks that exactly cover that prefix of ranks.

These two operations each visit only $O(\log n)$ tree cells. Their implementation does not need to know the original prefix-sum magnitudes; sorted ranks preserve every comparison relevant to the interval.

**Query before inserting the current prefix.**

For each current prefix $x$, the source computes

$$
l=\operatorname{rank}(x-\text{upper})
$$

and

$$
r=\operatorname{rank}(x-\text{lower}),
$$

using one-based ranks. Since `lower <= upper`, the numeric left boundary is no greater than the right boundary, so $l\le r$.

The number of earlier prefix sums whose ranks lie from $l$ through $r$ is

$$
\text{query}(r)-\text{query}(l-1).
$$

The first term counts everything up to the inclusive right boundary. Subtracting everything strictly before the left boundary leaves precisely the closed interval. This count is added to `ans`.

Only after the query does the source insert the current prefix $x$. That order enforces the index condition: a range's starting prefix must occur before its ending prefix. Inserting first could count the current prefix against itself whenever zero lies between `lower` and `upper`, creating an empty range, but the problem counts only nonempty ranges with $i\le j$.

At the beginning, the tree is empty. The first scanned prefix is the initial zero. It finds no earlier start, then it is inserted. When the next prefix is processed, that stored zero correctly represents a range beginning at original index zero.

**Walk through `[-2,5,-1]`.**

The prefix sequence is

$$
[0,-2,3,2].
$$

With `lower = -2` and `upper = 2`:

- For current prefix `0`, the tree is empty, so no range ends here. Insert `0`.
- For current prefix `-2`, the required earlier-prefix interval is `[-4,0]`. Stored prefix `0` lies inside it, representing range `[0,0]` with sum `-2`. Add one, then insert `-2`.
- For current prefix `3`, the interval is `[1,5]`. Neither prior `0` nor `-2` lies inside it, so add nothing, then insert `3`.
- For current prefix `2`, the interval is `[0,4]`. Prior prefixes `0` and `3` both qualify. They represent ranges `[0,2]` with sum `2` and `[2,2]` with sum `-1`. Add two.

The final count is three.

**Why every count is correct.**

Whenever a stored earlier prefix $y$ lies in $[x-\text{upper},x-\text{lower}]$, rearranging the inequalities gives

$$
\text{lower}\le x-y\le\text{upper}.
$$

Because insertion happens after querying, $y$ comes from a strictly earlier prefix index. Thus it defines one valid nonempty contiguous range ending at the current position. Each stored occurrence has a distinct prefix index, so frequency counting corresponds one-to-one with distinct ranges.

Conversely, take any valid range. Its ending prefix $x$ is eventually scanned, and its earlier starting prefix $y$ has already been inserted. The range-sum bound places $y$ inside exactly the queried interval, so that occurrence contributes one. It contributes only at its own ending prefix, preventing double counting. Therefore all and only valid ranges are counted.

## Complexity detail

Let $n$ be `len(nums)`. Creating the prefix list takes $O(n)$ time. Building up to $3(n+1)$ coordinate values and sorting the distinct ones takes $O(n\log n)$ time. For each of $n+1$ prefixes, the source performs binary searches plus two Fenwick queries and one update, each $O(\log n)$. Total time is $O(n\log n)$.

The prefix list, compressed coordinate array, and Fenwick storage each contain $O(n)$ values, so auxiliary space is $O(n)$.

The manifest's asymptotic bounds match these totals, but its summary names a merge-sort counting algorithm. The exact optimal source instead uses coordinate compression and a Fenwick tree; this explanation follows that actual data flow.

## Alternatives and edge cases

- **Divide-and-conquer merge counting:** Recursively sort prefix sums by index halves and use two monotone pointers to count cross-half differences in the target interval. It also achieves $O(n\log n)$ time and $O(n)$ space and matches the manifest summary, but it is not the checked-in source.

- **Enumerate every range:** There are $O(n^2)$ start-end pairs. Prefix sums can evaluate each in constant time, but the number of pairs remains too large for $n=10^5$.

- **Balanced ordered multiset:** Insert prior prefixes and query how many fall in a value interval. An augmented balanced tree can provide $O(n\log n)$ time, but Python's standard library has no direct order-statistics multiset, making compression plus Fenwick tree simpler.

- **Repeated prefix sums:** They must be stored as multiple occurrences. A Boolean presence structure would undercount different ranges sharing the same start-prefix value.

- **Inclusive endpoints:** Prefixes exactly equal to `x - upper` or `x - lower` correspond to range sums exactly `upper` or `lower` and must count. The preinserted boundary coordinates and inclusive Fenwick difference preserve both cases.

- **Zero-valued range:** When `lower <= 0 <= upper`, equal earlier and current prefix values form valid zero-sum ranges. Query-before-update prevents the current prefix from forming an invalid empty range with itself.

- **Single element:** The initial zero is inserted before the element's prefix is queried, so the one-element range is counted exactly when its value lies within the bounds.

- **Large and negative sums:** Compression depends only on ordering, not magnitude or sign. Python integers avoid overflow; fixed-width implementations should use a wide enough type for cumulative sums and shifted boundaries.
