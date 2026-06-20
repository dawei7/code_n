# Formal Mathematical Specification: Symmetric Tree Check

## 1. Definitions and Notation
A tree $T$ is symmetric if it is structurally and value-identical to its mirror image $\mathcal{M}(T)$.
$T = \mathcal{M}(T)$.

## 2. Algebraic Characterization
Define a binary predicate $\mathcal{E}(T_A, T_B)$ evaluating equivalence between a left branch and a mirrored right branch:
$$ \mathcal{E}(T_A, T_B) = \begin{cases}
\text{True} & \text{if } T_A = \emptyset \land T_B = \emptyset \\
\text{False} & \text{if } (T_A = \emptyset \oplus T_B = \emptyset) \\
r_A = r_B \land \mathcal{E}(T_{A,L}, T_{B,R}) \land \mathcal{E}(T_{A,R}, T_{B,L}) & \text{otherwise}
\end{cases} $$

The tree is symmetric iff $\mathcal{E}(T_L, T_R)$ is True.

## 3. Complexity Analysis
- **Time Complexity:** The predicate checks each pair of nodes at most once. $O(|V|)$.
- **Space Complexity:** Recursion depth is bounded by $O(\mathcal{H}(T))$.
