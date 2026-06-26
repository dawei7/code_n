# Formal Mathematical Specification: Mirror Tree

## 1. Definitions and Notation
Let $T = (r, T_L, T_R)$ be a binary tree.

## 2. Algebraic Characterization
The mirror function $\mathcal{M}: \mathcal{T} \to \mathcal{T}$ is an involution ($\mathcal{M}(\mathcal{M}(T)) = T$) defined by:
$$ \mathcal{M}(T) = \begin{cases} 
\emptyset & \text{if } T = \emptyset \\
(r, \mathcal{M}(T_R), \mathcal{M}(T_L)) & \text{if } T = (r, T_L, T_R)
\end{cases} $$

## 3. Complexity Analysis
- **Time Complexity:** Each node is visited and its children swapped exactly once. $O(|V|)$.
- **Space Complexity:** $O(\mathcal{H}(T))$.
