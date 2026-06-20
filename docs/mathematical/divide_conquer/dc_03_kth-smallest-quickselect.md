# Formal Mathematical Specification: Kth Smallest Element (Quickselect)

## 1. Definitions and Notation

Let $A = [a_0, a_1, \dots, a_{n-1}]$ be a sequence of $n$ elements drawn from a totally ordered set $(\mathcal{X}, \leq)$. We define the problem as finding the element $x \in A$ such that its rank in the sorted permutation of $A$ is $k$, where $1 \leq k \leq n$.

*   **Input:** A tuple $(A, k)$, where $A \in \mathcal{X}^n$ and $k \in \mathbb{Z}^+$.
*   **Output:** An element $x^* \in A$ such that $|\{a \in A : a < x^*\}| < k$ and $|\{a \in A : a \leq x^*\}| \geq k$.
*   **Partition Function:** Let $P(A, p)$ be a function that rearranges $A$ into $A'$ such that there exists an index $m$ (the pivot position) where:
    1. $\forall i < m, A'[i] \leq A'[m]$
    2. $\forall j > m, A'[j] \geq A'[m]$
    3. $A'[m]$ is the element originally at the chosen pivot index.

## 2. Algebraic Characterization

The algorithm relies on the **Partition Invariant**. Given a subarray $A[lo \dots hi]$, the partition operation produces a pivot index $m \in [lo, hi]$ such that $A[m]$ is in its correct sorted position relative to the subarray.

The algorithm is defined by the following recurrence relation for the selection function $S(A, k, lo, hi)$:

$$
S(A, k, lo, hi) = 
\begin{cases} 
A[m] & \text{if } m = k-1 \\
S(A, k, lo, m-1) & \text{if } m > k-1 \\
S(A, k, m+1, hi) & \text{if } m < k-1 
\end{cases}
$$

Where $m$ is the index returned by the partition operation on the range $[lo, hi]$. The correctness is guaranteed by the fact that after partitioning, the set of elements $\{A[lo], \dots, A[m-1]\}$ contains only elements $\leq A[m]$, and $\{A[m+1], \dots, A[hi]\}$ contains only elements $\geq A[m]$. Thus, the rank of $A[m]$ is invariant across recursive calls.

## 3. Complexity Analysis

### Time Complexity

The time complexity is governed by the recurrence $T(n) = T(n') + O(n)$, where $n'$ is the size of the subarray after partitioning.

**Average Case:**
Assuming a random pivot, the partition splits the array into two parts of expected size $n/2$. The recurrence is:
$$T(n) = T(n/2) + cn$$
By the Master Theorem (Case 3), or by expanding the geometric series:
$$T(n) = cn + c\frac{n}{2} + c\frac{n}{4} + \dots + c(1) = cn \sum_{i=0}^{\log n} \left(\frac{1}{2}\right)^i < 2cn$$
Thus, $T(n) = O(n)$.

**Worst Case:**
If the pivot is consistently the minimum or maximum element (e.g., already sorted array with poor pivot selection), the recurrence becomes:
$$T(n) = T(n-1) + cn$$
This is an arithmetic progression:
$$T(n) = \sum_{i=1}^{n} ci = c \frac{n(n+1)}{2} = O(n^2)$$

### Space Complexity

**Auxiliary Space:**
The algorithm operates in-place on the input array $A$. The auxiliary space is defined by the recursion stack depth $D$.
*   In the average case, the stack depth is $O(\log n)$ due to the halving of the search space.
*   In the worst case, the stack depth is $O(n)$.
*   If implemented iteratively (tail-call optimization), the auxiliary space complexity is $O(1)$, as the state can be maintained via two pointers ($lo, hi$) without additional stack frames.

**Total Space:**
Since the algorithm modifies the input array $A$ in-place, the total space complexity is $O(n)$ to store the input, with $O(1)$ additional space required for the partitioning variables and pointers.