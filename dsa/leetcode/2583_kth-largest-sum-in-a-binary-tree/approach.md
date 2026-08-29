## General

**Breadth-first search isolates tree levels**

Nodes belong to the same level when they have equal distance from the root. A queue naturally processes them in increasing distance order.

The queue begins with only `root`. At the start of each outer iteration, every node currently in `q` belongs to one level and no node from the next level has yet been processed. The code saves `len(q)` as the loop count.

During those iterations, it removes each current-level node, adds its value to `t`, and appends its existing children. Those children enter the back of the queue but are not processed by the current fixed-count loop. After the loop, `t` is exactly one level sum, and the queue contains exactly the next level.

**Why snapshotting the queue length matters**

If the code looped until the queue became empty inside one level, newly appended children would be consumed immediately and sums from several depths would mix. Taking `len(q)` once creates a boundary between the current level and its children.

The variable named `root` is reused for each popped node. This shadows the original root reference but does not harm traversal because all future work is already represented in the queue.

**Collect every level sum**

After each level, `arr.append(t)` stores its sum. When the outer queue becomes empty, every node has been visited exactly once and `arr` contains one value per tree level in top-to-bottom order.

The answer depends only on the multiset of level sums, not their original depth order. Equal sums remain separate entries because the $k$th largest is explicitly not required to be distinct.

For the sample, BFS creates `arr = [5,17,13,10]`. Ordered from largest, these are $17,13,10,5$, so the second largest is $13$.

**Detect too few levels**

If `len(arr) < k`, there is no $k$th level sum. The function returns $-1$ before attempting selection.

The constraint only guarantees $k\le n$, not that $k$ is at most tree height. A wide shallow tree can have many nodes but few levels, so this check is necessary.

**Select the `k` largest values**

The exact solution calls `nlargest(k, arr)` from Python's heap utilities. It returns a list containing the $k$ largest elements in descending order. The last element of that returned list is therefore the $k$th largest:

`nlargest(k, arr)[-1]`.

Duplicates are retained. If sums are `[10,10,5]` and $k=2$, the two largest list is `[10,10]`, so the answer is $10$, as required.

`nlargest` generally maintains a selection heap of size $k$ rather than fully sorting all level sums. This makes selection $O(h\log k)$ for $h$ levels in the general case, with library optimizations possible for special $k$ values.

**Exact implementation versus manifest summary**

The manifest says the traversal retains only the $k$ largest sums in a min-heap. The checked-in source instead first stores every level sum in `arr` and invokes `nlargest` afterward.

Both use heap-based selection and have similar worst-case time, but their memory behavior and data flow differ. The source needs storage for all $h$ level sums in addition to the selection structure. A streaming implementation could push each completed `t` into a size-$k$ heap immediately and avoid `arr`.

**Why the final result is correct**

The BFS invariant proves that `arr` contains every level sum exactly once. The insufficient-level branch handles the only case where rank $k$ does not exist.

Otherwise, `nlargest(k, arr)` contains precisely $k$ entries such that no excluded entry is larger than its last element. Because the list is descending, entries before the last occupy ranks one through $k-1$, and the last occupies rank $k$. Returning it gives the required value.

**Queue-space intuition**

The queue can hold an entire tree level at once. In a balanced tree, the bottom level may contain $\Theta(n)$ nodes, so BFS queue space is $O(n)$ even though tree height is only $O(\log n)$. In a path-shaped tree, the queue stays tiny but `arr` can contain $n$ level sums.

These complementary shapes explain why total auxiliary storage remains linear in all cases.

## Complexity detail

Let $N$ be the number of nodes and $h$ the number of levels. BFS visits each node once in $O(N)$ time. Appending $h$ sums costs $O(h)$. Selecting with `nlargest(k, arr)` costs $O(h\log k)$ in its standard heap-based regime.

Total time is $O(N+h\log k)$, bounded by $O(N\log k)$ because $h\le N$. The queue uses $O(N)$ worst-case space, `arr` uses $O(h)$, and `nlargest` returns $O(k)$ values. Total auxiliary-plus-selection space is $O(N+h+k)=O(N+k)$, which simplifies to $O(N)$ since $k\le N$.

## Alternatives and edge cases

- **Streaming min-heap of size `k`:** Push each level sum immediately and evict the smallest when size exceeds $k$. This matches the manifest summary and avoids storing all sums.
- **Sort all level sums:** Sorting `arr` takes $O(h\log h)$ time and is simple, but may do more work than selecting only $k$.
- **Depth-first accumulation:** DFS can add node values into an array indexed by depth, but recursion may be deep and still stores one sum per level.
- **Fewer than `k` levels:** Return $-1$ even if the tree has at least $k$ nodes.
- **Duplicate sums:** They occupy separate ranks and `nlargest` retains duplicates.
- **One requested rank:** The largest level sum is returned.
- **Path-shaped tree:** Every node forms its own level, making `arr` length $N$ while the queue remains size one.
- **Wide tree:** The queue can be linear even though the number of levels is small.
- **Positive node values:** Sums are positive, but the ordering method would also work with negative values.
- **Exact data flow:** The source stores all sums first; it does not maintain a size-$k$ heap during BFS.
