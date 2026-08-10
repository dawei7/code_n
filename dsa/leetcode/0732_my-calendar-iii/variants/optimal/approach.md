## General

**Turn each booking into a range increment**

After every new event, the calendar must report the greatest number of simultaneously active events anywhere on the timeline. Booking `[start, end)` increases the overlap count by one at every time inside that interval.

This is a repeated range-add and global-maximum problem. The endpoint domain extends to `10^9`, so allocating one array entry per time coordinate is impossible. The exact solution uses a dynamic segment tree: it creates only nodes reached by actual updates, while conceptually covering the complete domain.

**Map half-open time intervals to inclusive tree cells**

Each segment-tree node represents an inclusive integer range. The root covers `[1, 10^9 + 1]`. A booking `[start, end)` is updated as the inclusive integer range

`[start + 1, end]`.

One way to understand this shift is to let tree cell `x` represent the elementary time segment `[x - 1, x)`. Then the cells covered by `[start, end)` are exactly `start + 1` through `end`.

This mapping preserves touching boundaries. `[10, 20)` updates cells 11 through 20, while `[20, 30)` updates cells 21 through 30. They share no cell and therefore do not falsely overlap.

**Information stored in a node**

For node interval `[l, r]`:

- `v` is the maximum overlap count anywhere in that interval after all applied updates.
- `add` is a lazy increment known to apply uniformly to the whole interval but not necessarily pushed into descendants.
- `left` and `right` are child nodes, created only when partial updates require descending.
- `mid` splits the inclusive range into `[l, mid]` and `[mid + 1, r]`.

Dynamic construction avoids materializing the enormous complete tree. A path has only logarithmic depth because each level approximately halves the coordinate range.

**Apply a fully covered update lazily**

When the current node’s interval lies completely inside the update range, every point represented by the node gains the same value `v`, here one. The method increments both `node.v` and `node.add` and stops descending.

Updating `v` keeps the node’s maximum immediately correct. Updating `add` remembers that descendants must inherit the increment if a later partial operation needs them. This is the purpose of lazy propagation.

**Descend only for partial coverage**

If the node is only partly covered, `pushdown` first ensures both children exist. If the parent has a pending `add`, that amount is added to each child’s `v` and `add`, then cleared from the parent.

The update recurses into the left child only when `l <= node.mid` and into the right child only when `r > node.mid`. These comparisons select exactly the child ranges intersected by the requested inclusive interval.

After updating the relevant children, `pushup` sets the parent maximum to

`max(node.left.v, node.right.v)`.

The parent’s pending add has already been pushed before descent, so the children’s values now include all contributions and their maximum is the correct parent value.

**Why both children may be created**

During `pushdown`, the code creates a missing left and right child even if the current update will recurse into only one. The untouched child is still needed by `pushup`, which compares both child maxima. Its initial zero value, plus any propagated parent lazy amount, accurately represents its unmodified half.

The tree remains dynamic because children are created only along nodes reached by partial updates, not for the entire coordinate domain.

**Return the global maximum**

After `modify(start + 1, end, 1)`, the root’s `v` is the maximum overlap across its complete domain. The exact source obtains it through

`query(1, 10^9 + 1)`.

That query fully covers the root, so it immediately returns `root.v`. No traversal is needed. The returned value is the largest `k` for which some time segment is covered by `k` bookings.

**Trace touching and overlapping events**

After booking `[10, 20)`, cells 11 through 20 have value one, so the root maximum is one.

Booking `[20, 30)` increments cells 21 through 30. The two updated ranges are disjoint, and the maximum remains one.

Booking `[15, 25)` increments cells 16 through 25. Cells 16 through 20 overlap the first booking, and cells 21 through 25 overlap the second, so those cells reach two. The root maximum becomes two.

The cell mapping exactly mirrors nonempty intersections of the original half-open intervals.

**Why lazy propagation is correct**

For a fully covered node, adding one uniformly raises both every point in that interval and its maximum by one, so recording the increment in `v` and `add` is exact. Before a later partial descent, `pushdown` transfers every deferred uniform increment to both halves, preserving their point values. After recursive changes, `pushup` recomputes the maximum from the two exhaustive child ranges.

By induction over tree operations, every node’s `v` remains the true maximum over its represented interval. The root represents the entire possible timeline, so its maximum after each update is exactly the requested maximum simultaneous booking count.

## Complexity detail

Let `C` be the size of the coordinate domain, approximately `10^9`, and let `q` be the number of calls.

The tree depth is `O(log C)`. A contiguous range update with lazy propagation visits only nodes along the two boundary paths plus fully covered nodes between them, for `O(log C)` work. The full-domain query returns at the root in `O(1)` time. One booking therefore costs `O(log C)` time, and `q` bookings cost `O(q log C)`.

The dynamic tree creates `O(log C)` nodes per update in the worst case. Across `q` calls it uses `O(q log C)` space. The theoretical complete tree over all coordinates is never allocated.

Python recursion depth is safe here because the domain depth is only about 30 levels, not proportional to the number of bookings.

## Alternatives and edge cases

- **Sweep-line difference map:** Add one at each start and minus one at each end, then scan sorted deltas to find the largest prefix sum. It is much simpler, but rescanning all endpoints makes one call linear in accumulated coordinates and all calls quadratic.

- **Coordinate compression with a static segment tree:** If all bookings were known in advance, collect and sort endpoints, then build a tree over compressed segments. The online class receives calls incrementally, so future endpoints are not initially available.

- **Balanced disjoint interval map:** Split stored constant-coverage intervals at new endpoints, increment covered pieces, and maintain a maximum. It can be practical but may touch linearly many pieces in one call.

- **Allocate an array through `10^9`:** This is infeasible in both memory and initialization time. Dynamic nodes make cost depend on requests rather than coordinate magnitude.

- **Forget the half-open conversion:** Updating `[start, end]` directly would make two events touching at `end == next_start` share a tree point incorrectly. The shifted `[start + 1, end]` representation avoids that error.

- **Full node coverage:** Incrementing both `v` and `add` without descending is safe because every point in that node’s interval changes equally.

- **Partial update after lazy updates:** `pushdown` must transfer the parent’s pending amount before child recursion; otherwise child maxima would omit earlier full-cover bookings.

- **Repeated identical intervals:** Each update increments the same tree cells. The root maximum rises by one on every call, which is exactly the growing k-booking.

- **Disjoint intervals:** Their tree ranges do not share cells, so the global maximum need not increase after the first booking.

- **Boundary endpoints zero and `10^9`:** The shift maps `[0, 10^9)` to `[1, 10^9]`, safely inside the root’s inclusive range.
