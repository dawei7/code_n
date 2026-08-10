## General

**A parent needs a compact summary of each child subtree.**

Checking every possible subtree independently would revisit the same descendants many times. A postorder traversal avoids that repetition: first solve the left subtree, then the right subtree, and finally use their summaries to decide whether the current root forms a Binary Search Tree.

For a valid BST subtree, its parent needs three facts:

- its minimum value;
- its maximum value;
- its number of nodes.

The minimum and maximum let the parent verify the strict ordering boundary. The size lets the current node compute its own size in constant time rather than traversing descendants again.

The exact helper `dfs(root)` returns a triple `(minimum, maximum, size)`. The `size` is the current subtree's full node count only when that subtree is a BST. Invalid subtrees return a deliberately poisoned triple, while a separate nonlocal variable `ans` remembers the largest valid size found anywhere.

**Why postorder is the natural direction.**

A subtree rooted at node `root` is a BST only when all three conditions hold:

1. the complete left subtree is a BST;
2. the complete right subtree is a BST;
3. every left value is smaller than `root.val`, and every right value is greater.

If a valid left subtree reports its maximum `lmx`, then all its values are smaller than `root.val` exactly when

$$
lmx < \text{root.val}.
$$

If a valid right subtree reports its minimum `rmi`, then all its values are greater exactly when

$$
\text{root.val} < rmi.
$$

Thus, after both children have been processed, one chained comparison

$$
lmx < \text{root.val} < rmi
$$

contains all the cross-boundary ordering information the parent needs. This constant-time combination is what makes the full traversal linear.

**Make an empty subtree behave like a valid neutral child.**

For `root is None`, the helper returns

$$
(+\infty,-\infty,0).
$$

An empty tree is a valid BST of size zero. The unusual bounds are chosen to make comparisons work automatically:

- an empty left child's maximum is $-\infty$, which is smaller than every real node value;
- an empty right child's minimum is $+\infty$, which is greater than every real node value.

Consequently, a leaf with two empty children satisfies

$$
-\infty < \text{leaf.val} < +\infty
$$

and becomes a valid BST of size one without a special leaf branch.

**Poison an invalid subtree so no ancestor can accept it.**

If the current subtree is not a BST, the source returns

$$
(-\infty,+\infty,0).
$$

These are the opposite bounds from the empty case. If this invalid subtree later appears as a left child, its reported maximum is $+\infty$, so the condition $lmx < \text{parent.val}$ must fail. If it appears as a right child, its reported minimum is $-\infty$, so `parent.val < rmi` must fail.

This means the parent does not need a separate Boolean `is_bst`. Validity is encoded in the ordering of the returned bounds:

- empty valid subtree: minimum $+\infty$, maximum $-\infty$;
- nonempty valid subtree: genuine minimum no greater than genuine maximum;
- invalid subtree: poisoned minimum $-\infty$, maximum $+\infty$.

The poison propagates upward. A tree containing an invalid complete child subtree cannot itself be a BST, which is exactly the required behavior.

**Combine two valid children.**

When `lmx < root.val < rmi` succeeds, both child summaries must be valid and all cross-boundary values are ordered correctly. The current subtree's size is

$$
ln+rn+1,
$$

where `ln` and `rn` are the left and right BST sizes and the one counts `root`.

The source updates the global best with this size. It then returns the current valid subtree's bounds:

$$
\min(lmi,\text{root.val})
$$

for the minimum and

$$
\max(rmx,\text{root.val})
$$

for the maximum. In a valid nonempty left subtree, its minimum is below the root; if the left is empty, `lmi` is positive infinity and the root becomes the minimum. The right side behaves symmetrically for the maximum.

There is no need to include the right minimum when computing the overall minimum or the left maximum when computing the overall maximum. Once validity is established, every right value is greater than the root and every left value is smaller.

**Why invalid returns can use size zero.**

