## General

The competitive source uses the `next` pointers it has already established on one level to connect the level below it. That eliminates the queue: a completed level is itself a linked list from left to right.

The perfect-tree guarantee makes the method especially simple. Every non-leaf has both a left and a right child, and the leftmost node of the next level is always `head.left`.

**The outer-loop invariant**

At the start of an outer iteration, `head` is the leftmost node of one level, and all `next` links across that level are already correct.

This is true initially because the first level has only the root, whose initial `next` is null. The inner loop uses those valid links to walk every parent on the level and construct all links among their children.

After the level is complete, `head = head.left` descends to the next level's leftmost node. The newly created child links make the invariant true again.

At a leaf level, `head.left` is absent. The inner condition `cur and cur.left` skips all linking, and the outer update moves `head` to `None`, ending the traversal.

**The two kinds of child connection**

Every node on a non-leaf level needs two local operations.

First, `cur.left.next = cur.right` connects siblings. The left child and right child share the same parent, so both references are immediately available.

Second, if `cur.next` exists, `cur.right.next = cur.next.left` bridges between parent families. The current parent's right child is immediately followed horizontally by the next parent's left child. Because the current level's `next` links are already complete, `cur.next` provides access to that neighboring parent without a queue or parent pointer.

If `cur.next` is absent, `cur` is the rightmost parent. Its right child is the rightmost node of the next level and must point to null. The source leaves that pointer untouched, relying on the contract that all `next` fields initially start as null.

**Why processing must be top-down**

The cross-parent assignment needs `cur.next` before it can find `cur.next.left`. Therefore the parent level must be fully linked before its child level is constructed.

The outer loop enforces exactly that order. It never descends until the inner loop has followed `cur.next` across every parent and assigned both sibling and cross-parent child links.

Trying to start from the leaves would provide no convenient way to discover a node's horizontal neighbor because the nodes do not have parent pointers.

**Tracing the perfect seven-node tree**

At level zero, `head` and `cur` are node one. The sibling assignment creates `2.next = 3`. Node one has no horizontal neighbor, so node three remains linked to null.

The outer loop descends to node two. Its sibling assignment makes `4.next = 5`. Because `2.next` is node three, the cross-parent assignment makes `5.next = 3.left`, which is node six.

Advancing `cur = cur.next` reaches node three. It assigns `6.next = 7`; no next parent exists, so seven remains null. The next outer iteration starts at leaf four and performs no assignments.

The resulting levels are `1`, then `2 -> 3`, then `4 -> 5 -> 6 -> 7`.

**Why all links are covered**

Within a child level, every adjacent pair is either:

- two children of the same parent; or
- the right child of one parent followed by the left child of its next parent.

The two assignments cover exactly those cases. The last child has no successor and retains null. No other horizontal relationship exists in a perfect binary tree.

The inner loop reaches every parent because the current level's links are valid by the outer invariant. The completed child links then make that same traversal possible one level lower. Induction from the one-node root level proves correctness for the whole tree.

**Constant workspace and mutation**

Only `head` and `cur` are traversal references. The algorithm uses the output fields themselves as navigation infrastructure, so no queue, stack, or collection grows with the input.

It does not alter `left`, `right`, or `val`. The original tree shape remains, augmented with horizontal links.

**Return-contract discrepancy**

The active `Solution.connect` has no explicit `return`. Python therefore returns `None` after mutating the tree. The local Reference contract requires returning the original root.

Under an older void-style platform contract, this implementation's return behavior is expected. Under the current package contract, the pointer mutation is correct but the returned value is not. Adding `return root` would reconcile it, but the protected solution is not modified in this documentation campaign.

The file also contains `Solution2`, a recursive alternative. The selected class is the first `Solution`; the recursive class is not part of its execution.

## Complexity detail

Let $n$ be the number of nodes. Each internal node is visited once by `cur` and performs a constant number of pointer assignments and checks. The final leaf level is reached only by its leftmost node before the inner loop stops. Total time is $O(n)$; more precisely, work is proportional to the internal-node count, which is linear in a perfect tree.

The method stores only two node references regardless of tree size, so auxiliary space is $O(1)$. It satisfies the follow-up's workspace requirement without relying on ignored recursion space.

All new `next` fields are the required output inside existing nodes. No output container is allocated.

The source's complexity comments and manifest match the mutation algorithm. The separate return-value incompatibility does not change the traversal's asymptotic bounds, though it prevents full compliance with the package function contract.

## Alternatives and edge cases

- **Breadth-first queue:** Process exact level sizes and connect consecutive dequeued nodes. It works for arbitrary binary trees but uses $O(w)$ auxiliary space.
- **Recursive `Solution2`:** Connect siblings and cross-parent children, then recurse. It is concise and the follow-up permits ignoring implicit stack space, but standard analysis gives $O(h)$ stack use.
- **Return-root repair:** Add `return root` after the outer loop to satisfy the current package contract while preserving all pointer behavior and complexity.
- **Explicitly clear level tails:** Assign each rightmost child's `next` to `None` if the input may contain stale links.
- **Empty tree:** Both loops skip and the source returns `None`, which coincides with the empty root.
- **Single node:** No link changes are needed; however, the source still returns `None` rather than the root object.
- **Perfect-tree dependency:** `head = head.left` and direct child access rely on every internal node having two children. The same code is not a general solution for sparse trees.
- **Sibling link:** Always connect a parent's left child to its right child.
- **Cross-parent link:** Exists only when the parent has a horizontal successor.
- **Right edge of a level:** Its initial null link is retained.
- **Initial `next` guarantee:** The traversal and level-tail correctness assume links start null. Stale cycles could make `cur = cur.next` unsafe.
- **Top-down order:** Child-level bridges cannot be formed until parent-level links are available.
- **No queue hidden in the tree:** Traversing `next` fields uses required output pointers, so it does not add auxiliary storage.
- **Node class name:** The source calls its compatible structure `TreeNode`, while the Reference calls it `Node`; the accessed fields are the relevant interface.
- **Values:** Horizontal positions, not values, determine every assignment.
