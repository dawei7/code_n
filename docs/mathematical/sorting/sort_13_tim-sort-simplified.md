# Formal Mathematical Specification: Tim Sort (Simplified)

## 1. Definitions and Notation

Let $A = [a_0, a_1, \dots, a_{n-1}]$ be a sequence of $n$ elements drawn from a totally ordered set $(\mathcal{X}, \le)$. The objective is to produce a permutation $A'$ of $A$ such that $a'_0 \le a'_1 \le \dots \le a'_{n-1}$.

*   **Run:** A contiguous subsequence $R_{i,j} = [a_i, a_{i+1}, \dots, a_j]$ where $0 \le i \le j < n$.
*   **Sorted Run:** A run $R_{i,j}$ is sorted if $\forall k \in [i, j-1], a_k \le a_{k+1}$.
*   **MinRun:** A parameter $M \in \mathbb{Z}^+$, typically $M \approx 32$, defining the minimum length of a run to be processed by the merging phase.
*   **State Space:** The algorithm operates on the state $\mathcal{S} = (A, \mathcal{R})$, where $A$ is the current array and $\mathcal{R} = \{[i_0, j_0], [i_1, j_1], \dots, [i_k, j_k]\}$ is a partition of indices such that $\bigcup_{m=0}^k [i_m, j_m] = [0, n-1]$ and each $R_{i_m, j_m}$ is a sorted run.

## 2. Algebraic Characterization

The algorithm proceeds in two distinct phases: the **Run Generation Phase** and the **Merge Phase**.

### Phase 1: Run Generation
For each index $i \in \{0, \dots, n-1\}$, we identify a maximal sorted run $R_{i,j}$. If $j - i + 1 < M$, we extend the run to length $\min(i+M, n)$ and apply an insertion sort operator $\mathcal{I}: \mathcal{X}^m \to \mathcal{X}^m$, which maps an unsorted sequence to its sorted permutation. The invariant maintained is:
$$\forall [i, j] \in \mathcal{R}, \quad \text{length}(R_{i,j}) \ge M \lor j = n-1$$

### Phase 2: Merge Phase
Let $\mathcal{R}_t$ be the set of runs at iteration $t$. The merge operator $\mathcal{M}: \mathcal{X}^{n_1} \times \mathcal{X}^{n_2} \to \mathcal{X}^{n_1+n_2}$ is defined as the standard merge operation for two sorted sequences. The algorithm iteratively applies $\mathcal{M}$ to adjacent runs:
$$\mathcal{R}_{t+1} = \{ \mathcal{M}(R_{2k}, R_{2k+1}) \mid k = 0, \dots, \lfloor |\mathcal{R}_t|/2 \rfloor - 1 \} \cup \{ \text{remaining runs} \}$$
The process terminates when $|\mathcal{R}_t| = 1$. The correctness is guaranteed by the property that if $R_a$ and $R_b$ are sorted, then $\mathcal{M}(R_a, R_b)$ is sorted.

## 3. Complexity Analysis

### Time Complexity
The total time complexity $T(n)$ is the sum of the run generation time $T_g(n)$ and the merge time $T_m(n)$.

1.  **Run Generation:** For each block of size $M$, insertion sort takes $O(M^2)$. Since there are $n/M$ blocks, $T_g(n) = O(\frac{n}{M} \cdot M^2) = O(nM)$. Given $M$ is a constant, $T_g(n) = O(n)$.
2.  **Merge Phase:** The merging process forms a binary tree of height $\lceil \log_2(n/M) \rceil$. At each level of the tree, every element of the array is involved in exactly one merge operation, contributing $O(n)$ work per level.
    $$T_m(n) = \sum_{h=1}^{\log_2(n/M)} O(n) = O(n \log(n/M))$$
Since $M$ is constant, $T(n) = O(n) + O(n \log n) = O(n \log n)$.
*   **Best Case:** If the array is already sorted, $T_g(n) = O(n)$ and the merge phase detects the sorted property (or performs trivial merges), resulting in $T(n) = \Omega(n)$.

### Space Complexity
The algorithm requires auxiliary space for the merge operation. During the merge of two runs $R_1$ and $R_2$, a temporary buffer is required to store the elements before they are written back to the original array.
*   **Auxiliary Space:** In the worst case, the merge operation requires $O(n)$ space to hold the merged elements.
*   **Total Space:** $S(n) = O(n)$ for the input array plus $O(n)$ for the auxiliary buffer, yielding $O(n)$ total space complexity.