# Formal Mathematical Specification: Quick Sort

## 1. Definitions and Notation

Let $A = [a_0, a_1, \dots, a_{n-1}]$ be a sequence of $n$ elements drawn from a totally ordered set $(\mathcal{X}, \le)$. The objective is to compute a permutation $P$ of the indices $\{0, 1, \dots, n-1\}$ such that the resulting sequence $A' = [a_{P(0)}, a_{P(1)}, \dots, a_{P(n-1)}]$ satisfies the non-decreasing condition:
$$a_{P(i)} \le a_{P(j)} \quad \forall i, j \in \{0, \dots, n-1\} \text{ where } i < j$$

The algorithm operates on a sub-array defined by the index interval $[L, R] \subseteq \{0, \dots, n-1\}$. We define the partitioning function $\mathcal{P}: \mathcal{X}^{R-L+1} \to \mathcal{X}^{R-L+1} \times \mathbb{Z}^2$ which maps a sub-array to a reordered sub-array and a pair of indices $(lt, gt)$ such that:
1. $\forall k \in [L, lt-1]: A[k] < \text{pivot}$
2. $\forall k \in [lt, gt]: A[k] = \text{pivot}$
3. $\forall k \in [gt+1, R]: A[k] > \text{pivot}$

## 2. Algebraic Characterization

The correctness of the 3-way Quick Sort is governed by the **Loop Invariant** maintained during the partitioning phase. Let $i$ be the current scanning index, and $lt, gt$ be the boundaries of the "equal to pivot" region. At any iteration $k$ of the `while i <= gt` loop, the following partition holds:
- $A[L \dots lt-1] < \text{pivot}$
- $A[lt \dots i-1] = \text{pivot}$
- $A[i \dots gt]$ are elements yet to be classified
- $A[gt+1 \dots R] > \text{pivot}$

The algorithm terminates when $i > gt$, satisfying the post-condition where the array is partitioned into three contiguous segments. The recursion is defined by the recurrence relation for the number of comparisons $T(n)$:
$$T(n) = T(n_{<}) + T(n_{>}) + \Theta(n)$$
where $n_{<} + n_{=} + n_{>} = n$, and $n_{=}$ is the count of elements equal to the pivot. In the 3-way variant, $n_{=}$ elements are excluded from subsequent recursive calls, effectively reducing the problem size more aggressively than the standard 2-way partition.

## 3. Complexity Analysis

### Time Complexity
The time complexity is determined by the depth of the recursion tree and the work performed at each level.

- **Average Case:** Assuming the pivot selection partitions the array into two roughly equal halves, the recurrence is $T(n) = 2T(n/2) + \Theta(n)$. By the **Master Theorem** (Case 2), where $a=2, b=2, f(n)=n$, we have $T(n) = \Theta(n \log n)$.
- **Worst Case:** If the pivot consistently results in a highly unbalanced partition (e.g., $n_{<} = 0$ or $n_{>} = 0$), the recurrence becomes $T(n) = T(n-1) + \Theta(n)$. Expanding this summation:
  $$T(n) = \sum_{k=1}^{n} k = \frac{n(n+1)}{2} = \Theta(n^2)$$
  However, the 3-way partition ensures that if all elements are equal, $n_{<} = 0$ and $n_{>} = 0$, the algorithm terminates in $O(n)$ time, preventing the $O(n^2)$ degradation for arrays with high duplicate density.

### Space Complexity
The space complexity is dominated by the auxiliary stack required for recursion.

- **Auxiliary Space:** The algorithm uses an explicit stack to store sub-array boundaries $(L, R)$. In the worst case of unbalanced partitioning, the stack depth can reach $O(n)$.
- **Optimized Space:** By always pushing the larger sub-array onto the stack last and recursing into the smaller sub-array first, the maximum stack depth is bounded by $O(\log n)$.
- **Total Space:** Since the algorithm performs swaps in-place, the total auxiliary space complexity is $O(\log n)$ under the assumption of tail-call optimization or stack-size management.