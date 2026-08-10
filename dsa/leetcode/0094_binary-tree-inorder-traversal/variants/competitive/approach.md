## General

The selected competitive `Solution` uses Morris inorder traversal. Ordinary iterative traversal stores ancestors in a stack so it can return to a node after finishing that node's left subtree. Morris traversal obtains the same return route by temporarily using an otherwise empty right pointer in the tree. It later removes every temporary pointer, restoring the original structure.

The central object is a node's inorder predecessor: when `curr` has a left subtree, its predecessor is the rightmost node in that left subtree. This predecessor is the last node that inorder traversal should visit before `curr`. Its naturally empty right link can temporarily point back to `curr`.

**Case 1: no left child**

If `curr.left is None`, there is no unvisited left subtree. Inorder therefore visits `curr` immediately by appending its value, then moves to `curr.right`.

That right pointer may be an original child or a temporary thread leading back to an ancestor. The algorithm can follow either without additional state.

**Case 2: a left child exists**

The code starts `node = curr.left` and walks right until either:

- `node.right is None`, meaning no thread has yet been installed; or
- `node.right == curr`, meaning this predecessor already points back to the current node.

The second stopping condition is essential. Without it, the predecessor search would follow the thread back to `curr` and could loop through the modified structure.

On the first encounter, `node.right is None`. The method sets `node.right = curr` and descends to `curr.left`. It does not append `curr.val` yet, because inorder must finish the left subtree first.

Eventually traversal reaches the predecessor, visits it, and follows its threaded right link back to `curr`. The predecessor search now finds `node.right == curr`, identifying the second encounter. At this point the entire left subtree has been emitted. The code removes the thread with `node.right = None`, appends `curr.val`, and advances into the original right subtree.

**Why the first and second encounters are distinguishable**

The predecessor's right link is initially absent because it is the rightmost node of the left subtree. The algorithm itself changes that exact link to `curr`. No other operation gives it that value. Therefore “empty” uniquely means the left subtree has not yet been traversed for this ancestor, while “points to `curr`” uniquely means traversal has returned after completing it.

This is analogous to a recursive call's program counter: the thread records where to resume, and its presence records that the left call has already been initiated.

**Trace on a small tree**

For a root `2` with left child `1` and right child `3`:

1. At `2`, predecessor `1` has no right child. Set `1.right = 2` and move to `1`.
2. Node `1` has no left child, so append `1` and follow its right thread back to `2`.
3. Searching from `2.left` finds that `1.right == 2`. Remove that link, append `2`, and move to the original right child `3`.
4. Node `3` has no left child, so append `3`.

The result is `[1, 2, 3]`, and node `1`'s right link is again `None`.

**Why the order is correct**

For a node without a left child, visiting immediately is exactly inorder. For a node with a left child, the first encounter defers the visit and enters the left subtree. The thread returns only after traversal reaches the rightmost and therefore final inorder node of that subtree. The second encounter then visits the ancestor before entering its right subtree. These cases enforce left, node, right order at every node.

Every node is appended once. A no-left node is appended in its only direct encounter. A node with a left subtree is not appended when its thread is created and is appended exactly once when that thread is found and removed.

**Why the tree is restored**

The method creates a thread only in a right field that was `None`. The only matching second-encounter branch sets that same field back to `None`. Each created thread is necessarily followed after the predecessor finishes, because it is the traversal's route back to the ancestor. The loop does not exit early, so every thread is removed before return. Original nonempty child links are never overwritten.

The source file also defines `Solution2`, an explicit stack implementation using visited flags. It is not the selected class discussed here.

## Complexity detail

Let $n$ be the number of nodes. The outer loop may encounter a node with a left subtree twice. The nested predecessor loop can look alarming, but its work does not multiply to $O(nh)$. Each relevant right edge inside a left subtree is traversed at most twice: once while creating a thread and once while finding that thread for removal. Thread creation, removal, visits, and other pointer moves are also constant per node or edge. A tree has $n-1$ original edges, so total time is $O(n)$.

The exact selected algorithm uses only `result`, `curr`, and `node`, regardless of height. Excluding the output, its auxiliary space is $O(1)$.

This conflicts with the package manifest's declared $O(h)$ space. That bound matches the unselected `Solution2` stack method, not the selected first `Solution`. The executable Morris source should be described as $O(1)$ auxiliary space. The output list itself is $O(n)$ and remains mandatory.

## Alternatives and edge cases

- **Recursive DFS:** It is the clearest expression of inorder traversal and runs in $O(n)$ time, but uses $O(h)$ call-stack space.
- **Explicit node stack:** Push the left spine, pop and visit, then explore right. It satisfies the iterative follow-up without mutating the tree and uses $O(h)$ auxiliary space.
- **Visited-flag stack:** Store `(node, visited)` entries to encode recursive phases. It is flexible but has larger constant storage.
- **Temporary mutation:** Morris traversal restores the tree only if it completes normally. If visiting can throw an exception or the traversal may be interrupted, callers could observe installed threads; a stack method is safer in such environments.
- **Empty tree:** `curr` starts as `None`, the loop does not run, and `[]` is returned.
- **Single node:** With no left child, its value is appended and traversal ends.
- **Pure right chain:** No threads are needed; values are emitted while moving right.
- **Pure left chain:** One thread is created for each ancestor and later removed. Time stays linear even though nodes are revisited.
- **Duplicate values:** The method follows node links, not value comparisons. Equal values from distinct nodes are each emitted.
- **Predecessor stopping test:** Both conditions in `while node.right and node.right != curr` are required. Omitting the equality test can follow a thread into a cycle.
