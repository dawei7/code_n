# Formal Mathematical Specification: In-order Traversal

## 1. Definitions and Notation
Let $T = (r, T_L, T_R)$ be a binary tree.

## 2. Algebraic Characterization
We define the in-order traversal function $\mathcal{I}: \mathcal{T} \to V^*$.
$$ \mathcal{I}(T) = \begin{cases} 
\epsilon & \text{if } T = \emptyset \\
\mathcal{I}(T_L) \cdot r \cdot \mathcal{I}(T_R) & \text{if } T = (r, T_L, T_R)
\end{cases} $$

**Theorem (BST Property):** If $T$ is a Binary Search Tree, the sequence $\mathcal{I}(T)$ is monotonically non-decreasing.

## 3. Complexity Analysis
- **Time Complexity:** $O(|V|)$ since each node is visited once.
- **Space Complexity:** $O(H)$ where $H$ is the tree height.
