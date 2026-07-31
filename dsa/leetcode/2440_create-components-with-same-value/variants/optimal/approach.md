## General

Let $S$ be the sum of all node values. If deleting edges creates $c$ equal components, each component must have target value $T=S/c$. Thus $c$ must divide $S$, and $T$ cannot be smaller than the largest individual node value. The largest possible component count is consequently $\lfloor S/\max(\texttt{nums})\rfloor$.

Root the tree at node 0 once and record a traversal order and every node's parent. For a candidate target $T$, process nodes in reverse order. A node's subtotal initially contains its own value and later receives every unfinished child subtotal.

- A subtotal equal to $T$ forms a complete component. Conceptually cut its parent edge and pass nothing upward.
- A subtotal below $T$ is not complete, so add it to the parent.
- A subtotal above $T$ makes the candidate impossible. All node values are positive, so attaching more ancestors can never reduce it.

If the root finishes with subtotal $T$, all other completed subtrees also have value $T$. Their combined total forces exactly $c$ components, so $c-1$ edges are deleted. Conversely, any valid partition must cut precisely those rooted subtrees whose values reach $T$, making the postorder test necessary as well as sufficient.

Try component counts from the largest candidate down to 2 and skip non-divisors without traversing the tree. The first feasible count maximizes the number of components and therefore the number of removed edges. Return 0 when no nontrivial split works.

## Complexity detail

Let $n=\lvert\texttt{nums}\rvert$, let $S=\sum_i\texttt{nums[i]}$, and let $d(S)$ denote the number of positive divisors of $S$. Building the rooted order costs $O(n)$. At most $d(S)$ candidate counts divide $S$, and each corresponding postorder test costs $O(n)$, for $O(n\,d(S))$ time.

The adjacency list, parent array, traversal order, and working subtotals use $O(n)$ space. Iteration avoids recursion-depth failure on a chain of 20,000 nodes.

## Alternatives and edge cases

- **Recursive postorder:** It expresses the same subtree rule compactly, but a legal long chain exceeds Python's default recursion depth.
- **Enumerate deleted-edge subsets:** Checking all $2^{n-1}$ cut sets is exact only for tiny trees and grows exponentially.
- **Try every target value:** Most integers do not divide $S$ and cannot define equal component sums; divisor filtering avoids needless traversals.
- **Single node:** No edge exists, so the answer is 0.
- **All node values equal:** Every edge may be deleted, yielding $n$ one-node components.
- **Prime total:** Apart from special node values permitting target 1, a prime total often leaves no nontrivial component count.
- **Divisibility is not sufficient:** Even when $c$ divides $S$, the tree topology may prevent connected subtrees of target value.
- **Positive values:** The overshoot rejection relies on `nums[i] >= 1`; an unfinished subtotal can only grow toward the root.
