## General

A tree is height-balanced only when the condition holds at every node, not merely at the root. For each node, the heights of its left and right subtrees must differ by at most one, and both child subtrees must themselves be balanced.

A direct top-down implementation could calculate the two heights, compare them, and then separately recurse to check the children. That repeats height work: a descendant's height may be recomputed for several ancestors. The selected solution avoids the repetition by making one postorder traversal return both pieces of information in a single integer.

**One return value carries two meanings**

The nested `height(root)` function uses this convention:

- return a nonnegative integer when the subtree is balanced; that integer is its height;
- return `-1` when the subtree is not balanced.

This works because genuine heights in the chosen convention can never be negative. An empty tree has height zero, a leaf has height one, and every larger tree has height one plus a child height. Therefore `-1` is unambiguous: it cannot be mistaken for a valid result.

Using a sentinel is a compact substitute for returning a pair such as `(is_balanced, height)`. It lets every caller learn both whether a child is valid and, when it is valid, how tall it is.

**Why postorder is the natural traversal**

The balance decision at a node depends on information about both children. That information must be known before the parent can be decided. Postorder traversal does exactly this: solve the left subtree, solve the right subtree, and then process the current node.

For a nonempty node, the source evaluates `l, r = height(root.left), height(root.right)`. If either result is `-1`, some descendant on that side already violates the balance condition. A tree containing an unbalanced subtree is also unbalanced, so the current call returns `-1` without trying to reinterpret that value as a height.

If both child results are valid heights, the call checks `abs(l - r) > 1`. A difference of zero or one is permitted. A difference of two or more makes the current node the first detected violation on this return path, so the call again returns `-1`.

Only when both children are balanced and their height difference is at most one does the function return `1 + max(l, r)`. The longest downward path from the current node consists of the current node plus the taller child's longest path, which is why the maximum—not the sum—is used.

**Why the root test answers the whole problem**

Consider any call after both child calls have finished. If a child is unbalanced, its `-1` is propagated. If both are balanced but the current height difference is too large, this call creates `-1`. Otherwise it returns the exact height of a balanced subtree.

Starting at leaves, this rule establishes the return convention for the smallest trees. Applying the same reasoning upward establishes it for every larger subtree. By the time `height(root)` returns, a nonnegative value means every node below the root passed its local check; a negative value means at least one node failed.

The public expression `height(root) >= 0` converts that encoded result into the required Boolean. It does not care about the actual balanced height once validity is known.

**Tracing a balanced example**

In `[3,9,20,null,null,15,7]`, nodes `9`, `15`, and `7` are leaves, so each returns one. Node `20` receives heights one and one and returns two. Root `3` receives one from the left and two from the right; their difference is one, so it returns three. Since three is nonnegative, the public method returns `True`.

The empty tree follows the same logic without a special public branch. `height(None)` returns zero, and zero is nonnegative, so an empty tree is correctly considered balanced.

**Tracing where imbalance propagates**

In `[1,2,2,3,3,null,null,4,4]`, the lower leaves return one. Their parent returns two, but eventually a node receives child heights two and zero. Their difference exceeds one, so that node returns `-1`.

Every ancestor that receives this sentinel also returns `-1`, even if the ancestor's other child happens to have a numerically similar height. Once a descendant violates the rule, no ancestor can make the entire tree balanced again.

**Eager sibling evaluation in the exact source**

Python evaluates both right-hand expressions in the tuple assignment before executing the following `if`. Thus the right subtree is still traversed even when the left call has already returned `-1`. The sentinel prevents incorrect height arithmetic and propagates the answer, but this particular source does not short-circuit the sibling traversal.

That choice does not harm the $O(n)$ bound: each tree node is still reached once. A slightly different implementation could call the left side, immediately return on `-1`, and only then call the right side. Such an implementation may do less work on an early failure, but it has the same worst-case complexity.

**Source-level dependencies**

The file assumes `Optional` and `TreeNode` are supplied by the surrounding environment. The commented node definition is documentation, not active Python. The algorithm never inspects `val`; only `left` and `right` matter, so arbitrary node values within the contract do not affect the result.

## Complexity detail

Let $n$ be the number of nodes and $h$ the tree height measured as the maximum number of nodes on a root-to-leaf path. Every node's `height` call performs constant local work after exactly one call for each child. No subtree height is recomputed by an ancestor. Total time is therefore $O(n)$.

The active recursion stack follows one root-to-descendant path at a time and uses $O(h)$ space. For a balanced tree, $h=O(\log n)$. For a completely skewed input, $h=O(n)$, so the worst-case auxiliary space is $O(n)$. The manifest's $O(h)$ expresses both cases precisely.

No collection proportional to the number of nodes is allocated. Each frame stores the node reference and two integer results. The returned answer is a single Boolean, so there is no separate output-space term of significance.

Even on an unbalanced input, eager evaluation visits at most all $n$ nodes once. A short-circuit version can improve best-case work when a shallow violation appears, but worst-case time remains linear because a balanced tree must be fully inspected.

## Alternatives and edge cases

- **Boolean-and-height pair:** Return `(True, height)` or `(False, any_height)` instead of using `-1`. It is more explicit for beginners but carries the same information and complexity.
- **Short-circuit postorder:** Evaluate the left child, return immediately if it is unbalanced, then evaluate the right child. It may avoid visiting an unnecessary sibling subtree.
- **Top-down repeated height calculation:** Check heights at each node with a separate height function. It is conceptually direct but can repeat work and reach $O(n\log n)$ on balanced trees, with worse patterns possible without early stopping.
- **Iterative postorder:** Use an explicit stack and a map from nodes to computed heights. It avoids Python call-stack limits but generally needs $O(n)$ stored height information.
- **Empty tree:** Returns `True` because height zero is a valid balanced height.
- **Single node:** Both empty children have height zero, so the leaf returns height one and is balanced.
- **Difference exactly one:** This is allowed; only a difference greater than one fails.
- **Deep violation:** The `-1` sentinel propagates through every ancestor, so checking only `height(root) >= 0` is sufficient.
- **Node values:** Values may be negative, positive, repeated, or unordered; balance depends solely on shape.
- **Skewed tree:** It is quickly determined to be structurally unbalanced, but the recursive call depth can still approach $n$ before results return.
- **Python recursion limit:** The constraint permits 5,000 nodes. A sufficiently deep chain can raise `RecursionError` in a default Python environment even though the algorithmic space bound is correct.
- **Height convention:** This source gives an empty tree height zero and a leaf height one. Using empty height `-1` and leaf height zero is equally valid if the sentinel is changed so it cannot collide with a real height.
- **Sentinel collision:** Never use zero as the failure marker under this convention, because zero is the legitimate height of an empty subtree.
