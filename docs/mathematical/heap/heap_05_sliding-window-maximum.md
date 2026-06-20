# Formal Mathematical Specification: Sliding Window Maximum

## 1. Definitions and Notation

Let $A = [a_0, a_1, \dots, a_{n-1}]$ be a sequence of integers of length $n$, where $a_i \in \mathbb{Z}$. Let $k \in \mathbb{Z}^+$ be the window size such that $1 \le k \le n$.

We define a sliding window of size $k$ starting at index $i$ as the subsequence $W_i = [a_i, a_{i+1}, \dots, a_{i+k-1}]$ for $0 \le i \le n-k$.

The objective is to compute the sequence $M = [m_0, m_1, \dots, m_{n-k}]$, where each element $m_i$ is defined as the supremum of the window $W_i$:
$$m_i = \max \{a_j \mid i \le j \le i+k-1\}$$

We define the state space $\mathcal{S}$ of the monotonic deque as a sequence of indices $Q = [q_1, q_2, \dots, q_m]$ such that:
1. **Index Ordering:** $i-k < q_1 < q_2 < \dots < q_m \le i$.
2. **Monotonicity:** $a_{q_1} > a_{q_2} > \dots > a_{q_m}$.

## 2. Algebraic Characterization

The correctness of the monotonic deque approach relies on the maintenance of the invariant $\mathcal{I}$ at each step $i \in \{0, \dots, n-1\}$:

**Invariant $\mathcal{I}$:** For any index $j \in \{i-k+1, \dots, i\}$, if $j$ is not in $Q$, then there exists some $q \in Q$ such that $q > j$ and $a_q \ge a_j$.

**Transition Rules:**
Let $Q^{(i)}$ be the state of the deque after processing index $i$.
1. **Eviction of Outdated Indices:** $Q' = \{q \in Q^{(i-1)} \mid q > i-k\}$.
2. **Maintenance of Monotonicity:** Let $Q''$ be the sequence obtained by removing all $q \in Q'$ such that $a_q \le a_i$.
3. **Update:** $Q^{(i)} = Q'' \cup \{i\}$.

The maximum of the current window $W_i$ is given by the head of the deque:
$$m_i = a_{q_1} \quad \text{where } q_1 = \text{head}(Q^{(i)})$$

This holds because if $a_{q_1}$ were not the maximum, there would exist some $j \in \{i-k+1, \dots, i\}$ such that $a_j > a_{q_1}$. However, by the construction of $Q$, any index $j$ added to the deque that satisfies $a_j > a_{q_1}$ would have caused $q_1$ to be removed during the "Maintenance of Monotonicity" step, contradicting the existence of $q_1$ at the head.

## 3. Complexity Analysis

### Time Complexity
The algorithm processes each index $i \in \{0, \dots, n-1\}$ exactly once. 
Let $T(n)$ be the total time complexity. The operations performed at each step $i$ are:
1. `popleft()`: $O(1)$
2. `pop()`: $O(1)$ per element removed.
3. `append()`: $O(1)$

Let $c_i$ be the number of elements removed from the deque at step $i$. The total time is:
$$T(n) = \sum_{i=0}^{n-1} (1 + c_i)$$
Since each index $j \in \{0, \dots, n-1\}$ is added to the deque exactly once, it can be removed at most once. Thus, $\sum_{i=0}^{n-1} c_i \le n$.
Therefore, $T(n) = O(n) + O(n) = O(n)$. The amortized cost per step is $O(1)$.

### Space Complexity
The space complexity is determined by the maximum size of the deque $Q$. 
In the worst case (a strictly decreasing input sequence), the deque stores all $k$ elements of the current window. 
$$|Q| \le k$$
Thus, the auxiliary space complexity is $O(k)$. The total space complexity, including the input and output arrays, is $O(n + k) = O(n)$.