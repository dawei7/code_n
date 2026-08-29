## General

**Carry the path value instead of storing the path**

Each root-to-leaf path is a sequence of binary digits ordered from most significant to least significant. If the value represented by the digits already visited is `x` and the next node contains bit `b`, appending that bit produces

$$
x_{\text{new}} = 2x + b.
$$

Multiplication by two shifts every existing binary digit one position to the left, and adding `b` fills the new units position. The code writes the same operation as `x = x << 1 | root.val`. Left shift by one equals multiplication by two. Because `root.val` is guaranteed to be zero or one and the shifted value has a zero low bit, bitwise OR places the node bit there and has the same numeric effect as addition.

This recurrence lets a depth-first search carry one integer rather than a list or string containing every bit on the path. When the search reaches a leaf, that integer is already the complete value of the root-to-leaf binary number.

**The meaning of the recursive arguments**

The helper `dfs(root, x)` returns the sum of all binary numbers for root-to-leaf paths that begin at the current `root`, given that `x` is the value of the path strictly above that node.

The distinction between before and after the current node matters. Immediately after the null check, the helper updates `x` with `root.val`. From that point onward, `x` represents the complete prefix from the original tree root through the current node.

Python integers are immutable. Passing `x` into the left recursive call and the right recursive call gives each branch its own numeric value. Work in one branch cannot alter the prefix seen by the other branch, so no explicit backtracking or bit removal is needed.

**Why a missing node contributes zero**

The first condition is `if root is None: return 0`. A missing child does not define a root-to-leaf path, so it must add nothing to the sum. Zero is the additive identity, making the final expression

`dfs(root.left, x) + dfs(root.right, x)`

work uniformly whether a node has two children, one child, or no children.

For an actual leaf, the method returns before making those two null calls. That early return is both clearer and slightly more efficient.

**How the code recognizes a leaf**

After incorporating the current bit, the condition `root.left == root.right` detects a leaf in the platform's tree model. At a leaf, both fields are `None`, so they compare equal. At a node with exactly one child, one field is `None` and the other is a `TreeNode`, so they differ. At a node with two children, the two child objects are distinct nodes and also differ.

The conventional spelling is `root.left is None and root.right is None`. The exact solution uses equality as a compact equivalent under LeetCode's ordinary `TreeNode` identity semantics and valid-tree structure. Once the condition is true, `x` is the complete binary number for that leaf, so `dfs` returns `x` itself.

It is important not to treat a node with only one missing child as a leaf. A root-to-leaf path ends only at a node with no children. The equality test correctly distinguishes that case under the supplied node class.

**Combining subtrees**

If the current node is not a leaf, every root-to-leaf path below it belongs to exactly one of two disjoint groups: paths entering the left child and paths entering the right child. The helper recursively computes the sum for each group and adds them.

If one child is missing, its call returns zero and the existing child's contribution passes through unchanged. If both children exist, their path sets do not overlap, so addition neither omits nor double-counts a leaf.

This is why the helper returns a sum rather than changing a shared accumulator. Each call completely summarizes its subtree, and the parent combines two summaries with ordinary addition.

**A complete example**

Consider the complete tree represented by `[1,0,1,0,1,0,1]`. The initial call is `dfs(root, 0)`.

At the root bit one, the update changes zero to binary `1`. Moving left to bit zero changes the prefix to binary `10`, which is decimal two. Its left leaf bit zero produces `100`, decimal four, and its right leaf bit one produces `101`, decimal five. That subtree returns nine.

Moving right from the root begins again with the parent prefix one, not with any value left behind by the left search. Appending one produces `11`, decimal three. Its leaves produce `110` and `111`, decimal six and seven. That subtree returns thirteen.

The root call adds nine and thirteen and returns twenty-two. Every leaf contributed once, and each contribution used exactly the bits on its own root-to-leaf path.

