## General

**Turn every downward path into a difference of root prefixes**

For a node on the current root-to-node route, define its prefix sum as the sum from the tree root through that node. Suppose the current prefix is $S$, and an earlier prefix on the same route was $P$. The nodes strictly after that earlier position through the current node sum to

$$
S-P.
$$

That downward path equals `targetSum` exactly when

$$
P=S-\texttt{targetSum}.
$$

Therefore, at each node, the number of valid paths ending there is the number of earlier prefixes on the active ancestor route equal to `s - targetSum`.

This counts paths that can begin anywhere, not only at the root, while respecting the downward contiguous requirement.

**Seed the empty prefix**

`cnt = Counter({0: 1})` records one prefix sum of zero before the root. This conceptual empty prefix makes a path that begins at the root follow the same formula as every other path.

If the root-to-current sum itself equals the target, then `s - targetSum == 0`; the seeded entry contributes one. Without the seed, root-starting paths would need a separate condition.

**Process one node**

`dfs(node, s)` receives the prefix sum through the parent. For a real node, `s += node.val` extends that prefix through the current value.

Before inserting the current prefix, the code sets

`ans = cnt[s - targetSum]`.

Every counted occurrence belongs to an ancestor boundary. If the same prefix sum occurred several times along the route—possible because values may be zero or negative—each occurrence defines a different starting position and therefore a different valid path ending at the current node.

Only after counting does the code execute `cnt[s] += 1`. Inserting first could count a zero-length path when `targetSum == 0`; paths must contain nodes, so the current boundary must not be compared with itself.

The helper then recursively counts valid paths in the left and right subtrees and adds both results.

**Backtrack before entering a sibling branch**

After both children return, `cnt[s] -= 1` removes the current prefix from the active-route multiset before control returns to the parent.

This step is essential. A prefix from the left subtree is not an ancestor of a node in the right subtree. Leaving it active would subtract prefix sums across two branches and count a disconnected route that moves upward and then downward, violating the problem.

The counter at any recursive moment therefore represents exactly the prefix boundaries on the root-to-parent path of the node about to be processed, plus the empty prefix.

**A path-counting example**

Suppose the active prefix sums before a current node are `0, 10, 15, 18`, and after adding the current value the new sum is `23`. With target `8`, the helper looks for `23 - 8 = 15`. Because prefix `15` occurred once, the nodes after that boundary through the current node form one path summing to eight.

If `15` had occurred twice on the same ancestor route, two different starting positions would produce two valid paths, and the Counter value would correctly add two.


On entry to a real node, `cnt[P]` equals the number of times prefix sum $P$ appears among boundaries before that node on the active root route. The lookup therefore counts all and only downward paths ending at the node with target sum.

Adding the current prefix establishes the invariant for each child. Removing it afterward restores the exact parent state, so sibling branches remain independent. Every valid downward path has one unique ending node and is counted there once. Summing the node result with both recursive subtree results therefore yields the total number of valid paths.

**Why negative values are harmless**

The method never assumes prefix sums increase. It relies only on subtraction and equality, so negative, positive, and zero node values all work. This is an advantage over a two-pointer or sliding-window idea, which generally cannot shrink monotonically when values may be negative.

**Empty tree**

`dfs(None, s)` returns zero immediately. Thus an empty root yields zero without accessing any node fields or modifying the counter.

## Complexity detail

Let $n$ be the number of nodes and $h$ the tree height. Each node is visited once and performs average constant-time Counter operations, so expected time is $O(n)$.

The recursion stack uses $O(h)$ space. The Counter can retain up to $O(n)$ distinct prefix-sum keys in this exact Python implementation: decrementing a count to zero does not delete its key, so prefix sums encountered in completed branches may remain as zero-valued entries. Thus total auxiliary space is $O(n)$ in the worst case, matching the manifest. If zero entries were deleted, the active positive-count map would be bounded by $O(h)$.

## Alternatives and edge cases

- **Start a fresh DFS from every node:** Count target paths beginning at each possible start. It is straightforward but can take $O(n^2)$ time on a skewed tree.
- **Store the entire current route and sum suffixes:** This uses $O(h)$ route space but checks up to $h$ suffixes per node, also reaching $O(nh)$ time.
- **Sliding window:** Negative values destroy the monotonic property needed to decide which endpoint to move.
- **Forget the backtracking decrement:** Prefixes from one subtree would leak into another and create nonexistent cross-branch paths.
- **Insert the current prefix before querying:** For target zero, this would count an empty path at every node.
- **Path beginning at the root:** The seeded zero prefix counts it without a special branch.
- **Repeated prefix sums:** Counter multiplicity is necessary because each occurrence represents a distinct starting boundary.
- **Target zero:** Real zero-sum paths are counted through equal earlier/current prefixes; the current node is not paired with itself.
- **Negative target or node values:** Prefix subtraction remains valid with no special case.
- **Single-node tree:** It contributes one exactly when its value equals the target.
- **Empty tree:** The answer is zero.
