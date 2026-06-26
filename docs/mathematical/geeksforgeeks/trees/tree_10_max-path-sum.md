# Formal Mathematical Specification: Maximum Path Sum

## 1. Definitions and Notation
Let $w: V \to \mathbb{R}$ map each node to a scalar weight. We seek to maximize $\sum_{v \in P} w(v)$ over all simple paths $P \subseteq V$.

## 2. Algebraic Characterization
For a node $x \in V$, define $M(x)$ as the maximum path sum originating at $x$ and descending into at most one of its subtrees:
$$ M(x) = w(x) + \max(0, M(x_L), M(x_R)) $$
(with $M(\emptyset) = -\infty$).

Define $C(x)$ as the maximum path sum where $x$ is the highest node on the path (acting as the bridging vertex):
$$ C(x) = w(x) + \max(0, M(x_L)) + \max(0, M(x_R)) $$

The globally optimal path sum is $\max_{x \in V} C(x)$.

## 3. Complexity Analysis
- **Time Complexity:** $M(x)$ and $C(x)$ are computed in a single post-order traversal. $O(|V|)$.
- **Space Complexity:** $O(\mathcal{H}(T))$.
