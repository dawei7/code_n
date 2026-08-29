## General

Physically removing leaves round after round would repeatedly modify or rescan the tree. The exact solution notices that a node's removal round is already determined by its distance upward from the deepest leaf below it.

A leaf disappears in round zero. A node whose children disappear no later than round zero becomes a leaf and disappears in round one. More generally, a node disappears one round after its later-disappearing child. That gives the recurrence

$$
\operatorname{round}(node)=\max(\operatorname{round}(node.left),\operatorname{round}(node.right))+1
$$

if missing children are assigned round `-1`. The source uses an equivalent shifted convention: a missing child returns `0`, a real node returns its removal round plus one, and the group index is the maximum returned child height.

**The recursive return value.**

`dfs(root)` returns the number of node levels on the longest downward path from `root` to a leaf. Under this convention:

- A missing node returns `0`.
- A leaf has two missing children, so `l = r = 0`; it is placed in group `0` and returns `1`.
- A parent of leaves receives child returns of `1`; it is placed in group `1` and returns `2`.

The local variable `h = max(l, r)` is therefore both one less than the node's returned height and exactly its zero-based removal round.

This shift avoids negative heights in Python while preserving the same grouping as the more common “null is `-1`, leaf is `0`” definition.

**Why traversal must be postorder.**

The removal round of a parent depends on both children's heights. The source recursively evaluates the left child and then the right child before computing `h` for the current node. This is postorder traversal: children first, parent last.

A preorder traversal would see the parent before knowing how many removal rounds its subtrees survive. It could still work with later bookkeeping, but the direct recurrence naturally requires postorder.

**Growing the answer only when a new round appears.**

`ans[h]` is the list of values removed in round `h`. Initially `ans` is empty. When the first leaf is processed, `h` is zero and `len(ans) == h`, so the source appends an empty group before inserting the leaf value.

Later, the first node with group index one sees `len(ans) == 1` and creates the second group. The condition needs only equality, not a loop that appends multiple missing groups. Postorder guarantees there can be no gap: a node in round `h` has a descendant chain establishing every earlier round from zero through `h - 1`, and those descendants were processed first.

After ensuring the group exists, `ans[h].append(root.val)` records the current value. Nodes with the same height share the same removal round even when they lie in different branches.

**A trace of the example tree.**

For level-order tree `[1,2,3,4,5]`, nodes `4`, `5`, and `3` have no children. Each receives child heights zero, enters `ans[0]`, and returns one.

Node `2` receives height one from each child. Its `h` is one, so it enters `ans[1]` and returns two. Root `1` receives two from the left and one from the right; its `h` is two, so it enters `ans[2]`.

The output becomes `[[4,5,3],[2],[1]]` under this traversal order. The contract permits any ordering within one round, so other leaf orders are equally valid.

**Why height equals the physical removal round.**

For a leaf, both concepts are zero: it is removed immediately and has no edge below it. Assume each child is grouped in its correct removal round. A parent cannot be a leaf while either child remains, so it survives through the larger child round. Immediately after both children are removed, the parent has no children and is collected in the next round. Its round is therefore one greater than the maximum child round.

The source's `h = max(l, r)` computes exactly that value because `l` and `r` are each child round plus one. By induction from leaves to root, every node enters the correct group.

**Why every node appears exactly once.**

Tree traversal reaches each non-null node from its unique parent path. Each call performs exactly one append for its node after processing children. No call revisits or mutates the node, so no value occurrence is duplicated or omitted. Repeated node values are preserved as separate entries because grouping is by node identity during traversal, not by value uniqueness.

The tree itself remains intact. “Remove” is only the interpretation of the height groups; no child pointer is changed. This is safer for callers that may still need the original tree.

**The last group contains the root.**

The root has the greatest downward height in the tree, so it survives at least as long as every descendant. Once its subtrees have disappeared, it becomes the sole remaining node and is removed in the final round. Its computed group index is consequently the last index in `ans`.

For an unbalanced tree, several nodes outside the deepest branch can share earlier groups, while only ancestors along maximal-height paths determine how many total rounds exist.

## Complexity detail

Let $n$ be the number of tree nodes and $h$ the tree height measured in nodes along the longest root-to-leaf path.

Every node is visited once, and each visit performs constant work besides its recursive child calls and output append. Total running time is $O(n)$.

The active recursion stack contains at most $h$ calls, so auxiliary traversal space is $O(h)$. A balanced tree has $h=O(\log n)$, while a completely skewed tree has $h=O(n)$. The returned nested lists store all $n$ values and therefore require $O(n)$ output space. The manifest's $O(h)$ space is accurate when required output storage is excluded.

No separate height map or sorting array is allocated. Python recursion depth is safe under this package's maximum of 100 nodes, though an iterative postorder method may be preferable for much deeper unrestricted trees.

## Alternatives and edge cases

- **Repeated physical removal:** Find leaves, detach them, and repeat. This mirrors the story directly but can rescan surviving nodes many times and degrade to $O(n^2)$ on a skewed tree.

- **Store `(height, value)` pairs then sort:** Postorder can record every pair, followed by grouping after an $O(n\log n)$ sort. Direct indexing by height avoids the sort.

- **Iterative postorder:** Use an explicit stack and a map from node to computed child height. It avoids recursion limits but needs more explicit state.

- **Single-node tree:** Both child calls return zero, the root enters group zero, and the output is `[[root.val]]`.

- **Skewed tree:** Every node has a different removal round, so each output group contains one value and recursion uses $O(n)$ stack space.

- **Perfect tree:** All nodes at the same depth from the root also share a height from the leaves, producing one group per tree level in reverse vertical order.

- **Repeated values:** Equal values from different nodes are all appended. The answer groups nodes, not distinct values.

- **Missing one child:** Its return value is zero. The existing child's height determines the parent's round, as expected because the parent must wait for that subtree.

- **Null root outside the stated domain:** The source would return an empty list because `dfs(None)` returns zero and appends nothing. The local constraints guarantee a nonempty tree.

- **Order inside a round:** The source tends to produce left-subtree values before right-subtree values due to postorder, but the contract explicitly permits any intra-round order.

- **Input tree preservation:** No nodes are actually removed, so calling code retains the original structure after the method finishes.
