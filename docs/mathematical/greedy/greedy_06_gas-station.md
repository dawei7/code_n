# Formal Mathematical Specification: Gas Station (Circular Tour)

## 1. Definitions and Notation

Let $N \in \mathbb{Z}^+$ be the number of gas stations. We define the circular route as a set of indices $I = \{0, 1, \dots, N-1\}$. 
The input consists of two sequences:
- A gas availability sequence $G = \{g_0, g_1, \dots, g_{N-1}\}$, where $g_i \in \mathbb{R}_{\ge 0}$.
- A cost sequence $C = \{c_0, c_1, \dots, c_{N-1}\}$, where $c_i \in \mathbb{R}_{\ge 0}$.

We define the net gain at station $i$ as $d_i = g_i - c_i$. The cumulative gain function starting from index $s$ after $k$ steps is defined as:
$$f(s, k) = \sum_{j=0}^{k-1} d_{(s+j) \pmod N}$$

A starting index $s \in I$ is **valid** if and only if for all $k \in \{1, 2, \dots, N\}$:
$$f(s, k) \ge 0$$

The objective is to find $s^* \in I$ such that $s^*$ is valid, or return $-1$ if no such $s^*$ exists.

## 2. Algebraic Characterization

### Existence Condition
A necessary and sufficient condition for the existence of a valid starting index $s^*$ is that the total net gain over the circuit is non-negative:
$$\sum_{i=0}^{N-1} d_i \ge 0$$
If $\sum_{i=0}^{N-1} d_i < 0$, then for any $s \in I$, $f(s, N) < 0$, implying the tank will be exhausted before completing the circuit.

### The Greedy Invariant
Let $T_i$ be the state of the tank at step $i$ during a linear scan. We define the transition:
$$T_{i+1} = \max(0, T_i + d_i)$$
However, to identify the starting index, we maintain a running sum $S_i$ and a candidate start $s$:
1. Let $S_i = \sum_{j=s}^{i} d_j$.
2. If $S_i < 0$, then for all $k \in \{s, \dots, i\}$, the path starting at $k$ cannot reach $i+1$. Thus, we set $s = i+1$ and reset $S = 0$.

**Theorem:** If $\sum_{i=0}^{N-1} d_i \ge 0$, the index $s$ resulting from the single-pass greedy scan is the unique valid starting index.
*Proof Sketch:* Suppose the algorithm resets at index $i$. This implies $\sum_{j=s}^i d_j < 0$. Any starting point $k \in (s, i]$ would yield a partial sum $\sum_{j=k}^i d_j \le \sum_{j=s}^i d_j < 0$, violating the validity condition. Thus, the reset is safe.

## 3. Complexity Analysis

### Time Complexity
The algorithm performs a single linear traversal of the input arrays $G$ and $C$.
Let $W(N)$ be the total work performed. The algorithm executes:
- One summation to verify the existence condition: $\sum_{i=0}^{N-1} (g_i + c_i) \implies O(N)$.
- One loop of $N$ iterations, where each iteration performs a constant number of arithmetic operations (addition, comparison, assignment): $\sum_{i=0}^{N-1} c \implies O(N)$.

The total time complexity is:
$$T(N) = O(N) + O(N) = O(N)$$
Since the algorithm visits each element exactly once, the complexity is $\Theta(N)$.

### Space Complexity
The algorithm utilizes a fixed set of auxiliary variables:
- `tank` (scalar, $\mathbb{R}$)
- `start` (scalar, $\mathbb{Z}$)
- `i` (loop index, $\mathbb{Z}$)
- `total_gas`, `total_cost` (scalars, $\mathbb{R}$)

The auxiliary space $S(N)$ is independent of the input size $N$:
$$S(N) = O(1)$$
The total space complexity, including the input storage, is $O(N)$, but the auxiliary space complexity is strictly $O(1)$.