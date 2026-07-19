## General
**Consecutive key values matter only through their count**

Let `count[nodes]` be the number of BST structures over any fixed ordered set of that many distinct keys. Relabeling keys while preserving order does not change structural choices, so every interval of the same size has the same count.

**Each root position multiplies independent subtree choices**

If the chosen root has `left_size` smaller keys, exactly `nodes - 1 - left_size` larger keys remain for the right subtree. Every valid left structure combines independently with every valid right structure, so this root position contributes their count product. Sum over all `left_size` values from zero through `nodes - 1`.

**The empty-tree count is the multiplicative identity**

Set `count[0] = 1`. An empty side is one valid choice, which is the multiplicative identity needed for leaf nodes and one-sided trees.

**Compute sizes bottom-up so every factor is final**

After computing `count[nodes]`, it equals the number of valid BST structures for any ordered set of exactly `nodes` keys. All smaller entries are already final when the transition uses them.

**Trace the Catalan recurrence for three nodes**

For three nodes, root positions split subtree sizes as $(0,2)$, $(1,1)$, and $(2,0)$. With counts `count[0] = 1`, `count[1] = 1`, and `count[2] = 2`, the contributions are $1 \cdot 2 + 1 \cdot 1 + 2 \cdot 1 = 5$.

**Root splits produce the Catalan recurrence**

For a tree with `size` ordered keys, choosing the root fixes a left-subtree size `left` and right-subtree size `size - 1 - left`. Any valid left structure can be paired independently with any valid right structure, giving the product of their counts.

Every BST has exactly one root and one such subtree pair, while different roots or component structures yield different trees. Summing these disjoint products over all root positions therefore counts every BST exactly once.

## Complexity detail
For every size from `1` through `n`, the algorithm considers all possible left-subtree sizes, totaling $O(n^2)$ transitions. The table contains $n + 1$ integers, so auxiliary space is $O(n)$.

## Alternatives and edge cases
- **Construct every tree:** performs output-sized work even though only the count is required.
- **Unmemoized recursion:** repeats the same size subproblems exponentially often.
- **Closed-form Catalan arithmetic:** can use fewer iterations but requires careful exact integer division and is less directly derived from the tree decomposition.
- $n = 1$ uses one root with two empty children and returns one. The `count[0] = 1` base also supports generalized zero-node formulations.
- This problem asks only for a count; constructing nodes would add unnecessary Catalan-sized output work.
