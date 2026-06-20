# Formal Mathematical Specification: Selection Sort

## 1. Definitions and Notation

Let $A = [a_0, a_1, \dots, a_{n-1}]$ be a sequence of $n$ elements drawn from a totally ordered set $(\mathcal{X}, \le)$. The objective of the Selection Sort algorithm is to produce a permutation $A'$ of $A$ such that $A' = [a'_0, a'_1, \dots, a'_{n-1}]$ satisfies the condition $a'_0 \le a'_1 \le \dots \le a'_{n-1}$.

We define the state of the algorithm at any iteration $i \in \{0, 1, \dots, n-2\}$ by the partition of the array into two contiguous segments:
*   **Sorted Prefix:** $A[0 \dots i-1]$, where for all $j < k < i$, $a_j \le a_k$.
*   **Unsorted Suffix:** $A[i \dots n-1]$, where for all $x \in A[0 \dots i-1]$ and $y \in A[i \dots n-1]$, $x \le y$.

The algorithm operates on the state space $\mathcal{S} = \mathcal{X}^n$, transforming the initial configuration $A^{(0)} = A$ into the final configuration $A^{(n-1)}$ through a sequence of $n-1$ discrete swap operations.

## 2. Algebraic Characterization

The correctness of Selection Sort is governed by the following loop invariant: At the start of each iteration $i$, the subarray $A[0 \dots i-1]$ is sorted and contains the $i$ smallest elements of the original array.

### The Selection Function
In each iteration $i$, we define the selection of the index $m_i$ as:
$$m_i = \text{argmin}_{j \in \{i, \dots, n-1\}} \{A[j]\}$$
If multiple indices satisfy the condition, $m_i$ is defined as the smallest such index.

### The State Transition
The transition from state $i$ to $i+1$ is defined by the transposition $\tau_i = (i, m_i)$, which swaps the elements at indices $i$ and $m_i$:
$$A^{(i+1)} = A^{(i)} \circ \tau_i$$
where the composition denotes the application of the swap. The algorithm terminates when $i = n-1$, at which point the invariant implies:
$$\forall j, k \in \{0, \dots, n-1\}, j < k \implies A[j] \le A[k]$$

## 3. Complexity Analysis

### Time Complexity
The time complexity is determined by the number of comparisons performed. In each iteration $i$, the algorithm performs a linear scan of the unsorted suffix $A[i \dots n-1]$. The number of comparisons $C(n)$ is given by the summation:
$$T(n) = \sum_{i=0}^{n-2} \sum_{j=i+1}^{n-1} 1$$
Evaluating the inner sum:
$$\sum_{j=i+1}^{n-1} 1 = (n-1) - (i+1) + 1 = n - i - 1$$
Substituting into the outer sum:
$$T(n) = \sum_{i=0}^{n-2} (n - i - 1)$$
Let $k = n - i - 1$. As $i$ ranges from $0$ to $n-2$, $k$ ranges from $n-1$ down to $1$:
$$T(n) = \sum_{k=1}^{n-1} k = \frac{(n-1)n}{2} = \frac{1}{2}n^2 - \frac{1}{2}n$$
Thus, $T(n) = \Theta(n^2)$. Since the number of comparisons is independent of the initial permutation of $A$, the best, average, and worst-case time complexities are identical: $O(n^2)$.

### Space Complexity
The algorithm operates in-place. It requires a constant amount of auxiliary storage for the loop indices $i, j$ and the pointer $m_i$, regardless of the input size $n$. 
*   **Auxiliary Space:** $O(1)$.
*   **Total Space:** $O(n)$ to store the input array $A$.

The number of write operations (swaps) is bounded by $n-1$, as each iteration performs at most one swap, satisfying the requirement for minimal write operations in memory-constrained environments.