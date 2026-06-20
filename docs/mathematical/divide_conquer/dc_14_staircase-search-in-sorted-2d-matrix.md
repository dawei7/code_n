# Formal Mathematical Specification: Search a 2D Matrix (Staircase Search)

## 1. Definitions and Notation

Let $M$ be an $m \times n$ matrix of integers, where $m, n \in \mathbb{Z}^+$. We denote the element at row $i$ and column $j$ as $A_{i,j}$, where $0 \le i < m$ and $0 \le j < n$.

The matrix $A$ is defined by the following monotonicity properties:
1. **Row-wise monotonicity:** $\forall i \in \{0, \dots, m-1\}, \forall j \in \{0, \dots, n-2\}: A_{i,j} \le A_{i,j+1}$
2. **Column-wise monotonicity:** $\forall j \in \{0, \dots, n-1\}, \forall i \in \{0, \dots, m-2\}: A_{i,j} \le A_{i+1,j}$

The search objective is to determine the existence of a target value $\tau \in \mathbb{Z}$ such that:
$$f(A, \tau) = \begin{cases} 1 & \text{if } \exists (i, j) \in \{0, \dots, m-1\} \times \{0, \dots, n-1\} \text{ s.t. } A_{i,j} = \tau \\ 0 & \text{otherwise} \end{cases}$$

The state space $\mathcal{S}$ of the algorithm is defined by the tuple $(i, j)$, representing the current indices being inspected, where $(i, j) \in \{0, \dots, m-1\} \times \{0, \dots, n-1\}$.

## 2. Algebraic Characterization

The algorithm operates by maintaining a loop invariant that restricts the search space. Let $S_k$ be the set of candidate indices $(i, j)$ at iteration $k$ that could potentially contain $\tau$. Initially, $S_0 = \{0, \dots, m-1\} \times \{0, \dots, n-1\}$.

We initialize the pointer at the top-right corner: $(i_0, j_0) = (0, n-1)$. At each step $k$, we compare $A_{i_k, j_k}$ with $\tau$:

1. **Case 1 (Match):** If $A_{i_k, j_k} = \tau$, the search terminates with success.
2. **Case 2 (Elimination of Column):** If $A_{i_k, j_k} > \tau$, then by row-wise monotonicity, $\forall j' \ge j_k, A_{i_k, j'} \ge A_{i_k, j_k} > \tau$. Furthermore, by column-wise monotonicity, $\forall i' > i_k, A_{i', j_k} \ge A_{i_k, j_k} > \tau$. Thus, all elements in column $j_k$ at or below row $i_k$ are strictly greater than $\tau$. We update $j_{k+1} = j_k - 1$.
3. **Case 3 (Elimination of Row):** If $A_{i_k, j_k} < \tau$, then by column-wise monotonicity, $\forall i' \le i_k, A_{i', j_k} \le A_{i_k, j_k} < \tau$. Furthermore, by row-wise monotonicity, $\forall j' < j_k, A_{i_k, j'} \le A_{i_k, j_k} < \tau$. Thus, all elements in row $i_k$ at or to the left of column $j_k$ are strictly less than $\tau$. We update $i_{k+1} = i_k + 1$.

The invariant is that at any step $k$, if $\tau \in A$, then $\tau$ must exist in the sub-matrix defined by the remaining valid indices. The algorithm terminates when $i_k \ge m$ or $j_k < 0$, at which point the search space is empty, implying $\tau \notin A$.

## 3. Complexity Analysis

### Time Complexity
The algorithm performs a traversal starting from $(0, n-1)$ and terminates when the pointer exits the bounds of the matrix. In each iteration, either $i$ is incremented or $j$ is decremented. 
Let $T(m, n)$ be the number of steps. Since $i$ can increase at most $m$ times and $j$ can decrease at most $n$ times, the total number of iterations $K$ is bounded by:
$$K \le m + n$$
Each iteration performs a constant number of operations $O(1)$. Therefore, the total time complexity is:
$$T(m, n) = O(m + n)$$
This is optimal, as any algorithm must potentially inspect $O(m+n)$ elements to verify the absence of a target in the worst-case configuration of a sorted matrix.

### Space Complexity
The algorithm utilizes a constant number of auxiliary variables $(i, j, v)$ to track the current position and the value of the matrix element. No additional data structures proportional to the input size are required.
$$S(m, n) = O(1)$$
The space complexity is constant, satisfying the requirement for $O(1)$ auxiliary space.