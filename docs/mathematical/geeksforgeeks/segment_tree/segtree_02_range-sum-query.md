# Formal Mathematical Specification: Range Sum Query

## 1. Definitions and Notation

Let $A = [a_0, a_1, \dots, a_{n-1}]$ be an array of elements where $a_i \in \mathbb{R}$ (or any additive monoid). A Segment Tree $\mathcal{T}$ is a rooted binary tree where each node $v$ corresponds to a closed interval $[tl, tr] \subseteq [0, n-1]$.

*   **State Space:** The tree $\mathcal{T}$ is defined by a mapping $f: V \to \mathbb{R}$, where $V$ is the set of nodes. For a node $v$ covering $[tl, tr]$, the value $f(v)$ is defined as:
    $$f(v) = \sum_{i=tl}^{tr} a_i$$
*   **Query Input:** A query is defined by a pair of indices $(l, r)$ such that $0 \le l \le r \le n-1$.
*   **Query Output:** The objective is to compute the function $Q(l, r) = \sum_{i=l}^{r} a_i$.
*   **Identity Element:** We define the additive identity $e = 0$, such that for any $x$, $x + e = x$.

## 2. Algebraic Characterization

The query function $Q(v, tl, tr, l, r)$ is defined recursively based on the intersection of the node's interval $[tl, tr]$ and the query interval $[l, r]$. Let $tm = \lfloor \frac{tl + tr}{2} \rfloor$. The recurrence relation is given by:

$$
Q(v, tl, tr, l, r) = 
\begin{cases} 
0 & \text{if } [tl, tr] \cap [l, r] = \emptyset \\
f(v) & \text{if } [tl, tr] \subseteq [l, r] \\
Q(2v, tl, tm, l, r) + Q(2v+1, tm+1, tr, l, r) & \text{otherwise}
\end{cases}
$$

**Correctness Invariant:**
For any node $v$ covering $[tl, tr]$, the value $f(v)$ is maintained as the invariant:
$$f(v) = f(left\_child(v)) + f(right\_child(v))$$
This ensures that the summation property is preserved across the tree structure, allowing the decomposition of the range $[l, r]$ into a disjoint union of canonical nodes whose intervals partition $[l, r]$.

## 3. Complexity Analysis

### Time Complexity
The time complexity $T(n)$ is governed by the number of nodes visited in the tree. 
At any level of the tree, we visit at most a constant number of nodes. Specifically, for any query $[l, r]$, the algorithm visits at most 4 nodes per level of the tree. 

Let $H$ be the height of the tree, where $H = \lceil \log_2 n \rceil$. The recurrence for the number of nodes visited $W(n)$ is:
$$W(n) \le 2W(n/2) + O(1)$$
By the Master Theorem (Case 1), where $a=2, b=2, d=0$:
$$T(n) = O(n^{\log_2 2}) = O(n^0 \log n) = O(\log n)$$
Thus, the query operation is strictly bounded by $O(\log n)$.

### Space Complexity
*   **Tree Storage:** The segment tree is a complete binary tree (or a heap-indexed array) representing $n$ leaves. The number of nodes in a full binary tree with $n$ leaves is $2n - 1$. Using a 1-indexed array representation, we require an array of size $4n$ to accommodate the tree structure, yielding $O(n)$ space for the data structure.
*   **Auxiliary Space:** The recursion depth is equal to the height of the tree, $H = \lceil \log_2 n \rceil$. Therefore, the auxiliary space complexity for the call stack is $O(\log n)$. 

Total space complexity is $O(n)$ for the structure and $O(\log n)$ for the execution stack.