# Formal Mathematical Specification: K-th Largest Element

## 1. Definitions and Notation

Let $A = \langle a_1, a_2, \dots, a_N \rangle$ be a sequence of $N$ integers, where $a_i \in \mathbb{Z}$. We define the sorted version of $A$ as a non-decreasing sequence $S = \langle s_1, s_2, \dots, s_N \rangle$ such that $s_1 \le s_2 \le \dots \le s_N$. The $k$-th largest element of $A$ is defined as the element $s_{N-k+1}$.

Let $\mathcal{H}$ denote a Min-Heap data structure, which is a complete binary tree satisfying the heap property: for any node $u$ with children $v_L$ and $v_R$, the value $val(u) \le \min(val(v_L), val(v_R))$. 
- Let $|\mathcal{H}|$ denote the number of elements in the heap.
- Let $top(\mathcal{H})$ denote the element with the minimum value in $\mathcal{H}$, located at the root.
- Let $push(\mathcal{H}, x)$ be the operation of inserting $x$ into $\mathcal{H}$ in $O(\log |\mathcal{H}|)$ time.
- Let $pop(\mathcal{H})$ be the operation of removing $top(\mathcal{H})$ in $O(\log |\mathcal{H}|)$ time.

## 2. Algebraic Characterization

The algorithm maintains a state $\mathcal{H}_i$ after processing the $i$-th element of $A$. The invariant $\mathcal{I}$ is defined as follows: 
$\mathcal{H}_i$ contains the $k$ largest elements encountered in the prefix $\langle a_1, \dots, a_i \rangle$ for $i \ge k$.

**Transition Function:**
For each $a_i \in A$:
1. If $|\mathcal{H}| < k$:
   $$\mathcal{H}_{i} = \mathcal{H}_{i-1} \cup \{a_i\}$$
2. If $|\mathcal{H}| = k$ and $a_i > top(\mathcal{H}_{i-1})$:
   $$\mathcal{H}_{i} = (\mathcal{H}_{i-1} \setminus \{top(\mathcal{H}_{i-1})\}) \cup \{a_i\}$$
3. Otherwise:
   $$\mathcal{H}_{i} = \mathcal{H}_{i-1}$$

**Correctness Invariant:**
At the termination of the algorithm ($i=N$), the set $\mathcal{H}_N$ satisfies:
$$\forall x \in \mathcal{H}_N, \forall y \in \{A \setminus \mathcal{H}_N\}, x \ge y$$
Given $|\mathcal{H}_N| = k$, the minimum element of this set is the $k$-th largest element of the original sequence $A$:
$$result = \min(\mathcal{H}_N) = s_{N-k+1}$$

## 3. Complexity Analysis

### Time Complexity
The algorithm performs a single pass over the input sequence $A$ of length $N$. For each element $a_i$, we perform at most one $push$ and one $pop$ operation on a heap of maximum size $k$.

The cost of each heap operation is bounded by $O(\log k)$. The total time complexity $T(N, k)$ is given by the summation:
$$T(N, k) = \sum_{i=1}^{N} \text{cost}(op_i) \le \sum_{i=1}^{N} O(\log k) = O(N \log k)$$
Since the heap operations are logarithmic with respect to the size of the heap $k$, the upper bound is strictly $O(N \log k)$.

### Space Complexity
The space complexity $S(N, k)$ is determined by the auxiliary storage required for the Min-Heap $\mathcal{H}$. 
- The heap is constrained to a maximum size of $k$ elements.
- Each element occupies $O(1)$ space.
- Thus, the auxiliary space complexity is $O(k)$.

Total space complexity is $O(k)$, which is independent of $N$, making this approach optimal for streaming data where $N \gg k$.