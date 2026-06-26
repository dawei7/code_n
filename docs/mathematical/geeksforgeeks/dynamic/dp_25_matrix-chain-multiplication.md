# Formal Mathematical Specification: Matrix Chain Multiplication (Top-Down Memoization)

## 1. Definitions and Notation

Let $\mathcal{A} = \{A_1, A_2, \dots, A_n\}$ be a sequence of $n$ matrices. Each matrix $A_i$ has dimensions $d_{i-1} \times d_i$, where the sequence of dimensions is given by a vector $p \in \mathbb{Z}_{>0}^{n+1}$, such that $A_i \in \mathbb{R}^{p_{i-1} \times p_i}$.

The objective is to find the minimum number of scalar multiplications required to compute the product $A_1 A_2 \dots A_n$. Since matrix multiplication is associative, the product is well-defined, but the computational cost depends on the parenthesization.

- **State Space:** Let $\mathcal{S} = \{ (i, j) \in \mathbb{Z}^2 \mid 1 \le i \le j \le n \}$ be the set of all possible sub-chains of matrices.
- **Cost Function:** Let $m(i, j)$ be the minimum scalar multiplications required to compute the product $A_{i \dots j} = A_i A_{i+1} \dots A_j$.
- **Memoization Table:** We define a table $M \in \mathbb{Z}^{n \times n}$ where $M_{i,j}$ stores the computed value of $m(i, j)$.

## 2. Algebraic Characterization

The optimal cost $m(i, j)$ is defined by the following recurrence relation:

$$
m(i, j) = 
\begin{cases} 
0 & \text{if } i = j \\
\min_{i \le k < j} \{ m(i, k) + m(k+1, j) + p_{i-1} \cdot p_k \cdot p_j \} & \text{if } i < j
\end{cases}
$$

**Correctness Invariant:**
For any sub-chain $A_{i \dots j}$, the optimal cost is the minimum over all possible split points $k \in \{i, i+1, \dots, j-1\}$ of the sum of the costs of the two resulting sub-chains plus the cost of the final multiplication of the two resulting matrices, which have dimensions $(p_{i-1} \times p_k)$ and $(p_k \times p_j)$ respectively.

The memoization mechanism ensures that for every pair $(i, j) \in \mathcal{S}$, the value $m(i, j)$ is computed exactly once and stored, transforming the recursive structure into a dynamic programming evaluation over the state space $\mathcal{S}$.

## 3. Complexity Analysis

### Time Complexity
The time complexity is determined by the number of states in the memoization table and the work performed per state.

1. **State Space Size:** The number of unique pairs $(i, j)$ such that $1 \le i \le j \le n$ is given by the triangular number:
   $$|\mathcal{S}| = \sum_{i=1}^n \sum_{j=i}^n 1 = \frac{n(n+1)}{2} = O(n^2)$$
2. **Work per State:** For each state $(i, j)$, we iterate through $k$ from $i$ to $j-1$. The number of iterations is $j - i$. In the worst case, this is $O(n)$.
3. **Total Complexity:** The total time complexity $T(n)$ is the sum of work over all states:
   $$T(n) = \sum_{1 \le i \le j \le n} (j - i) \approx \int_1^n \int_i^n (j-i) \, dj \, di = O(n^3)$$
Thus, the algorithm operates in $\Theta(n^3)$ time.

### Space Complexity
1. **Auxiliary Space:** The memoization table $M$ requires $O(n^2)$ space to store the results of the sub-problems.
2. **Recursion Stack:** In the top-down approach, the maximum depth of the recursion tree is $n$. Thus, the stack space is $O(n)$.
3. **Total Space:** The total space complexity is dominated by the memoization table, yielding $O(n^2)$.