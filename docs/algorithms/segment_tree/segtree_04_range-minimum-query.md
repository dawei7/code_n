# Range Minimum Query

| | |
|---|---|
| **ID** | `segtree_04` |
| **Category** | segment_tree |
| **Complexity (required)** | $O(\log N)$ |
| **Difficulty** | 5/10 |
| **Interview relevance** | 5/10 |
| **LeetCode Equivalent** | N/A (Standard Data Structure Query) |

## Problem statement

Given a Segment Tree constructed for a specific array `arr`, execute a **Range Minimum Query (RMQ)**.
Find the minimum element in `arr` between indices `left` and `right` inclusive: `min(arr[left...right])`.
You must return the answer in strictly $O(\log N)$ time.

**Input:** Two integers `l` and `r` representing the query boundaries.
**Output:** An integer representing the minimum value in that sub-segment.

## When to use it

- This highlights the biggest advantage of Segment Trees over Fenwick Trees. Fenwick trees rely on mathematical inverses (e.g., A - B). The `min()` function has no mathematical inverse! Therefore, Fenwick Trees CANNOT do Range Minimum Queries. Segment Trees can!

## Approach

The traversal logic is absolutely identical to the Range Sum Query (`segtree_02`).
The only things that change are the **Merge Operation** and the **Identity Value**.

1. **Identity Value:** When a query hits a "No Overlap" node (the node is completely outside the query range), it must return a value that will *not affect* the final mathematical result.
   - For Sum, the identity is `0` (because X + 0 = X).
   - For Minimum, the identity is `Infinity` (because \min(X, \infty) = X).
2. **Merge Operation:** When a node splits a query to its left and right children, it must combine their answers.
   - For Sum, we use `+`.
   - For Minimum, we use `min()`.

*(Note: The internal `tree` array must also have been constructed using `min(left, right)` during the `_build` phase!)*

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for segtree_04: Range Minimum Query.

Build a min-segment tree on arr (each node stores
"""


def solve(arr, n, queries, q):
    """Range Minimum Query via segment tree."""
    if n == 0:
        return [0] * q
    tree = [0] * (4 * n)

    def build(node, lo, hi):
        if lo == hi:
            tree[node] = arr[lo]
        else:
            mid = (lo + hi) // 2
            build(2 * node, lo, mid)
            build(2 * node + 1, mid + 1, hi)
            tree[node] = min(tree[2 * node], tree[2 * node + 1])

    def query(node, lo, hi, l, r):
        if l > hi or r < lo:
            return float("inf")
        if l <= lo and hi <= r:
            return tree[node]
        mid = (lo + hi) // 2
        return min(query(2 * node, lo, mid, l, r),
                   query(2 * node + 1, mid + 1, hi, l, r))

    build(1, 0, n - 1)
    out = []
    for l, r in queries:
        out.append(query(1, 0, n - 1, l, r))
    return out
```

</details>

## Walk-through

Array: `[8, 2, 5, 1, 9]`. N=5.
Query: `[0, 2]`. (We expect the answer to be `min(8, 2, 5) = 2`).

Assume tree covers `[0, 4]`.
`_query(v=1, tl=0, tr=4, l=0, r=2)` -> Partial. Mid=2.
- **Left Branch (`[0, 2]`):** `_query(v=2, tl=0, tr=2, l=0, r=2)`
  - Total Overlap! `l(0) <= tl(0)` and `tr(2) <= r(2)`.
  - Returns `tree[2]`. (The precalculated minimum of `[8, 2, 5]` is `2`).
- **Right Branch (`[3, 4]`):** `_query(v=3, tl=3, tr=4, l=0, r=2)`
  - No Overlap! `tl(3) > r(2)`.
  - Returns `Infinity`.

Combine: `min(2, Infinity) = 2`.
Result: 2. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(1)$ | $O(\log N)$ |
| **Average** | $O(\log N)$ | $O(\log N)$ |
| **Worst** | $O(\log N)$ | $O(\log N)$ |

Traversal trims at boundaries, limiting max node visits per level to 4. Max depth is log N. Time complexity is strictly $O(\log N)$.
Space complexity is $O(\log N)$ for the recursive call stack.

## Variants & optimizations

- **Sparse Table:** If the array is *immutable* (no point updates will ever happen), RMQ can be solved in $O(N \log N)$ preprocessing time and strictly $O(1)$ query time using a Sparse Table! A Sparse Table stores the minimum of every range of length 2^k. To query an arbitrary range, you overlap two blocks of length 2^k that cover the range.
- **RMQ in $O(N)$ Space / $O(1)$ Query:** It is theoretically possible to do RMQ in $O(1)$ time with $O(N)$ preprocessing by reducing the problem to Lowest Common Ancestor (LCA) via a Cartesian Tree, and then reducing LCA back to a restricted RMQ using Farach-Colton and Bender algorithm. It is obscenely complex and never expected in an interview.

## Real-world applications

- **Lowest Common Ancestor (LCA):** As mentioned above, finding the lowest common ancestor in any tree can be mapped to a 1D array via an Euler Tour, turning the tree problem into a standard Range Minimum Query on the array!

## Related algorithms in cOde(n)

- **[segtree_02 - Range Sum Query](segtree_02_range-sum-query.md)** — The foundational pattern using Sum.
- **[segtree_05 - Lazy Propagation](segtree_05_range-update-with-lazy-propagation.md)** — How to do massive range updates on these trees.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
