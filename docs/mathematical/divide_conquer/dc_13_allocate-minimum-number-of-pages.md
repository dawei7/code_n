# Formal Mathematical Specification: Allocate Minimum Number of Pages

## 1. Definitions and Notation

Let $A = \{a_1, a_2, \dots, a_N\}$ be an ordered sequence of $N$ positive integers, where $a_i \in \mathbb{Z}^+$ represents the number of pages in the $i$-th book. Let $M \in \mathbb{Z}^+$ be the number of students.

We define a partition of $A$ into $M$ contiguous non-empty subsequences (subarrays) $S_1, S_2, \dots, S_M$, such that:
1. $\bigcup_{j=1}^M S_j = A$ and $S_j \cap S_k = \emptyset$ for $j \neq k$.
2. Each $S_j$ consists of a contiguous range of indices $[l_j, r_j]$ such that $l_1 = 1, r_M = N$, and $l_{j+1} = r_j + 1$.

Let $\sigma(S_j) = \sum_{i \in S_j} a_i$ denote the total pages assigned to the $j$-th student. The objective is to find the value $X^*$ defined by the minimax optimization problem:
$$X^* = \min_{\mathcal{P} \in \Omega} \left( \max_{1 \le j \le M} \sigma(S_j) \right)$$
where $\Omega$ is the set of all valid partitions of $A$ into $M$ contiguous subsequences.

The domain of the answer space is the interval $\mathcal{I} = [\max(A), \sum_{i=1}^N a_i]$.

## 2. Algebraic Characterization

The algorithm utilizes a monotonic predicate function $f: \mathbb{Z} \to \{0, 1\}$ to determine feasibility. For a given capacity $C \in \mathcal{I}$, $f(C) = 1$ if there exists a partition $\mathcal{P}$ such that $\forall j: \sigma(S_j) \le C$, and $f(C) = 0$ otherwise.

**Greedy Feasibility Criterion:**
To evaluate $f(C)$, we define a greedy function $g(C)$ that computes the minimum number of students $m_{req}$ required to ensure no student exceeds capacity $C$:
$$m_{req}(C) = 1 + \sum_{i=1}^{N-1} \mathbb{I}\left( \text{prefix\_sum}(i, \text{last\_reset}) + a_{i+1} > C \right)$$
where $\mathbb{I}(\cdot)$ is the indicator function. The predicate is defined as:
$$f(C) = \begin{cases} 1 & \text{if } m_{req}(C) \le M \\ 0 & \text{if } m_{req}(C) > M \end{cases}$$

**Monotonicity:**
The function $f(C)$ is monotonically non-decreasing with respect to $C$. Specifically, if $C_1 < C_2$, then $m_{req}(C_1) \ge m_{req}(C_2)$, implying $f(C_1) \le f(C_2)$. This property guarantees that the binary search converges to the unique minimum $X^*$ such that $f(X^*) = 1$.

**Loop Invariant:**
At the start of each iteration of the binary search with bounds $[L, R]$, the following invariant holds:
$$f(L-1) = 0 \quad \land \quad f(R) = 1$$
The search terminates when $L = R$, yielding the optimal $X^* = L$.

## 3. Complexity Analysis

### Time Complexity
The algorithm performs a binary search over the range $\mathcal{I} = [\max(A), \sum_{i=1}^N a_i]$. Let $S = \sum_{i=1}^N a_i$ and $K = \max(A)$. The number of iterations $T$ required to converge is:
$$T = \lceil \log_2(S - K + 1) \rceil$$
In each iteration, the function $f(C)$ performs a linear scan of the array $A$ to compute $m_{req}(C)$, which requires $\Theta(N)$ operations. Thus, the total time complexity is:
$$T_{total} = \Theta(N \cdot \log(S - K))$$

### Space Complexity
The algorithm maintains a constant number of scalar variables ($lo, hi, mid, needed, pages$) regardless of the input size $N$. 
- **Auxiliary Space:** $\Theta(1)$.
- **Total Space:** $\Theta(N)$ to store the input array $A$. 
Given that the input is provided, the auxiliary space complexity is strictly $O(1)$.