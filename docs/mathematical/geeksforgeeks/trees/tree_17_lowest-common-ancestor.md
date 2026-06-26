# Formal Mathematical Specification: Lowest Common Ancestor (LCA)

## 1. Definitions and Notation
Let $u, v \in V$. Node $a$ is an ancestor of $x$ if $a$ lies on the path from the root to $x$. 
The Lowest Common Ancestor $\text{LCA}(u, v)$ is the node $a$ that is an ancestor of both $u$ and $v$ such that $d(\text{root}, a)$ is maximized.

## 2. Algebraic Characterization
For a general binary tree, let $f(T)$ return $T$ if $T = u$ or $T = v$, otherwise compute recursively:
$$ L = f(T_L), \quad R = f(T_R) $$
$$ \text{LCA}(T) = \begin{cases} 
T & \text{if } T \in \{u, v\} \\
T & \text{if } L \neq \emptyset \land R \neq \emptyset \\
L \text{ or } R & \text{if exactly one of } L, R \neq \emptyset \\
\emptyset & \text{otherwise}
\end{cases} $$

*(For a BST, the structural invariant yields $\text{LCA}$ directly by finding the first node $a$ where $\min(u, v) \leq a.val \leq \max(u, v)$).*

## 3. Complexity Analysis
- **Time Complexity:** General binary tree requires a full traversal, $O(|V|)$. A BST allows binary search, bounded by $O(\mathcal{H}(T))$.
- **Space Complexity:** $O(\mathcal{H}(T))$.
