## General

**Treat every array index as a two-dimensional point**

Index `j` contributes the point:

$$
(a,b)=(\texttt{nums1}[j],\texttt{nums2}[j])
$$

with value $a+b$. A query $(x,y)$ asks for the largest point value among points in the upper-right region $a\ge x$ and $b\ge y$.

Checking all $n$ points for every query would take $O(nq)$. The solution handles the first threshold offline and leaves only a one-dimensional threshold for a Fenwick tree.

**Sort points and queries by decreasing first coordinate**

`nums` stores all paired coordinates sorted by decreasing `nums1`. Query indices are also processed by decreasing query `x`.

Maintain pointer `j` into the sorted points. Before answering a query with threshold `x`, advance `j` while `nums[j][0] >= x`. Every inserted point satisfies this query's first condition.

Because later processed queries have an equal or smaller `x`, inserted points remain eligible forever. No deletion is necessary. This monotone sweep is the reason offline ordering is powerful.

Answers still belong in original query order. The loop sorts indices rather than query objects, and writes each result to `ans[i]`.

**The remaining task is a suffix maximum on nums2**

After activating all points with $a\ge x$, a query needs the maximum $a+b$ among active points whose second coordinate satisfies $b\ge y$.

A normal coordinate ordering would make this a suffix query. Fenwick trees naturally query prefixes, so the implementation reverses ranks.

First, `nums2.sort()` creates the sorted coordinate list. For a value `v`, let:

`p = bisect_left(nums2, v)`.

There are `n - p` stored coordinate entries at least `v`. The code uses that number as the reversed Fenwick index:

`k = n - bisect_left(nums2, v)`.

Large second coordinates receive small indices; smaller coordinates receive larger indices.

**Why the reversed ranks implement b at least y**

If a point has $b\ge y$, its lower-bound position is at least the lower-bound position of $y$. Subtracting from $n$ reverses the inequality:

$$
\operatorname{rank}(b)\le\operatorname{rank}(y).
$$

Therefore all active points satisfying $b\ge y$ lie inside the Fenwick prefix ending at the query rank. `tree.query(k)` returns the maximum value stored in that prefix.

If `y` is larger than every coordinate, `bisect_left` returns `n` and `k=0`. Querying prefix zero returns `-1`, correctly indicating no eligible point.

**Fenwick tree stores maxima instead of sums**

Each tree cell `c[x]` stores a maximum. `update(k, value)` walks upward with `x += x & -x` and replaces each covered aggregate with the larger value.

`query(k)` walks downward with `x -= x & -x` and takes the maximum of the canonical Fenwick ranges covering prefix one through `k`.

Fenwick trees do not require addition specifically. Any associative prefix aggregate that can be updated monotonically works here. Since points are only inserted and stored maxima never need to decrease, maximum is suitable.

The initial value is `-1`. All legal point sums are positive, so `-1` safely represents an empty set.

**Coordinate duplicates are harmless**

`nums2` may contain repeated values. `bisect_left` maps every occurrence of the same coordinate to the same reversed rank. Multiple updates to that rank keep their maximum sum. Query correctness depends on coordinate order, not on assigning a separate unique rank to each duplicate.

The tree has size `n` even though coordinate compression could use only distinct values. This wastes at most a constant factor and simplifies indexing.

**Trace the first query pattern**

For a high `x` threshold, the sweep activates only points with sufficiently large first coordinates. Query rank `k` then includes only activated points whose second coordinates are at least `y`. The stored maximum is exactly the best sum in the query rectangle.

When the next query has a lower `x`, more points enter. Old points remain, and Fenwick maxima are updated with any better new sums. The earlier answer is already stored and cannot be affected retroactively.

**Important mutation detail**

The code constructs `nums = sorted(zip(nums1, nums2), ...)` before sorting `nums2` itself. Thus `nums` captures the original coordinate pairing. Sorting `nums2` afterward mutates the caller's second array only for coordinate lookup and does not corrupt the already materialized point tuples.


At each query's turn, the descending sweep has inserted exactly the points with first coordinate at least `x`: all earlier points qualify, and the next uninserted point does not. Reversed compression maps exactly those inserted points with second coordinate at least `y` into the queried Fenwick prefix. The tree stores their maximum $a+b$, or `-1` if the prefix is empty. Writing this value to the query's original index makes every answer correct and properly ordered.

## Complexity detail

Let $n$ be the number of points and $q$ the number of queries. Sorting points costs $O(n\log n)$, sorting `nums2` costs $O(n\log n)$, and sorting query indices costs $O(q\log q)$. Every point is inserted once and every query performs one Fenwick query, each in $O(\log n)$ time.

Total time is:

$$
O(n\log n+q\log q+(n+q)\log n),
$$

commonly summarized as $O((n+q)\log(n+q))$.

The point tuples, sorted query-index list, answer array, coordinate list, and Fenwick array use $O(n+q)$ space. The exact code sorts `nums2` in place, but still stores `nums` and the tree separately.

## Alternatives and edge cases

- **Scan every point per query:** Simple but costs $O(nq)$.
- **Segment tree:** Supports the same coordinate-compressed maximum queries but uses more code than a Fenwick tree.
- **Monotone Pareto frontier:** Another offline solution can maintain nondominated points, though boundary management is subtler.
- **No qualifying first coordinate:** No point is inserted for the query, so the tree returns `-1`.
- **y above every nums2 value:** Reversed rank is zero and the answer is `-1`.
- **y below every nums2 value:** The prefix includes every active point.
- **Duplicate second coordinates:** They share a rank and retain the best sum.
- **Equal query x values:** They see the same fully inserted eligibility set.
- **Original answer order:** Stored query indices undo offline sorting.
- **Input mutation:** `nums2` is sorted in place; `nums1` and `queries` are not reordered.
