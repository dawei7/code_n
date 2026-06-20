# Formal Mathematical Specification: Search in Rotated Sorted Array

## 1. Definitions and Notation

Let $A = [a_0, a_1, \dots, a_{n-1}]$ be an array of $n$ distinct integers. We define $A$ as a **rotated sorted array** if there exists a pivot index $k \in \{0, 1, \dots, n-1\}$ such that the sequence $S = [s_0, s_1, \dots, s_{n-1}]$ is strictly increasing (i.e., $s_i < s_{i+1}$ for all $0 \le i < n-1$), and the elements of $A$ are a cyclic shift of $S$ by $k$ positions:
$$a_i = s_{(i-k) \pmod n}$$

*   **Input:** A rotated sorted array $A$ of length $n$ and a target value $\tau \in \mathbb{Z}$.
*   **Output:** An index $idx \in \{0, 1, \dots, n-1\}$ such that $a_{idx} = \tau$, or $-1$ if $\tau \notin A$.
*   **State Space:** The algorithm maintains a search interval defined by the indices $[L, R]$, where $0 \le L \le R < n$.

## 2. Algebraic Characterization

The correctness of the algorithm relies on the **Sorted Half Property**. For any midpoint $M = \lfloor \frac{L+R}{2} \rfloor$, the subarray $A[L \dots R]$ is partitioned into two segments: $A[L \dots M]$ and $A[M+1 \dots R]$. 

**Lemma (Sorted Half Invariant):** In any rotated sorted array, at least one of the two segments $[L, M]$ or $[M+1, R]$ is monotonically increasing.
*   If $a_L \le a_M$, then the segment $A[L \dots M]$ is sorted.
*   Otherwise, the segment $A[M+1 \dots R]$ must be sorted.

**Decision Logic:**
Let $S_L$ be the predicate that $A[L \dots M]$ is sorted, defined as $a_L \le a_M$.
1. If $S_L$ is true:
   - If $a_L \le \tau < a_M$, the target $\tau$ is contained within $[L, M-1]$.
   - Otherwise, $\tau$ must reside in $[M+1, R]$.
2. If $S_L$ is false (implying $A[M+1 \dots R]$ is sorted):
   - If $a_{M+1} \le \tau \le a_R$, the target $\tau$ is contained within $[M+1, R]$.
   - Otherwise, $\tau$ must reside in $[L, M-1]$.

This logic maintains the invariant that if $\tau \in A$, then $\tau \in A[L \dots R]$ at the start of each iteration.

## 3. Complexity Analysis

### Time Complexity
The algorithm employs a divide-and-conquer strategy that reduces the search space by a factor of 2 in each iteration. Let $T(n)$ be the number of comparisons required for an array of size $n$.

The recurrence relation is:
$$T(n) = T\left(\frac{n}{2}\right) + c$$
where $c$ is the constant time required for the comparison logic at each step. By the Master Theorem, where $a=1, b=2, f(n)=O(1)$, we have:
$$T(n) = \Theta(\log n)$$
Thus, the time complexity is $O(\log n)$.

### Space Complexity
The algorithm operates in-place. We define the auxiliary space $S_{aux}$ as the memory required beyond the input array. The algorithm utilizes a fixed number of integer variables ($L, R, M, \text{pivot}$), each requiring $O(1)$ space. 
$$S_{aux} = O(1)$$
Since no recursion stack or auxiliary data structures are utilized, the total space complexity is $O(1)$.