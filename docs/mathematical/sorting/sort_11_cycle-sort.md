# Formal Mathematical Specification: Cycle Sort

## 1. Definitions and Notation

Let $A = [a_0, a_1, \dots, a_{n-1}]$ be an array of $n$ elements drawn from a totally ordered set $(\mathcal{X}, \leq)$. We define the sorting problem as finding a permutation $\sigma$ of the indices $\{0, 1, \dots, n-1\}$ such that the resulting array $A' = [a_{\sigma(0)}, a_{\sigma(1)}, \dots, a_{\sigma(n-1)}]$ satisfies $a_{\sigma(i)} \leq a_{\sigma(j)}$ for all $0 \leq i < j \leq n-1$.

*   **Target Position Function:** For any element $x \in A$, let $\text{pos}(x)$ be the rank of $x$ in $A$, defined as:
    $$\text{pos}(x) = \sum_{j=0}^{n-1} \mathbb{I}(a_j < x) + \sum_{j=0}^{k-1} \mathbb{I}(a_j = x)$$
    where $\mathbb{I}(\cdot)$ is the indicator function and $k$ is the current index of the element being placed.
*   **Cycle Decomposition:** The permutation required to sort $A$ can be decomposed into disjoint cycles. Let $\pi: \{0, \dots, n-1\} \to \{0, \dots, n-1\}$ be the mapping where $\pi(i)$ is the index where the element currently at $i$ must reside.
*   **State Space:** The algorithm operates on the state space $\mathcal{S} = \mathcal{X}^n \times \{0, \dots, n-1\} \times \mathcal{X}$, representing the current array configuration, the current cycle start index, and the "held" element being moved.

## 2. Algebraic Characterization

The algorithm relies on the decomposition of the permutation $\pi$ into disjoint cycles. A cycle is a sequence of indices $(i_0, i_1, \dots, i_m)$ such that $\pi(i_j) = i_{j+1 \pmod{m+1}}$.

**Loop Invariant:**
At the start of each iteration of the outer loop `cycle_start` $= s$, the subarray $A[0 \dots s-1]$ is sorted and contains the $s$ smallest elements of the original array in their correct positions.

**Transition Rule:**
Given an element $v$ at index $i$, the algorithm identifies the target index $j = \text{pos}(v)$. The swap operation is defined as:
$$(A[j], v) \leftarrow (v, A[j])$$
This operation is a transposition that places $v$ in its correct sorted position. Because the total number of elements is finite, the sequence of displacements $i \to j \to \dots \to i$ must terminate, forming a cycle. 

**Correctness:**
The algorithm is correct if, for every cycle $C = \{i_0, i_1, \dots, i_m\}$, the sequence of $m$ swaps results in $A[i_k]$ containing the element $x$ such that $\text{rank}(x) = i_k$. Since the algorithm iterates through all $i \in \{0, \dots, n-1\}$, and each element is moved at most once into its correct position, the final state $A'$ satisfies $A'[i] \leq A'[i+1]$ for all $i$.

## 3. Complexity Analysis

### Time Complexity
The time complexity is determined by the number of comparisons performed.

1.  **General Case:** For each `cycle_start` from $0$ to $n-2$, the algorithm performs a linear scan of the remaining array to determine the correct position of the current element.
    The total number of comparisons $T(n)$ is given by:
    $$T(n) = \sum_{i=0}^{n-2} (n - 1 - i) = \sum_{k=1}^{n-1} k = \frac{(n-1)n}{2}$$
    Thus, $T(n) = \Theta(n^2)$.

2.  **1-to-N Optimized Case:** When the input is a permutation of $\{1, \dots, n\}$, the target position is $\text{pos}(a_i) = a_i - 1$. The scan is replaced by an $O(1)$ lookup. Each swap places at least one element in its final position. Since there are $n$ elements, there are at most $n$ swaps. The total time complexity is $T(n) = O(n)$.

### Space Complexity
The algorithm performs all operations in-place.
*   **Auxiliary Space:** The algorithm requires a constant number of variables (`item`, `pos`, `cycle_start`, `i`) to track the current state.
*   **Total Space:** The space complexity is $O(1)$, as the memory usage does not scale with the input size $n$, satisfying the requirement for in-place sorting.