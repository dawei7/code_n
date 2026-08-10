## General

Maximum depth counts nodes, not edges, along the longest path from the current root to a leaf. A binary tree is recursively made from a root, a left subtree, and a right subtree, so its depth follows the same recursive structure.

For a node `root`, let $D(\texttt{root})$ be its maximum depth. Then:

$$
D(\texttt{root})=
\begin{cases}
0, & \text{if root is empty},\\
1+\max(D(\texttt{root.left}),D(\texttt{root.right})), & \text{otherwise}.
\end{cases}
$$

The selected code is a direct implementation of this definition.

**Why the empty tree has depth zero**

An empty tree contains no nodes, so its longest root-to-leaf path contains zero nodes. Returning zero is also the arithmetic base that makes a leaf work naturally.

A leaf has two empty children. Their depths are both zero, and the leaf returns:

$$
1+\max(0,0)=1.
$$

That agrees with the node-count definition: the path consisting of the leaf alone contains one node.

**Solving both child subproblems**

For a real node, the code recursively computes:

- `l`, the longest node-count path beginning at the left child; and
- `r`, the longest node-count path beginning at the right child.

Any downward path from the current node must choose exactly one child direction after including the current node. It cannot travel down the left subtree and later jump into the right subtree. Therefore the longest possible continuation is `max(l, r)`.

Adding one counts the current node itself. Omitting that one would count edges below the node and would return zero for a leaf, contradicting the contract.

**Trace through the Reference tree**

For `[3,9,20,null,null,15,7]`, each leaf—nine, fifteen, and seven—receives zero from both empty children and returns one.

Node twenty receives child depths one and one, so it returns two. Root three receives left depth one and right depth two, chooses two, and returns three. One longest path is `3 -> 20 -> 15`; the alternative through seven has the same length.

For `[1,null,2]`, the empty left child returns zero. Node two returns one. Root one returns `1 + max(0, 1) = 2`.

**Why postorder evaluation is necessary**

The parent cannot know its result until both child depths are known. The recursive calls therefore happen before the final calculation, which is a postorder-style computation: left result, right result, then parent result.

The tuple assignment evaluates both right-hand calls before binding `l` and `r`. Python evaluates them left to right, but correctness does not depend on which child is solved first because the subtrees are independent and the tree is not mutated.

**Why the recurrence is correct**

For an empty node, zero is correct. Assume recursive calls return correct maximum depths for both child subtrees.

Every root-to-leaf path from the current node consists of the current node plus a path entirely inside one child subtree. The longest left choice has length $1+l$ and the longest right choice has length $1+r$. Their maximum is $1+\max(l,r)$, exactly what the method returns.

Structural induction from empty children proves the result for every node, including the original root.

The method reads only child pointers. Node values do not affect depth and are never inspected.

## Complexity detail

Let $n$ be the number of nodes and $h$ the number of nodes on the longest root-to-leaf path. Every real node is called once, and every missing child causes a constant-time base call. Total work is $O(n)$.

At any moment, the call stack contains one active root-to-current path. Its maximum size is $O(h)$, matching the manifest. A balanced tree has $h=O(\log n)$; a skewed tree has $h=O(n)$.

The return value and local references use constant space per call. Python does not optimize this branching recursion into constant stack space.

Although both subtrees are computed, their call stacks do not remain active simultaneously. The complete left call returns before the right call begins, leaving only its integer result in the parent frame. Stack usage is therefore governed by the longest single path, not by total nodes or the sum of both subtree heights.

A proper tree has one parent per node, so no subtree result is requested from two different paths. Caching depths by node would consume extra memory without avoiding repeated computation.

With up to $10^4$ nodes, a maximally skewed tree can exceed Python's default recursion limit. That is a practical execution concern even though the asymptotic bound is correct.

## Alternatives and edge cases

- **Iterative DFS stack:** Store `(node, depth)` pairs, update the maximum, and avoid recursion-limit failure with $O(h)$ storage.
- **Level-order BFS:** Count completed levels. It uses $O(w)$ frontier space, where $w$ is maximum width.
- **Memoization:** Unnecessary for a proper tree because each node has one parent and no subtree is reached twice.
- **Empty root:** Returns zero immediately.
- **Single node:** Returns one through two zero-depth child results.
- **Only one child:** The missing side contributes zero; the existing path determines the result.
- **Balanced tree:** Both branches may have similar depth, but both still must be computed.
- **Node values:** Negative, positive, and duplicate values are irrelevant to structural depth.
- **Depth definition:** This problem counts nodes. An edge-count convention would differ by one for nonempty trees.
- **No early local shortcut:** Seeing one missing child does not determine the final depth; the existing child can contain an arbitrarily long path and must be solved.
