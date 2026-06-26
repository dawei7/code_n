# Formal Mathematical Specification: Union-Find (Disjoint Set Union, DSU)

## 1. Definitions and Notation

Let $S = \{0, 1, \dots, n-1\}$ be a finite set of $n$ elements. A **partition** $\mathcal{P}$ of $S$ is a collection of disjoint non-empty subsets $\{S_1, S_2, \dots, S_k\}$ such that $\bigcup_{i=1}^k S_i = S$ and $S_i \cap S_j = \emptyset$ for $i \neq j$.

The Disjoint Set Union (DSU) data structure maintains a representation of $\mathcal{P}$ through a forest of rooted trees $\mathcal{F} = \{T_1, T_2, \dots, T_k\}$. Each tree $T_i$ corresponds to a set $S_i \in \mathcal{P}$.

- **State Space:** The state is defined by a pair of mappings $(\pi, \rho)$, where:
    - $\pi: S \to S$ is the parent pointer function. For any node $x$, $\pi(x)$ denotes the parent of $x$. If $\pi(x) = x$, then $x$ is the **representative** (root) of its set.
    - $\rho: S \to \mathbb{N}_0$ is the rank function, where $\rho(x)$ provides an upper bound on the height of the subtree rooted at $x$.
- **Operations:**
    - $\text{find}(x)$: Returns the unique root $r \in S$ such that $r$ is the ancestor of $x$ in $\mathcal{F}$.
    - $\text{union}(x, y)$: Transforms $\mathcal{P}$ into $\mathcal{P}'$ by merging the sets containing $x$ and $y$.

## 2. Algebraic Characterization

The correctness of the DSU structure is governed by the following invariants and transition rules:

### Invariants
1. **Representative Invariant:** For any $x \in S$, the representative of the set containing $x$ is the unique element $r$ such that $\pi^{(k)}(x) = r$ for some $k \ge 0$, where $\pi^{(k)}$ denotes the $k$-th iteration of $\pi$, and $\pi(r) = r$.
2. **Rank Invariant:** For any node $x$, $\rho(x)$ is strictly less than $\rho(\pi(x))$ if $x$ is not a root. Furthermore, for any tree of height $h$, the root $r$ satisfies $\rho(r) \ge h$.

### Transition Rules (Union by Rank)
Given $r_x = \text{find}(x)$ and $r_y = \text{find}(y)$, the union operation updates $\pi$ and $\rho$ as follows:
- If $r_x = r_y$, the partition remains unchanged.
- If $r_x \neq r_y$:
    - If $\rho(r_x) < \rho(r_y)$, set $\pi(r_x) \leftarrow r_y$.
    - If $\rho(r_x) > \rho(r_y)$, set $\pi(r_y) \leftarrow r_x$.
    - If $\rho(r_x) = \rho(r_y)$, set $\pi(r_y) \leftarrow r_x$ and increment $\rho(r_x) \leftarrow \rho(r_x) + 1$.

### Path Compression
During $\text{find}(x)$, the mapping $\pi$ is updated for all nodes $v$ on the path from $x$ to the root $r$:
$$\forall v \in \text{path}(x, r), \pi(v) \leftarrow r$$
This transformation preserves the set partition $\mathcal{P}$ while reducing the path length for future operations.

## 3. Complexity Analysis

### Time Complexity
The amortized time complexity of a sequence of $m$ operations on $n$ elements is $O(m \cdot \alpha(n))$, where $\alpha$ is the inverse Ackermann function.

**Derivation:**
The Ackermann function $A_k(j)$ grows extremely rapidly. Its inverse, $\alpha(n) = \min \{k : A_k(1) \ge n\}$, grows extremely slowly. The proof, originally provided by Tarjan (1975), utilizes a potential function $\Phi$ defined on the state of the forest. 
Let $rank(x)$ be the rank of node $x$. We define a potential $\phi(x)$ based on the distance of $rank(x)$ to the rank of its parent. The total potential $\Phi = \sum \phi(x)$ is shown to decrease or remain stable during path compression, compensating for the $O(\log n)$ worst-case tree height. Summing the amortized costs over $m$ operations yields:
$$T(m, n) = \sum_{i=1}^m \text{cost}(op_i) \le O(m \cdot \alpha(n))$$
For all practical values of $n$ ($n < 2^{2^{65536}}$), $\alpha(n) \le 5$, rendering the operations effectively constant time.

### Space Complexity
The space complexity is $O(n)$.
- The parent array $\pi$ requires $n$ storage units.
- The rank array $\rho$ requires $n$ storage units.
- Total auxiliary space is $2n$, which is $\Theta(n)$. The input storage is $O(n+m)$, but the data structure itself is strictly linear with respect to the number of elements.