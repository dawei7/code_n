## General

**Store interval maxima so an entire basket range can be rejected at once.** The placement rule still requires the leftmost unused basket whose capacity is at least the current fruit quantity, but $n$ is now as large as $10^5$. Scanning every basket for every fruit would be quadratic.

The protected `SegmentTree` associates each node with a contiguous basket-index interval. `tr[u]` stores the maximum currently available capacity in that interval. If this maximum is less than fruit quantity $x$, no basket anywhere in the interval can hold that fruit, so the whole interval can be skipped.

The tree uses one-based logical basket positions even though the input list is zero-based. At a leaf `l == r`, build stores `nums[l - 1]`. Internal nodes recursively build both halves and call `pushup` to set their maximum from the two children.

**Find the leftmost sufficient basket by descending left first.** `query(u,l,r,v)` asks for the smallest index in the node's interval whose current capacity is at least `v`.

If `tr[u] < v`, the interval has no solution and returns $-1$. If the node is a leaf and its maximum passes, that leaf index is the answer.

At an internal node, the source first checks the left child's maximum. When `tr[u << 1] >= v`, at least one sufficient basket lies in the left half, so the leftmost answer must be there and recursion descends left. Otherwise, the entire left half is impossible and recursion descends right.

This is not a numeric binary search over capacities. It is a tree-guided search over indices, where stored interval maxima prove whether a half contains any feasible basket.

For `baskets = [3,5,4]` and fruit quantity four, the root knows some basket is sufficient. Its left interval covering indices one and two has maximum five, so query enters it. The left leaf capacity three fails and the search reaches the second basket, returning logical index two, which corresponds to zero-based index one—the required leftmost match.

**Consume a selected basket with a point update.** When query returns index `i`, `modify` descends to that leaf and replaces its tree value with zero. All fruit quantities are positive, so zero can never satisfy a later query. On the way back up, `pushup` recomputes every ancestor maximum, making subsequent searches see the basket as unavailable.

Only the tree is changed; the original `baskets` list referenced by `nums` is used during construction and is not overwritten by `modify`.

If query returns $-1$, no available basket has sufficient capacity and `ans` is incremented. Otherwise, one basket is consumed and the unplaced count stays unchanged.

**Why the search returns exactly the required basket.** At each internal node known to contain some solution, the algorithm chooses the left child whenever that child contains any solution. Every index in the left interval is smaller than every index in the right interval, so no right-side basket could be leftmost in that case. It chooses the right child only after the left maximum proves no left solution exists. Induction down the tree reaches the smallest feasible leaf.

After updating that leaf to zero, the maximum invariant remains correct because every ancestor is recomputed from correct child maxima. Thus, before each fruit, the tree represents exactly the capacities of unused baskets. Processing fruits in input order and querying the leftmost feasible leaf therefore simulates the required allocation exactly.

For the second example, quantity three consumes the first leaf with capacity six. Quantity six then sees that leaf as zero, rejects the middle capacity four, and finds capacity seven at the third index. Quantity one subsequently finds the still-unused middle basket. No reordering of fruits or baskets occurs.

**Why maximum is the right aggregate.** A sum, minimum, or count cannot answer whether an interval contains a capacity at least $x$. The maximum gives the exact existential test:

$$
\max(\text{interval})\ge x
\quad\Longleftrightarrow\quad
\text{some basket in the interval can hold }x.
$$

That equivalence is what permits one branch per tree level.

## Complexity detail

Building the segment tree visits $O(n)$ nodes and costs $O(n)$ time. Each fruit performs one query. A successful query follows one root-to-leaf path in $O(\log n)$ time, followed by a point update along another $O(\log n)$ path. A failed query can stop at the root in constant time or along a path, never exceeding $O(\log n)$.

Across $n$ fruits, total time is $O(n\log n)$. The tree array is allocated with $4n$ entries, so auxiliary space is $O(n)$. Recursive build, query, and update stacks have depth $O(\log n)$ and are dominated by tree storage. These bounds match the manifest.

## Alternatives and edge cases

- **Direct nested-loop simulation:** It is correct but costs $O(n^2)$ and is unsuitable for $n=10^5$.
- **Square-root decomposition:** Block maxima reduce time to $O(n\sqrt n)$ and appear in the editorial, but the segment tree is asymptotically faster.
- **Binary search on the raw basket array:** Capacities are not sorted and availability changes, so ordinary binary search cannot locate the leftmost sufficient basket.
- **Segment-tree range query plus external binary search:** This can cost $O(\log^2 n)$ per fruit; direct left-first descent finds the index in $O(\log n)$.
- **Choose the smallest sufficient capacity:** The problem requires the lowest basket index, not best fit by capacity.
- **Root maximum below the fruit quantity:** No basket can qualify, so query returns $-1$ without exploring leaves.
- **Capacity exactly equal to quantity:** The `>=` comparisons accept it.
- **Used basket:** Updating its leaf to zero permanently removes it because all quantities are at least one.
- **Several sufficient baskets:** Left-child preference guarantees the smallest index.
- **All baskets consumed:** The root maximum becomes zero and every later positive fruit is unplaced.
- **One basket:** Build creates one leaf, and query/update work without an internal node.
- **Input preservation:** Availability changes live in `tr`; the original `baskets` values remain unchanged.
