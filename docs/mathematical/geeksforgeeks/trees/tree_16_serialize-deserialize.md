# Formal Mathematical Specification: Tree Serialization

## 1. Definitions and Notation
Let $V \cup \{\#\}$ be the set of nodes including a null terminator. We define a bijective encoding map $E: \mathcal{T} \to (V \cup \{\#\})^*$.

## 2. Algebraic Characterization
Using a pre-order topological mapping:
$$ E(T) = \begin{cases} 
\# & \text{if } T = \emptyset \\
r \cdot E(T_L) \cdot E(T_R) & \text{if } T = (r, T_L, T_R)
\end{cases} $$
Because every node dictates exactly two subsequent recursive calls, the parsing algorithm possesses a deterministic unique inverse $E^{-1}$. 

## 3. Complexity Analysis
- **Time Complexity:** Both $E$ and $E^{-1}$ visit each structural node exactly once. $O(|V|)$.
- **Space Complexity:** The serialized string has size $2|V|+1$. Space is strictly $O(|V|)$.
