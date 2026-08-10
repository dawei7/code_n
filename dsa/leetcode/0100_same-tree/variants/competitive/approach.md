## General

The competitive implementation gives the recursive definition of tree equality in three cases. For each pair of corresponding references `p` and `q`:

- if both are absent, the subtrees match;
- if both exist, their values and both corresponding child subtrees must match; and
- if exactly one exists, the structures differ.

These cases are mutually exclusive and cover every possible pair.

**Both references are `None`**

An empty subtree has no values or child structure. Two empty subtrees are identical, so the first condition returns true. This is also the recursion base case reached beyond every pair of matching leaves.

Returning true here is essential. A leaf comparison needs both recursive child calls to succeed; its absent children are valid matching subtrees rather than errors.

**Both nodes exist**

The method returns one chained Boolean expression:

`p.val == q.val and isSameTree(p.left, q.left) and isSameTree(p.right, q.right)`

Python evaluates this from left to right. If values differ, neither child pair is explored. If values match but left subtrees differ, the right pair is skipped. Only when both preceding requirements succeed does it inspect the right subtrees.

This is logical short-circuiting, not a traversal-order requirement. Checking right before left would be equally correct; the selected order may simply discover certain mismatches sooner.

**Exactly one node exists**

If neither of the first two cases applied, one reference is `None` and the other is real. The final `return False` captures this structural mismatch. It must not compare values because the absent side has none.

**Why values alone are insufficient**

Trees `[1,2]` and `[1,null,2]` contain the same values if node positions are ignored. Yet at the roots' left position, one call receives a real node and `None`, so it returns false. The algorithm treats missing children as part of the tree representation.

Likewise, traversing only existing values without null-position information could confuse different shapes. Paired recursion retains position automatically through which child references are passed.

**Why corresponding directions matter**

The method compares `p.left` with `q.left` and `p.right` with `q.right`. A node appearing on the left in one tree and the right in the other is a structural difference, even if values match. Comparing crossed children would test mirror symmetry, not equality.

**Correctness by structural induction**

Two empty trees match, establishing the base. One empty and one nonempty tree cannot match. For two real roots, tree identity requires equal root values and identical left and right subtrees. The implementation checks exactly this conjunction.

Assuming recursive calls correctly decide smaller subtrees, the expression correctly decides the current pair. Induction over subtree size proves the method.

**No mutation or auxiliary node state**

The function reads `val`, `left`, and `right` only. It does not add markers, modify pointers, or require parent links. The top-level `TreeNode` class is platform-style support and does not participate beyond supplying those fields.

If the two inputs share some subtree object, recursion will compare that object with itself but this variant has no identity shortcut. It still walks the shared subtree and returns true. That is correct but may do more work than the Optimal source's initial equality test.

**A complete leaf-level trace**

Suppose both roots contain `1`, both left children contain `2`, and both right children are absent. Root values match, so the first recursive operand compares the two nodes valued `2`. Their values match, and each of their left and right child comparisons receives `(None, None)`, returning true. The root's left condition is therefore true. Its right comparison also receives `(None, None)`. All conjunction terms succeed, so the roots return true. If just one node-valued-two child had a nonempty descendant, the paired call at that exact position would instead reach the one-empty case and propagate false upward.

## Complexity detail

Let $n$ be the number of node pairs inspected before completion. Equal trees require visiting every real node and corresponding empty boundaries, which is $O(n)$ time. Unequal trees may return earlier, but the worst case remains linear.

The active recursive calls follow one corresponding root-to-leaf path. With comparison height $h$, auxiliary stack space is $O(h)$, matching the manifest. This is $O(\log n)$ for balanced trees and $O(n)$ for skewed trees.

The method allocates no containers or copied trees; aside from recursion, its working space is constant.

## Alternatives and edge cases

- **Iterative DFS:** Push pairs of corresponding nodes onto a stack. It uses $O(h)$ space and avoids call-stack limits.
- **Paired BFS:** A queue can expose the first shallow mismatch but may require $O(n)$ space on a wide tree.
- **Canonical serialization:** Include explicit null markers and compare serialized sequences. It is correct but allocates linear output solely for comparison.
- **Both empty:** Returns true in the first branch.
- **One empty:** Falls through to false without unsafe dereferencing.
- **Single equal nodes:** Values match and both pairs of empty children return true.
- **Same values, different positions:** The one-empty case detects the structural mismatch.
- **Duplicate values:** Repeated payloads are harmless because equality is checked at corresponding positions, not by searching for values.
- **Shared subtree references:** Correctly returns true for that region but still traverses it in this exact variant.
- **Identity optimization:** Adding `if p is q: return True` can skip a shared subtree safely because binary trees are acyclic under the contract. It changes best-case time, not the linear worst case.
- **Input size:** The stated 100-node maximum keeps recursive depth within normal Python limits.
