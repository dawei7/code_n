# Build Segment Tree

| | |
|---|---|
| **ID** | `segtree_01` |
| **Category** | segment_tree |
| **Complexity (required)** | $O(N)$ |
| **Difficulty** | 5/10 |
| **Interview relevance** | 6/10 |
| **Wikipedia** | [Segment tree](https://en.wikipedia.org/wiki/Segment_tree) |

## Problem statement

Given an array `arr` of size N, construct a **Segment Tree** to allow for fast $O(\log N)$ range queries (like sum, minimum, or maximum over a subarray) and $O(\log N)$ point updates.
You must implement the `build()` function that initializes the internal tree array from the original input array in $O(N)$ time.

**Input:** An integer array `arr`.
**Output:** An internal array `tree` representing the constructed Segment Tree.

## When to use it

- Segment Trees are the undisputed king of mutable range queries.
- Use it when you have an array that undergoes frequent **updates** and you simultaneously need to answer frequent **range queries** (e.g., "What is the sum from index L to R?").
- (If the array is *immutable*, Prefix Sum arrays or Sparse Tables are better. If you only need Point-Updates and Sum-Queries, Fenwick Trees are easier to write. Segment Trees can do *everything*).

## Approach

A Segment Tree is a perfectly balanced binary tree.
- The **root** node represents the entire array `arr[0...N-1]`.
- Each internal node represents the merged result of its two children.
- The **left child** represents the first half: `arr[0...mid]`.
- The **right child** represents the second half: `arr[mid+1...N-1]`.
- The **leaf nodes** represent the individual elements of the array: `arr[i]`.

**Array Representation:**
Instead of creating `Node` objects with pointers, we map the binary tree perfectly into a 1D array (just like a Binary Heap)!
- The root is at index `1` (1-indexed for easier math).
- The left child of node `v` is at index `2 * v`.
- The right child of node `v` is at index `2 * v + 1`.
- To safely hold a tree of N leaves, the tree array must be sized `4 * N`.

**Building (Post-Order Traversal):**
We use a Divide and Conquer recursion.
1. Start at the root (`v=1`) covering `[0, N-1]`.
2. Find the `mid`.
3. Recursively build the left child (`2*v`) covering `[0, mid]`.
4. Recursively build the right child (`2*v+1`) covering `[mid+1, N-1]`.
5. Once the children are built, the current node `v` simply merges their answers (e.g., `tree[v] = tree[2*v] + tree[2*v+1]`).
6. Base Case: If `left == right`, we are at a leaf. Just set `tree[v] = arr[left]`.

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for segtree_01: Build Segment Tree.

Build a sum-segment tree bottom-up and return as a flat list.
"""


def solve(arr, n):
    if n == 0:
        return []
    tree = [0] * (4 * n)

    def build(node, lo, hi):
        if lo == hi:
            tree[node] = arr[lo]
        else:
            mid = (lo + hi) // 2
            build(2 * node, lo, mid)
            build(2 * node + 1, mid + 1, hi)
            tree[node] = tree[2 * node] + tree[2 * node + 1]

    build(1, 0, n - 1)
    return tree
```

</details>

## Walk-through

`arr = [1, 3, 5]`. N=3. Tree size = 12.
Root `v=1` covers `[0, 2]`. `mid = 1`.

- **Left branch `v=2` covers `[0, 1]`. `mid = 0`.**
  - Left branch `v=4` covers `[0, 0]`. Leaf! `tree[4] = arr[0] = 1`.
  - Right branch `v=5` covers `[1, 1]`. Leaf! `tree[5] = arr[1] = 3`.
  - Merge `v=2`: `tree[2] = tree[4] + tree[5] = 1 + 3 = 4`.

- **Right branch `v=3` covers `[2, 2]`.**
  - Leaf! `tree[3] = arr[2] = 5`.

- **Merge Root `v=1`:**
  - `tree[1] = tree[2] + tree[3] = 4 + 5 = 9`.

Final Tree array (ignoring unused trailing zeros):
`[0, 9, 4, 5, 1, 3, 0, ...]`
*(Index 0 is unused. Root is 9. Its children are 4 and 5. Children of 4 are 1 and 3).* ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(N)$ | $O(N)$ |
| **Average** | $O(N)$ | $O(N)$ |
| **Worst** | $O(N)$ | $O(N)$ |

The recursion visits every node in the tree exactly once. A perfectly balanced binary tree with N leaves has 2N - 1 total nodes. Thus, the build time is strictly $O(N)$.
Space complexity is $O(N)$ because we allocate an array of size 4N.

## Variants & optimizations

- **Iterative Segment Tree:** It is possible to build and query Segment Trees iteratively from the bottom-up! Instead of starting at v=1, you start placing the leaves from index N to 2N-1, and then loop backwards from N-1 down to 1, doing `tree[i] = tree[2*i] + tree[2*i+1]`. This takes exactly 2N space and avoids all recursion overhead! It is heavily favored in competitive programming for its raw speed.

## Real-world applications

- **Database Indexes:** Used conceptually in hierarchical database architectures for fast multi-dimensional spatial queries.

## Related algorithms in cOde(n)

- **[segtree_02 - Range Sum Query](segtree_02_range-sum-query.md)** — The query operation that utilizes this built tree.
- **[fenwick_01 - Build Fenwick Tree](../fenwick/fenwick_01_build.md)** — A simpler, non-recursive alternative for specific types of range queries.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
