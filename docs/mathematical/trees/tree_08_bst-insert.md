# Formal Mathematical Specification: BST Insertion

## 1. Definitions and Notation
Let $T$ be a Binary Search Tree and $k$ be a scalar value to insert.

## 2. Algebraic Characterization
The insertion function $\mathcal{I}(T, k) \to T'$ produces a new structurally valid BST:
$$ \mathcal{I}(T, k) = \begin{cases} 
(k, \emptyset, \emptyset) & \text{if } T = \emptyset \\
(r, \mathcal{I}(T_L, k), T_R) & \text{if } k < r.val \\
(r, T_L, \mathcal{I}(T_R, k)) & \text{if } k > r.val \\
T & \text{if } k = r.val \text{ (assuming no duplicates)}
\end{cases} $$

## 3. Complexity Analysis
- **Time Complexity:** The path trace takes $O(\mathcal{H}(T))$ time.
- **Space Complexity:** Iterative manipulation uses $O(1)$ extra space.
