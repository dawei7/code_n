# Formal Mathematical Specification: Bubble Sort

## 1. Definitions and Notation

Let $A = [a_0, a_1, \dots, a_{n-1}]$ be a sequence of $n$ elements drawn from a totally ordered set $(\mathcal{X}, \le)$. The objective of the sorting algorithm is to produce a permutation $A' = [a'_0, a'_1, \dots, a'_{n-1}]$ such that $a'_i \le a'_{i+1}$ for all $0 \le i < n-1$.

- **State Space:** The state of the algorithm at any iteration is defined by the tuple $(A, k)$, where $A \in \mathcal{X}^n$ is the current configuration of the sequence and $k \in \{1, \dots, n-1\}$ represents the boundary of the unsorted suffix.
- **Swap Operator:** We define a swap operator $\sigma_i: \mathcal{X}^n \to \mathcal{X}^n$ such that for a sequence $A$, $\sigma_i(A)$ results in a sequence $A^*$ where $A^*_i = A_{i+1}$, $A^*_{i+1} = A_i$, and $A^*_j = A_j$ for $j \notin \{i, i+1\}$.
- **Comparison:** The algorithm relies on the predicate $P(i, A) \equiv (A_i > A_{i+1})$.

## 2. Algebraic Characterization

The correctness of Bubble Sort is established by the maintenance of a loop invariant. Let $k$ be the index such that all elements in the suffix $A[k \dots n-1]$ are in their final sorted positions.

**Loop Invariant:** At the start of each iteration of the outer loop (indexed by $k$ from $n-1$ down to $1$), the following conditions hold:
1. For all $j \ge k$, $A_j = \max(\{A_0, \dots, A_j\})$.
2. For all $p, q$ such that $k \le p < q < n$, $A_p \le A_q$.

**Transition Function:**
The inner loop performs a sequence of adjacent comparisons and swaps. For a fixed $k$, the inner loop executes the transformation:
$$A^{(i+1)} = \begin{cases} \sigma_i(A^{(i)}) & \text{if } A^{(i)}_i > A^{(i)}_{i+1} \\ A^{(i)} & \text{otherwise} \end{cases}$$
for $i = 0, 1, \dots, k-1$. 

After $k$ iterations of the inner loop, the element $A_k$ is guaranteed to be:
$$A_k = \max_{0 \le j \le k} \{A_j\}$$
This confirms that the "bubbling" process correctly places the maximum element of the unsorted prefix into the $k$-th position. By induction on $k$, the algorithm terminates when $k=0$, resulting in a sorted sequence.

## 3. Complexity Analysis

### Time Complexity
The time complexity is determined by the number of comparisons $C(n)$. The outer loop runs for $k = n-1, n-2, \dots, 1$. For each $k$, the inner loop performs $k$ comparisons.

The total number of comparisons is given by the arithmetic series:
$$T(n) = \sum_{k=1}^{n-1} k = \frac{(n-1)n}{2} = \frac{1}{2}n^2 - \frac{1}{2}n$$

- **Worst-Case:** When the input is in reverse order, every comparison results in a swap. The number of operations is $\Theta(n^2)$.
- **Best-Case:** With the early-exit optimization (checking if any swap occurred), if the array is already sorted, the algorithm performs only one pass of $n-1$ comparisons. Thus, $T_{best}(n) = \Omega(n)$.
- **Average-Case:** Since the number of inversions in a random permutation is on average $\frac{n(n-1)}{4}$, the expected number of swaps is $\Theta(n^2)$, leading to $T_{avg}(n) = \Theta(n^2)$.

### Space Complexity
The algorithm operates in-place. The only auxiliary storage required is for the loop indices ($k, i$) and a boolean flag for the optimization, all of which occupy $O(1)$ space. 

- **Auxiliary Space:** $S_{aux} = O(1)$.
- **Total Space:** $S_{total} = O(n)$ to store the input array $A$, plus $O(1)$ auxiliary space.