## General

**Inorder traversal exposes BST values in ascending order**

For every node in a binary search tree, values in its left subtree are smaller
than the node's value, and values in its right subtree are larger. Visiting the
left subtree first, then the node, then the right subtree therefore visits all
values in ascending order. This order is called inorder traversal.

Once nodes arrive in sorted order, the one-based $k$th smallest query becomes a
counting problem: decrement `k` at each visited node and return the value when
the counter reaches zero. There is no need to build a complete sorted list or
visit nodes larger than the answer.

**Use an explicit stack to simulate recursive calls**

A recursive inorder traversal naturally pauses a node while it explores that
node's left subtree. The exact source stores those paused nodes in `stk`.

The outer condition `while root or stk` says work remains if there is a current
subtree to descend into or an ancestor waiting on the stack. Each iteration has
one of two forms:

- If `root` is not `None`, push it and move to `root.left`. Repeating these
  iterations follows the current subtree's left spine.
- If `root` is `None`, the left descent has ended. Pop the latest paused node,
  visit it, then move to its right child.

Because the stack is last-in-first-out, the deepest unvisited ancestor is
popped first. That node has no unvisited value smaller than it within its left
subtree: the traversal reached the left boundary, and any nodes encountered on
the way have already been processed before their ancestors can pop.

The source writes this as one `if` per outer iteration rather than the common
form containing a nested `while root`. The behavior is the same; a series of
outer iterations pushes the entire left spine before the first pop.

**Rank nodes only when they are visited, not when pushed**

Pushing a node does not mean it is next in ascending order because its left
subtree may contain many smaller values. The source decrements `k` only in the
`else` branch, immediately after `root = stk.pop()`. At that moment the node's
left subtree is complete, making it the next inorder value.

If the decremented value is zero, exactly $k$ original-rank nodes have been
visited and `root.val` is returned. Otherwise setting `root = root.right`
begins the next inorder phase: descend to the smallest value in that right
subtree before returning to any older ancestor.

**Trace the first example**

For the BST `[3,1,4,null,2]`, the method pushes node 3 and moves left, then
pushes node 1 and reaches its missing left child. It pops 1, which is the first
inorder value. With requested `k = 1`, decrementing reaches zero and the method
returns 1 immediately. Nodes 2, 3, and 4 are never visited.

For a larger rank, after visiting 1 the traversal moves to its right child 2.
Node 2 has no left child, so it is the second visit. It then returns through the
stack to node 3 for the third visit, matching ascending order `[1,2,3,4]`.

**Why the stack always identifies the next smallest unvisited node**

Whenever a node is pushed, traversal commits to finishing its entire left
subtree before visiting it. Whenever a node is popped, that left subtree is
finished. All values there are smaller and have already been visited. The
node's right subtree is untouched and contains only larger values. Older stack
nodes are ancestors whose own left-side work includes the just-popped node, so
they cannot legally be visited earlier.

Thus every pop yields the smallest value not yet visited. By decrementing the
rank exactly once per pop, the zero counter identifies the $k$th value in the
globally sorted traversal.

The contract guarantees `1 <= k <= n`, so some pop must reduce the counter to
zero. The source has no return after the loop because invalid overlarge `k` is
outside the input domain.

**The local `root` variable can move without changing the tree**

Assignments such as `root = root.left` and `root = stk.pop()` change only the
method's local reference. No node's `left`, `right`, or `val` field is assigned.
The caller's tree remains intact.

The commented `TreeNode` class is platform-provided harness structure, and the
source expects `Optional` and `TreeNode` to exist in the execution environment.

## Complexity detail

Let $h$ be tree height. Before the first visit, the algorithm can push at most
$h$ nodes along a left spine. It visits exactly $k$ nodes before returning, and
right-subtree descents associated with those visits add only the nodes reached
on the way to those inorder positions. The standard output-sensitive time bound
is $O(h+k)$, with worst case $O(n)$.

The stack contains at most one root-to-current path, so auxiliary space is
$O(h)$. This is $O(\log n)$ for a balanced BST and $O(n)$ for a skewed one. No
array of all node values is created.

## Alternatives and edge cases

- **Recursive inorder traversal:** Recurse left, count the node, then recurse right. It expresses the order directly but needs shared rank/result state and uses the language call stack; early-return propagation must be handled carefully.
- **Build the entire inorder list:** Collect all values and return index `k - 1`. It is simple but always takes $O(n)$ time and $O(n)$ extra space, even when `k` is small.
- **Augment nodes with subtree sizes:** Store the size of each left subtree. Compare `k` with `left_size + 1` to descend directly, enabling $O(h)$ queries; insertions and deletions must update sizes along their paths. This addresses the frequent-modification follow-up.
- **Morris inorder traversal:** Temporarily thread predecessor pointers to achieve $O(1)$ auxiliary space. It is more intricate and must restore every modified link, especially when returning early.
- **`k = 1`:** The method descends to the leftmost node and returns it on the first pop.
- **`k = n`:** It visits the complete inorder sequence and returns the rightmost value.
- **One-node tree:** The root is pushed, its missing left child causes a pop, and valid `k = 1` returns its value.
- **Right-skewed tree:** The stack stays small, but reaching rank `k` visits the first `k` nodes in the chain.
- **Left-skewed tree:** The algorithm first pushes the entire height before visiting the minimum, using $O(n)$ stack space in the worst shape.
- **Node values including zero:** Ordering comparisons were already enforced when the BST was built; traversal treats values uniformly.
- **Invalid rank:** The reference excludes it. A production API would need a defined error or sentinel if the loop ended without reaching zero.
- **Input preservation:** The explicit stack stores references only, and the method never changes tree links or values.
