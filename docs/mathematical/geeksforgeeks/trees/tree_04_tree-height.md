# Formal Mathematical Specification: Tree Height

## 1. Definitions and Notation
Let $T$ be a binary tree. The height $\mathcal{H}(T)$ is defined as the maximum number of edges on the longest path from the root to any leaf.

## 2. Algebraic Characterization
$$ \mathcal{H}(T) = \begin{cases} 
0 & \text{if } T = \emptyset \\
1 + \max(\mathcal{H}(T_L), \mathcal{H}(T_R)) & \text{if } T = (r, T_L, T_R)
\end{cases} $$
*(Note: If height is defined by nodes rather than edges, the base case for an empty tree is 0, and a single node is 1).*

## 3. Complexity Analysis
- **Time Complexity:** $O(|V|)$.
- **Space Complexity:** $O(\mathcal{H}(T))$.
