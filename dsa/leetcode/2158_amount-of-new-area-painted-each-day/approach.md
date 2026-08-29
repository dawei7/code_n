## General

Each interval `[start, end]` describes continuous length `end - start`, naturally treated as half-open area $[start,end)$. With integer endpoints, that area can be represented by unit segments

$$
[start,start+1),[start+1,start+2),\ldots,[end-1,end).
$$

The exact solution maps those unit segments to inclusive integer labels `start + 1` through `end` and uses a dynamic segment tree to count which labels have already been painted.

**Understand each tree node**

A `Node` represents an inclusive coordinate interval `[l,r]`. It stores:

- `left` and `right` child references, created only when needed;
- `mid = (l + r) >> 1`;
- `v`, the number of painted unit segments in this node’s interval;
- `add`, a lazy marker indicating that the entire interval has been assigned painted.

The root covers `[1, 10**5 + 10]`, safely containing every mapped segment because legal endpoints are at most 50,000.

**Query previously painted length**

For one day, `l = start + 1` and `r = end`. The interval contains exactly

`r - l + 1 = end - start`

unit segments.

`tree.query(l, r)` returns the number already painted. When a node lies fully inside the query, its stored `v` is returned. Otherwise, lazy information is pushed down and the query recursively visits the intersecting children, adding their painted counts.

The new area is therefore

`r - l + 1 - v`.

This value is appended before the day’s interval is marked, so it counts only work not done on an earlier day.

**Mark the entire interval painted**

`tree.modify(l, r, 1)` applies a range assignment. When a node is fully covered, the code sets

`node.v = node.r - node.l + 1`

and `node.add = 1`. Every unit segment in that node is now painted.

For a partial overlap, `pushdown` creates missing children. If the parent has a lazy painted marker, both children are marked fully painted and the parent marker is cleared. Recursion updates whichever children intersect the requested range, and `pushup` restores the parent count as `left.v + right.v`.

Painting is monotone: segments only change from unpainted to painted and never back. Therefore a single truthy lazy marker is sufficient; there is no need to represent an unpaint assignment.

**Why coordinate mapping has no off-by-one loss**

Continuous interval $[1,4)$ has length three and consists of unit segments $[1,2)$, $[2,3)$, and $[3,4)$. The tree call uses inclusive labels `2,3,4`—also three labels. Two painting intervals that meet at an endpoint, such as $[1,4)$ and $[4,7)$, map to disjoint labels `2..4` and `5..7`. The shared point has zero length and is not double-counted.

For `[5,8)` after `[4,7)` was painted, labels `6,7` are already covered while label `8` is new, so the query-subtraction result is one.

**Why daily answers are correct**

Before processing a day, `v` values describe the union of every earlier interval. The query returns the measure of the intersection between today’s interval and that union in unit segments. Subtracting from today’s total length gives exactly its unpainted portion. The subsequent range assignment updates the stored union for the next day. Induction over days proves every output entry.

**Distinguish the exact structure from the manifest**

The manifest summary mentions path-compressed successor links, but `solution.py` implements a lazy dynamic segment tree. This explanation and the complexity below follow the actual classes and method calls on disk.

## Complexity detail

Let $U$ be the root coordinate-domain size, about $10^5$. A range query and a range assignment each traverse $O(\log U)$ boundary paths plus fully covered nodes, giving standard lazy segment-tree time $O(\log U)$ per operation. With two operations for each of $n$ days, total time is $O(n\log U)$.

Nodes are allocated dynamically by `pushdown`. Across all operations, at most the full binary tree over the domain can be created, so space is $O(U)$. An input-sensitive bound is also $O(\min(U,n\log U))$ up to tree-node constants. The answer list uses $O(n)$ output space.

These bounds differ from the successor-DSU complexity shown in the manifest because that is not the exact stored implementation.

## Alternatives and edge cases

- **Path-compressed successor links:** Jump from each already painted unit to the next unpainted one, visiting every unit once overall. This matches the manifest summary and can be very efficient on the bounded integer domain.
- **Difference array over days:** A simple global difference array can find final union length but does not directly separate how much became new on each chronological day.
- **Ordered disjoint intervals:** Maintain the painted union in a balanced structure and merge overlaps. This avoids a fixed coordinate tree but requires careful interval splitting.
- **Paint every unit directly:** With endpoints at most 50,000, a boolean array can work, but repeated long intervals may cause $O(nU)$ scanning.
- **No overlap:** Query returns zero for every day, so each answer is `end - start`.
- **Fully covered interval:** Query equals the interval length and new work is zero.
- **Partial overlap:** Only uncovered unit labels contribute after subtraction.
- **Touching endpoints:** Half-open geometry gives zero overlapping length, and the shifted labels remain disjoint.
- **Nested intervals:** A later interval fully inside an earlier one returns zero.
- **Repeated interval:** The first occurrence paints it; every repetition returns zero.
- **Single-unit interval:** `end = start + 1` maps to one label and returns either one or zero.
- **Lazy overwrite:** Marking an already painted full node again leaves `v` equal to its length, so repeated paint is idempotent.
- **Dynamic children:** `pushdown` creates both children before `pushup` reads them, preventing missing-child counts.
- **Input preservation:** The tree stores coverage separately and never changes `paint`.
