# Formal Mathematical Specification: Exponential Search (Galloping Search)

## 1. Definitions and Notation

Let $A$ be a sorted sequence of elements $A = \{a_0, a_1, a_2, \dots, a_{n-1}\}$ where $a_i \in \mathcal{D}$ and $\mathcal{D}$ is a totally ordered set. We define the search problem as finding an index $k \in \{0, 1, \dots, n-1\}$ such that $a_k = \tau$, where $\tau \in \mathcal{D}$ is the target value. If no such $k$ exists, the algorithm returns $\perp$ (undefined/null).

- **Input Domain:** A sorted array $A$ of length $n \in \mathbb{N}_0$ and a target $\tau$.
- **State Space:** The search space is defined by the interval $[L, R] \subseteq \mathbb{N}_0$.
- **Galloping Variable:** Let $b_j$ denote the bound at iteration $j$, where $b_0 = 1$ and $b_j = 2^j$.
- **Output:** The index $k = \text{argmin}_{i} \{a_i = \tau\}$ or $\perp$ if $\forall i, a_i \neq \tau$.

## 2. Algebraic Characterization

The algorithm proceeds in two distinct phases governed by the following logic:

### Phase I: Exponential Galloping
We seek the smallest integer $j$ such that $a_{2^j} \ge \tau$ or $2^j \ge n$. Let $b$ be the smallest power of 2 such that $b \ge \text{index}(\tau)$. The invariant maintained during the galloping phase is:
$$\forall i < \frac{b}{2}, a_i < \tau$$
The phase terminates at the first $b = 2^j$ such that $b \ge n$ or $a_b \ge \tau$. This establishes the search interval $I = [\frac{b}{2}, \min(b, n-1)]$.

### Phase II: Binary Search
Given the interval $I = [L, R]$ where $L = \frac{b}{2}$ and $R = \min(b, n-1)$, we apply the binary search predicate. Let $m = \lfloor \frac{L+R}{2} \rfloor$. The transition function is:
$$f(L, R, \tau) = \begin{cases} 
m & \text{if } a_m = \tau \\
f(m+1, R, \tau) & \text{if } a_m < \tau \\
f(L, m-1, \tau) & \text{if } a_m > \tau 
\end{cases}$$
The correctness is guaranteed by the monotonicity of $A$, ensuring that if $\tau \in A$, then $\tau \in [L, R]$.

## 3. Complexity Analysis

### Time Complexity
Let $i$ be the index such that $a_i = \tau$.

1. **Galloping Phase:** The loop terminates when $2^j \ge i$. The number of iterations $j$ satisfies $2^j \approx i$, thus $j \approx \log_2 i$. The work done is $O(\log i)$.
2. **Binary Search Phase:** The search interval has length $R - L \approx 2^j - 2^{j-1} = 2^{j-1} \approx \frac{i}{2}$. The number of comparisons in binary search is $\log_2(\text{length of interval}) = \log_2(\frac{i}{2}) = \log_2 i - 1$.

The total time complexity $T(i)$ is the sum of the two phases:
$$T(i) = O(\log i) + O(\log i - 1) = O(\log i)$$
In the worst case, where $i = n-1$, the complexity is $O(\log n)$.

### Space Complexity
The algorithm maintains a constant number of scalar variables ($bound, low, high, mid$). No auxiliary data structures are allocated that scale with the input size $n$. 

The auxiliary space complexity is:
$$S(n) = O(1)$$
The total space complexity, including the input storage, is $O(n)$, but the algorithm itself operates in $O(1)$ additional space.