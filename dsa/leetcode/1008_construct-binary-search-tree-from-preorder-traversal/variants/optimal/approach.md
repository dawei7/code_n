## General

**Use both preorder order and the BST ordering rule**

Preorder traversal lists a subtree in this order:

1. the subtree root;
2. every node in its left subtree;
3. every node in its right subtree.

For a binary search tree with unique values, every left-subtree value is smaller than the root and every right-subtree value is larger.

Therefore, within the preorder segment belonging to one subtree, the first value is its root, followed by one contiguous block of smaller values and then one contiguous block of larger values. Finding the boundary between those two blocks completely determines the recursive subproblems.

**Define the recursive interval**

Helper `dfs(i, j)` constructs the BST whose preorder traversal is the inclusive subarray `preorder[i..j]`.

If `i > j`, the segment is empty and the corresponding child is `None`.

Otherwise, `preorder[i]` is the first value in this subtree's preorder segment, so the method creates:

`root = TreeNode(preorder[i])`.

The remaining task is to divide indices `i + 1` through `j` into the root's left and right subtree segments.

**Why the smaller and larger values form contiguous blocks**

Preorder completely traverses the left subtree before entering the right subtree. Every value in the left block is below the current root value, and every value in the right block is above it.

Thus the predicate

`preorder[index] > preorder[i]`

is false for all left-subtree indices and true for all right-subtree indices. It is monotone across this valid subtree segment, making binary search applicable.

This would not be safe for an arbitrary permutation. It is safe because the input is guaranteed to be the preorder traversal of some BST with unique values.

**Binary-search the first right-subtree index**

The search interval is half-open:

`l = i + 1` and `r = j + 1`.

The loop looks for the first index whose value is greater than the root:

- if `preorder[mid] > preorder[i]`, the boundary is at `mid` or earlier, so set `r = mid`;
- otherwise, `mid` belongs to the smaller-valued left block, so set `l = mid + 1`.

When the loop ends, `l` is the first right-subtree index.

Two boundary cases work naturally:

- If the first remaining value is already larger, `l = i + 1` and the left segment is empty.
- If no remaining value is larger, `l = j + 1` and the right segment is empty.

**Build both children from their exact segments**

The recursive calls are:

`root.left = dfs(i + 1, l - 1)`

and

`root.right = dfs(l, j)`.

These segments are disjoint, cover every remaining element, and retain original preorder order. The root is then returned to its parent call.

No value comparison is needed during child attachment after the boundary is known; the interval definitions already encode the BST placement.

**Trace `[8, 5, 1, 7, 10, 12]`**

At the full interval, root value is eight. Binary search finds index four, value ten, as the first value greater than eight.

- Left segment is `[5, 1, 7]`.
- Right segment is `[10, 12]`.

For left root five, the first larger value within its segment is seven, so one becomes its left child and seven its right child.

For right root ten, twelve is immediately the first larger value, so its left subtree is empty and twelve becomes its right child.

The resulting tree has preorder exactly `8, 5, 1, 7, 10, 12` and satisfies every BST comparison.

**Why uniqueness matters**

The code classifies values with strict greater-than. Equal values would require a separate convention about whether duplicates belong left or right, and the boundary predicate might not match the required BST definition.

The contract guarantees all values are unique, so each non-root value belongs unambiguously to the smaller or larger block.

**Why the construction is correct**

Use induction on interval length. An empty interval correctly produces no node, and a one-element interval produces a leaf.

For a larger valid preorder segment, its first value must be the subtree root. The monotone boundary divides exactly the traversal of its left subtree from the traversal of its right subtree. Every left value is smaller and every right value is larger.

By the induction hypothesis, each recursive call constructs the correct BST for its own preorder block. Attaching them to the root therefore produces a valid BST whose preorder is the entire input segment. Applying this to `dfs(0, N - 1)` constructs the required tree.

**No global insertion simulation is needed**

Inserting preorder values one by one into a BST would also reconstruct the tree, but a skewed input could make each insertion traverse a long path. The interval method derives whole subtree membership directly from traversal structure.

## Complexity detail

Let `N` be the preorder length and `H` the height of the resulting tree.

The exact protected implementation creates each node once, but it also performs a binary search within every node's subtree segment. A binary search costs `O(\log m)` for segment length `m`. The safe overall bound is `O(N \log N)` time; this worst case is approached by highly skewed segments whose sizes decrease one by one.

The recursion stack has depth `O(H)`. Apart from the returned tree nodes, each call stores constant local state, so auxiliary space is `O(H)`.

An upper-bound recursion or monotonic-stack construction can achieve `O(N)` time, but that is a different implementation from the boundary binary searches used here.

## Alternatives and edge cases

- **Recursive upper bound with one shared index:** Consume preorder once, creating a node only when the next value fits the current bound. It runs in `O(N)` time and `O(H)` stack space.
- **Monotonic stack:** Attach smaller values as left children and pop smaller ancestors to find a larger value's right parent. It is iterative and linear.
- **Repeated BST insertion:** Simple, but a sorted preorder creates `O(N^2)` work.
- **Sort to obtain inorder:** Combine sorted inorder with preorder to reconstruct the tree in `O(N \log N)` time and `O(N)` extra storage.
- **Strictly increasing preorder:** Every left segment is empty, producing a right-skewed tree.
- **Strictly decreasing preorder:** Every right segment is empty, producing a left-skewed tree.
- **Single value:** The search interval is empty and both recursive child calls return `None`.
- **Boundary at `j + 1`:** It means no right subtree; the left call receives all remaining values.
- **Boundary at `i + 1`:** It means no left subtree; the right call receives all remaining values.
- **Valid-preorder guarantee:** The monotone partition property depends on it; malformed input would require validation.
- **Input preservation:** The preorder list is only read and is not sorted or modified.
