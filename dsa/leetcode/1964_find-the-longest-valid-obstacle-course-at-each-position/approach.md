## General

**Turn the course condition into a prefix maximum query**

For current obstacle height $x$, a valid course ending here can extend any earlier course whose final height is at most $x$. Among all such courses, choose the greatest length and add one for the current obstacle.

The algorithm needs a data structure supporting:

- query the maximum course length among heights $\le x$;
- update the best course length ending at height $x$.

A Binary Indexed Tree is adapted from prefix sums to prefix maxima to perform both operations efficiently.

**Compress large height values into ranks**

Obstacle heights may be as large as $10^7$, but only their relative order matters. `sorted(set(obstacles))` builds `nums`, the increasing list of distinct heights. `bisect_left(nums, x) + 1` maps $x$ to a one-based rank.

If height $a\le b$, then its compressed rank is also at most $b$'s rank. Therefore a prefix query through rank `i` represents exactly all course-ending heights less than or equal to $x$.

The `+1` is necessary because Fenwick trees use index zero as a stopping sentinel.

**Store prefix maxima in a Fenwick tree**

Tree array `c` does not store one height per cell directly. Each Fenwick index summarizes a range determined by its lowest set bit.

`update(x, v)` visits index $x$ and its Fenwick ancestors with `x += x & -x`, replacing each stored summary with the maximum of its old value and `v`.

`query(x)` walks downward with `x -= x & -x`. The visited ranges partition ranks one through $x$, so taking their maximum returns the greatest stored course length across that complete prefix.

Unlike a sum Fenwick tree, a maximum update cannot undo or lower prior values. That is fine because processing more obstacles can only improve the best known length for a height range.

**Process obstacles in original order**

For each original height $x$, the code computes its rank `i` and appends `tree.query(i) + 1`. Querying through `i` rather than `i - 1` allows courses to extend an equal-height obstacle, exactly matching the non-decreasing rule.

It then updates that same rank with the new length. Because the query occurs before the update, the current obstacle cannot reuse itself; every contributing course ends at an earlier index.

For `[2,2,1]`, the first two has prefix maximum zero and gets length one. The second two queries the same rank, sees length one, and gets two. Height one queries only its smaller rank and gets one.

**Why one best value per height prefix is enough**

Suppose several earlier courses end at eligible heights. Only their lengths matter for extending with $x$, and a longer eligible course always dominates a shorter one. The Fenwick summaries may forget which indices formed the course, but the problem asks only for lengths and the stored value came from a real earlier course.

By induction, every update stores a valid course ending at its height, and every query finds the longest eligible earlier course. Adding the current obstacle creates the optimal course required to end at that position.

**Trace ranks rather than raw tree cells**

For `obstacles = [3, 1, 5, 4]`, compression gives `nums = [1, 3, 4, 5]`. Height three has rank two. Its prefix query is initially zero, so its answer is one and rank two is updated with one. Height one has rank one and cannot see rank two in its prefix, so it also gets one.

Height five has rank four and queries all ranks, finds a best length of one, and gets two. Height four has rank three; it can extend either the course ending at one or three but cannot use the earlier five at rank four. Its prefix maximum is one and its answer is two. The rank boundary enforces the height inequality while original processing order enforces the index inequality.

**Why a Fenwick maximum remains valid**

For sums, Fenwick updates add deltas. Here each update applies `max` to every covering cell. A later course of the same or larger stored range can only raise a prefix answer; no future query needs to recover an older smaller value. This monotone property is what makes the modified Fenwick tree correct even though general point assignment with arbitrary decreases would not be supported.

## Complexity detail

Let $N$ be the number of obstacles and $U$ the number of distinct heights.

Building the set and sorting it takes $O(N\log N)$ time in the worst case. Each of $N$ obstacles performs one binary search, one Fenwick query, and one update, each $O(\log U)$. Total time is $O(N\log N)$.

The compressed values, Fenwick array, and returned answer each contain $O(N)$ entries, so auxiliary plus output space is $O(N)$.

## Alternatives and edge cases

- **Patience-sorting tails:** Maintain the smallest tail for every course length and use `bisect_right`. It gives the same $O(N\log N)$ bounds and is shorter, but the exact source uses prefix-max queries.
- **Quadratic DP:** Compare every current obstacle with every earlier one. It is direct but takes $O(N^2)$ time.
- **Segment tree:** It supports the same rank-prefix maximum and point update with larger constants.
- **Equal heights:** Querying the current rank includes them, so repeated equal obstacles can extend one another.
- **Strictly decreasing heights:** Each rank prefix has no positive eligible earlier course, so every answer is one.
- **Strictly increasing heights:** Every obstacle extends the full prior course, yielding one through $N$.
- **Duplicate compression:** `set` creates one rank per height; the Fenwick cell retains the best length seen at that height.
- **One obstacle:** Its query returns zero and its answer is one.
- **One-based indexing:** Without the rank offset, height at compressed index zero could not be updated or queried correctly.
- **Maximum-only update:** Course lengths never need to decrease, so an irreversible max Fenwick operation is valid.
- **Current obstacle exclusion:** Querying before updating prevents the new obstacle from artificially extending itself.
- **Large raw heights:** Compression makes tree size depend on distinct input values, not the numeric maximum $10^7$.
- **Input order:** Compression sorts only a separate value list; obstacles themselves are processed in original order.
