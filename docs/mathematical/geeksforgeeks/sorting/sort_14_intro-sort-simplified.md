# Formal Mathematical Specification: Intro Sort (Introspective Sort)

## 1. Definitions and Notation

Let $A = [a_0, a_1, \dots, a_{n-1}]$ be a sequence of $n$ elements drawn from a totally ordered set $(\mathcal{X}, \le)$. The objective is to produce a permutation $A'$ of $A$ such that $a'_0 \le a'_1 \le \dots \le a'_{n-1}$.

*   **State Space:** The algorithm operates on the set of all permutations of $A$, denoted $\mathcal{S}_n$.
*   **Depth Limit:** Let $d_{max} = 2 \lfloor \log_2 n \rfloor$ be the maximum recursion depth allowed for the Quicksort component.
*   **Partition Function:** Let $P(A, lo, hi)$ be a function that selects a pivot $p \in A[lo \dots hi-1]$ and rearranges the sub-array such that $\forall x \in A[lo \dots p_{idx}-1], x \le A[p_{idx}]$ and $\forall y \in A[p_{idx}+1 \dots hi-1], y \ge A[p_{idx}]$.
*   **Heapify/Sift-Down:** Let $H(A, lo, hi)$ be the transformation that satisfies the max-heap property $\forall i \in [lo, hi-1]: A[i] \ge A[2i+1]$ and $A[i] \ge A[2i+2]$ (relative to the offset $lo$).

## 2. Algebraic Characterization

Intro Sort is defined as a recursive procedure $I(lo, hi, d)$ where $d$ is the remaining recursion depth. The algorithm is governed by the following piecewise transition logic:

$$
I(lo, hi, d) = 
\begin{cases} 
\text{InsertionSort}(A, lo, hi) & \text{if } (hi - lo) < k \\
\text{HeapSort}(A, lo, hi) & \text{if } d = 0 \\
\text{let } p = P(A, lo, hi) \text{ in } \{I(lo, p, d-1); I(p+1, hi, d-1)\} & \text{otherwise}
\end{cases}
$$

Where $k$ is a small constant (typically $16$). 

**Invariants:**
1. **Partition Invariant:** After the execution of $P(A, lo, hi)$, the pivot element is at its final sorted position $p_{idx}$.
2. **Heap Invariant:** After $\text{HeapSort}(A, lo, hi)$, the sub-array $A[lo \dots hi-1]$ satisfies the condition $a_i \le a_j$ for all $lo \le i < j < hi$.
3. **Termination Invariant:** Since $d$ is strictly decreasing in the recursive branch and $d_{max} \ge 0$, the recursion depth is bounded by $2 \log_2 n$, ensuring the stack depth is $O(\log n)$.

## 3. Complexity Analysis

### Time Complexity
The time complexity $T(n)$ is the sum of the costs of the three constituent algorithms. 

1. **Quicksort Phase:** In the average case, the recursion tree has depth $\log_2 n$. Each level performs $O(n)$ work, yielding $O(n \log n)$.
2. **Heap Sort Bailout:** If the recursion depth exceeds $d_{max} = 2 \log_2 n$, the algorithm invokes Heap Sort. Heap Sort has a worst-case complexity of $T_{heap}(m) = O(m \log m)$ for a sub-array of size $m$. 
3. **Total Complexity:** Since the depth limit $d_{max}$ ensures that the Quicksort recursion tree cannot exceed $O(\log n)$ depth, and the total number of elements processed by Heap Sort across all branches is bounded by $n$, the total time complexity is:
   $$T(n) = \sum_{i=1}^{k} O(n_i \log n_i) \implies O(n \log n)$$
   where $\sum n_i = n$. Because $O(n \log n)$ is the upper bound for both the Quicksort phase (when balanced) and the Heap Sort phase (when unbalanced), the worst-case time complexity is strictly $O(n \log n)$.

### Space Complexity
The space complexity $S(n)$ is dominated by the recursion stack and auxiliary storage.

1. **Auxiliary Space:** The algorithm is in-place, requiring $O(1)$ auxiliary space for swaps and pointers.
2. **Stack Space:** The recursion depth is explicitly capped at $d_{max} = 2 \log_2 n$. Each stack frame consumes $O(1)$ space. Thus, the total stack space is:
   $$S_{stack} = O(d_{max}) = O(\log n)$$
3. **Total Space:**
   $$S(n) = S_{aux} + S_{stack} = O(1) + O(\log n) = O(\log n)$$
This satisfies the requirement for logarithmic space complexity, distinguishing it from Merge Sort, which requires $O(n)$ space.