# Formal Mathematical Specification: Randomized Quicksort

## 1. Definitions and Notation

Let $A = [a_0, a_1, \dots, a_{n-1}]$ be an array of $n$ elements drawn from a totally ordered set $(\mathcal{X}, \le)$. The objective is to find a permutation $\sigma$ of the indices $\{0, 1, \dots, n-1\}$ such that the resulting array $A' = [a_{\sigma(0)}, a_{\sigma(1)}, \dots, a_{\sigma(n-1)}]$ satisfies $a_{\sigma(i)} \le a_{\sigma(j)}$ for all $0 \le i < j < n$.

We define the state space $\mathcal{S}$ as the set of all permutations of $A$. The algorithm operates via a recursive function $Q(A, \text{lo}, \text{hi})$, which sorts the subarray $A[\text{lo} \dots \text{hi}]$. 

Let $\mathcal{R}$ be a random variable representing the choice of pivot index, where $\mathcal{R} \sim \text{Uniform}(\text{lo}, \text{hi})$. The partitioning function $P(A, \text{lo}, \text{hi}, \mathcal{R})$ maps the subarray to a pivot index $p \in [\text{lo}, \text{hi}]$ such that:
1. $\forall k \in [\text{lo}, p-1] : A[k] \le A[p]$
2. $\forall k \in [p+1, \text{hi}] : A[k] > A[p]$

## 2. Algebraic Characterization

The correctness of the algorithm is governed by the recursive decomposition of the problem. Given a pivot index $p$ chosen at random, the algorithm partitions the problem into two sub-problems of size $k$ and $n-k-1$.

The recurrence relation for the expected number of comparisons $T(n)$ is given by:
$$T(n) = (n-1) + \frac{1}{n} \sum_{k=0}^{n-1} (T(k) + T(n-k-1))$$
where:
- $(n-1)$ represents the cost of the partitioning step (Lomuto partition).
- $\frac{1}{n} \sum_{k=0}^{n-1} (\dots)$ represents the expectation over the uniform choice of the pivot index $k$, which determines the sizes of the resulting sub-arrays.

**Loop Invariant:**
For the partitioning step, let $i$ be the index such that $A[\text{lo} \dots i-1] \le \text{pivot}$ and $A[i \dots j-1] > \text{pivot}$. At each iteration $j \in [\text{lo}, \text{hi}-1]$, the invariant holds that the subarray is partitioned into elements less than or equal to the pivot and elements strictly greater than the pivot.

## 3. Complexity Analysis

### Time Complexity
To derive the expected time complexity $E[T(n)]$, we simplify the recurrence:
$$T(n) = (n-1) + \frac{2}{n} \sum_{k=0}^{n-1} T(k)$$
Multiplying by $n$:
$$n T(n) = n(n-1) + 2 \sum_{k=0}^{n-1} T(k)$$
Subtracting the equation for $n-1$:
$$n T(n) - (n-1) T(n-1) = 2(n-1) + 2 T(n-1)$$
$$n T(n) = (n+1) T(n-1) + 2(n-1)$$
Dividing by $n(n+1)$:
$$\frac{T(n)}{n+1} = \frac{T(n-1)}{n} + \frac{2(n-1)}{n(n+1)}$$
Using the method of telescoping sums, we observe that $\frac{T(n)}{n+1} \approx 2 \sum \frac{1}{n} \approx 2 \ln n$. Thus, $T(n) = O(n \log n)$. 

The worst-case complexity remains $T(n) = \sum_{i=1}^n i = O(n^2)$, occurring when the pivot selection consistently yields the minimum or maximum element, though the probability of this sequence is $P = \prod_{i=1}^n \frac{2}{i} = \frac{2^n}{n!}$, which approaches $0$ as $n \to \infty$.

### Space Complexity
The space complexity is determined by the maximum depth of the recursion stack. 
- **Average Case:** The expected depth of the recursion tree is $O(\log n)$, leading to an expected auxiliary space complexity of $O(\log n)$.
- **Worst Case:** In the event of highly unbalanced partitions, the recursion depth can reach $O(n)$, resulting in $O(n)$ space complexity. 
- **Total Space:** Since the algorithm operates in-place, the total space complexity is $O(n)$ to store the input, with $O(\log n)$ expected auxiliary space for the call stack.