For the single-node tree `[0]`, appending the root bit leaves `x = 0`. Both children are `None`, so the leaf condition returns zero. The fact that the value is zero does not make the path absent; it is a real path whose represented number is zero and whose contribution is correctly zero.

**Why the recursion is correct**

For any call `dfs(node, prefix)`, first append `node.val` so the working value represents the path through that node. If the node is a leaf, there is exactly one path in its subtree, and returning that value is correct.

If the node is internal, every leaf below it lies in either the left subtree or the right subtree. By the same reasoning recursively, each child call returns exactly the sum of paths ending in that child's subtree, using the already updated prefix. Adding the two results gives exactly the sum for the current subtree.

The top-level call uses prefix zero, so it introduces no digits before the root. Structural induction over the tree therefore proves that `dfs(root, 0)` equals the requested sum over all leaves.

**Why all nodes must be visited**

Every node can affect at least one root-to-leaf number. A changed bit near the root changes all leaf values below it, while a changed leaf bit changes its own path value. There is no safe way to ignore an arbitrary subtree. The DFS performs the necessary single visit to every real node and carries only the information required for that node's path prefix.

## Complexity detail

Let `N` be the number of nodes and `H` be the tree height measured in nodes on the longest root-to-leaf path. Each real node is entered once and performs a constant amount of work: a shift, an OR, child checks, and at most one addition. Missing-child calls also total `O(N)` in a binary tree. The running time is `O(N)`, matching the manifest.

The source guarantees that the total answer fits in a 32-bit integer. Because every path value is nonnegative, each individual path value also fits within that bound. The arithmetic operations therefore act on bounded-size integers in this problem, supporting the constant-time-per-node analysis.

At most one recursive chain per tree level is active at once. The call stack uses `O(H)` space. A balanced tree has `H = O(\log N)`, while a completely skewed tree has `H = O(N)`. No array of node values or path digits is allocated. The scalar `x` values stored in active frames account for the same `O(H)` bound.

## Alternatives and edge cases

- **Iterative depth-first search:** Store pairs of node and prefix value in an explicit stack. This avoids language recursion limits and has the same `O(N)` time and `O(H)` typical stack requirement, with up to `O(N)` entries depending on tree shape.
- **Breadth-first search:** A queue can carry each node with its prefix and add values at leaves. It is also linear but may store an entire wide level, requiring `O(W)` space where `W` is maximum width.
- **Build path strings:** Append `'0'` or `'1'` while descending and parse the string at every leaf. This stores and converts information the numeric recurrence can update directly, and careless string copying can increase total work.
- **Shared accumulator with backtracking:** A recursive traversal can add leaf values into a nonlocal sum. It is correct, but returning subtree sums avoids mutable shared state and makes the combination rule explicit.
- **Morris traversal:** Temporary predecessor links can produce `O(1)` auxiliary space, but the bookkeeping for removing path bits and restoring the tree is substantially more complex and temporarily mutates the structure.
- **Single node containing zero:** It is a genuine leaf path representing zero, so the answer is zero.
- **Single node containing one:** The first shift and OR produce one, which is immediately returned.
- **Leading zero on a path:** A root value of zero is allowed. Binary `01101` and `1101` have the same numeric value, and the recurrence naturally handles the leading zero without special treatment.
- **Only one child:** The node is not a leaf. The missing child contributes zero, while the existing branch continues with the correct prefix.
- **Skewed tree:** The arithmetic stays linear, but recursion depth becomes `N`. An iterative stack may be safer in a runtime with a strict recursion limit.
- **Leaf detection shorthand:** `root.left == root.right` relies on both children being `None` only at a leaf under the platform's normal tree-node identity behavior. In a custom class with structural equality or shared child references, the explicit two-`None` test would be safer.
- **Operator meaning:** `x << 1 | root.val` is a binary digit append, not an arbitrary bit trick. It is equivalent to `2 * x + root.val` only because every node value is zero or one.
