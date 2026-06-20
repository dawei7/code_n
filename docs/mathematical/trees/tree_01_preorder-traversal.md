# Formal Mathematical Specification: Pre-order Traversal

## 1. Definitions and Notation
Let $T$ be a binary tree defined recursively as either empty ($\emptyset$) or a tuple $T = (r, T_L, T_R)$ where $r \in V$ is the root node, and $T_L, T_R$ are binary trees representing the left and right subtrees.
Let $V$ be the set of all nodes in $T$.

## 2. Algebraic Characterization
We define the pre-order traversal function $\mathcal{P}: \mathcal{T} \to V^*$ (mapping a tree to a sequence of nodes).
$$ \mathcal{P}(T) = \begin{cases} 
\epsilon & \text{if } T = \emptyset \\
r \cdot \mathcal{P}(T_L) \cdot \mathcal{P}(T_R) & \text{if } T = (r, T_L, T_R)
\end{cases} $$
where $\cdot$ denotes sequence concatenation and $\epsilon$ is the empty sequence.

## 3. Complexity Analysis
- **Time Complexity:** The function $\mathcal{P}$ is applied exactly once per node $v \in V$. Thus time is $O(|V|)$.
- **Space Complexity:** The recursion depth is bounded by the height of the tree $H$. Space is $O(H)$.
