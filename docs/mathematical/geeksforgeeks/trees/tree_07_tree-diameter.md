# Formal Mathematical Specification: Tree Diameter

## 1. Definitions and Notation
Let $d(u, v)$ be the distance (number of edges) between nodes $u, v \in V$.
The diameter $\mathcal{D}(T)$ is defined as $\max_{u, v \in V} d(u, v)$.

## 2. Algebraic Characterization
For any node $x \in V$, let $P(x)$ be the length of the longest path passing through $x$ such that $x$ is the highest node (closest to the root) on the path.
$$ P(x) = \mathcal{H}(x_L) + \mathcal{H}(x_R) $$
where $\mathcal{H}$ is the height defined by number of nodes.
The diameter is structurally bounded by the global maximum:
$$ \mathcal{D}(T) = \max_{x \in V} P(x) $$

## 3. Complexity Analysis
- **Time Complexity:** A post-order traversal computes $\mathcal{H}(x_L)$ and $\mathcal{H}(x_R)$ for all nodes sequentially. Evaluating the global max is an $O(1)$ scalar operation at each step. Total time is $O(|V|)$.
- **Space Complexity:** Recursion depth $O(\mathcal{H}(T))$.
