# Formal Mathematical Specification: Point Update

## 1. Definitions and Notation

Let $A = [a_0, a_1, \dots, a_{N-1}]$ be an array of $N$ elements where $a_i \in \mathbb{R}$. A Segment Tree $\mathcal{T}$ is a rooted binary tree representing a partition of the index range $[0, N-1]$.

*   **Tree Structure:** Each node $v$ in $\mathcal{T}$ corresponds to an interval $[L_v, R_v] \subseteq [0, N-1]$.
*   **State Space:** The tree $\mathcal{T}$ is represented by an array $T$ of size $4N$. For a node $v$, let $T[v]$ denote the value stored at that node, defined by the associative binary operator $\oplus$ (e.g., summation):
    $$T[v] = \bigoplus_{i=L_v}^{R_v} a_i$$
*   **Leaf Nodes:** A node $v$ is a leaf if $L_v = R_v = i$, in which case $T[v] = a_i$.
*   **Internal Nodes:** For a non-leaf node $v$ with children $u_{left}$ and $u_{right}$ covering $[L_v, M]$ and $[M+1, R_v]$ respectively, where $M = \lfloor (L_v + R_v) / 2 \rfloor$:
    $$T[v] = T[u_{left}] \oplus T[u_{right}]$$
*   **Update Operation:** Given a position $p \in \{0, \dots, N-1\}$ and a new value $x \in \mathbb{R}$, the update function $\text{update}(v, p, x)$ modifies $A$ such that $a_p \leftarrow x$ and updates all $T[v]$ such that $p \in [L_v, R_v]$.

## 2. Algebraic Characterization

The correctness of the Point Update algorithm is governed by the recursive definition of the tree nodes. Let $T^{(t)}$ denote the state of the tree at time $t$. The update operation is defined by the following recurrence relation for a node $v$ covering $[L_v, R_v]$:

1.  **Base Case (Leaf):** If $L_v = R_v = p$, then:
    $$T^{(t+1)}[v] = x$$
2.  **Recursive Step (Internal):** If $L_v \leq p \leq R_v$ and $L_v < R_v$:
    Let $M = \lfloor (L_v + R_v) / 2 \rfloor$.
    If $p \leq M$, then $T^{(t+1)}[v] = T^{(t+1)}[u_{left}] \oplus T^{(t)}[u_{right}]$.
    If $p > M$, then $T^{(t+1)}[v] = T^{(t)}[u_{left}] \oplus T^{(t+1)}[u_{right}]$.

**Invariant:** For any node $v$ such that $p \notin [L_v, R_v]$, $T^{(t+1)}[v] = T^{(t)}[v]$. The update operation maintains the invariant that for all $v \in \mathcal{T}$, $T[v]$ remains the result of the associative operation $\oplus$ applied to the elements in its range $[L_v, R_v]$ under the modified array $A'$.

## 3. Complexity Analysis

### Time Complexity
The algorithm traverses a path from the root to a leaf. Let $H$ be the height of the tree. Since the tree is a balanced binary tree constructed over $N$ elements, the height is $H = \lceil \log_2 N \rceil$.

At each level $k \in \{0, 1, \dots, H\}$, the algorithm performs a constant number of operations:
1.  Comparison of $p$ with $M$.
2.  Recursive call (or base case assignment).
3.  The merge operation $T[v] = T[u_{left}] \oplus T[u_{right}]$ during the backtracking phase.

The total work $W(N)$ is given by the recurrence:
$$W(N) = W(N/2) + O(1)$$
By the Master Theorem, where $a=1, b=2, f(n)=O(1)$, we have $W(N) = O(\log N)$. Thus, the time complexity is $\Theta(\log N)$.

### Space Complexity
*   **Auxiliary Space:** The algorithm uses a recursive call stack. Since the depth of the recursion is equal to the height of the tree, the maximum depth of the stack is $H = \lceil \log_2 N \rceil$. Therefore, the auxiliary space complexity is $O(\log N)$.
*   **Total Space:** The tree structure itself occupies $O(N)$ space (typically $4N$ nodes to accommodate the heap-like indexing). The update operation is performed in-place, requiring $O(1)$ additional space beyond the recursion stack. Thus, the total space complexity is $O(N)$.