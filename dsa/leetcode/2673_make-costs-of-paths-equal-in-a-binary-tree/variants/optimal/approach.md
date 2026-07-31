## General

Process internal nodes from the last parent back to the root. By the time a parent is visited, each child entry can represent the maximum cost of a path from that child to a leaf after all paths inside that child's subtree have already been equalized.

Let the two child subtree path costs be $L$ and $R$. Because costs can only increase, both sides must ultimately reach at least $\max(L,R)$. Raising the smaller side by $\lvert L-R\rvert$ is therefore necessary, and it is sufficient because every path within each child subtree is already equal. Add that difference to the answer, then add $\max(L,R)$ to the parent's cost so its parent receives the resulting subtree path cost.

This greedy choice is optimal independently at every sibling pair: increments applied above the pair affect both sides equally and cannot repair their difference, while increasing the larger side would only raise the target. Bottom-up processing accounts for each necessary difference once, so the accumulated increments are globally minimal.

## Complexity detail

Each internal node is processed once, giving $O(n)$ time. The algorithm stores subtree path costs back into `cost` and uses only scalar variables, so its auxiliary space is $O(1)$; the input array is modified in place.

## Alternatives and edge cases

- **Recursive postorder:** Returning each subtree's maximum path cost expresses the same recurrence clearly but uses $O(\log n)$ call-stack space for this perfect tree.
- **Recompute subtree maxima:** Calculating both child maxima from scratch for every parent is correct but repeats descendants and takes $O(n \log n)$ time on a perfect tree.
- Equal sibling subtree costs require no increments at that parent.
- A large difference deep in the tree and another difference above it are both necessary; balancing only the leaf level is insufficient.
- The root's own cost never affects differences among root-to-leaf paths because it belongs to every path.
