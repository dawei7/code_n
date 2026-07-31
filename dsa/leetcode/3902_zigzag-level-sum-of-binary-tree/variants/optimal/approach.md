## General

**Keep structural traversal separate from level scoring**

Breadth-first search naturally produces the tree one complete level at a time. Store the current level in ordinary left-to-right tree order. Before moving on, append every non-null left and right child of every current node to the next-level list. This discovery step must include children even when the scoring rule has already stopped; the early stop changes only the current sum, not which deeper tree nodes exist.

**Inspect the same level in its required direction**

For an odd-numbered level, scan the stored list from beginning to end. For an even-numbered level, scan it in reverse. At each node, first test the required child—`left` for an odd level or `right` for an even one. If that child is absent, stop without adding the node. Otherwise add its value and continue. Append the completed sum, replace the current list with the next level, and toggle the parity.

At the start of every iteration, the list contains exactly the nodes at one depth in left-to-right order because it was formed by scanning the preceding level in that order and appending each left child before its right child. The chosen forward or reverse scan therefore matches the specified zigzag direction. The loop adds precisely the maximal prefix whose nodes satisfy the relevant child requirement and stops before the first violation, which is exactly the requested level sum. Since structural discovery always processes the complete level, induction also guarantees that every later level is reached once.

## Complexity detail

Let $N$ be the number of nodes and $W$ the maximum number of nodes on any one level. Every node is visited once while its level is scored and once while its children are collected, so the total time is $O(N)$.

The current and next level lists together contain nodes from at most two adjacent levels. Their combined size is $O(W)$; the returned answer has one integer per tree level.

## Alternatives and edge cases

- **Repeated depth searches:** Running a fresh traversal from the root to obtain each depth is correct, but it can revisit a length-$N$ chain quadratically instead of completing one breadth-first pass.
- **Reverse the stored level in place:** This can work for scoring, but child discovery must still use canonical left-to-right order; mixing the reversed scoring order into discovery changes the node order at the next depth.
- **Stop the complete traversal:** Discarding children after the first failing node is incorrect. Only that level's sum stops; deeper levels must still reflect the entire original tree.
- **Include the failing node:** The stop occurs immediately before that node, so its value must not be added.
- **Single-node tree:** The root has no left child, so the sole odd-level sum is `0`.
- **Negative values:** Sums may be negative, and `0` is not a lower bound; ordinary integer addition is required.
- **Wide sums:** Up to $10^5$ values of magnitude $10^5$ may contribute, so languages with fixed-width integers need a 64-bit sum.
- **Deep skewed tree:** Iterative breadth-first traversal avoids recursion-depth failure at the $10^5$-node limit.
