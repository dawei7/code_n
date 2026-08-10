## General

For every falling square, two interval operations are needed:

1. find the maximum existing height anywhere under the square's horizontal footprint;
2. assign the square's new top height across that entire footprint.

The exact solution supports these operations with a dynamically allocated segment tree over the fixed coordinate domain from `1` through `10^9`. Lazy propagation allows a whole covered interval to be assigned one height without visiting every coordinate.

**Representing a square's footprint**

An input pair `[l, w]` describes a square with left edge `l` and side length `w`. The code uses the inclusive integer interval

`[l, r]` where `r = l + w - 1`.

This encoding preserves the “side contact does not overlap” rule for integer coordinates. A square ending geometrically at coordinate `l+w` occupies encoded positions through `l+w-1`. Another square beginning at `l+w` starts at the next encoded position, so their query intervals do not intersect.

If two footprints overlap with positive width, their inclusive encoded ranges share at least one integer position.

**What each segment-tree node stores**

A `Node` represents an inclusive coordinate interval `[node.l, node.r]` and stores:

- `mid`, its midpoint;
- `left` and `right` children, created only when needed;
- `v`, the maximum surface height anywhere in the interval;
- `add`, a pending lazy assignment meaning the entire interval has that uniform height.

The field name `add` is slightly misleading: it is not an amount to add. It stores an assignment value.

The root covers `[1, 10^9]`. The tree does not allocate a billion leaves. Children are created by `pushdown` only along intervals reached by queries and updates.

**Querying the supporting height**

`query(l, r)` returns the maximum stored height in the requested footprint.

If the current node is completely covered, `node.v` is already the answer for that component interval.

For partial coverage, `pushdown(node)` ensures children exist and propagates any pending uniform assignment into both children. The query then recurses only into children whose ranges intersect the requested interval and takes the maximum returned value.

An uncovered part of the domain effectively has height zero. The local accumulator `v` begins at zero.

**Computing a square's landing height**

For a square of side `w`, let `base` be the maximum height under any part of its footprint. The falling square stops when its bottom reaches that highest support. Its top is therefore

$$
h=\textit{base}+w.
$$

The code computes exactly:

`h = tree.query(l, r) + w`.

Even if lower areas or gaps exist elsewhere under the square, the rigid square is held at the greatest supporting height. Once landed, its horizontal top side is flat at height `h` across the entire footprint.

**Why interval assignment is correct**

After landing, `tree.modify(l, r, h)` assigns height `h` over the full footprint.

This is not a maximum update in the node code; fully covered nodes receive `node.v = v` and `node.add = v`. Assignment is safe because `h = base + w` and `w > 0`, so `h` is strictly greater than every old height within the footprint. The new square covers and raises the visible surface everywhere it spans.

For a fully covered segment, the lazy tag postpones pushing that uniform height to smaller coordinates. Future partial operations call `pushdown` and receive the correct child values before descending.

**Pushdown and pushup**

`pushdown` first creates missing children for the two halves.

If `node.add` is nonzero, both children are assigned that same height in `v` and `add`, and the parent's tag is cleared. Zero safely means “no pending assignment” because every landed-square height is positive.

After a partial modification, `pushup` sets:

`node.v = max(node.left.v, node.right.v)`.

The parent then again represents the maximum height across the union of its child intervals.

**Maintaining the reported global height**

The segment tree answers local footprint maxima. The variable `mx` separately stores the tallest top seen anywhere after all drops so far.

After calculating `h`, the code performs `mx = max(mx, h)` and appends `mx` to `ans`. A new square that lands below the existing tallest stack does not reduce the reported height.

The tree update may occur after appending because `h` was already calculated and `mx` does not depend on the internal update order for that same square. The update is completed before the next square is processed.

**A trace**

For `positions = [[1, 2], [2, 3], [6, 1]]`:

- The first footprint is `[1, 2]`. Its base is zero, so its top is `2`. The reported maximum is `2`.
- The second footprint is `[2, 4]`. It overlaps the first at encoded coordinate `2`, so the query returns base `2`. Its top is `2 + 3 = 5`, and the reported maximum becomes `5`.
- The third footprint `[6, 6]` has base zero and top one. The global maximum remains `5`.

The result is `[2, 5, 5]`.

**Why the data structure stays correct**

Initially every coordinate has height zero, matching the empty plane.

Assume the tree represents the visible top surface after earlier squares. The range maximum query gives exactly the highest support under the next footprint. Adding the side length gives the correct top. Assigning that top across the footprint produces exactly the new visible surface, while coordinates outside remain unchanged.

Lazy propagation changes only when values are materialized, not their meaning. By induction, every later query and every appended global maximum is correct.

## Complexity detail

Let `N` be the number of squares and let `C = 10^9` be the fixed root-domain width.

A range query or range assignment descends through at most `O(\log C)` tree levels and visits a logarithmic number of component nodes. Each square performs one of each, so time is

$$
O(N\log C).
$$

Here `\log_2 C` is about `30`. Because `C` is a fixed constant in the implementation, this behaves linearly in `N`, but `O(N\log C)` most accurately describes the dynamic tree.

Nodes are allocated only on paths touched by operations. Across `N` intervals, at most `O(N\log C)` nodes are created in the conservative bound. Thus tree space is

$$
O(N\log C).
$$

With the source's fixed coordinate ceiling, the depth factor is bounded and this is often reported as `O(N)`. The answer list uses an additional `O(N)` space.

## Alternatives and edge cases

- **Coordinate compression plus array segment tree:** Collect every left endpoint and `left + size - 1`, map them to `O(N)` indices, and use a conventional lazy tree. This gives `O(N\log N)` time and `O(N)` space with less dependence on the numeric coordinate ceiling.

- **Quadratic simulation:** For each new square, compare it with every earlier square to find overlapping support. It is simpler and takes `O(N^2)` time, acceptable only for smaller inputs.

- **Touching side edges:** `r = l + w - 1` ensures adjacent intervals do not overlap merely because one geometric right edge equals another left edge.

- **Partial overlap:** Any positive horizontal intersection appears in both encoded ranges, so the later square uses the earlier top as possible support.

- **Bridging uneven stacks:** The query uses the maximum support, and the assignment makes the new top uniform across its full footprint.

- **Square landing on the ground:** An untouched interval queries as zero, so top height equals its side length.

- **Lazy tag value zero:** Zero means no pending assignment; valid square tops are always positive.

- **Assignment versus addition:** `modify` must assign the new top, not add it to every previous height. The square has one rigid landing height based on the maximum support.

- **Large sparse coordinates:** Dynamic allocation avoids memory proportional to `10^9`.

- **Query-created nodes:** `pushdown` may allocate children even during a read. This preserves correctness but contributes to the dynamic-node space bound.

- **Global maximum:** Returning each new `h` directly would be wrong when a later isolated square is shorter than an earlier stack; `mx` preserves the historical maximum.

- **Inclusive tree intervals:** All boundary comparisons in `modify` and `query` assume both endpoints are included.
