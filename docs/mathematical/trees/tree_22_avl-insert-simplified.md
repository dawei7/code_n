# Formal Mathematical Specification: AVL Tree Insertion

## 1. Definitions and Notation
An AVL tree is a BST where $\forall x \in V, |\mathcal{H}(x_L) - \mathcal{H}(x_R)| \leq 1$.
Define the balance factor $\delta(x) = \mathcal{H}(x_L) - \mathcal{H}(x_R)$.

## 2. Algebraic Characterization (Rotations)
When an insertion violates the AVL property (i.e., $\exists x, |\delta(x)| = 2$), we apply $O(1)$ pointer rotations:
- **Left Rotation $\text{Rot}_L(x)$:** Let $y = x_R$. $x_R \leftarrow y_L$, $y_L \leftarrow x$.
- **Right Rotation $\text{Rot}_R(x)$:** Let $y = x_L$. $x_L \leftarrow y_R$, $y_R \leftarrow x$.

Balance corrections map deterministically:
1. $\delta(x) = 2 \land \delta(x_L) = 1 \implies \text{Rot}_R(x)$
2. $\delta(x) = 2 \land \delta(x_L) = -1 \implies \text{Rot}_L(x_L) \circ \text{Rot}_R(x)$
3. $\delta(x) = -2 \land \delta(x_R) = -1 \implies \text{Rot}_L(x)$
4. $\delta(x) = -2 \land \delta(x_R) = 1 \implies \text{Rot}_R(x_R) \circ \text{Rot}_L(x)$

## 3. Complexity Analysis
- **Time Complexity:** Descent is $O(\mathcal{H}(T))$. Height updates and rotations on ascent are $O(1)$ per level. Total time $O(\mathcal{H}(T)) = O(\log |V|)$.
- **Space Complexity:** $O(\log |V|)$ recursive depth.
