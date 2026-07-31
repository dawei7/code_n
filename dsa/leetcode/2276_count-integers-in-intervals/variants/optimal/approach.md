## General

**Represent the enormous coordinate range only where updates touch it**

The legal domain contains $10^9$ integers, so allocating one entry per
coordinate is infeasible. Use an implicit segment tree whose root represents
the complete inclusive range $[1,10^9]$. Create a child node only when an
addition intersects that half of its parent's range.

Each node stores `total`, the number of covered integers in its segment, and a
`covered` flag indicating that the entire segment belongs to the union.

**Stop descending when an update covers a whole segment**

To add `[left, right]`, recursively visit only intersecting tree segments. If
the update fully contains the current segment, set its covered total to the
segment length and discard its children. If a node is already fully covered,
the update cannot change it and returns immediately.

After a partial update, the node's total is the sum of its existing children's
totals; a missing child contributes zero. When this sum reaches the complete
segment length, mark the parent covered and prune both children. The root total
is therefore always the current answer, so `count()` returns it directly.

**Why totals equal the size of the interval union**

A leaf represents one integer and is counted exactly when some addition covers
it. For an internal node, the left and right child segments are disjoint and
partition the parent's segment, so adding their covered totals counts every
covered integer once. A full-cover assignment is exact because every integer
in that segment belongs to the new interval. Induction from leaves to the root
shows that the root total equals the number of distinct integers covered by
all additions, regardless of overlap or insertion order.

## Complexity detail

Let $Q$ be the number of method calls after construction and $U=10^9$ the
coordinate-domain size. An addition descends through $O(\log U)$ levels along
the interval boundaries and prunes fully covered segments; `count()` takes
$O(1)$ time. Across the trace, time is $O(Q\log U)$.

Only visited nodes are allocated. An addition creates at most
$O(\log U)$ boundary-path nodes after covered subtrees are pruned, giving
$O(Q\log U)$ worst-case space and $O(\log U)$ recursion depth.

## Alternatives and edge cases

- **Boolean coordinate array:** Direct marking would require space proportional to $10^9$ and may also scan enormous intervals.
- **Rebuild a merged interval list:** Scanning all stored disjoint intervals after every addition is correct but can take $O(Q^2)$ total time.
- **Ordered disjoint intervals:** A balanced ordered set can merge only overlapping neighbors efficiently, but Python's standard library provides no built-in balanced tree.
- **Duplicate or nested addition:** A fully covered node returns immediately, so the total does not increase.
- **Partially overlapping intervals:** Child totals add only newly covered coordinates.
- **Touching intervals:** Inclusive intervals such as `[1,2]` and `[3,4]` cover four consecutive integers even though they do not overlap.
- **Single-point interval:** `[x,x]` contributes exactly one new integer unless `x` was already covered.
- **Coordinate extremes:** Both 1 and $10^9$ belong to the represented domain.
- **Full-domain addition:** The root becomes covered with total $10^9$ in one assignment.
