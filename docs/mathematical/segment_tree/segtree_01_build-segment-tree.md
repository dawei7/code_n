# Formal Mathematical Specification: Build Segment Tree

## 1. Definitions and Notation

Let $A = [a_0, a_1, \dots, a_{n-1}]$ be an input sequence of elements from a set $\mathcal{X}$ equipped with an associative binary operation $\oplus: \mathcal{X} \times \mathcal{X} \to \mathcal{X}$. 

A **Segment Tree** is a rooted binary tree $\mathcal{T} = (V, E)$ representing a hierarchical decomposition of the index set $I = \{0, 1, \dots, n-1\}$. 
- Each node $v \in V$ is associated with a sub-interval $[l_v, r_v] \subseteq I$.
- The root node $v_{root}$ is associated with $[0, n-1]$.
- For any internal node $v$ with interval $[l_v, r_v]$, let $m = \lfloor \frac{l_v + r_v}{2} \rfloor$. The left child $v_L$ is associated with $[l_v, m]$ and the right child $v_R$ with $[m+1, r_v]$.
- Leaf nodes are nodes where $l_v = r_v$.

We map $\mathcal{T}$ to an array $T$ of size $M = 4n$ using the indexing function $idx: V \to \{1, \dots, M\}$:
- $idx(v_{root}) = 1$.
- $idx(v_L) = 2 \cdot idx(v)$ and $idx(v_R) = 2 \cdot idx(v) + 1$.

The state space $\mathcal{S}$ of the tree is defined by the mapping $f: V \to \mathcal{X}$, where $f(v)$ stores the result of the range query over $[l_v, r_v]$.

## 2. Algebraic Characterization

The construction of the tree is governed by the following recurrence relation for the values stored in the nodes:

$$
f(v) = 
\begin{cases} 
a_{l_v} & \text{if } l_v = r_v \text{ (Base Case)} \\
f(v_L) \oplus f(v_R) & \text{if } l_v < r_v \text{ (Recursive Step)}
\end{cases}
$$

**Correctness Invariant:**
For any node $v$ covering the interval $[l_v, r_v]$, the value $f(v)$ satisfies:
$$f(v) = \bigoplus_{i=l_v}^{r_v} a_i$$
Given that $\oplus$ is associative, the order of evaluation in the post-order traversal is guaranteed to produce the correct result for any range $[l, r] \subseteq [0, n-1]$.

**Structural Invariant:**
The tree is a complete binary tree structure embedded in an array. For an input of size $n$, the number of leaves is $n$, and the total number of nodes $|V| = 2n - 1$. The array size $4n$ is chosen such that for any $n \ge 1$, $4n \ge 2^{\lceil \log_2 n \rceil + 1} - 1$, ensuring no index out-of-bounds error occurs during the mapping $idx(v)$.

## 3. Complexity Analysis

### Time Complexity
The algorithm employs a post-order traversal of the tree. Let $T(n)$ be the time complexity to build a segment tree for an array of size $n$. The recurrence relation is:
$$T(n) = T\left(\left\lfloor \frac{n}{2} \right\rfloor\right) + T\left(\left\lceil \frac{n}{2} \right\rceil\right) + O(1)$$
By the Master Theorem (or the recursion tree method), since the work done at each node is constant $O(1)$ and the number of nodes is $2n-1$, the total time complexity is:
$$T(n) = \sum_{v \in V} O(1) = O(2n - 1) = O(n)$$
Thus, the build process is linear with respect to the input size $n$.

### Space Complexity
The space complexity is determined by the storage required for the array $T$. 
- **Auxiliary Space:** The recursion stack depth is $O(\log n)$, representing the height of the balanced binary tree.
- **Total Space:** The algorithm allocates an array of size $4n$. Since $4n$ is a constant multiple of $n$, the total space complexity is:
$$S(n) = O(n) + O(\log n) = O(n)$$
The $O(n)$ space requirement is optimal for a static representation of the segment tree structure.