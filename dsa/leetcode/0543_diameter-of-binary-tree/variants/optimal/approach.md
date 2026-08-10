## General

The diameter may pass through any node, not necessarily the root. At a chosen node, the longest path passing through it combines:

- the longest downward path into its left subtree;
- the longest downward path into its right subtree.

A postorder depth-first traversal can compute those downward heights and evaluate every node as a possible highest point of the diameter.

The helper `dfs(root)` returns the height of the current subtree measured in **nodes** along its longest downward path. For a null subtree it returns zero.

This node-count convention makes a leaf return one: both child heights are zero, then `1 + max(0, 0)` is one.

**Process children before the current node.** The calls:

`l, r = dfs(root.left), dfs(root.right)`

compute the longest downward node paths from each child before the current node uses them. This is postorder traversal.

If `l` is three, there is a path starting at the left child and descending through three nodes. The edge from the current node to that child is not counted inside `l` as an extra value; however, when building a path through the current node, a child path of `l` nodes also corresponds to `l` edges from the current node down to its endpoint.

**Evaluate a diameter passing through the current node.** A path whose highest node is the current node can descend to a deepest left endpoint and a deepest right endpoint. Its edge count is:

$$
l+r.
$$

There are `l` edges from the current node into and through the chosen left path, and `r` on the right. The code updates:

`ans = max(ans, l + r)`.

If one child is absent, its height is zero and this formula describes a one-sided path from the current node down the other subtree. If both are absent, the candidate is zero edges, correct for a single node.

**Return only one branch upward.** A path passed to the parent must begin at the current node and descend through either the left child or the right child; it cannot take both, because that would branch and cease to be a simple path.

Therefore `dfs` returns:

`1 + max(l, r)`.

The added one counts the current node in the downward height. The other branch is still considered for the global diameter at this node through `l + r`, even though it is not returned.

For tree `[1,2,3,4,5]`, node two has left and right leaf heights one and one, producing local diameter two edges. At node one, the left height is two and right height is one, producing three edges. That corresponds to path four–two–one–three or five–two–one–three.

**Why a single global answer is necessary.** Returning only subtree height cannot communicate a diameter lying entirely below a node. For example, the longest path may join two deep leaves in the left subtree and never touch the root. `ans` is updated at every node, so such an internal path remains recorded even after recursion returns only one height branch.

**Why every possible diameter is considered.** Any simple path in a tree has a unique highest node relative to the root: the lowest common ancestor of its endpoints. At that node, the path consists of at most one downward branch on the left and at most one on the right. The algorithm's `l + r` candidate uses the longest possible such branches, so it is at least as long as that path. Since every candidate the algorithm constructs is itself a valid tree path, the maximum is exactly the diameter.

**Why units do not become off by one.** The helper counts nodes in a downward path, but `l` and `r` exclude the current node. Adding them counts edges from the current node to both endpoints. The returned answer is therefore in edges, as required.

Variable `ans` begins at zero, the diameter of a one-node tree. `nonlocal ans` lets all recursive frames update the same maximum.

Node values are never inspected because only tree structure affects path length.

## Complexity detail

Let $n$ be the number of nodes and $h$ the tree height. Each node is visited once and performs constant work after its children return, so time is $O(n)$.

The recursion stack has at most one frame per level, requiring $O(h)$ auxiliary space, matching the manifest. A balanced tree has $O(\log n)$ height, while a skewed tree can have $O(n)$ height.

Only `ans` and local height integers are stored beyond the call stack.

## Alternatives and edge cases

- **Run a depth search from every node:** It can find the longest path but repeats work and may take $O(n^2)$ time.
- **Two graph traversals from a farthest node:** It is a valid tree-diameter method after treating edges undirected, but requires parent/adjacency handling.
- **Store full paths:** Only their lengths are required; storing node sequences wastes memory.
- **Single node:** Both heights are zero, so the diameter remains zero edges.
- **Two nodes:** The root candidate is one, producing the single connecting edge.
- **Skewed tree:** Every local path is one-sided; the root-to-leaf chain becomes the diameter.
- **Diameter below the root:** The global `ans` retains a candidate found in a descendant subtree.
- **Negative or duplicate values:** Values are irrelevant to structural distance.
- **Null-child height:** Returning zero makes a leaf height one and keeps the edge formula consistent.
- **Recursion depth:** A highly skewed 10,000-node tree may require an iterative equivalent in environments with low recursion limits.
- **Do not return `l + r` as height:** A parent can extend only one child branch, so doing so would describe a branched shape rather than a path.
