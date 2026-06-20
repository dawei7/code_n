# Formal Mathematical Specification: Coin Change (Count Ways)

## 1. Definitions and Notation

Let $C = \{c_1, c_2, \dots, c_n\}$ be a finite set of positive integers representing the available coin denominations, where $c_i \in \mathbb{Z}^+$. Let $A \in \mathbb{N}_0$ be the target amount.

We define the objective as finding the number of non-negative integer solutions $(x_1, x_2, \dots, x_n)$ to the linear Diophantine equation:
$$\sum_{i=1}^{n} x_i \cdot c_i = A, \quad \text{where } x_i \in \{0, 1, 2, \dots\}$$

Let $\mathcal{S}$ be the state space of the dynamic programming table, defined as a sequence $dp = (dp_0, dp_1, \dots, dp_A)$, where $dp_j$ represents the number of unique combinations of coins that sum to exactly $j$.

## 2. Algebraic Characterization

The problem is equivalent to finding the coefficient of $z^A$ in the generating function $P(z)$:
$$P(z) = \prod_{i=1}^{n} \left( \sum_{k=0}^{\infty} z^{k \cdot c_i} \right) = \prod_{i=1}^{n} \frac{1}{1 - z^{c_i}}$$

To compute this via dynamic programming, we define $dp[i][j]$ as the number of ways to form amount $j$ using only the first $i$ coin denominations. The recurrence relation is:
$$dp[i][j] = dp[i-1][j] + dp[i][j - c_i]$$
subject to the base cases:
1. $dp[i][0] = 1$ for all $0 \le i \le n$ (one way to make zero: use no coins).
2. $dp[0][j] = 0$ for all $j > 0$ (zero ways to make a positive amount with no coins).

By observing that $dp[i][j]$ depends only on the current row $i$ and the previous row $i-1$, we optimize the space by collapsing the state into a 1D array $dp[j]$. The transition becomes:
$$dp[j] \leftarrow dp[j] + dp[j - c_i]$$
where the update is performed for $j \in \{c_i, c_i+1, \dots, A\}$. The order of iteration (outer loop over $C$, inner loop over $A$) ensures that each coin $c_i$ is considered as an "addition" to existing combinations, effectively enforcing a canonical ordering of coins that prevents the counting of permutations.

## 3. Complexity Analysis

### Time Complexity
The algorithm consists of a nested loop structure. The outer loop iterates over the set of denominations $C$, which has cardinality $n$. The inner loop iterates over the range of amounts from $c_i$ to $A$. 

The total number of operations $T(n, A)$ is given by the summation:
$$T(n, A) = \sum_{i=1}^{n} (A - c_i + 1)$$
Since $c_i \ge 1$, we have $A - c_i + 1 \le A$. Thus:
$$T(n, A) \le \sum_{i=1}^{n} A = n \cdot A$$
Therefore, the time complexity is $O(n \cdot A)$. Given that each inner operation is a constant-time addition, the complexity is strictly $\Theta(n \cdot A)$.

### Space Complexity
The algorithm utilizes a 1D array $dp$ of size $A+1$ to store the number of ways to form each sub-amount. 
- **Auxiliary Space:** The space required for the DP table is $A+1$ integers.
- **Total Space:** $O(A)$.

As the algorithm does not require the storage of the full $n \times A$ matrix, the space complexity is optimal at $O(A)$, where $A$ is the target amount.