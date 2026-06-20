# Range Update with Lazy Propagation (Sum)

| | |
|---|---|
| **ID** | `segtree_05` |
| **Category** | segment_tree |
| **Complexity (required)** | $O(\log N)$ |
| **Difficulty** | 8/10 |
| **Interview relevance** | 5/10 |
| **Wikipedia** | [Segment tree (Lazy propagation)](https://en.wikipedia.org/wiki/Segment_tree) |

## Problem statement

Standard Segment Trees support $O(\log N)$ point updates. However, if you need to update an entire range of elements (e.g., "Add 5 to all elements from index L to R"), calling the point update function for every element takes $O((R - L + 1)$ log N) time, which degrades to $O(N \log N)$ worst-case!
Implement a **Range Update** mechanism that guarantees strict $O(\log N)$ time for massive continuous updates.

**Input:** Query bounds `l` and `r`, and a delta value `val` to add to the range.
**Output:** The Segment Tree modified in-place.

## When to use it

- The absolute pinnacle of mutable array management. You need this when an array undergoes massive block operations (adding values, setting values, flipping bits) alongside continuous range queries.

## Approach

**The Problem:**
If we add 5 to the range `[0, 1000]`, visiting all 1000 leaves to update them is too slow.

**The Solution: Lazy Propagation**
Instead of updating the leaves immediately, we stop at the highest possible nodes that completely cover the range, update their total sum directly, and leave a "post-it note" (a lazy value) on them saying: *"Hey, my children also need 5 added to them, but I'm too lazy to tell them right now."*
We only push these lazy updates down to the children when a future query or update actually needs to visit them!

1. Create a `lazy` array of the same size as the `tree` array, initialized to 0.
2. **Push Down:** Create a helper function that checks if a node `v` has a lazy value. If it does:
   - Add the lazy value to the actual sum of both children. (Wait, if a child covers 4 elements, adding 5 to the child means its total sum increases by 5 x 4 = 20. We must multiply by the segment length!).
   - Add the lazy value to the `lazy` tracking array of both children so they can pass it down later.
   - Clear the lazy value from `v`.
3. **Range Update:** Traverse the tree just like a Range Query.
   - *Crucial:* Always call **Push Down** before processing a node!
   - If Total Overlap: Update the current node's sum (`val * length`). Add `val` to this node's `lazy` tracker. Return! (Do not visit children!).
   - If Partial Overlap: Push down, recurse left and right, and update the current node from its children.
4. **Range Query:** Traverse the tree exactly as before, but ALWAYS call **Push Down** before processing a node!

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for segtree_05: Range Update with Lazy Propagation.

Build a sum-segment tree, then apply a sequence
"""


def solve(arr, n, range_updates, queries, q):
    """Sum-segment tree with lazy-propagation range updates."""
    if n == 0:
        return [0] * q
    tree = [0] * (4 * n)
    lazy = [0] * (4 * n)

    def build(node, lo, hi):
        if lo == hi:
            tree[node] = arr[lo]
            return
        mid = (lo + hi) // 2
        build(2 * node, lo, mid)
        build(2 * node + 1, mid + 1, hi)
        tree[node] = tree[2 * node] + tree[2 * node + 1]

    def apply(node, lo, hi, val):
        """Apply a pending update of `val` to this node."""
        tree[node] += val * (hi - lo + 1)
        lazy[node] += val

    def push(node, lo, hi):
        """Push pending lazy update down to children."""
        if lazy[node] != 0 and lo != hi:
            mid = (lo + hi) // 2
            apply(2 * node, lo, mid, lazy[node])
            apply(2 * node + 1, mid + 1, hi, lazy[node])
            lazy[node] = 0

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
        tree[node] = tree[2 * node] + tree[2 * node + 1]

    def query(node, lo, hi, l, r):
        if l > hi or r < lo:
            return 0
        if l <= lo and hi <= r:
            return tree[node]
        push(node, lo, hi)
        mid = (lo + hi) // 2
        return query(2 * node, lo, mid, l, r) + query(2 * node + 1, mid + 1, hi, l, r)

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

Array: `[0, 0, 0, 0]`.
`update_range(0, 3, addend=5)`:
- Root `v=1` covers `[0, 3]`. Total Overlap!
- `tree[1] += 5 * 4 = 20`.
- `lazy[1] += 5`.
- **Return instantly!** The children (`v=2, 3`) are untouched. $O(1)$ time spent!

`query(0, 1)`:
- Root `v=1` covers `[0, 3]`. Partial overlap.
- **Push Down!** `lazy[1]` is 5.
  - Left child `v=2` covers `[0, 1]`. `tree[2] += 5 * 2 = 10`. `lazy[2] = 5`.
  - Right child `v=3` covers `[2, 3]`. `tree[3] += 5 * 2 = 10`. `lazy[3] = 5`.
  - `lazy[1] = 0`.
- Recurse Left Branch `v=2` (`[0, 1]`):
  - Total Overlap! Return `tree[2]` (10).
- Recurse Right Branch `v=3` (`[2, 3]`):
  - No Overlap! Return 0.
- Result: `10 + 0 = 10`. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(1)$ | $O(\log N)$ |
| **Average** | $O(\log N)$ | $O(\log N)$ |
| **Worst** | $O(\log N)$ | $O(\log N)$ |

By returning immediately on Total Overlap, Range Updates take strictly $O(\log N)$ time, exactly matching the complexity of Range Queries!
Space complexity is $O(N)$ for the new `lazy` array.

## Variants & optimizations

- **Assignment Updates:** Instead of `+= delta`, you might need to strictly set `arr[L...R] = val`. The lazy propagation logic is identical, except when pushing down, you *overwrite* the child's lazy value instead of adding to it (`lazy[v*2] = lazy[v]`), and you *overwrite* the child's tree value (`tree[v*2] = lazy[v] * length`). You also need a special flag (like `lazy != None`) to distinguish between "Set to 0" and "No pending update".

## Real-world applications

- **Calendar Systems:** Booking a block of days sets the availability array `[start_date, end_date]` to `False` in $O(\log N)$ time.

## Related algorithms in cOde(n)

- **[segtree_06 - Range Min Lazy Update](segtree_06_range-min-with-lazy-updates.md)** — The exact same logic adapted for Minimum Segment Trees.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
