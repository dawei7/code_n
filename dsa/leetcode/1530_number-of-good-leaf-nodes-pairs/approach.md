## General

**Count each pair at its lowest common ancestor**

For two leaves, their shortest path rises to their lowest common ancestor and descends to the other leaf. At that ancestor, one leaf lies in the left subtree and the other in the right subtree.

The exact solution recursively counts good pairs already contained entirely in each child subtree, then counts pairs crossing between the two child subtrees of the current root.

This partitions pairs by their lowest common ancestor, so each pair is counted once.

**The depth-limited helper**

`dfs(root, cnt, i)` records how many leaves occur at each distance `i` from the current main root. It is called on a child with `i = 1`.

If the node is null or `i >= distance`, it returns. A leaf at distance at least the limit cannot form a cross pair, because the other leaf is at distance at least one and their sum would exceed `distance`.

If the node is a leaf before that cutoff, `cnt[i] += 1` records it. Otherwise, the helper descends to both children with distance `i + 1`.

Two separate counters, `cnt1` and `cnt2`, collect distances for left and right leaves.

**Pairs already below the current root**

The method begins

`countPairs(root.left, distance) + countPairs(root.right, distance)`.

Those recursive calls count pairs whose lowest common ancestors lie fully inside the left or right subtree. They cannot count a cross pair because neither child subtree contains both leaves.

**Counting cross pairs**

For every left distance `k1` with multiplicity `v1` and right distance `k2` with multiplicity `v2`, the path through the current root has length `k1 + k2`.

If that sum is at most the limit, every one of the `v1` left leaves pairs with every one of the `v2` right leaves. The source adds `v1 * v2`.

Because one endpoint comes from each side, a pair is never reversed and counted twice at this node.

**Why the complete recursion is correct**

Any two distinct leaves are either both in one child subtree or split across the children. In the first case, the corresponding recursive call counts them. In the second, their lowest common ancestor is the current node, the helper records both distances, and the nested loops test their exact path length.

These cases are disjoint and exhaustive. Induction on subtree size proves that the returned total is exact.

**The source repeatedly scans descendants**

This is not the one-pass postorder histogram method described later in the editorial. At every node, after recursively solving its children, the source launches fresh depth-limited DFS scans into those child subtrees.

The repeated scans are bounded by the small maximum distance, but they do revisit nodes near many ancestors. This distinction affects complexity.

**Why the cutoff excludes distance itself**

The helper stops when `i >= distance`. A cross pair needs another leaf on the other side at distance at least one, so a leaf at distance `distance` would yield total at least `distance + 1`. Excluding it cannot remove a good cross pair.

Pairs within that same subtree are handled recursively and do not depend on the current root's cutoff scan.

## Complexity detail

Let $N$ be node count, $D$ the distance limit, and $H$ tree height. The recursive `countPairs` visits every node as a main root once.

At each main root, the two helper scans visit nodes within fewer than $D$ downward edges. In a binary tree this can be $O(\min(N,2^D))$ nodes. The nested counter loops use at most $O(D^2)$ distance combinations.

A faithful bound for the exact source is therefore

$$
O\left(N\min(N,2^D)+ND^2\right).
$$

With the contractual $D\le10$, this is linear in $N$ with a potentially large fixed factor. If $D$ were allowed to grow with $N$, worst-case repeated scanning could approach $O(N^2)$. The manifest's $O(ND^2)$ describes the one-pass histogram approach more directly than this implementation.

The main recursion stack uses $O(H)$. Each helper uses up to $O(D)$ additional depth, and its counters hold at most $D$ keys. Total live auxiliary space is $O(H+D)$, apart from recursive frames and small counters; a broad safe bound is $O(H+D)$ rather than the manifest's histogram-frame $O(HD)$.

## Alternatives and edge cases

- **Postorder distance histograms:** Return leaf counts by distance from each node and merge child arrays. This gives $O(ND^2)$ time without rescanning descendants.
- **Prefix-summed histogram merge:** Count cross pairs in $O(D)$ per node for $O(ND)$ time.
- **Convert to graph and BFS from every leaf:** It is simple but can require $O(N^2)$ time.
- **Single leaf:** No pair of different leaves exists, so the answer is zero.
- **Distance one:** Distinct leaves cannot be one edge apart in a binary tree, and the helper cutoff records no cross candidates.
- **Sibling leaves:** Each is distance one from their parent, producing path length two.
- **One empty child:** One counter is empty, so no cross pair is added.
- **Pair below current root:** It is counted by a child recursive call, not again at the current node.
- **Pruned distant leaf:** It cannot participate in a valid cross pair through this ancestor.
- **Recursion depth:** A tree near the maximum 1024 nodes can approach Python's usual recursion threshold if highly skewed.
