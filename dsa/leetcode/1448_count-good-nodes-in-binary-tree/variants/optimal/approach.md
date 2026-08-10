## General

**A node needs only one fact about its ancestors.** A node is good when no value on the root-to-node path is greater than its own value. It is unnecessary to carry the entire path to test this rule. The only ancestor information that matters is the maximum value seen so far. If the current value is at least that maximum, then it is at least every ancestor value and the node is good. If it is smaller, the ancestor that established the maximum proves the node is not good.

The recursive helper `dfs(root, mx)` carries exactly this summary. Here the parameter named `root` is the current node of the recursive call, while `mx` is the greatest value on the path before considering that current node. The outer method's root is simply the first current node passed into the helper.

The initial call uses `mx = -1000000`. Every legal node value is at least `-10000`, so this sentinel is smaller than the actual root value. The root therefore always passes the comparison, matching the definition: there is no earlier node on its path that could be greater.

**Handle an absent child immediately.** Recursive calls are made for both `root.left` and `root.right` even when a child is missing. The first condition returns when `root is None`. A missing child contains no node, contributes nothing to the count, and must not try to access `root.val`.

This early return also keeps the two recursive call sites simple. Each real node handles its own value and then delegates to both child positions without surrounding each call with a separate condition.

**Count a good node and update the path maximum.** The comparison `mx <= root.val` directly matches the definition. Equality is allowed: a node is disqualified only by an ancestor with a strictly greater value. If the comparison succeeds, `ans` is incremented through `nonlocal ans`.

The same successful comparison means the current node is at least as large as every earlier path value, so it becomes the maximum that its descendants should see. The code assigns `mx = root.val`. If the current node is not good, its value is below the existing maximum, so `mx` is deliberately left unchanged. In both cases, after the condition `mx` equals the maximum value on the path including the current node.

This conditional assignment is equivalent to writing `mx = max(mx, root.val)` after the count test. The stored form avoids a separate maximum call: on the true branch the current value is the maximum, and on the false branch the old value remains the maximum.

**Pass independent state down each branch.** The updated `mx` is passed to both children. Integers are immutable values in Python, and each recursive call receives its own local parameter binding. Work performed deeper in the left subtree cannot accidentally alter the path maximum used for the right subtree. Both children share exactly the ancestors down to the current node, so both should begin with the same updated maximum.

The count `ans` is different: it represents a global total across all branches, so every successful node must update the same outer integer binding. The declaration `nonlocal ans` tells Python that assignments inside `dfs` refer to the variable created in `goodNodes` rather than to a new local variable.

**Trace a path to see what mx means.** Consider path values `3, 1, 3`. The root sees the very small sentinel, is counted, and passes `mx = 3` downward. The node with value one fails `3 <= 1`, is not counted, and still passes `mx = 3`. The final node has value three, passes `3 <= 3`, and is counted. Equality with the earlier maximum is enough to be good.

On path `3, 4, 2`, the root sets the maximum to three. Value four is good and raises it to four. Value two then fails against four. The helper does not merely compare a node with its parent; it compares against the greatest value anywhere above it.

**The traversal order does not change the answer.** This DFS visits a node before its children, then explores the left subtree and the right subtree. Preorder is convenient because the ancestor maximum is ready when descending. However, what makes the method correct is that every node travels with the state for its unique root path. Visiting the right subtree before the left would produce the same count.

**The maintained invariant.** On entry to a real node, `mx` is the maximum value among its strict ancestors. The sentinel establishes this interpretation for the root. The comparison therefore labels the node correctly. After the conditional update, `mx` is the maximum over the ancestors plus the current node, exactly the value needed on entry to either child. Induction down the tree proves the invariant for every call.

Every real node is reached exactly once because a binary tree gives each non-root node one parent. The algorithm increments `ans` exactly when that node satisfies the good-node condition. Consequently, after DFS returns, `ans` equals the number of good nodes in the entire tree.

**Why the sentinel is safe but contract-dependent.** The chosen `-1000000` is not magical; it only has to be below every possible node value. The documented bound makes it safe. A more general implementation might pass negative infinity or initialize from `root.val` and count the root separately. For this exact problem, the fixed sentinel correctly avoids special root logic.

## Complexity detail

Let `n` be the number of real tree nodes and `h` its height. DFS performs constant work at each real node. It also makes calls on missing child positions, but a binary tree has only `O(n)` such positions, and each returns immediately. Total time is `O(n)`.

The recursive call stack contains at most one call per node along the current root-to-leaf path, so it uses `O(h)` space. A balanced tree has `h = O(log n)`, while a completely skewed tree has `h = n`. The manifest states the safe worst-case bound `O(n)`.

Apart from recursion, the algorithm stores the scalar counter and a constant amount of local information per active call. It does not build an array of path values or copy subtrees.

With up to `100000` nodes, a deeply skewed tree can exceed Python's default recursion limit even though the asymptotic reasoning is correct. An iterative stack avoids that runtime limitation while using the same worst-case `O(n)` memory.

## Alternatives and edge cases

- **Iterative depth-first search:** Store pairs of node and path maximum in an explicit stack. It preserves `O(n)` time and worst-case space while avoiding Python recursion-depth failures.
- **Breadth-first search:** A queue can carry the same node-and-maximum pairs. It is equally correct because each node has one root path, but its memory is governed by maximum tree width rather than height.
- **Carry the whole path:** Recomputing a maximum from a path list at every node adds unnecessary storage and can lead to quadratic time. One running maximum is a sufficient summary.
- **Compare only with the parent:** This is incorrect. A node can exceed its parent while still being smaller than a more distant ancestor.
- **Return subtree counts instead of nonlocal ans:** Each call can return its own good indicator plus left and right counts. That removes shared state and is equally valid, though the stored source uses one outer accumulator.
- **Use negative infinity:** `float("-inf")` is a general sentinel below every integer and avoids relying on value constraints. The fixed integer sentinel is safe for the stated range.
- **Single-node tree:** The sentinel is below the root, so it is counted and the answer is one.
- **All values equal:** Equality is permitted, so every node is good.
- **Strictly increasing root-to-leaf paths:** Every later node establishes a new maximum and is good.
- **Strictly decreasing path:** Only the root is good because its value remains the path maximum for every descendant.
- **Negative values:** The comparison works normally. The sentinel is far below the minimum allowed value, so a negative root is still counted.
- **Duplicate maximum:** A descendant equal to the greatest ancestor is good because the condition rejects only a strictly greater ancestor.
- **Missing children:** Calls on `None` return before accessing fields and add nothing.
- **Branch independence:** A large value in the left subtree must not affect a node in the right subtree because it is not on that node's root path. Per-call `mx` bindings preserve this separation.
- **Very deep tree:** The algorithmic result remains correct, but an iterative implementation is safer under Python's default recursion limit.
- **Nonempty-tree guarantee:** The source assumes a real root. If an empty tree were allowed, the helper would return and `ans` would correctly remain zero, despite the type contract normally providing a node.
