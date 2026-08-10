## General

The selected competitive class validates the same strict-inorder property but uses Morris traversal rather than recursion or a stack. It temporarily points an inorder predecessor's empty right link back to an ancestor, creating a route for returning after the left subtree. On a completed valid traversal, every such thread is removed.

`prev` stores the previously visited node object, while `cur` is the current traversal node. Comparing node values through these references avoids needing a numerical sentinel, so the full 32-bit value range is handled naturally.

**When `cur` has no left child**

There is no unvisited left subtree, so inorder visits `cur` immediately. If `prev` exists and `prev.val >= cur.val`, the sequence is not strictly increasing and the method returns false. Otherwise `prev` becomes `cur`, and traversal moves to `cur.right`.

That right link may be an original right child or a temporary thread returning to an ancestor.

**When `cur` has a left child**

The method finds the rightmost node in `cur.left`, which is `cur`'s inorder predecessor. The search stops if its right link is empty or already points to `cur`.

- If `node.right is None`, this is the first encounter with `cur`. The code installs `node.right = cur` and descends left without visiting `cur`.
- Otherwise the thread proves the left subtree has finished and traversal has returned for a second encounter. The current node is now next in inorder.

On a normal second encounter, the code checks strict increase, removes the thread, records `cur` in `prev`, and moves right.

**Why local inorder comparison validates the whole BST**

Inorder places every left-subtree node before its ancestor and every right-subtree node afterward. If each visited value is strictly larger than the immediately previous value, transitivity makes every earlier value smaller than every later value. Thus all left descendants are smaller than their ancestor and all right descendants are larger.

Conversely, a valid BST necessarily has a strictly increasing inorder sequence. Morris changes only how traversal remembers its return path; it visits nodes in the same order as recursive inorder.

**Why the nested predecessor search remains linear**

Although a `while` loop appears inside the outer traversal, each relevant right edge is followed only a constant number of times: while installing a thread and while finding it for removal. A tree has $n-1$ original edges, so aggregate predecessor-search work is linear rather than $O(nh)$.

**Restoration on the successful path**

A thread is installed only into a right pointer that was originally `None`. On the matching second encounter, it is reset to `None`. If traversal reaches the final `True`, every created thread has been encountered again and removed, so the input tree is restored exactly.

**The early-failure mutation defect**

The exact source checks for an ordering violation and returns immediately. On a second encounter, it performs the comparison before `node.right = None`. Therefore a violation at that node leaves even its current predecessor thread installed.

A violation in the no-left-child branch can also occur while threads for one or more ancestors remain active. Returning skips their future removal. The Boolean answer is still correctly false, but the caller's tree may now contain temporary back-links and cycles.

This is materially different from a fully restoration-safe Morris validator. A robust version must clean all active threads before returning, or record invalidity and continue traversal solely to remove threads. Using an explicit stack avoids temporary mutation entirely.

The later `Solution2` in the file uses recursive bounds and does not have this restoration issue; it is not the selected first class.

## Complexity detail

On a complete traversal, each node and edge is processed a constant number of times, so time is $O(n)$. Failure may return earlier.

The selected Morris algorithm keeps only `prev`, `cur`, and `node` references, so its intended auxiliary space is $O(1)$. This conflicts with the manifest's $O(h)$ claim, which matches the unselected recursive `Solution2`, not the selected class. The temporary threads occupy existing tree fields rather than an additional collection.

If one modifies the algorithm to track active threads explicitly for cleanup, that tracking can require $O(h)$ space; continuing the Morris traversal after detecting invalidity can retain $O(1)$ space.

## Alternatives and edge cases

- **Recursive bounds:** Pass exclusive `(low, high)` limits. It uses $O(h)$ stack space but never mutates the tree and can safely short-circuit.
- **Iterative inorder stack:** Compare successive values with $O(h)$ storage and no recursion-depth risk.
- **Restoration-safe Morris:** Set a flag on violation and continue traversing until all threads are removed, returning the flag at the end.
- **Duplicate keys:** The `>=` comparison rejects equal adjacent inorder values.
- **First visited node:** `prev is None` skips comparison without inventing a sentinel.
- **Extreme integer values:** Node-to-node comparison handles both allowed endpoints without overflow or sentinel collision.
- **Single node:** It has no left child, becomes `prev`, and returns true.
- **Skewed tree:** Time remains linear. Morris uses constant auxiliary storage where recursion might overflow.
- **Caller-visible mutation:** A false return from this exact source may leave the tree changed; do not traverse or reuse it afterward without repairing or rebuilding it.
- **Supporting class:** The top-level `TreeNode` definition is harness support and does not alter the traversal analysis.
