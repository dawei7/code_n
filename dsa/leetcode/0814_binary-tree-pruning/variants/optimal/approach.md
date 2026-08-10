## General

**A subtree can be judged only after its children**

A node should remain if and only if its entire subtree contains at least one value equal to 1. Whether a zero-valued node survives therefore depends on what remains below it. This naturally calls for postorder recursion: prune the left subtree, prune the right subtree, and only then decide whether the current node has become useless.

The function `pruneTree(root)` returns one of two things:

- the pruned version of the subtree originally rooted at `root`, if that subtree contains a 1;
- `None`, if the entire subtree contains only zeroes.

This return meaning does two jobs at once. It constructs the answer and tells the parent whether the child subtree should be attached or removed.

**The empty-subtree base case**

If `root is None`, there is no node and therefore no 1. The implementation returns `root`, which is already `None`. This makes missing children participate naturally in the same recursion as real children.

Although the problem guarantees at least one input node, recursive calls still reach `None` at every absent left or right child, so this base case is necessary.

**Prune both children before inspecting the current node**

The assignments

`root.left = self.pruneTree(root.left)`

and

`root.right = self.pruneTree(root.right)`

recursively process both child subtrees and replace the original child references with their pruned results. If a child subtree contains no 1, its call returns `None` and the assignment disconnects that entire subtree. If it contains a 1, the assignment keeps its surviving root.

These assignments mutate the given tree in place. The algorithm does not build copies of nodes. Nodes that belong to a useful subtree retain their identity, while references to all-zero subtrees are removed.

**The exact condition for deleting the current node**

After both recursive assignments finish, the code checks

`root.val == 0 and root.left == root.right`.

In a proper binary tree using the standard `TreeNode` class, the post-pruning children satisfy `root.left == root.right` here when both are `None`. A nonempty left and nonempty right child are distinct node objects, and one nonempty child cannot equal `None`. Thus, the condition compactly means:

- the current node's own value is 0;
- no surviving left child contains a 1;
- no surviving right child contains a 1.

When all three facts hold, the entire current subtree contains no 1, so the function returns `None`. Otherwise, either the current node is 1 or at least one pruned child remains. In either case, the subtree contains a 1, and the function returns `root`.

A more explicit equivalent test would be `root.val == 0 and root.left is None and root.right is None`. The exact implementation uses equality between the two child references after pruning.

**Why the traversal must be bottom-up**

Imagine a zero-valued node whose descendants are also all zero. Before inspecting its children, the node is not a leaf, so a top-down “remove zero leaves” pass would not remove it immediately. Once its zero-only children are pruned, it becomes a zero leaf and must also be removed.

Postorder recursion handles this chain in one pass. Deepest zero leaves return `None` first. Their parents then see missing children and may return `None` in turn. The deletion decision propagates upward as far as the all-zero region extends.

Conversely, if a deep descendant equals 1, every recursive call on the path back to the root returns a nonempty node. Even zero-valued ancestors survive because a child reference remains, correctly preserving the path needed to connect the 1 to the tree.

**A small example**

Consider a subtree rooted at 0 with a left child 0 and a right child 1.

The left leaf recursively receives two `None` children, has value 0, and returns `None`. The right leaf also receives two `None` children, but its value is 1, so it returns itself. The parent is updated to have no left child and a surviving right child. Its deletion condition is false because its children are not both `None`, so the zero-valued parent remains.

Now consider a zero root whose descendants are all zero. Every leaf returns `None`. Each internal zero node then has both child references pruned away and also returns `None`. Eventually, the original root returns `None`, correctly representing an empty output tree.

**Why the result is correct**

We can reason by induction on subtree size. An empty subtree contains no 1 and returns `None`, so the claim holds for the base case.

Assume both recursive child calls correctly return a pruned nonempty subtree exactly when their original subtrees contain a 1. After assigning those results, a child reference is nonempty precisely when that side contains a 1. The current subtree contains a 1 exactly when `root.val == 1` or at least one child reference is nonempty.

The deletion condition is the negation of that fact for the allowed values 0 and 1: current value zero and both children absent. Therefore, the function returns `None` exactly for all-zero subtrees and returns the correctly pruned root for every subtree containing a 1. Applying the claim to the original root proves that all and only forbidden subtrees are removed.

## Complexity detail

Let `n` be the number of nodes and `h` be the tree height.

Every real node is visited once. At a node, the algorithm performs two recursive calls, two pointer assignments, and a constant number of comparisons. Null child positions also take constant time and are proportional to the number of nodes. The total time complexity is `O(n)`.

The algorithm creates no new tree nodes and uses no collection proportional to the tree size. Its auxiliary storage is the recursion call stack. At most one root-to-leaf path is active at a time, so the space complexity is `O(h)`.

For a balanced tree, `h = O(\log n)`. For a completely skewed tree, `h = O(n)`, giving the worst-case stack usage of `O(n)`. Mutating child pointers in place keeps non-stack auxiliary space at `O(1)`.

## Alternatives and edge cases

- **Separate contains-one and deletion passes:** One pass could annotate whether subtrees contain 1 and another could remove them. It works but repeats traversal or needs extra storage. The return value here combines both tasks in one postorder pass.

- **Repeatedly remove zero leaves:** Iterative rounds eventually reach the correct tree, but a long zero chain may require many full passes. Postorder recursion removes the entire chain during one traversal.

- **Construct a copied tree:** Building new nodes can preserve the input, but the contract asks for the same tree after pruning. In-place pointer updates use less memory and match that intent.

- **Empty recursive child:** `None` returns immediately and tells the parent that side contains no 1.

- **Single node with value 0:** Both child calls return `None`, the deletion condition succeeds, and the entire result is `None`.

- **Single node with value 1:** Its value prevents deletion, so the original node is returned.

- **Zero ancestor of a 1:** The ancestor remains because the pruned child on the path to that 1 is nonempty.

- **One all-zero child and one useful child:** The all-zero side becomes `None`; the useful side and current node remain.

- **All-zero tree:** Pruning propagates from the leaves to the original root, which finally returns `None`.

- **All-one tree:** No node satisfies the zero-valued deletion condition, so every node remains.

- **Equality of child references:** In the standard proper-tree model, `root.left == root.right` after pruning is used as a compact “both are `None`” test. The reasoning assumes ordinary `TreeNode` identity semantics and no shared child object, both supplied by the tree contract.

- **Recursion depth:** The input has at most 200 nodes, so even a skewed tree has a manageable recursion depth in Python.

- **Mutation visibility:** The original node objects are reused. Any caller retaining references to pruned nodes could still hold those separate objects, but they are no longer reachable from the returned root.
