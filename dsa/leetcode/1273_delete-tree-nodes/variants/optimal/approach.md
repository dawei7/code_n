## General

**A parent decision requires complete child information**

Whether a subtree disappears depends on the sum of every value inside it. This is naturally a postorder computation: process all children first, combine their results with the current node, and only then decide whether the current subtree has sum zero.

The parent array is converted to child adjacency lists in `g`. For every non-root node `i`, the code appends it to `g[parent[i]]`. This works even if a parent has a larger numeric index than its child; it relies on relationships, not input ordering. Node zero is skipped because its parent marker is `-1`.

**Return both sum and surviving count**

Function `dfs(i)` returns a pair `(s, m)`. Variable `s` is the total value sum of the original subtree rooted at `i`. Variable `m` is the number of nodes from that subtree that remain after zero-sum deletions.

The state begins with the current node alone: `s = value[i]` and `m = 1`. For every child `j`, recursion returns `(t, n)`. The parent adds `t` to its subtree sum and `n` to its surviving count.

After all children have been combined, `s` is the complete subtree sum. If `s == 0`, the whole subtree rooted at `i` must be removed, including any descendants that had otherwise survived, so `m` is reset to zero. The sum is still returned as zero. If `s` is nonzero, `m` remains the current node plus all child survivors.

Keeping the sum of a deleted child is safe because such a child is deleted only when its sum is zero. Adding that zero to an ancestor is exactly equivalent to removing the child first. Thus bottom-up deletion and computing sums on the original tree agree for ancestor decisions.

**Why the pair recurrence is correct**

For a leaf, `s` equals its value and `m` begins at one. A zero-valued leaf returns count zero; a nonzero leaf returns count one, exactly matching the rule.

Assume every child returns its correct subtree sum and remaining-node count. Adding child sums plus the current value gives the current subtree's exact sum. If it is zero, the rule deletes every node there, so count zero is correct. Otherwise, the current node stays and the only removed descendants are those already assigned zero counts by child calls, so one plus their surviving counts is correct. Induction proves the returned pair for every node.

The public answer is `dfs(0)[1]` because node zero roots the entire tree. If the whole tree sums to zero, the root call returns zero survivors.

In the first example, zero-sum branches contribute zero remaining nodes while their zero sums do not change ancestors. The root's nonzero surviving structure ultimately contains two nodes.

**Why counting must wait until the sum is known**

A node with nonzero personal value can still disappear because descendants cancel it, while a zero-valued node can remain when its descendants give the full subtree a nonzero sum. For that reason, the algorithm cannot decide survival when first entering a node. It tentatively counts the node, obtains every child result, and makes exactly one deletion decision after the total is complete. Resetting `m` rather than returning early during child processing also ensures that a later child has the opportunity to change a partial sum from zero to nonzero or back again.

## Complexity detail

Let $n$ equal `nodes`. Building adjacency lists processes $n-1$ parent relations in $O(n)$ time. DFS visits each node once and traverses each parent-child edge once, also $O(n)$. Total time is $O(n)$.

The adjacency lists contain $n-1$ entries and use $O(n)$ space. Recursion uses $O(h)$ frames for tree height $h$, at most $O(n)$. Total auxiliary space is $O(n)$.

The exact recursive source can approach depth $n$ on a chain. With up to ten thousand nodes, that can exceed Python's default recursion limit even though the asymptotic method is correct. An iterative postorder implementation avoids this runtime concern.

## Alternatives and edge cases

- **Iterative postorder:** Build an explicit traversal order, then process it backward while accumulating sums and counts. It retains $O(n)$ time and space without recursion-depth risk.
- **Index-order accumulation:** Processing nodes backward works only if parents are guaranteed to have smaller indices. This contract does not require that, so adjacency-based traversal is safer.
- **Delete nodes during traversal:** Physically modifying adjacency lists is unnecessary; returning zero survivors represents deletion cleanly.
- **Zero-valued leaf:** Its one-node subtree has sum zero and disappears.
- **Zero-sum internal subtree:** All its descendants are removed even if some child subtrees individually had nonzero sums.
- **Deleted child and ancestor sums:** A deleted subtree contributes exactly zero, so it cannot change the ancestor's total.
- **Entire tree sums to zero:** The root count is reset to zero.
- **Single nonzero node:** It remains and the answer is one.
- **Negative values:** They are essential because positive and negative descendants may cancel; no greedy sign rule is valid.
- **Deep chain:** Use iterative traversal if the execution environment cannot support the exact recursion depth.
