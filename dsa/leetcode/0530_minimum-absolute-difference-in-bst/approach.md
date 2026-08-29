## General

The binary-search-tree ordering is the decisive property. An inorder traversal—left subtree, node, right subtree—visits node values in sorted, nondecreasing order. Once values are seen in sorted order, the minimum difference over all pairs must occur between two consecutive values.

To understand the consecutive-pair fact, take sorted values `v[0] <= v[1] <= ...`. For any nonadjacent pair `v[i]` and `v[j]` with `j > i + 1`:

$$
v[j]-v[i]=(v[i+1]-v[i])+\cdots+(v[j]-v[j-1]).
$$

Every term is nonnegative, so the wide difference cannot be smaller than all consecutive differences inside it. Checking adjacent inorder values is therefore sufficient; comparing every node pair would be redundant.

The nested `dfs` performs inorder traversal:

1. recursively visit `root.left`;
2. process `root.val`;
3. recursively visit `root.right`.

The parameter name `root` inside `dfs` refers to the current subtree root. If it is `None`, that subtree has no value to contribute and the function returns.

**Remember only the previous sorted value.** Variable `pre` stores the value processed immediately before the current node in inorder order. Variable `ans` stores the smallest consecutive difference observed so far.

When a node is processed, the traversal has already completed all smaller values in its left subtree, and `pre` is the greatest value among everything visited so far. Therefore:

`root.val - pre`

is the difference between the current sorted value and its immediate predecessor.

The code updates:

`ans = min(ans, root.val - pre)`

and then sets `pre = root.val` so the current node becomes the predecessor for the next inorder value.

No absolute-value function is needed. Inorder order guarantees `root.val >= pre` after the first real node, so the subtraction is nonnegative. If equal values are allowed by a particular BST convention, their adjacent difference is zero and is necessarily optimal.

**Handle the first inorder node without a branch.** Before traversal, `pre = -inf` and `ans = inf`. For the smallest node, `root.val - (-inf)` is positive infinity, so taking the minimum leaves `ans` as infinity. The node value then replaces `pre`.

The second real node produces the first finite difference. The source guarantees at least two nodes, so by the end `ans` is finite. This sentinel technique avoids a separate “has previous value” boolean while preserving the same logic.

For BST `[4, 2, 6, 1, 3]`, inorder values are one, two, three, four, six. The computed consecutive differences are one, one, one, and two. The minimum is one.

For the tree containing values zero, one, twelve, forty-eight, and forty-nine, inorder traversal compares them in that order. The gaps between zero and one and between forty-eight and forty-nine are both one, so the result is one even though those nodes may lie in different parts of the tree.

**Why tree adjacency is irrelevant.** The requested pair need not have a parent-child relationship. Inorder adjacency refers to neighboring values in sorted order. The traversal carries `pre` across subtree boundaries: after completing a left subtree, it compares that subtree's maximum with its parent, and after the parent, it eventually compares with the right subtree's minimum. These are exactly the pairs a local parent-child-only method might miss.

**Why all necessary pairs are examined.** Inorder traversal visits every node once and yields the complete sorted sequence. Except for the first value, every value is compared with its immediate predecessor. Thus every consecutive sorted pair is examined exactly once. The sorted-pair argument proves at least one such pair attains the global minimum, so `ans` is the requested result.

The `nonlocal pre, ans` declaration allows the nested function to rebind the two variables created in the enclosing method. They retain their values across recursive calls, forming one traversal-wide stream rather than separate state per subtree.

The algorithm does not build a list of node values. It consumes the sorted order online, keeping only the one predecessor needed for the next comparison.

## Complexity detail

Let $n$ be the number of nodes and $h$ the tree height. Every node is entered once and processed with constant work, so time is $O(n)$.

The only growing auxiliary storage is the recursion stack. At most one call per level is active, giving $O(h)$ space, matching the manifest. A balanced BST has $h=O(\log n)$; a skewed BST can have $h=O(n)$.

The scalar values `pre` and `ans` use $O(1)$ space. No $O(n)$ inorder list and no sorting step are used.

## Alternatives and edge cases

- **Collect inorder values:** Traversing into a list and scanning adjacent entries is correct but uses an additional $O(n)$ list.
- **Collect arbitrary values and sort:** It works even for a non-BST, but costs $O(n\log n)$ time and misses the opportunity supplied by BST order.
- **Compare every node pair:** It takes $O(n^2)$ time and is unnecessary because the minimum lies between sorted neighbors.
- **Iterative inorder traversal:** An explicit stack avoids language recursion limits while retaining $O(n)$ time and $O(h)$ space.
- **Exactly two nodes:** The second visit creates the only finite difference, which is returned.
- **Skewed tree:** Ordering remains correct, but recursive stack depth becomes linear.
- **Values on different subtrees:** The shared predecessor state compares across subtree boundaries.
- **Nonnegative values:** They do not conflict with the negative-infinity sentinel.
- **Possible duplicate values:** Consecutive equal inorder values produce zero, the smallest possible absolute difference.
- **No `abs` call:** Sorted visitation makes each current-minus-previous difference nonnegative.
- **At least two nodes:** This guarantee ensures the infinity answer sentinel is replaced by a finite difference.
