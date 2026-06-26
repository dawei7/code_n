# Formal Mathematical Specification: Pancake Sort

## 1. Definitions and Notation

Let $A = [a_0, a_1, \dots, a_{n-1}]$ be a sequence of $n$ distinct integers. We define the state space $\mathcal{S}$ as the set of all permutations of $A$. The objective is to reach the sorted state $A^* = [s_0, s_1, \dots, s_{n-1}]$ such that $s_0 < s_1 < \dots < s_{n-1}$ using only the prefix reversal operator.

*   **Prefix Reversal Operator:** Define $\rho_k: \mathcal{S} \to \mathcal{S}$ as the function that reverses the prefix of length $k+1$ (indices $0$ to $k$). Formally, for a sequence $A$, the transformed sequence $A' = \rho_k(A)$ is defined as:
    $$a'_i = \begin{cases} a_{k-i} & \text{if } 0 \le i \le k \\ a_i & \text{if } k < i < n \end{cases}$$
*   **Input:** A permutation $A \in \mathcal{S}$.
*   **Output:** A sequence of indices $\mathcal{K} = [k_1, k_2, \dots, k_m]$ such that $\rho_{k_m}(\dots \rho_{k_1}(A) \dots) = A^*$.
*   **Active Boundary:** Let $j$ denote the current size of the unsorted prefix, where $j \in \{n, n-1, \dots, 2\}$.

## 2. Algebraic Characterization

The algorithm operates by maintaining a loop invariant regarding the suffix of the array.

**Loop Invariant:** At the start of each iteration $j$ (where $j$ is the number of elements in the current unsorted prefix), the suffix $A[j \dots n-1]$ is sorted and contains the $n-j$ largest elements of the original set $A$, such that $\forall x \in \{0, \dots, j-1\}, \forall y \in \{j, \dots, n-1\}: a_x < a_y$.

**Transition Logic:**
Let $m_j$ be the index of the maximum element in the prefix $A[0 \dots j-1]$, such that $a_{m_j} = \max \{a_0, \dots, a_{j-1}\}$. The algorithm performs the following state transitions:
1. If $m_j \neq 0$, apply $\rho_{m_j}$ to move the maximum to the front: $A \leftarrow \rho_{m_j}(A)$.
2. Apply $\rho_{j-1}$ to move the maximum to the end of the current active prefix: $A \leftarrow \rho_{j-1}(A)$.

The correctness is guaranteed by the fact that after these two operations, the element $a_{j-1}$ is the global maximum of the set $\{a_0, \dots, a_{j-1}\}$, satisfying the invariant for $j-1$. The process terminates when $j=1$, as a single-element prefix is trivially sorted.

## 3. Complexity Analysis

### Time Complexity
The algorithm consists of an outer loop that iterates $n-1$ times. Within each iteration $j$:
1. **Finding the maximum:** A linear scan over $j$ elements requires $j-1$ comparisons.
2. **Reversal operations:** The `flip` operation (prefix reversal) involves $\lfloor \frac{k+1}{2} \rfloor$ swaps. In the worst case, $k = j-1$, requiring $O(j)$ operations.

The total time complexity $T(n)$ is the sum of the work performed across all iterations:
$$T(n) = \sum_{j=2}^{n} (O(j) + O(j)) = \sum_{j=2}^{n} O(j)$$
Using the arithmetic series summation formula $\sum_{i=1}^{n} i = \frac{n(n+1)}{2}$, we obtain:
$$T(n) = O\left(\frac{n(n+1)}{2}\right) = O(n^2)$$
Thus, the algorithm is bounded by $O(n^2)$ in the worst and average cases.

### Space Complexity
The algorithm performs all operations in-place. 
*   **Auxiliary Space:** The variables `max_idx`, `size`, `start`, and `end` require $O(1)$ space.
*   **Total Space:** Since the input array is modified directly and no additional data structures proportional to $n$ are required for the sorting logic itself (excluding the output sequence $\mathcal{K}$), the auxiliary space complexity is $O(1)$. If the sequence of flips $\mathcal{K}$ must be stored, the space complexity is $O(n)$, as the number of flips is bounded by $2n - 3$.