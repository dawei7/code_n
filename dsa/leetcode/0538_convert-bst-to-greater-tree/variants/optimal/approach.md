## General

For each original key `x`, the new value must equal `x` plus every original key greater than `x`. A binary search tree already organizes larger keys to the right, and a reverse inorder traversal visits all keys from greatest to smallest.

Ordinary inorder order is left, node, right and produces ascending values. Reversing it to right, node, left produces descending values.

The solution maintains running sum `s` of all original values visited so far in that descending order.

The nested `dfs(root)` follows three steps for every non-null node:

1. visit the right subtree;
2. add the current original value to `s` and replace the node value with `s`;
3. visit the left subtree.

**Visit greater keys first.** In a valid BST with unique values, every node in `root.right` has an original key greater than `root.val`. Recursing right before processing the node ensures all those greater values have already been added to `s`.

The traversal also includes greater ancestors and values from previously completed branches. Globally, reverse inorder visits the complete tree in descending order, so `s` is not merely a right-subtree sum; it contains every original key greater than the current key.

**Add the current original key before overwriting it.** The line:

`s += root.val`

reads the node's original value and adds it to the accumulated greater-key sum. Only then does:

`root.val = s`

replace the node. The new value therefore includes both all strictly greater original keys and the node's own original key, exactly as required.

If the assignment occurred first or if a mutated value were added later, sums could include already-aggregated totals and double-count keys. The current ordering avoids that.

**Then move to smaller keys.** Every value in the left subtree is smaller than the current original key. After the current value joins `s`, each left-subtree node should include it in its own greater-key total. Recursing left last makes that happen.

For the largest node in the BST, the right subtree is empty and `s` is initially zero. Its new value remains its own original key. The next smaller node receives the largest value plus itself. This continues cumulatively down to the smallest node, whose new value becomes the sum of the entire tree.

Consider BST values zero and one, with one as the right child. Reverse inorder visits one first: `s` becomes one and the node remains one. Then it visits zero: `s` remains one after adding zero, so the root becomes one. The result is `[1, null, 1]`.

In a larger tree rooted at four, all values eight, seven, six, and five are processed before four. Their sum is 26; adding four makes 30, so the root's new value is 30, as in the example.

**Why mutations do not break traversal.** Child pointers determine recursion, and the code never changes them. Although node values are overwritten, the algorithm does not perform later comparisons or navigation based on those mutated values. The traversal order was structurally fixed by the original BST shape.

**What `s` means at the processing moment.** Immediately after the right-subtree call and before adding `root.val`, `s` equals the sum of all original keys strictly greater than the current key. This is true for the maximum key because the sum is zero. Moving through descending order preserves it: after processing one key, that key joins the sum used for the next smaller key.

Adding the current value and assigning the result therefore establishes the correct transformed value for that node. Reverse inorder reaches every node once, so all nodes are transformed.

The `nonlocal s` declaration lets recursive calls share and update one integer defined in `convertBST`. A separate sum per recursive frame would lose contributions from greater branches.

If `root` is `None`, DFS returns immediately and the method returns `None` unchanged. This handles the permitted empty tree.

The transformation occurs in place. After DFS, the method returns the original root reference, now connected to nodes whose values have all been updated.

## Complexity detail

Let $n$ be the number of nodes and $h$ the tree height. Reverse inorder visits every node exactly once and does constant work there, so time is $O(n)$.

The recursion stack contains at most one frame per tree level, giving $O(h)$ auxiliary space, matching the manifest. A balanced tree uses $O(\log n)$ stack depth, while a skewed tree can use $O(n)$.

Only the scalar running sum is stored beyond the call stack. The output reuses the existing tree and allocates no new tree nodes.

## Alternatives and edge cases

- **Iterative reverse inorder:** An explicit stack performs the same descending traversal in $O(n)$ time and $O(h)$ space while avoiding recursion-depth limits.
- **Collect and sort all values:** It ignores the BST's traversal order and requires additional $O(n)$ storage plus sorting.
- **For each node, rescan greater nodes:** It can become $O(n^2)$ and repeats work already summarized by `s`.
- **Reverse Morris traversal:** It can achieve $O(1)$ auxiliary space by temporarily threading the tree, but pointer manipulation is more intricate.
- **Empty tree:** DFS returns immediately and the method returns `None`.
- **Single node:** It has no greater key, so its value stays unchanged.
- **Largest key:** It is visited first and remains its original value.
- **Smallest key:** It is visited last and becomes the sum of all original keys.
- **Negative keys:** Descending order and cumulative addition remain correct even if the running sum rises or falls numerically.
- **Unique-value guarantee:** It makes “greater than” align cleanly with strict reverse inorder order.
- **In-place mutation:** Adding the original value before overwriting prevents aggregated values from being counted again.
- **Skewed BST:** Time remains linear, but recursion depth reaches $O(n)$.
