# Formal Mathematical Specification: Range Update, Range Query (Dual BIT)

## 1. Definitions and Notation

Let $A = \{a_1, a_2, \dots, a_n\}$ be an array of $n$ elements, initially $a_i = 0$ for all $i \in \{1, \dots, n\}$. We define the state of the system by the sequence of updates applied to $A$.

*   **Update Operation:** A range update is defined by the tuple $(l, r, \delta)$, where $1 \le l \le r \le n$ and $\delta \in \mathbb{R}$. The operation transforms $A$ such that $a_i \leftarrow a_i + \delta$ for all $i \in [l, r]$.
*   **Query Operation:** A range query is defined by the tuple $(l, r)$, returning the sum $S(l, r) = \sum_{i=l}^r a_i$.
*   **Difference Array:** Let $D = \{d_1, d_2, \dots, d_n, d_{n+1}\}$ be the difference array such that $d_i = a_i - a_{i-1}$ (with $a_0 = 0$). Consequently, $a_i = \sum_{j=1}^i d_j$.
*   **Fenwick Tree (BIT):** A BIT is a data structure representing an array $B$ that supports point updates and prefix sum queries in $O(\log n)$ time. We denote $BIT(B, x) = \sum_{j=1}^x B_j$.

## 2. Algebraic Characterization

To support range updates and range queries, we express the prefix sum $P(x) = \sum_{i=1}^x a_i$ in terms of the difference array $D$.

Expanding the definition of $a_i$:
$$P(x) = \sum_{i=1}^x \sum_{j=1}^i d_j$$

By changing the order of summation (counting how many times each $d_j$ contributes to the total sum):
$$P(x) = \sum_{j=1}^x d_j \cdot (x - j + 1)$$
$$P(x) = (x + 1) \sum_{j=1}^x d_j - \sum_{j=1}^x (d_j \cdot j)$$

We define two Fenwick Trees, $T_1$ and $T_2$, to maintain the components of this identity:
1. $T_1$ stores the difference array $D$, such that $T_1.query(x) = \sum_{j=1}^x d_j$.
2. $T_2$ stores the product array $D'$, where $d'_j = d_j \cdot j$, such that $T_2.query(x) = \sum_{j=1}^x (d_j \cdot j)$.

**Update Transition:**
For a range update $(l, r, \delta)$, the difference array $D$ is modified at indices $l$ and $r+1$:
*   $d_l \leftarrow d_l + \delta$
*   $d_{r+1} \leftarrow d_{r+1} - \delta$

Correspondingly, the updates to $T_1$ and $T_2$ are:
*   $T_1$: Update index $l$ by $\delta$, and index $r+1$ by $-\delta$.
*   $T_2$: Update index $l$ by $\delta \cdot l$, and index $r+1$ by $-\delta \cdot (r+1)$.

**Query Formulation:**
The prefix sum $P(x)$ is computed as:
$$P(x) = (x + 1) \cdot T_1.query(x) - T_2.query(x)$$
The range sum $S(l, r)$ is then given by the fundamental theorem of summation:
$$S(l, r) = P(r) - P(l-1)$$

## 3. Complexity Analysis

### Time Complexity
Let $N$ be the number of elements and $M$ be the number of operations.
*   **Update:** The `range_update` operation performs four point updates across two BITs. Each point update in a BIT of size $N$ traverses the height of the tree, which is $\lceil \log_2 N \rceil$. Thus, the complexity is $O(\log N)$.
*   **Query:** The `range_query` operation performs two prefix sum calculations, each involving two BIT queries. Each BIT query takes $O(\log N)$ time. Thus, the complexity is $O(\log N)$.
*   **Total Time:** $O(M \log N)$.

### Space Complexity
The algorithm maintains two arrays of size $N+2$ to represent the Fenwick Trees $T_1$ and $T_2$.
*   **Total Space:** $O(N)$.
The auxiliary space is minimal, as the structure operates in-place on the two BIT arrays, satisfying the requirement for memory efficiency compared to a segment tree, which typically requires $O(4N)$ space.