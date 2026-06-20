# Range Sum Query

| | |
|---|---|
| **ID** | `segtree_02` |
| **Category** | segment_tree |
| **Complexity (required)** | $O(\log N)$ |
| **Difficulty** | 5/10 |
| **Interview relevance** | 6/10 |
| **LeetCode Equivalent** | [Range Sum Query - Mutable](https://leetcode.com/problems/range-sum-query-mutable/) |

## Problem statement

Given a Segment Tree constructed for a specific array `arr`, execute a range sum query.
Calculate the sum of the elements of `arr` between indices `left` and `right` inclusive: `sum(arr[left...right])`.
You must return the answer in strictly $O(\log N)$ time by traversing the pre-built Segment Tree.

**Input:** Two integers `l` and `r` representing the query boundaries.
**Output:** An integer representing the sum.

## When to use it

- When you need to extract aggregated data (sum, min, max, XOR) from an arbitrary sub-segment of a massive array, and that array might change in the future.

## Approach

A node in a Segment Tree is responsible for a specific segment `[tl, tr]` (tree left, tree right).
When we query for a range `[l, r]`, we start at the root node (which covers `[0, N-1]`) and recursively traverse down the tree.

At any node `v` covering `[tl, tr]`, there are three possibilities:
1. **No Overlap:** The node's segment `[tl, tr]` is completely *outside* the query range `[l, r]`.
   - Action: This node is useless. Return `0` (the identity value for Sum).
2. **Total Overlap:** The node's segment `[tl, tr]` is completely *inside* the query range `[l, r]`!
   - Action: This node's pre-calculated answer is perfectly relevant! We do not need to traverse any deeper. Instantly return `tree[v]`. This is where the massive $O(\log N)$ speedup comes from!
3. **Partial Overlap:** The node's segment overlaps the query range, but isn't completely inside it.
   - Action: We must split the query and ask both children!
   - Recurse Left Child (`2*v`) covering `[tl, tm]`.
   - Recurse Right Child (`2*v+1`) covering `[tm+1, tr]`.
   - Return the sum of both recursive calls.

*(Note: When recursing down, we usually just pass `l` and `r` unchanged, or mathematically clamp them using `min`/`max`. The easiest way is to pass `l` and `r` unchanged and rely on the "No Overlap" base case to kill out-of-bounds queries!).*

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for segtree_02: Range Sum Query.

Build a segment tree, then for each (l, r) return the
range sum. O(log n) per query.
"""


def solve(arr, n, queries, q):
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
            tree[node] = tree[2 * node] + tree[2 * node + 1]

    def query(node, lo, hi, l, r):
        if l > hi or r < lo:
            return 0
        if l <= lo and hi <= r:
            return tree[node]
        mid = (lo + hi) // 2
        return query(2 * node, lo, mid, l, r) + query(2 * node + 1, mid + 1, hi, l, r)

    build(1, 0, n - 1)
    out = []
    for l, r in queries:
        out.append(query(1, 0, n - 1, l, r))
    return out
```

</details>

## Walk-through

Array: `[1, 3, 5]`. N=3. Tree covers `[0, 2]`.
Query: `[0, 1]`.

`_sum(v=1, tl=0, tr=2, l=0, r=1)`
- `[0, 2]` is not entirely inside `[0, 1]`. Partial Overlap!
- `tm = 1`. Recurse left and right.

**Left Branch:** `_sum(v=2, tl=0, tr=1, l=0, r=1)`
- `[0, 1]` IS entirely inside `[0, 1]`. Total Overlap!
- Return `tree[2]`. (We know from `segtree_01` that `tree[2]` stores `1 + 3 = 4`).

**Right Branch:** `_sum(v=3, tl=2, tr=2, l=0, r=1)`
- `l (0) > tr (2)` is False. `r (1) < tl (2)` is TRUE!
- No Overlap! Return `0`.

Combine: `sum_left (4) + sum_right (0) = 4`.
Result: 4. ✓ *(Correct, 1 + 3 = 4).*

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(1)$ | $O(\log N)$ |
| **Average** | $O(\log N)$ | $O(\log N)$ |
| **Worst** | $O(\log N)$ | $O(\log N)$ |

Because we stop recursing the absolute instant a node is completely inside the query range, we never visit more than 4 nodes per depth level. The depth of the tree is log N. Thus, the time complexity is strictly bounded to $O(\log N)$.
Space complexity is $O(\log N)$ for the recursive call stack.

## Variants & optimizations

- **Clamping the query range:** Some implementations prefer to clamp `l` and `r` when passing them to the children: `_sum(v*2, tl, tm, l, min(r, tm))`. This prevents passing invalid boundaries like `l > r` entirely, avoiding the need for the `l > tr` check. Both approaches are functionally identical and $O(\log N)$.
- **Iterative Query:** If the tree was built bottom-up iteratively, you can query from the leaves UP to the root in exactly a `while l <= r:` loop, which is much faster practically.

## Real-world applications

- **Financial Ledger:** Summing the total volume of trades that occurred between timestamp T_1 and T_2 in a live database where new trades are constantly updating historical aggregations.

## Related algorithms in cOde(n)

- **[segtree_04 - Range Minimum Query](segtree_04_range-minimum-query.md)** — The exact same traversal logic, just changing `+` to `min()`.
- **[fenwick_02 - Query](../fenwick/fenwick_02_query.md)** — Fenwick tree achieves this same $O(\log N)$ query using a much simpler loop.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
