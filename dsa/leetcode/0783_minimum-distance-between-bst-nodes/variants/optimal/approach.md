## General

**Use the ordering guaranteed by a binary search tree**

For every node in a binary search tree, values in its left subtree come before the node's value in sorted order, and values in its right subtree come after it.

An in-order traversal visits:

1. the complete left subtree;
2. the current node;
3. the complete right subtree.

Applying that rule recursively emits all node values in nondecreasing order. The algorithm uses this property to turn a tree problem into the simpler problem of finding the closest pair in a sorted sequence.

**Why only adjacent sorted values need comparison**

Suppose sorted values contain $a \le b \le c$. The distance from `a` to `c` is `c - a`, which is split into the two nonnegative gaps `b - a` and `c - b`.

Therefore a pair with one or more values between its endpoints cannot have a smaller difference than both neighboring gaps along that interval. The global minimum must appear between two consecutive values in sorted order.

This removes the need to compare every pair of nodes. Once traversal provides the next sorted value, only the immediately previous value matters.

**Stream the sorted order instead of storing a list**

Variable `pre` holds the value of the node visited immediately before the current node in in-order order. Variable `ans` holds the smallest consecutive difference seen so far.

At a node, after finishing its left subtree, the current value is the next item in sorted order. The algorithm updates:

`ans = min(ans, root.val - pre)`

and then assigns:

`pre = root.val`.

It must update `pre` before entering the right subtree so that the right subtree's smallest value is compared with the current node, its true in-order predecessor.

No earlier value besides `pre` is needed. This is the improvement over first collecting all values into an array and scanning that array later.

**Understand the recursive order exactly**

Function `dfs(root)` returns immediately for a missing child. For a real node it recursively processes `root.left`, performs the comparison and state update at the current node, and then processes `root.right`.

The placement of the comparison between the two recursive calls is essential. A pre-order traversal would see the root before smaller values in its left subtree, so `pre` would not consistently be the sorted predecessor. A post-order traversal has the same problem. Only in-order traversal exposes values monotonically for a BST.

**Initialize the first comparison safely**

Before traversal, `pre = -inf` and `ans = inf`.

The first visited node is the tree's minimum value. Its computed difference from negative infinity is positive infinity. Taking the minimum with `ans` leaves `ans` unchanged. This behaves like a special “no predecessor yet” state without adding a branch inside every visit.

The tree contains at least two nodes. Consequently a second value is eventually visited, producing a finite difference and replacing infinity. By the end, `ans` is a valid integer minimum.

Using negative infinity is safe even though the contract's node values are nonnegative. It is strictly below every real value and cannot accidentally create a smaller candidate.

**Why `nonlocal` is needed**

The variables `pre` and `ans` are created in `minDiffInBST` but updated inside nested function `dfs`. The `nonlocal` declaration tells Python that assignments should modify those enclosing variables rather than create new local variables inside `dfs`.

This lets all recursive calls share one traversal state. Without it, the assignment to `pre` or `ans` would either raise a scope error when reading the enclosing value or fail to preserve the update for later nodes.

**Trace the first example**

For the tree represented by `[4,2,6,1,3]`, in-order traversal visits values:

`1, 2, 3, 4, 6`.

The first visit leaves `ans` at infinity. The later consecutive differences are one, one, one, and two. The running minimum becomes one and remains one, so the method returns one.

Notice that a nonadjacent pair such as one and four has difference three. The values two and three lie between them and provide smaller adjacent gaps, illustrating why nonadjacent comparisons add no useful candidate.

**The traversal invariant**

Immediately before processing a real node after its left recursion returns:

- every value earlier in in-order order has already been processed;
- `pre` is the greatest of those processed values, hence the current node's sorted predecessor;
- `ans` is the minimum adjacent gap among all already processed consecutive pairs.

Comparing the current value with `pre` adds the one newly completed adjacent pair. Updating `pre` makes the invariant true for the next visit. The recursive in-order structure ensures every node participates in this sequence exactly once.

**Why the final result is globally minimal**

By the invariant, after traversal `ans` is the minimum difference between consecutive values in the complete sorted node sequence. The sorted-neighbor argument proves that at least one globally closest pair is consecutive. Therefore `ans` equals the minimum difference among every pair of distinct nodes, not merely among the pairs explicitly tested.

If duplicate values were permitted by a BST convention, they would appear consecutively and produce zero, which is necessarily minimal. The same reasoning remains valid.

## Complexity detail

Let $n$ be the number of nodes and $h$ the tree height. Every node is entered once and performs constant work besides its recursive calls, so total time is $O(n)$.

The algorithm does not store an in-order list. Its auxiliary storage is the recursion stack, whose maximum depth is $O(h)$. A balanced tree has $h = O(\log n)$, while a completely skewed tree has $h = O(n)$. The two scalar state values use $O(1)$ additional space.

## Alternatives and edge cases

- **Store the in-order array:** It gives the same adjacent-gap scan in $O(n)$ time but uses an extra $O(n)$ list in addition to the traversal stack.

- **Iterative in-order traversal:** An explicit stack also uses $O(h)$ space and avoids reliance on Python's recursive call depth.

- **Compare every pair:** It ignores BST ordering and costs $O(n^2)$ time.

- **Compare only each parent with its children:** The closest values need not have a direct tree edge, so this can miss the answer.

- **Minimum node count:** With exactly two nodes, the first comparison is ignored and the second produces their difference.

- **Skewed tree:** Time remains linear, but recursion depth reaches $O(n)$.

- **First visited value:** The negative-infinity sentinel prevents it from creating a finite candidate.

- **Difference zero:** If equal values are allowed, zero is found through adjacent in-order positions and cannot be improved.

- **Input preservation:** The traversal reads pointers and values without modifying the tree.
