## General

The competitive source answers two questions about every subtree at the same time:

- if the subtree is balanced, what is its height?
- if it is not balanced, how can that failure be reported to its parent?

It encodes both answers in the return value of `getHeight`. A nonnegative value is a genuine height, while `-1` is a failure sentinel. This bottom-up design avoids the redundant subtree scans of a top-down method that repeatedly asks for heights.

**The height and sentinel convention**

`getHeight(None)` returns zero. Consequently, a leaf receives zero from each child and returns `max(0, 0) + 1`, which is one. All valid heights are therefore at least zero, leaving `-1` safely outside the valid range.

For a real node, the helper obtains `left_height` and `right_height`. Three conditions make the current subtree invalid:

- `left_height < 0`, meaning the left subtree already found an imbalance;
- `right_height < 0`, meaning the right subtree already found one; or
- `abs(left_height - right_height) > 1`, meaning both children are balanced but this node violates the allowed height difference.

If any condition holds, the helper returns `-1`. Otherwise it returns one plus the larger child height.

Testing `< 0` rather than `== -1` is slightly more general than necessary for this exact helper, which emits only `-1` as a negative result. It clearly communicates that every negative value is invalid rather than a usable height.

**Why child results must come first**

Balance at a node cannot be determined from the node itself. It depends on the complete heights and validity of both children. The recursion therefore follows postorder: left child, right child, current node.

When both child calls return nonnegative numbers, those numbers are exact heights. Their absolute difference directly tests the local balance rule. When either returns a negative number, the corresponding subtree contains a violation somewhere below, and the current subtree must also be classified as unbalanced regardless of its other side.

This gives a compositional guarantee: each completed call summarizes an entire subtree in one integer. Parents never need to traverse that subtree again.

**Why no violation can be missed**

An empty subtree returns valid height zero. A leaf therefore returns valid height one. Assume both child calls correctly return either their balanced heights or `-1`.

If either child is invalid, propagating `-1` is correct because every subtree of a balanced tree must itself be balanced. If both are valid but differ by more than one, the current root violates the definition. If neither case applies, both children are balanced and the current difference is permitted, so the current subtree is balanced and `max(...) + 1` is its exact height.

This reasoning applies upward from the leaves to the original root. Hence `getHeight(root) >= 0` is true exactly when no node in the entire tree violates the rule.

**Example flow**

For the balanced example with root `3`, leaf `9` returns one. Leaves `15` and `7` also return one, allowing node `20` to return two. Root `3` compares one and two, accepts their difference of one, and returns three. The public comparison converts three to `True`.

In the unbalanced example, the deepest leaves first return one. At the first ancestor whose child heights differ by two, the helper returns `-1`. That negative result travels upward; ancestors do not accidentally treat it as a very short legitimate subtree.

For `root = None`, `getHeight` returns zero. The comparison `0 >= 0` yields `True`, matching the definition that an empty tree is height-balanced.

**What the exact evaluation order does**

The continued line assignment evaluates both recursive calls before the subsequent condition. Python does not stop after the left result becomes negative; it still computes the right height. Therefore this implementation is bottom-up and failure-propagating, but not maximally short-circuiting.

It remains linear because no node is evaluated more than once. A left-first version with an immediate negative check could save work on some unbalanced inputs, especially when a violation is found near the left side of the root, but it cannot improve the worst-case asymptotic bound.

**Tree class and data independence**

The source defines a module-level `TreeNode` with `val`, `left`, and `right`. The method can also operate on any compatible node object supplied by the harness because it only reads the two child attributes. It never compares or changes values, and it does not mutate any tree links.

## Complexity detail

Let $n$ denote the node count. `getHeight` is called once for every real node, plus constant-cost calls for empty child positions. Each real call performs a constant number of comparisons, one absolute difference, and one maximum. Total running time is $O(n)$.

Let $h$ be the maximum root-to-leaf path length. At most one recursive path is active at any moment, so the call stack uses $O(h)$ auxiliary space. This becomes $O(\log n)$ for a balanced tree and $O(n)$ for a chain.

The algorithm stores no height map or node collection. Once a child call returns, its entire subtree is represented by one integer. The final output is one Boolean and requires $O(1)$ output space.

Because both child calls are eagerly evaluated, an early sentinel does not guarantee sublinear work on an unbalanced tree. The worst case and the simple exact upper bound are both $O(n)$. A short-circuit variant has the same worst case but potentially better early-failure behavior.

## Alternatives and edge cases

- **Explicit `(balanced, height)` result:** A tuple avoids sentinel encoding and can make the two meanings clearer, at the cost of a slightly larger return object per call.
- **Left-first short circuit:** Return as soon as the left result is negative, then do the same after the right call. This preserves correctness while sometimes visiting fewer nodes.
- **Repeated top-down height checks:** Compute child heights and separately call `isBalanced` below them. It is easy to derive from the definition but repeats work and is asymptotically weaker.
- **Iterative postorder with a height dictionary:** Avoid recursive stack overflow by processing nodes with an explicit stack. The dictionary can use $O(n)$ memory.
- **Empty input:** Height zero is valid, so the result is `True`.
- **One node:** Child heights are both zero, and the node is balanced with height one.
- **Exactly one level of difference:** `abs(...) > 1` correctly allows a difference of one.
- **Violation in either child:** A negative child result is propagated even if the other child's numerical height would make the local difference appear small.
- **Arbitrary values:** The balance definition ignores `val`; only the topology matters.
- **No mutation:** The source reads links but never rewires the input tree.
- **Tall skewed input:** Auxiliary space grows to $O(n)$ and the result is false once returns expose a two-level difference.
- **Python stack limit:** A chain with thousands of nodes can exceed the interpreter's recursion limit before returning a Boolean. An iterative postorder implementation avoids that runtime limitation.
- **Alternative height origin:** Empty height `-1` and leaf height zero are common, but then `-1` cannot also serve as the imbalance sentinel. A distinct marker such as `None` or a more negative value would be required.
- **Why `max`, not addition:** Tree height follows the longest downward path. Adding child heights would measure neither height nor balance correctly.
