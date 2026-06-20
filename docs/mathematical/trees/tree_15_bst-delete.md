# Formal Mathematical Specification: BST Deletion

## 1. Definitions and Notation
Let $T$ be a Binary Search Tree and $k$ the key to delete.

## 2. Algebraic Characterization
Deletion function $\mathcal{D}(T, k) \to T'$:
1. Search phase identical to $\mathcal{S}(T, k)$.
2. If $T = \emptyset$, return $\emptyset$.
3. Let $x$ be the node where $x.val = k$.
   - **Case 1 (Leaf):** If $x_L = \emptyset \land x_R = \emptyset$, return $\emptyset$.
   - **Case 2 (One Child):** If $x_L = \emptyset$, return $x_R$. If $x_R = \emptyset$, return $x_L$.
   - **Case 3 (Two Children):** Find the inorder successor $y$ (minimum node in $x_R$). Replace $x.val \leftarrow y.val$. Recursively apply $\mathcal{D}(x_R, y.val)$.

## 3. Complexity Analysis
- **Time Complexity:** The path to $x$ is $O(\mathcal{H}(T))$. Finding the inorder successor $y$ requires descending further, but the total descent never exceeds $\mathcal{H}(T)$. Total time is mathematically bounded by $O(\mathcal{H}(T))$.
- **Space Complexity:** $O(\mathcal{H}(T))$ for recursion, $O(1)$ for iterative.
