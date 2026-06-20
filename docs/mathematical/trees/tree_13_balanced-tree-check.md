# Formal Mathematical Specification: Balanced Tree Check

## 1. Definitions and Notation
A binary tree $T$ is height-balanced if and only if for every node $x \in V$, the height difference between its subtrees is bounded by 1.

## 2. Algebraic Characterization
We evaluate the predicate $\mathcal{B}(T) \in \{\text{True}, \text{False}\}$:
$$ \mathcal{B}(T) \iff \forall x \in V, |\mathcal{H}(x_L) - \mathcal{H}(x_R)| \leq 1 $$

Let $f: \mathcal{T} \to \mathbb{Z}$ compute the height of a balanced tree, returning $-1$ if unbalanced:
$$ f(T) = \begin{cases} 
0 & \text{if } T = \emptyset \\
-1 & \text{if } f(T_L) = -1 \lor f(T_R) = -1 \\
-1 & \text{if } |f(T_L) - f(T_R)| > 1 \\
1 + \max(f(T_L), f(T_R)) & \text{otherwise}
\end{cases} $$

Then $\mathcal{B}(T) \iff f(T) \neq -1$.

## 3. Complexity Analysis
- **Time Complexity:** Since $f(T)$ computes both height and balance status simultaneously in a single post-order pass, time is strictly $O(|V|)$.
- **Space Complexity:** $O(\mathcal{H}(T))$.
