# Range Minimum Query with Lazy Updates

| | |
|---|---|
| **ID** | `segtree_06` |
| **Category** | segment_tree |
| **Complexity (required)** | $O(\log N)$ |
| **Difficulty** | 7/10 |
| **Interview relevance** | 4/10 |
| **LeetCode Equivalent** | [Falling Squares](https://leetcode.com/problems/falling-squares/) |

## Problem statement

Adapt the Lazy Propagation technique to a **Range Minimum Query** Segment Tree.
Support two operations:
1. `add_range(l, r, val)`: Add `val` to all elements in `arr[l...r]`.
2. `query_min(l, r)`: Find the minimum element in `arr[l...r]`.
Both operations must run in strict $O(\log N)$ time.

**Input:** An sequence of range addition and range query operations.
**Output:** The results of the range queries.

## When to use it

- To understand the nuanced differences in how Lazy Propagation affects different aggregation functions. Sum trees multiply the lazy value by the segment length. Min/Max trees *do not*!

## Approach

The core structure is identical to `segtree_05`. We need a `tree` array to store minimums, and a `lazy` array to store pending additions.

**The Crucial Difference (Pushing Down):**
If a node represents the segment `[0, 1000]`, and its current minimum is `15`.
If we add `5` to every single element in this segment, what happens to the minimum?
Every element increases by 5. Therefore, the minimum element *also* increases by exactly 5! It becomes `20`.
Unlike the Sum Segment Tree, **we DO NOT multiply the lazy value by the segment length!** The minimum value shifts by the exact same `delta` as the elements themselves!

This makes Lazy Propagation for Min/Max trees actually *easier* to write than for Sum trees, because you don't even need to calculate or pass down the segment lengths (`tm - tl + 1`) during the `_push` operation!

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for segtree_06: Range Min with Lazy Updates.

Build a min-segment tree on arr. Apply a sequence
"""


def solve(arr, n, range_updates, queries, q):
    """Min-segment tree with lazy-assignment range updates."""
    if n == 0:
        return [0] * q
    INF_VAL = 10**9
    tree = [INF_VAL] * (4 * n)
    lazy = [None] * (4 * n)   # None = no pending assignment.

    def build(node, lo, hi):
        if lo == hi:
            tree[node] = arr[lo]
            return
        mid = (lo + hi) // 2
        build(2 * node, lo, mid)
        build(2 * node + 1, mid + 1, hi)
        tree[node] = min(tree[2 * node], tree[2 * node + 1])

    def apply(node, lo, hi, val):
        """Apply a pending assignment of `val` to this node."""
        tree[node] = val
        lazy[node] = val

    def push(node, lo, hi):
        """Push pending assignment down to children."""
        if lazy[node] is not None and lo != hi:
            mid = (lo + hi) // 2
            apply(2 * node, lo, mid, lazy[node])
            apply(2 * node + 1, mid + 1, hi, lazy[node])
            lazy[node] = None

    def update(node, lo, hi, l, r, val):
        if l > hi or r < lo:
            return
        if l <= lo and hi <= r:
            apply(node, lo, hi, val)
            return
        push(node, lo, hi)
        mid = (lo + hi) // 2
        update(2 * node, lo, mid, l, r, val)
        update(2 * node + 1, mid + 1, hi, l, r, val)
        tree[node] = min(tree[2 * node], tree[2 * node + 1])

    def query(node, lo, hi, l, r):
        if l > hi or r < lo:
            return INF_VAL
        if l <= lo and hi <= r:
            return tree[node]
        push(node, lo, hi)
        mid = (lo + hi) // 2
        return min(query(2 * node, lo, mid, l, r),
                   query(2 * node + 1, mid + 1, hi, l, r))

    build(1, 0, n - 1)
    for l, r, val in range_updates:
        update(1, 0, n - 1, l, r, val)
    out = []
    for l, r in queries:
        out.append(query(1, 0, n - 1, l, r))
    return out
```

</details>

## Walk-through

Array: `[10, 20, 30]`. Tree covers `[0, 2]`. Root minimum is `10`.
`update_range(0, 2, addend=5)`:
- Root `v=1` covers `[0, 2]`. Total Overlap!
- `tree[1] += 5`. (Minimum is now 15).
- `lazy[1] += 5`.
- Return instantly.

`query_min(1, 2)`:
- Root `v=1`. Partial overlap.
- **Push Down!** `lazy[1]` is 5.
  - Left child (covers `[0, 1]`, old min `10`): `tree[2] += 5 = 15`. `lazy[2] = 5`.
  - Right child (covers `[2, 2]`, old min `30`): `tree[3] += 5 = 35`. `lazy[3] = 5`.
  - `lazy[1] = 0`.
- Recurse Left `[0, 1]`: Partial overlap.
  - **Push Down!** `lazy[2]` is 5.
    - Leaf `0` (val `10`): `tree[4] += 5 = 15`.
    - Leaf `1` (val `20`): `tree[5] += 5 = 25`.
  - ... Ultimately returns `tree[5] = 25`.
- Recurse Right `[2, 2]`: Total overlap.
  - Returns `tree[3] = 35`.
- Merge: `min(25, 35) = 25`. ✓

*(Array is conceptually `[15, 25, 35]`. Min of indices 1 and 2 is indeed 25).*

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(1)$ | $O(N)$ |
| **Average** | $O(\log N)$ | $O(N)$ |
| **Worst** | $O(\log N)$ | $O(N)$ |

Strict $O(\log N)$ for both queries and range updates.

## Variants & optimizations

- **Assignment Updates (Set Range):** If the update is `set_range(l, r, val)`, then `tree[v]` simply becomes `val` (because the minimum of an array where every element is identical is just that element itself!).

## Real-world applications

- **Resource Allocation:** Managing a timeline of available CPU cores. When scheduling a job that takes C cores from time T_1 to T_2, you do a range subtraction. A query for the maximum available cores in a timeframe is a Range Maximum Query.

## Related algorithms in cOde(n)

- **[segtree_05 - Lazy Propagation Sum](segtree_05_range-update-with-lazy-propagation.md)** — Explains the core philosophy of lazy tracking.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
