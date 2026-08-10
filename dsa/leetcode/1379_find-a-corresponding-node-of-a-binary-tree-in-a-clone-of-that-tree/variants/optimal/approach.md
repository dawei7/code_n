## General

**Traverse the two trees in lockstep**

The cloned tree has exactly the same structure as the original, but its nodes are different objects. If a traversal takes the same sequence of left and right edges in both trees, the two current nodes always occupy corresponding positions.

The nested helper `dfs(root1, root2)` maintains this positional invariant:

- `root1` is a node in the original tree.
- `root2` is the node at the identical position in the cloned tree.

The initial call `dfs(original, cloned)` clearly satisfies it at the roots. When recursion calls `dfs(root1.left, root2.left)` or the corresponding right-child pair, taking the same edge preserves it.

**Why comparing the original node reference matters**

The target argument is a reference to the particular node object in the original tree. The search must identify that object and return the paired object from the clone. It must never return `target` itself, because that object belongs to the original tree.

The exact condition is `root1 == target`. In the provided `TreeNode` model, no custom value-based equality method is defined, so `==` uses object identity and succeeds only for the target object. Writing `root1 is target` would express the identity intent even more explicitly.

Identity comparison also answers the follow-up with repeated values. If several nodes store the same value, a value comparison such as `root1.val == target.val` might stop at the wrong position. Comparing the node reference still selects precisely the supplied target object, regardless of duplicates.

**The recursive control flow**

If `root1 is None`, this original-tree position contains no node and cannot be the target, so the helper returns `None`. Because the clone has the same structure, `root2` is also null at this position.

If `root1` is the target, the lockstep invariant proves `root2` is its corresponding clone node. Returning `root2` immediately gives the required reference.

Otherwise, the method searches the paired left subtrees and then the paired right subtrees:

`dfs(root1.left, root2.left) or dfs(root1.right, root2.right)`.

In Python, `or` returns the first truthy operand, not merely a Boolean. If the left search finds the node, it returns a `TreeNode` object, which is truthy, and the right search is skipped. If the left search returns `None`, evaluation continues to the right and returns its result.

This is a preorder depth-first search because the current original node is checked before its children. The exact visit order does not affect correctness; synchronized movement is what matters.

**A positional example**

Suppose the target is reached by going right from the root and then left. The first paired call holds both roots. The right recursion holds the original right child and cloned right child. Its left recursion then holds the target and the cloned node reached by the same right-left path. The identity check succeeds on the original side, and the helper returns the cloned-side node without relying on its value.

**Why no map from original to clone is needed**

One could traverse both trees first and build a dictionary mapping every original node to its clone. That stores $N$ associations even though only one target is queried. Lockstep DFS implicitly carries the mapping for the current position through its two parameters and stops as soon as the target is found.

**Why the algorithm is correct**

Prove the lockstep invariant by induction on recursion depth. It is true for the two roots. If it is true for a node pair, identical tree structure means their left children correspond and their right children correspond, so it remains true in either recursive child call.

The DFS examines every original node unless it finds the target earlier. The contract guarantees the target belongs to the original tree, so eventually a call has `root1` equal to that exact object. By the invariant, its `root2` is the corresponding node in the clone, and that is what the method returns. No other call can pass the identity test. Short-circuit propagation carries the found cloned reference unchanged back to the outer call.

The method never changes a child pointer, value, tree, or target. It only reads references, satisfying the no-modification rule.

## Complexity detail

Let $N$ be the number of tree nodes and $H$ the tree height. In the worst case, the target is visited last in DFS order, so every node is checked once. Time is $O(N)$.

The recursive stack follows one root-to-current path and uses $O(H)$ space. A balanced tree has $H=O(\log N)$, while a skewed tree has $H=O(N)$. The manifest's $O(N)$ space is the correct worst-case bound; $O(H)$ is the sharper shape-sensitive statement.

Short-circuiting may stop much earlier when the target lies near the beginning of preorder, but worst-case analysis cannot assume its position.

## Alternatives and edge cases

- **Iterative paired DFS:** Store tuples of corresponding nodes on a stack. It preserves the same invariant and avoids recursion-depth issues, using up to $O(N)$ explicit space.
- **Paired breadth-first search:** Queue corresponding nodes level by level. It is correct but may hold an entire wide level, and depth order provides no special benefit here.
- **Inorder traversal:** Traverse left, current, right in both trees. It works, but preorder can test the root immediately and is simpler in the exact implementation.
- **Map every node pair:** Build an original-to-clone dictionary, then look up `target`. This supports repeated queries but wastes $O(N)$ retained mapping space for one query.
- **Compare values:** Unique values make it appear sufficient in the base problem, but it fails the repeated-value follow-up and ignores the fact that `target` is already an object reference.
- **Target is the root:** The first comparison succeeds and returns `cloned` immediately.
- **Target is a leaf:** Null children return `None` normally; the target leaf itself is checked before descending.
- **Target in the right subtree:** The left search returns `None`, causing `or` to evaluate and return the right search.
- **Repeated values:** Reference identity still finds the correct position; no value uniqueness is needed by the traversal.
- **Identical structure:** Accessing `root2.left` alongside `root1.left` is safe because the clone is guaranteed to have the same shape.
- **Target membership:** The contract guarantees a result. Without that guarantee, the helper would exhaust the tree and return `None`.
- **Equality semantics:** The exact `==` behaves as identity for the supplied node class. `is` would be safer if a future class defined value-based `__eq__`.
- **No mutation:** Unlike Morris traversal, this DFS does not temporarily rewrite tree pointers.
- **Recursion depth:** A skewed tree with up to 10,000 nodes can exceed Python's default recursion limit; an explicit paired stack avoids that operational failure.
