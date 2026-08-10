## General

**Create a dummy parent so the real root is finalized uniformly**

Postorder must delay a node until both subtrees are complete. Morris traversal simulates return paths with temporary threads rather than a recursion stack.

The source creates `dummy = TreeNode(0)` and sets `dummy.left = root`. The dummy’s value is never output. It ensures that the real root belongs to a left subtree whose completion will trigger the same boundary-processing rule as every other subtree.

Without the dummy, special cleanup would be needed after the main root’s final right subtree.

`cur` begins at this dummy node. If `cur.left` is null, there is no left subtree waiting to be processed, so traversal moves directly to `cur.right`.

**Find or recognize the predecessor thread**

When `cur.left` exists, `node` starts there and follows right pointers until either:

- its right pointer is null; or
- its right pointer leads back to `cur`.

The first case means this left subtree has not yet been threaded. The source assigns `node.right = cur` and moves `cur` left. The temporary link is a return route from the left subtree’s rightmost boundary node back to its parent context.

The second case means traversal has returned through a thread. At that moment, every ordinary node in `cur.left`’s subtree has been explored structurally. The algorithm must emit the appropriate postorder boundary, remove the thread, and continue to `cur.right`.

**Why `traceBack` reverses a right boundary**

On thread removal, the path from `cur.left` to `node` by following right pointers is a subtree boundary in top-down order:

`subtree root -> ... -> rightmost predecessor`

Postorder needs those boundary nodes in the opposite order:

`rightmost predecessor -> ... -> subtree root`

`traceBack(frm, to)` collects values along that right-pointer path, includes the endpoint, reverses the temporary value list, and returns it.

The main method extends `result` with that reversed boundary. It does not reverse tree edges; it reverses only the collected values.

Why does boundary emission cover more than just one path? Threads are nested. Interior subtrees have already emitted their own reversed boundaries when their threads were removed. At the moment an outer boundary is emitted, every node branching off that boundary has already been handled. Reversing the boundary then places each remaining root after its left and right descendants.

**Why every node is output once**

Each real node lies on exactly one right boundary that is emitted when the thread belonging to the appropriate ancestor context is removed. The dummy guarantees this statement also covers the actual tree root.

No value is appended when a thread is created. Creation only descends and establishes a future return. Appending happens on removal, after the corresponding subtree traversal.

The dummy itself is not emitted because processing `dummy.left` traces from the real root to its predecessor; the boundary ends before `dummy`.

For `[1, null, 2, 3]`, traversal eventually finalizes node `3` before node `2`. The dummy’s closing boundary then places node `1` last, yielding `[3, 2, 1]`.

**Why the original tree is restored**

A thread is installed only where `node.right` was originally null. When the same predecessor is found with `node.right == cur`, the source sets it back to `None`. Original non-null child links are never overwritten.

Normal completion therefore restores the tree exactly. As with all Morris methods, an interruption between creating and deleting a thread could leave temporary mutation visible.

`traceBack` itself only reads right pointers, so it introduces no additional structural modifications.

## Complexity detail

Let $n$ be the node count and $h$ the tree height.

Although predecessor searches are nested syntactically, each relevant edge participates only a bounded number of times across thread creation and removal. Every node’s value is collected once in boundary output. The total time is $O(n)$.

The main traversal keeps a constant number of pointers and one dummy node. However, this exact `traceBack` allocates a temporary Python list containing one right-boundary’s values. A boundary can have length $O(h)$, so auxiliary space excluding the final result is $O(h)$, matching the manifest.

This contradicts the source comment claiming $O(1)$ space for the exact implementation. A Morris postorder that temporarily reverses boundary pointers and emits directly can attain $O(1)$ auxiliary space, but this source instead materializes and reverses value lists.

The returned `result` contains $n$ values, so including output gives $O(n+h)=O(n)$ storage.

## Alternatives and edge cases

- **Recursive postorder:** Recurse left, recurse right, append root. It is clearest and uses $O(h)$ stack space.
- **Visited-flag stack:** Schedule a node to be emitted after scheduling its children. It avoids tree mutation and uses $O(h)$ to $O(n)$ space.
- **Root-right-left then reverse:** An iterative modified preorder followed by list reversal is straightforward but uses an explicit stack.
- **Pointer-reversing Morris:** Reverse each boundary’s right links, emit values directly, and restore the links. It removes `traceBack`’s $O(h)$ temporary list but is more delicate.
- **Empty tree:** The dummy has a null left child, traversal moves to null, and `[]` is returned.
- **Single node:** The dummy thread ensures the real root is included during final boundary processing.
- **Left-only chain:** Nested threads are created and removed; values emerge leaf-to-root.
- **Right-only chain:** The dummy’s left subtree has a long right boundary, which `traceBack` reverses into correct deepest-to-root order.
- **Thread restoration:** Failing to clear `node.right` would leave a cycle in the input tree.
- **Boundary endpoint:** `traceBack` explicitly appends `to.val` after the loop; omitting it would lose the predecessor node.
- **Source-comment mismatch:** Temporary boundary lists mean this selected code is $O(h)$ auxiliary, not strict $O(1)$.
- **Later `Solution2`:** The secondary class uses an explicit visited-flag stack and is not the selected primary Morris implementation.
