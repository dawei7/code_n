# Formal Mathematical Specification: Post-order Traversal

## 1. Definitions and Notation
Let $T = (r, T_L, T_R)$ be a binary tree.

## 2. Algebraic Characterization
We define the post-order traversal function $\mathcal{O}: \mathcal{T} \to V^*$.
$$ \mathcal{O}(T) = \begin{cases} 
\epsilon & \text{if } T = \emptyset \\
\mathcal{O}(T_L) \cdot \mathcal{O}(T_R) \cdot r & \text{if } T = (r, T_L, T_R)
\end{cases} $$

## 3. Complexity Analysis
- **Time Complexity:** $O(|V|)$.
- **Space Complexity:** $O(H)$.
