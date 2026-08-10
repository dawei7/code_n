## General

Two features make this tree problem unusual:

1. selecting a node flips the sign of every value in its subtree, so a later ancestor inversion negates the complete result already optimized below it;
2. selected inversion nodes in different branches must still be at pairwise distance at least `k`.

The source handles the first feature by storing both maximum and minimum subtree sums. It handles the second by indexing states with the distance from the subtree root to the nearest selected inversion node.

**Root the undirected tree without recursion**

The adjacency list stores every edge in both directions. Starting from node zero, the source builds:

- `parent[u]`, the rooted-tree parent of each node;
- `order`, a parent-before-child traversal order.

Iterating `reversed(order)` then processes every child before its parent. This avoids recursive depth problems when $n$ is as large as $5\cdot10^4$.

**Meaning of a distance state**

For a subtree rooted at `u`, define $d$ as the minimum distance from `u` to any inverted node inside that subtree, capped at `k`:

- values $0$ through $k-1$ are exact nearest distances;
- state $k$ means the nearest inversion is at distance at least $k$, or no inversion exists in the subtree.

`node_max[d]` is the greatest final sum attainable for the subtree with that distance state. `node_min[d]` is the smallest attainable sum for the same state.

Impossible maximum states contain `negative_infinity`, and impossible minimum states contain `positive_infinity`.

Why keep a minimum when the final goal is a maximum? If `u` itself is inverted, every current final value in its subtree changes sign. The greatest negated sum comes from the smallest pre-negation sum:

$$
\max(-S)=-\min(S).
$$

The paired arrays make that transformation available without remembering individual configurations.

**Initialize a subtree before choosing its root**

Before incorporating children or selecting the node, a one-node partial subtree has no inversion. Its nearest-distance state is `k` and its sum is `nums[node]`:

`node_max[k] = node_min[k] = nums[node]`.

Children are merged into this state one at a time. Only after all children have been incorporated does the source add the option of inverting the node itself.

**Lift a child's distances to its parent**

A selected inversion at distance $d$ from a child root is one edge farther from the parent. The merge first transforms each child state to:

$$
\min(k,d+1).
$$

Several child distances can collapse into capped state $k$, so `lifted_max` takes their maximum sums and `lifted_min` takes their minimum sums.

After lifting, both the accumulated parent side and the new child side express nearest-inversion distance from the same parent node.

**The cross-branch distance condition**

Suppose the accumulated current side has nearest inversion distance $a$ from the parent, and the new child side has nearest distance $b$. Any path between an inversion in one side and an inversion in the other passes through the parent. The closest cross-side pair has distance $a+b$.

The merge is legal exactly when:

$$
a+b\ge k.
$$

The merged state's nearest distance is $\min(a,b)$.

To compute all merged states in linear rather than quadratic time, fix an output distance $d$. There are two symmetric ways for the minimum to equal $d$:

1. the current side has exact distance $d$, while the child side has distance $b\ge d$ and $b\ge k-d$;
2. the child side has exact distance $d$, while the current side satisfies those two inequalities.

Both requirements combine into:

$$
b\ge\max(d,k-d).
$$

The source names this lower bound `threshold`.

**Suffix extrema make each threshold query constant time**

`current_suffix_max[t]` stores the maximum current-side sum among every distance at least $t$. `current_suffix_min[t]` stores the corresponding minimum. The child has analogous suffix arrays after lifting.

These arrays are built from right to left in $O(k)$. For each exact output distance $d$, the source can then obtain the best or worst compatible opposite-side state at `threshold` in constant time.

For maximum sums, it tries:

- `current_max[d] + child_suffix_max[threshold]`;
- `lifted_max[d] + current_suffix_max[threshold]`.

For minimum sums, it uses the parallel minimum expressions. Taking extrema handles every compatible pair. Cases where both sides have the same nearest distance may be represented twice, but duplicate representation does not affect a maximum or minimum.

This merge enforces every cross-branch pair. Restrictions internal to each side were already enforced by their DP states, so the combined configuration satisfies the global pairwise condition.

**Add the option to invert the current node**

After every child is merged, selecting `node` is compatible only with a configuration whose existing nearest inversion has capped distance `k`. Any descendant inversion closer than `k` would violate the distance rule with the node.

Selecting the node makes the new nearest distance zero and negates the entire accumulated subtree sum. Therefore:

`node_max[0] = max(node_max[0], -node_min[k])`

and

`node_min[0] = min(node_min[0], -node_max[k])`.

This correctly captures overlapping subtree operations. Descendant inversions may already have changed signs; applying the ancestor inversion afterward negates their complete final subtree result, which is exactly what the max/min swap models.

The no-inversion-at-node states remain available alongside this new state.

**Move completed states upward**

`pending_max` and `pending_min` hold partially accumulated arrays for ancestors whose later children are still being processed. When a node is reached in reversed traversal order, its pending arrays already include all of its children.

After adding the node-inversion option, its completed state is merged into its parent. At the root there is no parent, and every distance state is allowed. The source returns `max(node_max)`.

Every legal inversion set induces one state through these merges, with its exact final sum represented between the stored extrema. Every constructed transition respects pairwise distance and sign effects. Hence the root maximum is the desired answer.

## Complexity detail

Let $n$ be the node count and $K=k$.

Building the graph and traversal order takes $O(n)$. Each child-to-parent merge performs a constant number of length-$K+1$ scans: lifting, suffix extrema, and merged-state construction. Across $n-1$ edges, time is $O(nK)$.

Each active node state contains two arrays of length $K+1$. The graph, parent array, and order use $O(n)$ space. The conservative worst-case bound for pending DP arrays is $O(nK)$, matching the manifest.

The iterative traversal also avoids an $O(n)$ call stack on a path-shaped tree.

## Alternatives and edge cases

- **Enumerate inversion-node subsets:** There are $2^n$ subsets before checking distance, which is infeasible.
- **Store only maximum subtree sums:** Selecting an ancestor negates the complete subtree, so the best negated result depends on the previous minimum. Both extrema are essential.
- **Track only whether the root is inverted:** Cross-branch inversions can violate the distance constraint even when neither child root is selected. Nearest distance carries the required information.
- **Combine every pair of distance states directly:** That costs $O(K^2)$ per edge. Suffix extrema reduce compatible-range selection to $O(1)$ per output distance.
- **Forget to lift child distances:** A child's inversion is one edge farther from the parent; using the child-local distance directly would reject or allow wrong pairs.
- **Use threshold `k - d` only:** The opposite distance must also be at least $d$ so that the merged minimum remains exactly $d$. Hence `max(d, k - d)`.
- **Invert a node with a nearby descendant inversion:** Only state `k` is eligible before creating distance-zero state, enforcing the pairwise rule.
- **No inversion selected:** State `k` preserves the original subtree sum and remains available to the root maximum.
- **`k = 1`:** Distinct tree nodes are always at distance at least one, so any subset of nodes may be inverted; the DP still applies.
- **Large `k` relative to tree diameter:** At most one inversion can be selected. Capped distance states represent this naturally.
- **Negative original values:** Minimum states can become valuable when an ancestor inversion negates them into a large positive sum.
- **Sibling inversions:** Their distance is the sum of their depths from the parent; the merge admits them exactly when that sum reaches `k`.
- **Path-shaped tree:** Iterative order construction prevents recursion overflow, and pending states propagate bottom-up.
- **Sentinel arithmetic:** The source checks that a state is reachable before adding its sentinel value to another state.
