## General

**A parent needs two summaries from each child**

Whether a node qualifies cannot be decided from the child roots alone. It
needs the total value and the number of nodes across both child subtrees.
Postorder traversal supplies exactly that information: process the children
first, then combine their summaries with the current node.

For a missing child, use sum zero and count zero. If the left child returns
$(S_L,C_L)$ and the right child returns $(S_R,C_R)$, the current subtree has

$$
S=S_L+S_R+\texttt{node.val}
\qquad\text{and}\qquad
C=C_L+C_R+1.
$$

The node qualifies precisely when `S // C == node.val`. After recording that
match, return $(S,C)$ so the parent can perform the same calculation.

**Why one postorder traversal is sufficient**

A leaf combines two empty summaries, giving its own value and count one, so it
always matches its subtree average. Inductively, suppose both child summaries
contain the exact sums and counts of their subtrees. Adding them and the
current node therefore gives the exact summary of the current subtree, and
integer division computes the required rounded-down average. Thus every node
is tested against the correct value when it is processed. Since postorder
visits every node once, the accumulated match count is the requested answer.

## Complexity detail

Let $n$ be the number of nodes and $h$ the tree height. Each node is entered
and combined once, so the running time is $O(n)$. The recursive calls use
$O(h)$ auxiliary stack space, which is $O(n)$ for a skewed tree.

## Alternatives and edge cases

- **Recompute each subtree independently:** Starting a fresh sum-and-count traversal at every node is correct but can take $O(n^2)$ time on a skewed tree.
- **Store every subtree's values:** Materializing value lists makes the average easy to calculate but duplicates data and can also require quadratic total work and space.
- **Leaf node:** Its subtree average equals its own value, so every leaf qualifies.
- **Rounded-down average:** Use integer floor division; do not compare against a floating-point mean or round to the nearest integer.
- **Zero values:** A subtree sum and average may both be zero, and such nodes must be counted normally.
- **Iterative postorder for a skewed tree:** An explicit stack avoids dependence on the language's recursion-depth limit but needs additional bookkeeping for completed child summaries.
- **Repeated values:** Several ancestors may all qualify; each node contributes separately.
