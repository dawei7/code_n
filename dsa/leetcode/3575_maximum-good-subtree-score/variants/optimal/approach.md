## General

Represent the decimal digits used by a value with a $D$-bit mask, where $D=10$. While extracting digits, encountering a bit that is already set makes the value unusable: selecting that node alone would repeat a digit. Otherwise, two selections are compatible exactly when their masks are disjoint.

For each node $u$, define `dp[mask]` as the maximum sum of a good subset in $u$'s processed subtree that uses exactly `mask`; unreachable masks hold `-1`. Before processing children, the empty subset gives `dp[0] = 0`, and the node's own value supplies one additional state when its digit mask is valid.

Process nodes in reverse root-first order, so every child's table is ready before its parent. To merge a child, combine a parent-side mask $a$ and child mask $b$ only when $a\mathbin{\&}b=0$, and maximize the entry for $a\mathbin{|}b$. The implementation chooses between two equivalent enumerations: Cartesian products of currently reachable masks when the tables are sparse, or all submasks of the digits not used by $a$ when dense. This hybrid changes constants, not the states or result.

Inductively, the initial table contains every legal choice involving only the node. A disjoint merge considers every union of one legal choice from the accumulated children and one from the next child, while rejecting exactly the digit-conflicting unions. After all children, the table therefore represents every good subset of the complete subtree and stores the largest score for each exact mask. Its maximum is `maxScore[u]`; summing those maxima and applying the modulus gives the requested result.

## Complexity detail

Let $D=10$. For a fixed left mask $a$, submask enumeration visits $2^{D-\operatorname{popcount}(a)}$ compatible right masks. Summed over every $a$, this is

$$
\sum_{a\subseteq\{0,\ldots,D-1\}}2^{D-\lvert a\rvert}=3^D.
$$

The hybrid always chooses work no greater than this dense enumeration after scanning the two $2^D$ tables. Each of the $n-1$ child merges therefore costs $O(3^D)$ time, and tree construction plus traversal is linear, for $O(n3^D)$ total time. Retaining one $2^D$ table per node uses $O(n2^D)$ space, in addition to $O(n)$ tree storage.

The benchmark fixes six active decimal digits and uses a chain of size $S=n$. The accepted postorder computation processes every edge once, so its growth in $S$ is linear. The calibrated alternative independently rebuilds a digit-mask knapsack for every rooted subtree; the chain has $\Theta(S^2)$ total subtree membership and exposes its extra factor of $S$.

## Alternatives and edge cases

- **Recompute every subtree independently:** Running a fresh node-by-node mask knapsack for each root is correct but repeats descendants and costs $O(n^2 2^D)$ on a chain.
- **Unrestricted mask Cartesian product:** Testing all $2^D\cdot2^D$ mask pairs per edge costs $O(n4^D)$; disjoint-submask enumeration reduces the dense bound to $O(n3^D)$.
- **Greedy by node value:** A large value can block several compatible smaller values, so local magnitude does not determine the best subset.
- **Repeated digit inside one value:** Such a node has no selectable state, but its descendants remain available through the empty parent-side choice.
- **Digit zero:** Zero receives an ordinary mask bit when it occurs inside a positive value such as `10`; leading zeros do not exist in decimal representation.
- **Empty subset:** `dp[0] = 0` ensures every subtree has a valid score even when all of its values repeat digits internally.
- **Parent indices:** Parent identifiers need not precede their children numerically, so derive an explicit traversal from node `0`.
- **Modulo timing:** Table scores must retain their true sums for maximization; apply the modulus only to the final sum of subtree maxima.
