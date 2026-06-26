# Formal Mathematical Specification: Insertion Sort

## 1. Definitions and Notation

Let $A = [a_0, a_1, \dots, a_{n-1}]$ be a sequence of $n$ elements drawn from a totally ordered set $(\mathcal{X}, \le)$. The objective of the Insertion Sort algorithm is to produce a permutation $A'$ of $A$ such that $A'$ is sorted in non-decreasing order:
$$a'_0 \le a'_1 \le \dots \le a'_{n-1}$$

We define the state of the algorithm at any iteration $i$ (where $1 \le i < n$) by the configuration of the array $A^{(i)}$. The algorithm maintains a partition of the array into two contiguous sub-segments:
1. **The Sorted Prefix:** $A[0 \dots i-1]$, which is a permutation of the original elements $\{a_0, \dots, a_{i-1}\}$ such that $A[k] \le A[k+1]$ for all $0 \le k < i-1$.
2. **The Unsorted Suffix:** $A[i \dots n-1]$, containing the remaining elements yet to be processed.

## 2. Algebraic Characterization

The correctness of Insertion Sort is established via a **Loop Invariant**. Let $P(i)$ be the predicate that the sub-array $A[0 \dots i-1]$ consists of the elements originally in $A[0 \dots i-1]$ in sorted order.

**Initialization:** For $i=1$, the sub-array $A[0 \dots 0]$ is trivially sorted. $P(1)$ holds.

**Maintenance:** Assume $P(i)$ holds. We define the "key" as $k = A[i]$. We seek an index $j \in \{0, \dots, i\}$ such that:
$$A[m] \le k \text{ for } m < j \quad \text{and} \quad A[m] > k \text{ for } j \le m < i$$
The algorithm performs a right-shift operation on the elements $A[j \dots i-1]$ to create a vacancy at index $j$, effectively transforming the sorted prefix $A[0 \dots i-1]$ into $A[0 \dots i]$ such that $P(i+1)$ holds.

**Termination:** The loop terminates when $i = n$. At this state, the invariant $P(n)$ implies that the entire array $A[0 \dots n-1]$ is sorted.

The transition function for the inner loop, which shifts elements, can be expressed as:
$$A[m+1] \leftarrow A[m] \quad \forall m \in \{j, j+1, \dots, i-1\}$$
followed by the assignment $A[j] \leftarrow k$.

## 3. Complexity Analysis

### Time Complexity
The time complexity $T(n)$ is determined by the number of comparisons and assignments performed. Let $c_i$ be the number of shifts performed during the $i$-th iteration. The total time is:
$$T(n) = \sum_{i=1}^{n-1} (c_i + 1)$$

*   **Worst-Case:** Occurs when the input is in reverse order. For each $i$, $c_i = i$.
    $$T_{worst}(n) = \sum_{i=1}^{n-1} (i + 1) = \sum_{k=2}^{n} k = \frac{n(n+1)}{2} - 1 = \Theta(n^2)$$
*   **Best-Case:** Occurs when the input is already sorted. For each $i$, $c_i = 0$ (the inner loop condition fails immediately).
    $$T_{best}(n) = \sum_{i=1}^{n-1} 1 = n - 1 = \Omega(n)$$
*   **Average-Case:** Assuming all permutations are equally likely, the expected number of shifts $E[c_i] = i/2$.
    $$T_{avg}(n) = \sum_{i=1}^{n-1} \left(\frac{i}{2} + 1\right) = \frac{1}{2} \frac{(n-1)n}{2} + (n-1) = \Theta(n^2)$$

### Space Complexity
The algorithm operates **in-place**. It requires a constant amount of auxiliary space for the variables `key`, `i`, and `j`, regardless of the input size $n$.
$$S(n) = O(1)$$
The total space complexity is $O(n)$ to store the input array, but the auxiliary space complexity is strictly $O(1)$.