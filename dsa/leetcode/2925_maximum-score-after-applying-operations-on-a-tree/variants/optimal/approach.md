## General

**Maximizing selected value is minimizing retained value.** All initial values
are positive, so a final root-to-leaf sum is nonzero exactly when that path
contains at least one node that was not selected. Let the total initial value
be $T$. If the minimum total value that must remain is $L$, the maximum score
is $T-L$.

**Compute the cheapest path-hitting set in each subtree.** Let
`minimum_retained[u]` be the least value that must remain in the subtree of
$u$ when no ancestor has already been retained. There are two possibilities:

- retain $u$, paying `values[u]`; then $u$ protects every path below it and
  all descendants may be selected;
- select $u$; then every child subtree must independently retain a node on each
  of its paths, costing the sum of the children's states.

For a leaf, the second choice is invalid because its root-to-leaf path would
retain nothing, so its state equals its own value. For an internal node the
recurrence is

$$
\texttt{minimum\_retained[u]} =
\min\left(\texttt{values[u]},
\sum_{v\text{ child of }u}\texttt{minimum\_retained[v]}\right).
$$

Root the tree iteratively and evaluate nodes in reverse root-first order.
Induction from the leaves shows that both exhaustive choices at every subtree
use optimal child losses, so the root state is the global minimum retained
value. Subtracting it from $T$ yields the maximum healthy score.

## Complexity detail

Let $n=\lvert\texttt{values}\rvert$. Rooting the tree and evaluating the
dynamic program each inspect every node and edge a constant number of times,
for $O(n)$ time. The adjacency lists, parent/order arrays, and retained-value
states use $O(n)$ auxiliary space.

## Alternatives and edge cases

- **Enumerate selected subsets:** Testing all $2^n$ node subsets and every root-to-leaf path is correct but exponential.
- **Maximum-score state:** A DP can directly track whether a path is already protected, but minimizing the unavoidable retained value yields a simpler one-state recurrence.
- **Recursive depth-first search:** It has the same recurrence and bounds, but a path of 20,000 nodes can exceed the call stack; iterative postorder avoids that risk.
- **Leaf node:** With no retained ancestor, a leaf must keep its own value because selecting it would zero its entire path.
- **Retained internal node:** Once an internal node remains positive, all descendants may be selected without endangering paths through it.
- **Branching node:** Selecting the node requires each child subtree to pay its own path-covering loss; keeping just one child branch is insufficient.
- **Large totals:** The score can exceed 32-bit signed range, so fixed-width implementations need 64-bit sums.

