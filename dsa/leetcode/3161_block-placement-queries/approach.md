## General

**Represent free space by gaps between obstacles**

A block can touch an obstacle but cannot cross it. If consecutive obstacles are at positions $a<b$, the available interval between them has length $b-a$. A type-2 query asks whether some free interval contained in $[0,x]$ has length at least `block_size`.

The code places permanent sentinel obstacles at 0 and at `max_coord`, one position beyond every query coordinate. The origin sentinel lets a gap from 0 to the first real obstacle be handled like every other gap. The right sentinel ensures every insertion always has a next obstacle.

For each obstacle $r$, the segment tree stores at coordinate $r$:

$$
\operatorname{gap}[r]=r-\operatorname{previousObstacle}(r).
$$

Thus each complete free gap is stored at its right endpoint.

**Use a Fenwick tree as an ordered set**

Coordinates are bounded, so the Fenwick tree `bit` stores 1 at every present obstacle coordinate and 0 elsewhere. `bit_sum(x)` returns how many obstacles are at positions at most $x$.

`bit_find(order)` performs Fenwick binary lifting to find the zero-based coordinate of the obstacle with the requested one-based rank.

When inserting new obstacle $x$, the contract guarantees it is absent. Let

`before = bit_sum(x)`.

Because $x$ is not yet an obstacle, `before` is the number of obstacles strictly to its left. Therefore:

- `bit_find(before)` is the previous obstacle;
- `bit_find(before + 1)` is the next obstacle.

This gives ordered predecessor and successor operations without a balanced-tree library.

**Split one gap during insertion**

Before insertion, successor `next_obstacle` stores the complete gap

$$
\texttt{next\_obstacle}-\texttt{prev\_obstacle}.
$$

Adding $x$ splits it into:

$$
x-\texttt{prev\_obstacle}
$$

ending at $x$, and

$$
\texttt{next\_obstacle}-x
$$

ending at `next_obstacle`.

The code marks $x$ in the Fenwick tree, sets the segment-tree value at $x$ to the first length, and replaces the successor's value with the second length. No other gap changes.

Array `present` is initialized and updated but never read. It consumes coordinate-sized memory without affecting behavior; duplicate insertions are already excluded by the input guarantee.

**Answer a placement query**

For `[2, x, block_size]`, free intervals inside $[0,x]$ fall into two categories.

First are complete gaps whose right endpoint is an obstacle at or before $x$. Their maximum length is

`seg_max(0, x)`.

Second is the possibly incomplete trailing gap from the nearest obstacle at or before $x$ to the query boundary $x$. The Fenwick rank lookup finds `prev_obstacle`, and its usable length is

`x - prev_obstacle`.

The largest legal space is the maximum of these two quantities. A block fits exactly when that maximum is at least its size. Equality is allowed because touching obstacles and the boundary is permitted.

If $x$ itself is an obstacle, predecessor lookup returns $x$ and the trailing partial length is zero. The complete gap ending at $x$ is already represented in the segment tree.

**Segment-tree invariant**

At every obstacle coordinate $r$, the leaf stores the distance from the previous obstacle to $r$. At nonobstacle leaves, it stores zero. Every internal node stores the maximum of its children, so `seg_max(left,right)` returns the longest complete gap whose right endpoint lies in that coordinate range.

Initialization has obstacles 0 and `max_coord`. The latter stores gap `max_coord - 0`. Each insertion updates exactly the two endpoints whose predecessor relationship changes, preserving the invariant.

Combining that invariant with the separately measured trailing interval covers every possible block location in $[0,x]$, proving each Boolean answer correct.

**Coordinate sizing**

`max_coord = max(query[1] for query in queries) + 1` exceeds every $x$ appearing in either query type. It is therefore a safe right sentinel. `size = max_coord + 1` provides array slots for coordinates 0 through `max_coord`.

The Fenwick tree internally shifts external coordinates by one so coordinate zero can be represented. The segment tree uses external zero-based coordinates directly at its leaves.

## Complexity detail

Let $q$ be the query count and $C=\max x+1$ be the sentinel coordinate.

Fenwick prefix sums, order-statistic searches, and updates each take $O(\log C)$. Segment-tree point updates and range maxima also take $O(\log C)$. Each type-1 or type-2 query performs a constant number of these operations, so processing costs $O(q\log C)$.

Constructing the segment-tree node array is done implicitly through array allocation and no recursive node objects; finding its power-of-two base and allocating arrays costs $O(C)$. Total time is $O(C+q\log C)$. The manifest omits the initialization term and states the per-query-dominant $O(q\log C)$ bound.

The Fenwick tree, segment tree, and unused `present` array each use $O(C)$ space. The Boolean result uses $O(q)$ output space. Auxiliary space is $O(C)$ because the coordinate bound is at least proportional to relevant query coordinates, matching the manifest.

The generated-source note in the file records provenance only; the invariants above explain the exact implementation.

## Alternatives and edge cases

- **Balanced sorted set plus segment tree:** This is the editorial's direct forward approach. A sorted set finds neighbors in $O(\log q)$, while the segment tree handles maximum gaps.
- **Offline reverse processing:** Start with all obstacles and remove them backward. Gaps only merge, allowing a Fenwick prefix-maximum structure plus an ordered set.
- **Scan obstacles per query:** It can take $O(q^2)$ time.
- **Store only the globally largest gap:** Insufficient because a query boundary $x$ may exclude that gap.
- **Origin sentinel:** It makes free space before the first obstacle a normal gap and allows blocks to touch coordinate 0.
- **Right sentinel:** It guarantees a successor for every real insertion and is never inside a queried range.
- **Obstacle at query boundary:** The trailing partial gap is zero, but the complete gap ending at that obstacle remains eligible.
- **Block exactly fills a gap:** `>=` returns true because touching obstacles is allowed.
- **Insertion splits one interval:** Only the new obstacle and its former successor require segment updates.
- **No duplicate insertions:** The guarantee is essential because the source does not consult its unused `present` array before updating.
- **Sparse coordinates:** The source still allocates $O(C)$ arrays; a coordinate-compressed or dynamic tree could reduce memory when coordinates were much larger.
- **Queries do not place blocks:** Type-2 queries never modify either tree, so they remain independent placement tests.
