## General

**Choose one reference value**

A tree is uni-valued exactly when every node equals the root's value. The code stores `x = root.val` and recursively verifies that condition.

The contract guarantees at least one node, so reading `root.val` is safe. If empty trees were allowed, the outer function would need a separate null check.

**Meaning of the helper**

`dfs(root)` returns true when every node in the subtree rooted at `root` has value `x`.

For `root is None`, the subtree contains no counterexample, so it returns true. This identity lets leaves pass naturally because both missing-child calls return true.

For a real node, three conditions must all hold:

- `root.val == x`;
- the left subtree contains only `x`;
- the right subtree contains only `x`.

The return expression joins these conditions with `and`.

**Why short-circuiting helps**

Python evaluates `and` from left to right.

If the current value differs, neither subtree is explored because the answer is already false. If the left subtree fails, the right subtree is skipped.

This does not improve the worst-case linear bound, but it can terminate much earlier when a mismatch appears near the root.

**Trace**

For root value one, every visited node is compared with one. Missing children return true. If all nodes equal one, every conjunction resolves to true from leaves back to the root.

If a node with value five appears under a root with value two, its call evaluates `root.val == x` as false and returns without descending farther. That false propagates through parent calls.

**Why one captured value is sufficient**

Another valid method compares each child with its parent. Along a connected tree, transitivity would make all nodes equal to the root.

Using one captured `x` is simpler. Every recursive call has the same contract and every node is checked against the same standard.


The empty subtree correctly returns true.

Assume recursive calls correctly decide smaller subtrees. A nonempty subtree is uni-valued with reference `x` exactly when its root equals `x` and both child subtrees contain only `x`. The helper returns that exact conjunction.

Structural induction proves the outer result is true precisely for a uni-valued tree.

**No visited set is needed**

A proper binary tree has one path from the root to each node and contains no cycles. Recursion reaches each node once. A visited set would add memory without preventing any repeated traversal.

The method does not modify node values or child links.

**Why an empty subtree returns true rather than false**

The helper's question is whether every node in a subtree has value `x`. An empty subtree has no node that violates the condition, so the statement is vacuously true.

Returning false for a missing child would incorrectly reject every leaf, because every finite tree eventually reaches missing child references. Using true makes the recursive conjunction behave correctly: only real mismatching nodes can cause failure.

**How false propagates**

Suppose a mismatch occurs several levels below the root. That call returns false. Its parent combines the false child result with `and` and returns false as well. This continues through every ancestor until the outer call receives false.

No special global variable is necessary. The Boolean return value itself carries the discovery upward through the call stack.

**Why skipped subtrees cannot rescue a failure**

When short-circuiting skips a subtree, one earlier condition is already false. A uni-valued tree requires every condition to hold, so no result from the skipped subtree could change the final answer back to true.

Likewise, when the current node and left subtree are valid, evaluating the right subtree is necessary and does occur. Short-circuiting saves only work that is logically irrelevant.

**A structural view**

The property is hereditary: if the whole tree is uni-valued, each child subtree is uni-valued with the same reference. Conversely, if the root matches `x` and both child subtrees satisfy the property, their union with the root also satisfies it.

This exact decomposition is why the simple recursive conjunction is complete rather than merely a useful heuristic.

## Complexity detail

Let `N` be node count and `H` tree height.

In the all-equal case, every node is visited once and performs constant work, so time is `O(N)`. A mismatch may terminate traversal earlier.

The recursion stack contains at most one root-to-leaf path, giving `O(H)` auxiliary space. Balanced trees have `O(log N)` height; chain-shaped trees have `O(N)`.

## Alternatives and edge cases

- **Iterative DFS:** Use an explicit stack and compare every node with the root value. It avoids recursion limits.
- **Breadth-first search:** A queue works but may hold an entire wide level.
- **Collect values in a set:** Check whether the final set has size one. It uses extra memory and typically scans the whole tree.
- **Compare parent and child:** Correct through transitivity, but the single root reference gives a cleaner invariant.
- **Single node:** Both children are empty and the answer is true.
- **All values equal:** Every node succeeds.
- **Mismatch near the root:** Short-circuiting stops quickly.
- **Mismatch deep in the tree:** False propagates through every ancestor call.
- **Value zero:** It is an ordinary valid reference.
- **Empty child:** It returns true because absence cannot violate equality.
- **Nonempty-root guarantee:** The outer code relies on it before reading `root.val`.
