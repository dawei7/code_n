## General

Minimum depth counts nodes on the shortest path from the root to a leaf. The word “leaf” is essential: a path is complete only when it ends at a node with no left child and no right child. It is not enough to reach a missing child pointer beside a non-leaf node.

The selected recursive solution computes the answer for each subtree, but it treats one-child nodes carefully. The tempting formula `1 + min(left_depth, right_depth)` is valid only when both children exist. If one child is absent, its recursive depth would be zero, and taking the minimum would incorrectly select a path that ends in empty space rather than at a leaf.

**What each recursive result means**

`minDepth(root)` returns the number of real nodes on the shortest path from `root` to a leaf in that subtree. For `root is None`, it returns zero because an empty tree contains no nodes and no root-to-leaf path.

For a real node, the current node contributes one to every valid path below it. The remaining question is which child can continue that path.

- If the left child is absent, only the right child can lead to a leaf, so the answer is `1 + minDepth(root.right)`.
- If the right child is absent, only the left child can lead to a leaf.
- If both children exist, both offer valid ways to reach a leaf, so the shorter child depth may be selected.

These branches also handle a leaf automatically. A leaf has no left child, so the first child test returns `1 + minDepth(None)`, which is one. No separate leaf condition is necessary.

**Why a missing child cannot win**

Consider a root with no left child and a right chain of four more nodes. A naive formula would compute left depth zero and right depth four, then return `1 + min(0, 4) = 1`. That claims the root itself is a leaf, even though it has a right child.

The selected source instead sees the missing left child and is forced to follow the right subtree. It returns five, which counts every real node from the root through the actual leaf. This is exactly the situation represented by the second Reference example.

The distinction can be expressed another way: zero is a useful answer for an entirely empty input, but it is not a candidate path length when the current non-leaf node has another real child.

**Why the recursive cases are complete**

Every binary-tree node is in exactly one of four structural states:

- both children absent;
- only the left child present;
- only the right child present; or
- both children present.

The two explicit missing-child checks cover the first three states. In the leaf state, the first check safely reaches the empty right subtree and produces one. The final `min` case is reached only for the fourth state, where both child depths represent genuine paths to leaves.

Suppose recursive calls correctly return minimum depths for smaller subtrees. At a one-child node, every root-to-leaf path must enter the existing child, so adding one to that child's minimum is exact. At a two-child node, every path enters one child or the other; the shorter of those two best paths, plus the current root, is exact. Starting from empty trees and leaves, this reasoning covers the entire input tree.

**Tracing the balanced example**

For `[3,9,20,null,null,15,7]`, node `9` is a leaf and returns one. Nodes `15` and `7` also return one. Node `20` has both children, so it returns `1 + min(1, 1) = 2`.

The root has two real children. Its candidates are depth one through node `9` and depth two through node `20`; it returns `1 + min(1, 2) = 2`. The path contains root `3` and leaf `9`, so the result counts two nodes as required.

**Tracing the one-sided example**

For `[2,null,3,null,4,null,5,null,6]`, every non-leaf node lacks its left child. Each call therefore follows the right child rather than taking a minimum with zero. The leaf `6` returns one, node `5` returns two, and the count continues upward until root `2` returns five.

This example is a useful test because implementations that confuse a null pointer with a leaf often return one instead of five.

**What the source does and does not use**

When both children exist, Python evaluates both recursive arguments to `min`, so DFS explores both subtrees. There is no breadth-first early return at the first shallow leaf. Worst-case correctness still requires examining enough of the tree to establish each recursive answer, and no node is processed more than once.

The node values are irrelevant. Only the presence and arrangement of `left` and `right` links determine depth. The method does not mutate the tree.

The active file expects `Optional` and `TreeNode` to be available from the surrounding harness; the node class shown at the top is commented out.

## Complexity detail

Let $n$ be the number of nodes and $h$ the maximum number of nodes on any root-to-leaf path. Every real node is entered once, and each call performs constant local work beyond its child calls. The worst-case time complexity is $O(n)$.

The recursive call stack follows one downward path at a time and uses $O(h)$ auxiliary space. A balanced tree has $h=O(\log n)$, while a completely skewed tree has $h=n$, giving $O(n)$ worst-case stack space.

The manifest lists $O(w)$ space, where $w$ is maximum width, but that is not the workspace used by this exact DFS source. $O(w)$ is the usual queue bound for a breadth-first solution. For this implementation, $O(h)$ is the accurate auxiliary bound.

The returned integer uses $O(1)$ output space, and the algorithm allocates no node collection. On a chain, $w=1$ while $h=n$, demonstrating why substituting the width bound for the recursive height bound materially understates memory.

## Alternatives and edge cases

- **Breadth-first search:** Process nodes level by level and return when the first leaf is dequeued. This naturally finds minimum depth, can stop early, and uses $O(w)$ queue space.
- **DFS with a best-so-far depth:** Carry the current depth and update a global minimum at leaves. Pruning branches already as deep as the best leaf can reduce work on some inputs, though the worst case remains $O(n)$.
- **Unified `min` with infinity for absent children:** Treat a missing child beneath a real node as infinite rather than zero. Then a single minimum formula works, but the empty-root case still needs separate handling.
- **Naive `1 + min(left, right)` everywhere:** This fails whenever exactly one child exists because zero represents absence, not a completed leaf path.
- **Empty tree:** Returns zero before accessing child fields.
- **Leaf root:** Returns one; depth counts nodes, not edges.
- **Exactly one child:** The recursion must follow the existing child even if that route is long.
- **Two children:** Only here is the smaller child depth a valid choice.
- **Very wide shallow tree:** DFS stack can be small even when a BFS queue would be large.
- **Deep chain:** The correct depth may be $n$, and recursive stack usage also becomes $O(n)$.
- **Python recursion limit:** With up to $10^5$ nodes, a sufficiently deep chain can raise `RecursionError`; iterative BFS or DFS avoids that interpreter limitation.
- **Arbitrary values:** Negative values, duplicates, and ordering have no effect because only tree structure matters.
- **Node-count convention:** If depth were measured in edges, a leaf would have depth zero. This contract measures nodes, so a leaf has depth one and an empty tree alone returns zero.
- **Manifest discrepancy:** Attribute $O(w)$ to the BFS alternative, not to this selected recursive file.
