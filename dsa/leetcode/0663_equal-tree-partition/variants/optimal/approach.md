## General
**Every removable edge identifies one proper subtree**

Cutting the edge above a non-root node separates that node's entire subtree from the rest. If its sum is `s` and the whole tree sums to `T`, the two components are equal exactly when $s = T - s$, or $s = T / 2$.

Use postorder traversal to compute each subtree sum after both child sums are known. Store every computed sum, including duplicates because distinct nodes represent distinct possible cuts.

**Exclude the whole tree from cut candidates**

The root's computed sum is `T`, but no edge lies above the root. Remove that final postorder sum before searching for $T / 2$. This matters when $T = 0$: leaving the root sum in the collection would incorrectly claim that every zero-sum tree can be partitioned.

**Why the half-sum test is complete**

If a valid edge exists, its child-side subtree is proper and has sum $T / 2$, so postorder records it. Conversely, any recorded proper subtree with that sum has a real parent edge; cutting it leaves sum $T - T/2 = T/2$. An odd total cannot split into two equal integer sums and is rejected immediately.

## Complexity detail
Postorder visits each of the `N` nodes once and performs constant work, giving $O(N)$ time. The stored subtree sums and recursion stack use $O(N)$ space in the worst case.

## Alternatives and edge cases
- **Two traversals without storing all sums:** compute the total first, then search for a proper half-sum subtree; this uses $O(H)$ stack space but needs a second pass.
- **Iterative postorder with a node-to-sum map:** avoids recursion depth concerns while retaining $O(N)$ time and space.
- **Recompute a subtree sum for every possible cut:** is direct but revisits descendants and becomes $O(N^2)$ on a skewed tree.
- A single-node tree has no removable edge and must return `False`.
- A zero total requires a proper zero-sum subtree; the root alone is not a candidate.
- Negative node values do not change the half-sum argument.
- Duplicate subtree sums are harmless because only existence of a valid cut matters.
