# Formal Mathematical Specification: Stock Span Problem

## 1. Definitions and Notation

Let $P = \langle p_0, p_1, \dots, p_{n-1} \rangle$ be a sequence of $n$ daily stock prices, where $p_i \in \mathbb{R}_{\geq 0}$ for all $i \in \{0, 1, \dots, n-1\}$. 

The **span** of the stock price on day $i$, denoted $s_i$, is defined as the cardinality of the maximal contiguous sub-segment of indices ending at $i$ such that all prices in that segment are less than or equal to $p_i$. Formally:
$$s_i = \max \{ k \in \mathbb{Z}^+ : \forall j \in \{i-k+1, \dots, i\}, p_j \leq p_i \}$$

We define the output as a sequence $S = \langle s_0, s_1, \dots, s_{n-1} \rangle$.

Let $\mathcal{S}$ denote the state of the stack, represented as an ordered tuple of indices $\langle idx_1, idx_2, \dots, idx_m \rangle$ such that $idx_1 < idx_2 < \dots < idx_m$. The stack maintains the **monotonicity property**:
$$\forall j \in \{1, \dots, m-1\}, p_{idx_j} > p_{idx_{j+1}}$$

## 2. Algebraic Characterization

To determine $s_i$, we seek the index of the **Previous Greater Element (PGE)**. Let $PGE(i)$ be defined as:
$$PGE(i) = \max \{ j < i : p_j > p_i \} \cup \{-1\}$$

The span $s_i$ can be expressed as:
$$s_i = i - PGE(i)$$

### Loop Invariant
At the start of each iteration $i \in \{0, \dots, n-1\}$, the stack $\mathcal{S}$ contains indices $j < i$ such that $p_j$ are the prices of the "visible" elements to the left of $i$. Specifically, for any $j \in \mathcal{S}$, there exists no $k$ such that $j < k < i$ and $p_k \geq p_j$. 

The transition for the stack state $\mathcal{S}_{i+1}$ given $\mathcal{S}_i$ is:
1. **Pop phase:** $\mathcal{S}' = \mathcal{S}_i \setminus \{idx \in \mathcal{S}_i : p_{idx} \leq p_i\}$
2. **Push phase:** $\mathcal{S}_{i+1} = \mathcal{S}' \cup \{i\}$

The correctness of the algorithm relies on the fact that if $p_j \leq p_i$ for some $j < i$, then for any future day $t > i$, the price $p_j$ will never be the PGE because $p_i$ will be encountered first and $p_i \geq p_j$. Thus, $j$ is redundant.

## 3. Complexity Analysis

### Time Complexity
The time complexity is determined by the total number of stack operations. Let $T(n)$ be the total number of operations. Each index $i \in \{0, \dots, n-1\}$ is pushed onto the stack exactly once. An index is popped from the stack only if it is smaller than or equal to the current price $p_i$. Since each index is pushed once, it can be popped at most once.

The total work $W$ is:
$$W = \sum_{i=0}^{n-1} (1 + \text{pop}_i)$$
where $\text{pop}_i$ is the number of elements popped during iteration $i$. Since $\sum_{i=0}^{n-1} \text{pop}_i \leq n$, we have:
$$W \leq n + n = 2n$$
Thus, $T(n) = O(n)$. The amortized cost per element is $O(1)$.

### Space Complexity
The space complexity is governed by the auxiliary storage required for the stack $\mathcal{S}$ and the output array $S$.
1. **Output Array:** $S$ requires $O(n)$ space to store $n$ integers.
2. **Stack:** In the worst-case scenario (a strictly decreasing sequence of prices, $p_0 > p_1 > \dots > p_{n-1}$), no elements are ever popped. The stack size grows to $n$. Thus, the stack requires $O(n)$ space.

Total space complexity is $O(n) + O(n) = O(n)$.