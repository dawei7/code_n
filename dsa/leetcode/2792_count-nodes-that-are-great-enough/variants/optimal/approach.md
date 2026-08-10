## General

**A node only needs to know its subtree's smallest values**

A node is great enough when at least `k` nodes in its subtree have values strictly smaller than its own. The node itself cannot count as smaller than itself, so the relevant candidates are its proper descendants.

To decide whether at least `k` descendant values are below `root.val`, it is sufficient to know the `k` smallest descendant values. If fewer than `k` descendants exist, the size condition fails. If at least `k` exist, the node qualifies exactly when the largest among those `k` smallest values—the kth-smallest descendant value—is still less than `root.val`.

The exact recursive DFS returns this bounded summary to each parent.

**Use a max-heap simulated with negative values**

Python's `heapq` is a min-heap. The solution stores `-value`. Among negative encodings, the smallest number corresponds to the largest original value. For example, original values 2, 5, and 7 become -2, -5, and -7; heap root -7 represents original maximum seven.

Helper `push(pq, x)` receives an already negated value:

1. push `x`;
2. if the heap now has more than `k` entries, pop its smallest negative entry.

The popped negative is the most negative, which corresponds to the largest original value. Repeating this retention rule leaves the `k` smallest original values.

This reversal is easy to misread: `l[0]` is the negative of the largest value among the retained small values, so `-l[0]` is their kth-smallest threshold when the heap has size `k`.

**Compute children before the parent**

`dfs(root)` is postorder:

- recursively obtain heap `l` from the left subtree;
- recursively obtain heap `r` from the right subtree;
- merge every value from `r` into `l` through bounded `push`;
- evaluate the current node against the merged descendant summary;
- then insert the current node's own value before returning to its parent.

Checking before inserting `root.val` is essential. The current node belongs to its own subtree according to the definition, but its value is not strictly smaller than itself and must not occupy one of the `k` smaller slots used for its qualification. For the parent, however, this current node is a proper descendant and must be included, so insertion happens after the check.

**Merge only bounded summaries**

Each child returns at most `k` negative values. To find the `k` smallest values across both child subtrees, it is enough to merge these summaries; any value discarded by a child was larger than at least `k` values in that same child subtree, so it can never become one of the parent's global `k` smallest descendants.

The code reuses `l` as the merged heap and pushes each entry from `r` into it. The bounded helper removes excess large original values after each insertion.

If a child is null, its DFS returns an empty list. The same merge logic handles leaves and one-child nodes without special branches.

**Test both necessary conditions at once**

The qualification condition is:

`len(l) == k and -l[0] < root.val`.

`len(l) == k` means at least `k` proper descendants exist. The heap never holds more than `k`, so a full heap is the certificate for sufficient subtree size.

`-l[0]` is the kth-smallest descendant value. If it is strictly below `root.val`, then all `k` retained values are smaller and the node is great enough. If it is equal or larger, fewer than `k` descendants are strictly smaller.

The strict `<` correctly handles duplicate values: descendants equal to the node do not count.

**A walkthrough**

Suppose `k = 2` and a node of value 6 has descendant values 4, 3, and 8. Their two smallest values are 3 and 4. Negative heap entries retain -3 and -4, with heap root -4. `-l[0] = 4 < 6`, so at least two descendants are smaller and the node qualifies.

If the node value were 4, the test would be `4 < 4`, false. Only one retained value, 3, is strictly smaller; equality does not help.

After checking value 6, the code pushes -6. For the parent, the summary becomes the two smallest among 3, 4, and 6, still 3 and 4.

**Why bounded summaries remain correct**

For a null subtree, the empty heap correctly lists its smallest values. Assume each child returns the minimum of `k` and its subtree size smallest values. Merging these two lists and repeatedly discarding the largest original value leaves exactly the `k` smallest values across both child subtrees. The node test is therefore based on the correct descendants.

Adding the current value and bounding again creates exactly the `k` smallest values in the entire current subtree, which is the summary its parent needs. Induction over postorder proves every returned heap and every qualification decision.

**The source is recursive, not iterative**

The Optimal manifest refers to iterative postorder. The exact source uses recursive calls and reuses child heaps. The algorithmic summary idea is the same, but recursion adds `O(h)` call-stack behavior and potential depth limitations.

## Complexity detail

Each node merges at most `k` entries from its right child and performs one additional push for its own value. A heap push or pop costs `O(log k)`. Total time is `O(nk log k)` in a detailed bound.

Because the constraint fixes `k <= 10`, `log k` is a small constant, and the manifest simplifies the work to `O(nk)`, which is also `O(n)` for this bounded domain.

Each active subtree summary holds at most `k` entries. Across recursive frames, bounded heaps and the call stack use at most `O(hk)` live auxiliary storage in a direct execution view, with a broad safe bound `O(nk)`. The recursion itself is `O(h)` and may reach `O(n)`. This is consistent with the manifest's broad `O(nk)` space, though the exact source is not iterative.

## Alternatives and edge cases

- **Collect and sort every subtree:** It repeats large descendant lists and can become quadratic. Retaining only `k` smallest values uses the small `k` bound.
- **Balanced ordered multiset:** It can maintain bounded minima but offers no advantage over a size-`k` heap here.
- **Iterative postorder:** It avoids recursion-depth problems and matches the manifest, while storing summaries in an explicit map or stack.
- **Fewer than `k` descendants:** The heap size is below `k` and the node cannot qualify.
- **Exactly `k` descendants:** Every descendant is retained; the largest must still be strictly smaller than the node.
- **Duplicate values equal to node:** The strict comparison rejects equality as a smaller value.
- **Leaf:** Its descendant heap is empty, so it never qualifies for positive `k`; its own value is then returned for ancestors.
- **Null child:** It contributes an empty summary.
- **Very skewed tree:** Recursive depth can approach the node count and may exceed Python's default recursion limit.
- **Negative heap signs:** Popping the smallest negative removes the largest original value, which is what retains the smallest `k`.
- **Current node timing:** It is checked before insertion so it cannot count itself, then inserted because it is a descendant of ancestors.
- **Input preservation:** Heap lists are newly built summaries; tree nodes and links are not modified.
