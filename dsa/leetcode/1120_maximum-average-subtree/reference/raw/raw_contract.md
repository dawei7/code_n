## Function Contract

**Inputs**

- `root`: the root of a nonempty binary tree. cOde(n) fixtures serialize the tree in level order, using `null` for an absent child.

Let $N$ be the number of nodes in the tree. For a node $u$, its subtree contains $u$ and every node descended from $u$ through left- or right-child links. Its average is

$$
\frac{\text{sum of values in the subtree rooted at }u}{\text{number of nodes in that subtree}}.
$$

**Return value**

- The maximum subtree average over all $N$ possible roots. Answers within $10^{-5}$ of the exact value are accepted.
