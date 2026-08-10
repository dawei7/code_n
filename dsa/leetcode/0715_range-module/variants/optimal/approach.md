## General

The module tracks real-number half-open ranges `[left, right)` over a huge coordinate domain. Three operations must:

- mark every point in a range as tracked;
- mark every point as untracked;
- report whether every point in a range is tracked.

The exact solution uses an implicit lazy segment tree over integer coordinates `1` through `10^9`. Because all endpoints are integers, half-open `[left,right)` is represented by the inclusive integer interval `[left,right-1]`.

**Meaning of a node**

Each node represents one inclusive coordinate segment determined by recursive parameters `l,r`.

`node.v` is true exactly when the entire represented segment is tracked. A false value means at least one point is untracked; it may mean the whole segment is untracked or the segment is mixed.

`node.add` is a lazy assignment tag:

- `1` means the whole segment is tracked;
- `-1` means the whole segment is untracked;
- `0` means no uniform assignment is waiting to be propagated.

Children are created only when a partial operation needs them.

**Initial state**

The root is false with no children and no lazy tag. This represents an entirely untracked domain.

Not allocating all coordinates is essential: the domain has one billion positions, while at most ten thousand operations occur.

**Full-cover modification**

If a node's segment lies completely within the update interval, the method does not descend.

For an add update, it sets `add = 1` and `v = True`. For removal, it sets `add = -1` and `v = False`.

This assignment overwrites any earlier state throughout the covered segment, exactly matching range add/remove semantics.

**Partial modification and pushdown**

Before descending into part of a node, `pushdown` ensures both children exist.

If the parent has a nonzero lazy tag, both children inherit that tag and corresponding Boolean coverage, then the parent tag is cleared. This materializes the uniform parent state before one child is changed.

The midpoint divides `[l,r]` into `[l,mid]` and `[mid+1,r]`. Recursion visits only children intersecting the requested update.

Afterward, `pushup` recomputes the parent:

`node.v = left.v and right.v`.

The parent is fully covered only when both halves are fully covered.

**Querying complete coverage**

If the current node lies fully inside the query, `node.v` directly answers whether every point of that component is tracked.

For a partial query, pushdown establishes correct child states. The local result starts as true, the identity for logical AND. It is combined with every intersected child query.

This differs from a range-maximum tree, which combines with max. The question asks whether all points are covered, so one false child must make the answer false.

**Half-open conversion**

Public calls translate:

`[left,right) -> [left,right-1]`.

This preserves adjacency correctly. Adding `[10,20)` tracks integer positions ten through nineteen. Querying `[20,25)` does not overlap it merely at boundary twenty.

The source guarantees `left < right`, so `right-1 >= left` and the inclusive interval is nonempty.

**A trace**

- `addRange(10,20)` assigns true over `[10,19]`.
- `removeRange(14,16)` assigns false over `[14,15]`, splitting the logical coverage.
- `queryRange(10,14)` asks `[10,13]` and returns true.
- `queryRange(13,15)` includes untracked point fourteen and returns false.
- `queryRange(16,17)` lies in the still-covered right portion and returns true.

Lazy nodes may represent these regions at different tree depths, but their Boolean meaning is exact.

**Why query may allocate nodes**

A partial query calls `pushdown`, which creates missing children even though no coverage is changing. These children inherit a uniform tag when one exists or default to false otherwise.

This simplifies logic but means reads can contribute to memory growth.


For every materialized node, `v` correctly states complete coverage of its segment, and a nonzero `add` correctly states a uniform assignment for that segment not yet expanded to descendants.

Full updates establish the invariant directly. Pushdown preserves the represented pointwise state while moving a tag to children. Partial updates modify exactly intersecting halves, and pushup restores the parent's AND summary. Queries combine complete-coverage answers with AND.

By induction over operations, public query results are true exactly when the entire requested half-open range is tracked.

## Complexity detail

Let `C = 10^9` be the coordinate-domain width and `q` the number of operations.

The tree depth is `O(\log C)`, about thirty. A range assignment or range query decomposes its interval into `O(\log C)` boundary/component nodes, giving

$$
O(\log C)
$$

time per operation and `O(q\log C)` total time.

Dynamic child creation can allocate `O(\log C)` nodes per operation in the conservative bound, including partial queries. Total persistent space is

$$
O(q\log C).
$$

Because `C` is fixed by the contract, these factors are small constants in practice.

## Alternatives and edge cases

- **Sorted disjoint intervals:** Maintain merged half-open intervals. Queries can be logarithmic, while additions/removals may touch many stored intervals.

- **Coordinate compression:** It is difficult online because future endpoints are unknown, but possible offline when all operations are available first.

- **Adjacent ranges:** Half-open ranges `[a,b)` and `[b,c)` touch without overlapping but together fully cover `[a,c)` after both are added.

- **Remove an untracked range:** Assigning false again is harmless.

- **Add an already tracked range:** Assigning true again preserves coverage.

- **Mixed node:** `v = False` alone does not mean every point is false; child information distinguishes mixed coverage.

- **Lazy tag sign:** `1` and `-1` encode assignments, while zero means no pending assignment.

- **Query combination:** Logical AND is required because every requested point must be tracked.

- **Domain boundaries:** The recursive root includes both one and one billion; public right endpoints are converted before use.

- **Query-created storage:** Read-only operations may allocate due to unconditional pushdown on partial overlap.

- **No empty public interval:** `left < right` prevents invalid `[left,right-1]` ranges.
