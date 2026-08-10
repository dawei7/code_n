## General

The active competitive `Solution` constructs the flattened chain from back to front. Desired preorder is root, left, right. Reversing that processing order gives right, left, root. If recursion first prepares the suffix that comes after a node, the node can point directly to that suffix and become the new head.

The helper `flattenRecu(root, list_head)` returns the head of a chain containing the preorder traversal of `root`'s subtree followed by the already prepared chain `list_head`.

This contract explains both the unusual right-before-left recursion and the second parameter.

**The suffix passed into an empty subtree**

If `root` is absent, the subtree contributes no nodes. The correct result for “empty subtree followed by `list_head`” is simply `list_head`, so the base case returns it unchanged.

This behavior makes missing children natural. A missing right child leaves the caller's suffix untouched, and a missing left child leaves the flattened right chain untouched.

**Why the right subtree is processed first**

For a real root, the final local order must be:

`root -> flattened left subtree -> flattened right subtree -> incoming suffix`.

The helper begins with `flattenRecu(root.right, list_head)`. By the helper contract, this returns a chain containing the right subtree followed by the incoming suffix. The returned head is stored back in `list_head`.

It then calls `flattenRecu(root.left, list_head)`. Now the suffix passed to the left call already begins with the flattened right subtree. The returned chain is therefore the flattened left subtree followed by the flattened right subtree and then the original suffix.

Finally, the source assigns `root.right = list_head`, clears `root.left`, and returns `root`. The current root becomes the head in front of the prepared left-right suffix. That yields the exact preorder sequence.

**A small call-level example**

Suppose a node has left subtree `L`, right subtree `R`, and an incoming continuation `S`.

After the right call, `list_head` represents `preorder(R) -> S`. After the left call, it represents `preorder(L) -> preorder(R) -> S`. Linking the node produces:

`node -> preorder(L) -> preorder(R) -> S`.

This is the helper promise for the current subtree. The base case establishes the promise for empty trees, and the two recursive transformations preserve it for every real node.

**Tracing the Reference tree**

For root one, recursion first enters the original right subtree rooted at five. It processes six, links five to six, and returns five as the head of that suffix.

The recursion then processes the left subtree rooted at two while passing five as its continuation. Within that subtree, node four is processed before node three in reverse construction order. The resulting returned head is two, whose chain is `2 -> 3 -> 4 -> 5 -> 6`.

Finally root one points right to that head and clears its left pointer. The caller's original root now begins `1 -> 2 -> 3 -> 4 -> 5 -> 6`.

The runtime execution order is not the same as the final traversal order. Processing right first is necessary precisely because nodes are being prepended to an already built suffix.

**Why mutation does not destroy unprocessed subtrees**

Both original child recursions complete before the source overwrites the current node's `right` and `left` fields. Therefore the method still has access to the original right and left subtrees when it needs them.

After they are flattened, their relevant heads are held in `list_head`; original child pointers are no longer needed. Assigning `root.right` to the combined suffix and clearing `root.left` safely commits the current node.

No new tree nodes are created. Every original node becomes exactly one element of the right chain, and every left pointer is cleared when that node's call finishes.

**Public return behavior**

`flatten` calls the helper with `None` as the suffix but deliberately ignores the returned head. That is correct because the head of the flattened entire tree is the same original `root` object. The helper mutates it in place.

The public method has no explicit return and therefore returns `None`, satisfying the function contract.

**Active `Solution` versus `Solution2`**

The file also defines `Solution2`, which uses a mutable `list_head` attribute and the same reverse-preorder concept. Under the standard class name, the active implementation is the first `Solution`.

The active helper passes its suffix explicitly, so it has no persistent cross-call state. `Solution2.list_head`, by contrast, is declared at class scope and is not reset in `flatten`; reusing an instance across separate trees could link a later tree to stale state. That issue does not apply to the selected `Solution`.

## Complexity detail

Let $n$ be the node count and $h$ the maximum root-to-leaf path length. Every real node is processed once, with constant pointer work after its two child calls. Total time is $O(n)$.

Recursive stack depth is $O(h)$. It is $O(\log n)$ for a balanced tree and $O(n)$ for a skewed tree. The helper's `list_head` parameter is only one reference per frame and does not alter that bound.

The manifest states $O(1)$ space, but this exact recursive source uses the Python call stack and therefore does not satisfy the constant-extra-space follow-up. Its source header's $O(h)$ claim is accurate.

The output reuses all original nodes, so there is no separate result allocation. Excluding the mutated tree itself, auxiliary memory is solely the recursive stack.

## Alternatives and edge cases

- **Constant-space iterative splice:** For each node with a left child, attach the old right subtree to the left subtree's current rightmost chain, move left to right, and continue. It meets the $O(1)$ follow-up.
- **Recursive left-tail joining:** Flatten left and right subtrees, link the left tail to the right head, and return the final tail. It also uses $O(h)$ stack space but follows a more conventional child-first explanation.
- **Explicit reverse-preorder stack:** Simulate right-left-root processing without recursion. It avoids interpreter recursion limits but uses explicit memory.
- **Forward preorder stack:** Push right before left and connect each previously visited node to the current node. It is often easier to trace but still not constant-space.
- **Empty tree:** The helper returns the incoming `None` suffix, and the public method returns `None`.
- **Single node:** Both child calls return the suffix; the node's right becomes that suffix and its left becomes null.
- **Only right children:** Right recursion builds the existing order backward, then each parent reconnects to the same successor sequence.
- **Only left children:** Reverse construction turns the descending left path into a right chain in root-first order.
- **Both children:** Right must be prepared before left so the left chain can terminate at the right head.
- **Changing recursion to left first:** Incorrect for this prepend-to-suffix design; it would place regions in the wrong final order unless the linking logic also changed.
- **Original right pointer:** It is consumed recursively before being overwritten, so its nodes remain reachable.
- **Node values:** Values do not affect pointer ordering.
- **Python recursion depth:** A legal 2,000-node chain can exceed the default recursion limit. The constant-space iterative source avoids this failure mode.
- **Return value:** Returning the helper's head from public `flatten` would violate the stated `None` contract even though the object identity is the same root.
- **Manifest discrepancy:** Reserve $O(1)$ for the iterative splice branch; report $O(h)$ for this selected recursive implementation.
