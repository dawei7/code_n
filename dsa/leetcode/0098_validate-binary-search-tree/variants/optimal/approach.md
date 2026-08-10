## General

Checking only each node against its immediate children is insufficient. A descendant deep in the left subtree must still be smaller than the ancestor, and a descendant deep in the right subtree must still be larger. The selected solution uses an equivalent global property:

> The inorder traversal of a valid BST with strict ordering must be strictly increasing.

Inorder visits the entire left subtree, then the node, then the entire right subtree. In a BST, all left values are smaller and all right values are larger, so this visit order sorts the node values. Conversely, if inorder values are strictly increasing, every node appears after all nodes in its left subtree and before all nodes in its right subtree, enforcing the required comparisons.

**Meaning of `prev`**

`prev` stores the value of the most recently visited node in inorder sequence. Immediately before visiting the current node, every earlier inorder node has already been validated, and `prev` is the largest among them because the validated sequence is strictly increasing.

The current value must satisfy

$$
\texttt{prev}<\texttt{root.val}.
$$

The source rejects `prev >= root.val`. Equality is deliberately invalid because the Reference requires keys to be strictly less or strictly greater; duplicates are not permitted anywhere in a valid BST.

**How recursive inorder works**

For a nonempty node, the helper performs three operations in order:

1. validate the left subtree;
2. compare and record the current node; and
3. validate the right subtree.

If the left recursive call returns false, the current call immediately returns false. There is no reason to inspect more nodes after one violation proves the whole tree invalid.

After the left side succeeds, `nonlocal prev` allows the helper to read and update the variable created by `isValidBST`. If the current value is not strictly larger, it returns false. Otherwise it assigns `prev = root.val`, so the next inorder node will be compared with this one.

Finally, returning `dfs(root.right)` forwards the right subtree's result directly.

**Why an empty subtree is valid**

`dfs(None)` returns true. An absent subtree contains no pair of values that can violate ordering, and this base case lets leaves succeed after both missing children are checked.

**A global violation that child-only checks miss**

Consider root `5`, right child `6`, and node `3` as the left child of `6`. Node `3` is smaller than its parent `6`, so the local left-child rule appears satisfied. But `3` lies in root `5`'s right subtree and must be greater than `5`.

Inorder produces `5, 3, 6`. After visiting `5`, `prev` is five; visiting `3` fails the strict-increase comparison. The method therefore detects the ancestor-level violation without explicitly carrying ancestor bounds.

**Why adjacent inorder comparisons are enough**

Suppose the complete inorder sequence is strictly increasing. Then every earlier value is smaller than every later value by transitivity, not merely smaller than its immediate successor.

For any node, all members of its left subtree appear before it in inorder, so they are all smaller. All members of its right subtree appear after it, so they are all larger. The same argument applies recursively to every subtree. Therefore strict inorder increase is both necessary and sufficient for the BST definition.

**Initialization and the exact source dependency**

Before the first real node, there is no previous value. The code intends to initialize `prev` to negative infinity so every allowed 32-bit value passes the first comparison.

However, the exact `solution.py` writes `prev = -inf` without importing or defining `inf`. A normal standalone Python execution raises `NameError` before traversal begins. The intended implementation needs `from math import inf`, `float("-inf")`, or a `prev is None` sentinel check. This is a source defect that the explanation must not conceal.

The tree itself is read-only: this recursive variant never changes child pointers or node values.

## Complexity detail

Let $n$ be the number of nodes and $h$ the tree height. In the worst case, every node is visited once, and each visit performs constant work, so time is $O(n)$. An invalid tree may stop earlier, but worst-case valid trees require the full traversal.

The recursion stack contains at most one root-to-current path, using $O(h)$ auxiliary space, matching the manifest. A balanced tree has $h=O(\log n)$; a skewed tree has $h=O(n)$. Only the scalar `prev` is stored beyond the stack.

The stated maximum of $10^4$ nodes can exceed Python's default recursion limit for a highly skewed tree, even though the asymptotic analysis is correct.

## Alternatives and edge cases

- **Recursive valid bounds:** Carry an exclusive lower and upper limit to each node. It is equally $O(n)$ time and $O(h)$ stack space and makes ancestor constraints explicit.
- **Explicit inorder stack:** Simulate the recursion iteratively, avoiding Python recursion-depth failure while using $O(h)$ storage.
- **Morris inorder traversal:** Temporarily thread the tree to obtain $O(1)$ auxiliary space, but restoration is subtle, especially on early failure.
- **Duplicate values:** `prev >= root.val` rejects equality exactly as required.
- **Minimum 32-bit value:** A real negative-infinity sentinel is smaller than $-2^{31}$; using $-2^{31}$ itself would incorrectly reject that legal first value.
- **Single node:** Both empty child calls succeed, and its value is greater than negative infinity.
- **Deep ancestor violation:** Inorder comparison detects it even when every immediate parent-child pair seems locally ordered.
- **Nonempty contract:** The Reference guarantees at least one node, though the helper would consider an empty root valid if called outside the contract.
- **Missing import:** Define `inf` before executing this exact source; type annotations and platform `TreeNode` support do not supply it.
