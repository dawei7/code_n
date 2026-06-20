# Formal Mathematical Specification: Largest Rectangle in Histogram

## 1. Definitions and Notation

Let $H = [h_0, h_1, \dots, h_{n-1}]$ be a sequence of non-negative integers representing the heights of $n$ bars, where each bar has unit width. We define the domain of indices as $\mathcal{I} = \{0, 1, \dots, n-1\}$.

A rectangle defined by the interval $[L, R] \subseteq \mathcal{I}$ has a height constrained by the minimum bar within that interval:
$$h_{\min}(L, R) = \min_{k \in [L, R]} h_k$$
The area of a rectangle spanning from index $L$ to $R$ is given by:
$$A(L, R) = h_{\min}(L, R) \times (R - L + 1)$$
The objective is to find the maximum area $A^*$ over all possible intervals:
$$A^* = \max_{0 \le L \le R < n} A(L, R)$$

To facilitate the algorithm, we augment $H$ with a sentinel value $h_n = 0$ to ensure all elements are popped from the stack upon termination. Let $S$ be a stack containing a strictly increasing sequence of indices $i_1, i_2, \dots, i_m$ such that $h_{i_1} < h_{i_2} < \dots < h_{i_m}$.

## 2. Algebraic Characterization

For any bar $i \in \mathcal{I}$, let $L_i$ be the index of the **Previous Smaller Element (PSE)** and $R_i$ be the index of the **Next Smaller Element (NSE)**. Formally:
$$L_i = \max \{j < i \mid h_j < h_i\} \cup \{-1\}$$
$$R_i = \min \{j > i \mid h_j < h_i\} \cup \{n\}$$

The largest rectangle with height $h_i$ as its minimum is defined by the maximal width $w_i = R_i - L_i - 1$. The global maximum area is:
$$A^* = \max_{i \in \mathcal{I}} (h_i \times (R_i - L_i - 1))$$

**Loop Invariant:**
At the start of each iteration $i \in \{0, \dots, n\}$, the stack $S$ contains indices $s_1, s_2, \dots, s_k$ such that:
1. $h_{s_1} < h_{s_2} < \dots < h_{s_k}$.
2. For any index $j$ processed such that $j < i$ and $j \notin S$, the maximum area $A^*$ has been updated to include the maximal rectangle where $j$ is the minimum height.
3. For any $s_j \in S$, $L_{s_j} = s_{j-1}$ (with $s_0 = -1$).

When $h_i < h_{s_k}$, the element $s_k$ is popped. Since $h_i$ is the first element to the right smaller than $h_{s_k}$, we have $R_{s_k} = i$. The PSE is the new top of the stack, $s_{k-1}$, thus $L_{s_k} = s_{k-1}$. The area is calculated as $h_{s_k} \times (i - s_{k-1} - 1)$.

## 3. Complexity Analysis

### Time Complexity
The algorithm performs a single pass over the input array $H$ of size $n$. 
- Each index $i \in \{0, \dots, n-1\}$ is pushed onto the stack exactly once.
- Each index $i$ is popped from the stack at most once.
- The operations inside the `while` loop (pop, comparison, area calculation) are $O(1)$.

Let $T(n)$ be the total time complexity. The total number of push operations is $n+1$ (including the sentinel), and the total number of pop operations is at most $n+1$. The total work is:
$$T(n) = \sum_{i=0}^{n} (\text{push}_i + \text{pop}_i) = O(n)$$
Thus, the algorithm is $\Theta(n)$ in the average and worst cases.

### Space Complexity
The space complexity is dominated by the auxiliary stack $S$.
- In the worst case (a strictly increasing sequence of heights), the stack will contain all $n$ indices.
- The space required is $S(n) = O(n)$.
- No additional data structures proportional to $n$ are required, maintaining the auxiliary space complexity at $O(n)$.