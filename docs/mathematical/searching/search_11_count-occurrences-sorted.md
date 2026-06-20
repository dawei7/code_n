# Formal Mathematical Specification: Count Occurrences in Sorted Array

## 1. Definitions and Notation

Let $A = [a_0, a_1, \dots, a_{n-1}]$ be a sequence of integers of length $n \in \mathbb{N}_0$, where the sequence is non-decreasing, such that $a_i \leq a_{i+1}$ for all $0 \leq i < n-1$. Let $x \in \mathbb{Z}$ be the target value.

We define the following sets and functions:
*   **Index Set:** $\mathcal{I} = \{0, 1, \dots, n\}$.
*   **Lower Bound Function:** $L(A, x) = \min \{ i \in \{0, \dots, n\} \mid i = n \lor a_i \geq x \}$.
*   **Upper Bound Function:** $U(A, x) = \min \{ i \in \{0, \dots, n\} \mid i = n \lor a_i > x \}$.
*   **Occurrence Count:** The objective is to compute the cardinality of the set of indices where the target appears:
    $$\mathcal{C}(A, x) = |\{ i \in \{0, \dots, n-1\} \mid a_i = x \}|$$

## 2. Algebraic Characterization

The correctness of the algorithm relies on the properties of the binary search functions $L$ and $U$. Given the sorted property of $A$, the following relations hold:

**Theorem 1 (Count Identity):** The number of occurrences of $x$ in $A$ is given by the difference of the upper and lower bounds:
$$\mathcal{C}(A, x) = U(A, x) - L(A, x)$$

**Proof Sketch:**
1. By definition, $L(A, x)$ is the smallest index $i$ such that $a_i \geq x$. If no such $i$ exists, $L(A, x) = n$.
2. By definition, $U(A, x)$ is the smallest index $j$ such that $a_j > x$. If no such $j$ exists, $U(A, x) = n$.
3. For all $k$ such that $L(A, x) \leq k < U(A, x)$, it must hold that $a_k = x$.
4. Thus, the indices of $x$ form a contiguous interval $[L(A, x), U(A, x) - 1]$. The number of elements in this interval is $(U(A, x) - 1) - L(A, x) + 1 = U(A, x) - L(A, x)$.

**Loop Invariant:**
For a binary search over the range $[lo, hi]$, let $P$ be the predicate defining the boundary. The invariant maintained at the start of each iteration is:
*   $0 \leq lo \leq hi \leq n$
*   For all $k < lo$, $\neg P(a_k)$ is true.
*   For all $k \geq hi$, $P(a_k)$ is true.
Upon termination, $lo = hi$, and $lo$ is the unique index satisfying the boundary condition.

## 3. Complexity Analysis

### Time Complexity
The algorithm performs two independent binary searches. Let $T(n)$ be the time complexity.
Each binary search operates by halving the search space $\mathcal{S}$ at each step $k$. The size of the search space at step $k$ is given by:
$$|\mathcal{S}_k| = \frac{n}{2^k}$$
The search terminates when $|\mathcal{S}_k| = 1$, which implies $k = \log_2 n$. 
Since each step involves a constant number of comparisons and arithmetic operations, the work per search is $W = O(1) \cdot \log_2 n$.
The total time complexity is:
$$T(n) = T_{lower}(n) + T_{upper}(n) = O(\log n) + O(\log n) = O(\log n)$$

### Space Complexity
The algorithm utilizes a fixed number of auxiliary variables (pointers `lo`, `hi`, `mid`, and the return values `first`, `last`). 
Let $S(n)$ be the auxiliary space complexity. Since the number of variables is independent of the input size $n$:
$$S(n) = \Theta(1)$$
The algorithm operates in-place on the input array $A$, thus the total space complexity is $O(1)$ beyond the input storage.