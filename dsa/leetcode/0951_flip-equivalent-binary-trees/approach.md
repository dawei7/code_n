## General

**At every node, there are only two valid alignments**

A flip swaps a node's left and right subtrees. Therefore, after two current roots are known to represent the same value, their children can correspond in exactly two ways:

- no flip at this node: left matches left and right matches right;
- flip at this node: left matches right and right matches left.

The recursive helper tests these two possibilities. It does not need to construct flipped trees physically because choosing crossed recursive arguments represents a flip logically.

**Base cases before recursion**

The first condition is `root1 == root2 or (root1 is None and root2 is None)`.

When both references are `None`, their empty trees are equivalent. When both variables reference the same node object, the subtrees are literally identical and also equivalent. In ordinary separate input trees, the equality shortcut mainly covers both-null pairs. The explicit both-null part is logically redundant after reference equality in Python, but it makes the intended empty-tree case visible.

Next, the helper returns false if:

- exactly one root is `None`;
- their values differ.

A flip changes only child positions. It cannot create a missing node or change a node value, so either mismatch makes equivalence impossible at this pair.

**Testing the unflipped arrangement**

The first conjunction is:

`dfs(root1.left, root2.left) and dfs(root1.right, root2.right)`.

Both child-subtree pairs must be flip equivalent. If the left comparison fails, Python's short-circuit `and` skips the right comparison because the whole unflipped arrangement is already impossible.

**Testing the flipped arrangement**

If the unflipped arrangement does not succeed, the second conjunction tests:

`dfs(root1.left, root2.right) and dfs(root1.right, root2.left)`.

This corresponds to flipping one current node. It does not matter which of the two trees is described as flipped; swapping either side creates the same child pairing.

The two conjunctions are joined by `or`. Success of either complete alignment is enough.

**Local choices combine into a global transformation**

Each recursive call makes its own flip-or-no-flip decision. A tree may need a flip at the root, no flip at one child, and another flip several levels lower.

This independence is why recursion fits the definition. Once a current child pairing is selected, operations inside those subtrees do not affect nodes outside them.

**Trace conceptually**

Suppose both roots hold one, but the left child of the first root holds two while the right child of the second root holds two. The unflipped left-left comparison quickly fails due to different values. The crossed comparison aligns the two-valued subtrees and separately aligns the other children.

Within the two-valued subtree, the helper repeats the same reasoning. A later pair of children may match without another flip or may require another crossed alignment.

**Why the recursion is correct**

If the helper returns true through the unflipped branch, both corresponding child pairs can independently be made equal. Applying those subtree flips makes the whole rooted trees equal without flipping the current node.

If it returns true through the crossed branch, flip one current node, then apply the recursively established transformations inside the crossed child pairs. The complete rooted trees become equal.

Conversely, suppose two rooted trees are flip equivalent. Their roots must either both be absent or have equal values. At a present root, the successful transformation either flips that node or does not. In the first case, the crossed child pairs must be flip equivalent; in the second, the aligned pairs must be. The helper tests both possibilities, so it cannot miss a valid transformation.

This structural induction proves both soundness and completeness.

**Why unique values help**

The contract gives unique values within each tree. When two non-null child roots have different values, the wrong orientation fails immediately rather than exploring deep ambiguous matches. This supports the linear traversal behavior of the exact implementation.

## Complexity detail

Let `n` be the total number of nodes examined and `h` the greater tree height.

With unique node values, each meaningful matching node pair is processed a constant number of times, and mismatched orientations stop immediately. Time complexity is `O(n)`.

The recursion stack follows at most one root-to-leaf path within each active conjunction, so auxiliary space is `O(h)`. Balanced trees use `O(log n)` stack depth, while chain-shaped trees use `O(n)`.

No tree nodes are copied or mutated.

## Alternatives and edge cases

- **Physically flip nodes during search:** This mutates input and complicates backtracking. Crossed recursive arguments represent the same choice safely.
- **Canonical tree serialization:** Recursively order child representations and compare canonical forms. It can be elegant but constructs extra strings or tuples.
- **Iterative stack of node pairs:** It avoids recursion-depth concerns but must still choose aligned or crossed children based on values.
- **Both trees empty:** The first base case returns true.
- **Exactly one tree empty:** The null mismatch returns false.
- **Different root values:** No flip can change values, so the result is immediately false.
- **Leaf nodes with equal values:** Both child pairs are empty, so the unflipped branch succeeds.
- **Already identical trees:** Every node succeeds through the aligned branch.
- **Flip required at several levels:** Each recursive pair independently chooses the crossed branch where needed.
- **Short-circuit evaluation:** It avoids evaluating unnecessary branches after success or obvious failure, which is important for keeping the search controlled.
