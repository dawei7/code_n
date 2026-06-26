# Point Update

| | |
|---|---|
| **ID** | `segtree_03` |
| **Category** | segment_tree |
| **Complexity (required)** | $O(\log N)$ |
| **Difficulty** | 4/10 |
| **Interview relevance** | 6/10 |
| **LeetCode Equivalent** | [Range Sum Query - Mutable](https://leetcode.com/problems/range-sum-query-mutable/) |

## Problem statement

Given a constructed Segment Tree, implement a function to update the value of a single element in the original array.
When an element `arr[pos]` is changed to `new_val`, the Segment Tree must be updated to reflect this change.
The update must execute in $O(\log N)$ time, updating only the specific tree nodes that contain the changed element.

**Input:** An integer `pos` (the index in the array) and an integer `new_val`.
**Output:** The Segment Tree modified in-place.

## When to use it

- This is the operation that makes Segment Trees (and Fenwick Trees) superior to standard Prefix Sum arrays. Prefix Sum arrays take $O(1)$ to query but $O(N)$ to update. Segment Trees take $O(\log N)$ to query and $O(\log N)$ to update, providing the perfect balance for mutable data.

## Approach

A point update is essentially a specialized traversal down to a single leaf.
When we update `arr[pos]`, we must update the leaf node responsible for `pos`. But we must also update every ancestor node all the way up to the root, because their aggregated values (e.g. sums) are now outdated!

**The Logic:**
1. Start at the root node `v=1` covering `[0, N-1]`.
2. Check if the current node is a leaf (`tl == tr`).
   - If it is, we have reached the exact node for `pos`! Update its value in `tree[v]` and return.
3. If it's not a leaf, calculate `tm = (tl + tr) // 2`.
4. Determine which child contains the index `pos`:
   - If `pos <= tm`, the target index lives in the left half. Recurse down the Left Child (`2*v`).
   - If `pos > tm`, the target index lives in the right half. Recurse down the Right Child (`2*v+1`).
5. **Backtracking (The Crucial Step):** As the recursion unwinds back up to the root, the current node `v` must re-calculate its value by merging its two children: `tree[v] = tree[v*2] + tree[v*2+1]`. Because one of the children just had its value changed, this ensures the change perfectly bubbles up to the root!

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for segtree_03: Point Update.

Apply point updates and return the resulting array.
"""


def solve(arr, n, updates, q):
    work = list(arr)
    for idx, val in updates:
        if 0 <= idx < n:
            work[idx] = val
    return work
```

</details>

## Walk-through

Array: `[1, 3, 5]`. N=3. Tree array (values): `[0, 9, 4, 5, 1, 3]`.
Update: `pos = 1` (the value `3`), `new_val = 10`.

`_update(v=1, tl=0, tr=2, pos=1, val=10)`
- `tm = 1`. `pos (1) <= tm (1)`. Go Left!

`_update(v=2, tl=0, tr=1, pos=1, val=10)`
- `tm = 0`. `pos (1) > tm (0)`. Go Right!

`_update(v=5, tl=1, tr=1, pos=1, val=10)`
- `tl == tr`! Leaf node reached.
- `tree[5] = 10`. Return.

**Unwind back to `v=2`:**
- `tree[2] = tree[4] + tree[5]`
- `tree[2] = 1 + 10 = 11`. (Updated from 4 to 11!). Return.

**Unwind back to `v=1`:**
- `tree[1] = tree[2] + tree[3]`
- `tree[1] = 11 + 5 = 16`. (Updated from 9 to 16!). Return.

Update complete! The path from the leaf to the root was updated in 3 steps. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(\log N)$ | $O(\log N)$ |
| **Average** | $O(\log N)$ | $O(\log N)$ |
| **Worst** | $O(\log N)$ | $O(\log N)$ |

The height of a perfectly balanced binary tree for N elements is strictly \lceil log_2 N \rceil. We only visit one node per level on the way down, and update one node per level on the way back up. Thus, time complexity is $O(\log N)$.
Space complexity is $O(\log N)$ for the recursive call stack.

## Variants & optimizations

- **Delta Updates:** Instead of passing `new_val`, sometimes updates are of the form `arr[pos] += delta`. In this case, you just add `delta` to `tree[v]` at every step on the way down, entirely skipping the need to merge the children on the way back up! `tree[v] += delta`.
- **Iterative Update:** In a bottom-up segment tree, the leaf node is at index `p = pos + N`. You update `tree[p] = new_val`. Then you just use a `while p > 1: p //= 2; tree[p] = tree[2*p] + tree[2*p+1]` loop to blast up to the root in 3 lines of code!

## Real-world applications

- **Leaderboards:** When a player's score changes (Point Update), the global ranking thresholds and sum totals (Range Queries) need to update instantly without freezing the game servers.

## Related algorithms in cOde(n)

- **[fenwick_03 - Point Update](../fenwick/fenwick_03_update.md)** — A much lighter and faster $O(\log N)$ update, though restricted strictly to reversible operations (like Sum/XOR) unlike Segment Trees.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
