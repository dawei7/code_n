# Formal Mathematical Specification: BST Search

## 1. Definitions and Notation
Let $T = (r, T_L, T_R)$ be a Binary Search Tree (BST). By definition, $\forall x \in T_L, x.val < r.val$ and $\forall y \in T_R, y.val > r.val$.

## 2. Algebraic Characterization
Define the search function $\mathcal{S}(T, k) \to \{ \text{True}, \text{False} \}$:
$$ \mathcal{S}(T, k) = \begin{cases} 
\text{False} & \text{if } T = \emptyset \\
\text{True} & \text{if } r.val = k \\
\mathcal{S}(T_L, k) & \text{if } k < r.val \\
\mathcal{S}(T_R, k) & \text{if } k > r.val
\end{cases} $$

## 3. Complexity Analysis
- **Time Complexity:** The number of recursive calls is bounded by the height of the tree $\mathcal{H}(T)$. Thus, time is $O(\mathcal{H}(T))$, which is $O(\log |V|)$ in a balanced tree and $O(|V|)$ in the worst case.
- **Space Complexity:** Iterative evaluation strictly uses $O(1)$ space. Recursive evaluation uses $O(\mathcal{H}(T))$ call stack space.