An invalid current subtree may still contain a large BST lower down. The helper does not return that descendant's size in its third field. Instead, each valid descendant updates `ans` at the moment it is recognized. Because postorder visits all descendants before their parent, their contributions are already preserved before an invalid parent returns `(negative infinity, positive infinity, 0)`.

This cleanly separates two meanings:

- the returned `size` describes the whole current subtree only if it is a BST;
- `ans` describes the greatest BST seen anywhere so far.

Mixing a “best descendant size” into the returned valid-subtree size would make `ln + rn + 1` incorrect, so the source's separation is important.

**Walk through the first example.**

In the subtree rooted at `5`, leaves `1` and `8` each return their own value as both minimum and maximum with size one. Since

$$
1 < 5 < 8,
$$

the subtree rooted at `5` is a BST of size three, with bounds `1` and `8`. The global answer becomes three.

At node `15`, the left child is empty and the right child contains `7`. Although each child subtree is individually a BST, the boundary test requires

$$
15 < 7,
$$

which is false. Node `15` therefore returns poisoned bounds. When root `10` reads that invalid right summary, its comparison fails automatically. The entire tree is not a BST, but the previously recorded size three remains the answer.

This example also shows why checking only each parent against its immediate child is insufficient. The condition must account for all descendant values, which the subtree minimum and maximum summarize.

**Why the result is correct.**

Use induction on subtree height. The empty subtree summary is correct. Assume both child summaries correctly identify valid BSTs and report their exact bounds and sizes, while invalid children return poison.

If the source's comparison succeeds, neither child can be poisoned, both are BSTs by induction, every left value is below the root through `lmx`, and every right value is above through `rmi`. The current subtree is therefore a BST, and its computed size and bounds are exact.

If the comparison fails, either a child is invalid or a boundary value violates strict BST order. In either case, the complete current subtree is not a BST, so poisoning it is correct. Every valid subtree is eventually recognized at its own root and updates `ans`. Thus the returned `ans` is exactly the maximum size over all BST subtrees.

## Complexity detail

Let $n$ be the number of tree nodes. Each node is visited once. It performs two recursive calls and then a constant number of comparisons, minimum/maximum operations, and arithmetic operations. Total time complexity is $O(n)$.

The recursion stack uses $O(h)$ space for tree height $h$, which is $O(n)$ in the worst case of a skewed tree. Apart from call frames and constant-size triples, no structure proportional to all nodes is allocated. The worst-case auxiliary space is therefore $O(n)$, or more precisely $O(h)$.

The manifest's asymptotic bounds match the source, but its summary describes iterative postorder summaries that also return the best descendant result. The checked-in optimal solution is recursive and stores the best globally in `ans`; this explanation follows those exact choices.

## Alternatives and edge cases

- **Iterative postorder:** Use an explicit stack and a map from nodes to summaries. This avoids recursion-depth limits and matches the manifest's traversal wording, but normally needs $O(n)$ explicit storage.

- **Validate every subtree separately:** For every node, run a full BST validation and node count. Repeated descendant scans can take $O(n^2)$ or worse; the postorder summary removes that duplication.

- **Inorder validation per subtree:** A BST has strictly increasing inorder values, but restarting inorder traversal at every candidate root still repeats work. It also needs a separate count unless more information is returned.

- **Empty tree:** `dfs(None)` returns the neutral triple, `ans` remains zero, and the public method returns zero.

- **Leaf:** Two neutral child summaries make the strict comparison succeed, producing size one.

- **Duplicate value:** Strict inequalities reject a duplicate equal to an ancestor boundary. The problem's BST definition uses less than and greater than, not less-than-or-equal.

- **A valid BST inside an invalid tree:** The child updates `ans` before its invalid ancestor is evaluated, so its size is not lost when poison propagates.

- **Extreme allowed values:** Real values are finite, so the positive and negative infinity sentinels remain safely outside their range and cannot collide with a node value.

- **Recursion depth:** A tree may contain `10000` nodes. A highly skewed shape can exceed Python's default recursion limit; iterative postorder would preserve the same state logic without that implementation-level risk.
