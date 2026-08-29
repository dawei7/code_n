# Larger Digit Permutation - Optimal Approach

## 1. Problem Essence & Formal Mathematical Formulation

For a $k$-digit positive integer $n$ (without leading zero), let $T(n)$ be the number of strictly larger $k$-digit integers formed by permuting the digits of $n$.
Define $S(k) = \sum_{n \text{ is } k\text{-digit}} T(n)$.
Given:
- $S(3) = 1701$

Find $S(12)$.

---

## 2. The Naive Approach & Fundamental Bottlenecks

### Individual Integer Permutation Counting
- There are $9 \times 10^{11}$ twelve-digit positive integers.
- Sorting and analyzing permutations for each number independently is impossible.

---

## 3. Core Intuition & Mathematical Structure

### Equivalence Classes over Digit Multisets
Permuting the digits of $n$ preserves the multiset of digits $M = (c_0, c_1, \dots, c_9)$ where $\sum_{d=0}^9 c_d = k$.
The total number of valid $k$-digit integers (avoiding a leading zero) formed from multiset $M$ is:

$$
C(M) = \frac{k!}{\prod_{d=0}^9 c_d!} - \frac{(k-1)!}{(c_0 - 1)! \prod_{d=1}^9 c_d!} = \frac{(k - c_0)(k-1)!}{\prod_{d=0}^9 c_d!}
$$

---

## 4. Rigorous Mathematical Breakthrough & Derivations

### Triangular Sum over Sorted Permutations
When the $C(M)$ valid numbers formed by multiset $M$ are sorted in strictly increasing order $n_1 < n_2 < \dots < n_{C(M)}$:
- The $i$-th number has exactly $T(n_i) = C(M) - i$ strictly larger permutations.
Summing $T(n)$ over the entire multiset class $M$ yields the triangular number:

$$
\sum_{n \in M} T(n) = \sum_{i=1}^{C(M)} (C(M) - i) = \sum_{j=0}^{C(M) - 1} j = \binom{C(M)}{2} = \frac{C(M)(C(M) - 1)}{2}
$$

Thus, the global sum $S(k)$ is simply:

$$
\begin{aligned}
S(k) = \sum_{\substack{c_0 + c_1 + \dots + c_9 = k \\ c_0 < k}} \binom{C(c_0, \dots, c_9)}{2}
\end{aligned}
$$

The number of digit multisets for $k = 12$ is $\binom{12 + 10 - 1}{9} = \binom{21}{9} = \mathbf{293,930}$.

---

## 5. Concrete Step-by-Step Example Walkthrough

### Walkthrough for $k = 3$:
- Multisets of 3 digits ($c_0 + \dots + c_9 = 3$):
  - 3 identical non-zero digits (e.g. $111$): $C(M) = 1 \implies \binom{1}{2} = 0$.
  - 2 identical non-zero digits + 1 other (e.g. $112$): $C(M) = 3 \implies \binom{3}{2} = 3$.
  - 1 zero + 2 identical (e.g. $110$): $C(M) = 2 \implies \binom{2}{2} = 1$.
  - 3 distinct non-zero (e.g. $123$): $C(M) = 6 \implies \binom{6}{2} = 15$.
  - 1 zero + 2 distinct non-zero (e.g. $120$): $C(M) = 4 \implies \binom{4}{2} = 6$.
  - 2 zeros + 1 non-zero (e.g. $100$): $C(M) = 1 \implies \binom{1}{2} = 0$.
- Summing over all $\binom{12}{9} = 220$ multisets yields $S(3) = \mathbf{1701}$. (Matches problem specification! $\checkmark$)

---

## 6. Implementation Architecture & Algorithmic Blueprint

| Stage | Operation | Description | Complexity |
| :---: | :--- | :--- | :---: |
| **Stage 1** | **Factorial Array** | Precompute $0! \dots 12!$ | $\mathcal{O}(k)$ |
| **Stage 2** | **Multiset DFS** | Depth-first search generating compositions $c_0 + \dots + c_9 = 12$ | $293,930$ nodes |
| **Stage 3** | **Multinomial & Triangular Sum** | Compute $C(M)$ and add $\binom{C(M)}{2}$ | $\mathcal{O}(1)$ per multiset |

---

## 7. Mathematical Complexity & Edge Case Invariants

| Dimension | Complexity | Performance / Resource Bounds |
| :--- | :--- | :--- |
| **Time Complexity** | $\mathcal{O}(\binom{k+9}{9}) \approx 0.15\text{ s}$ | Real-time execution |
| **Space Complexity** | $\mathcal{O}(1) \le 1\text{ MB}$ | Recursion stack of depth 10 |
| **Implementation Standard** | $100\%$ Pure Python | Zero external dependencies |

### Critical Invariants Handled:
1. **Leading Zero Exclusion**: Multiplying by $(k - c_0)$ precisely removes permutations with a leading zero.
2. **All-Zeros Edge Case**: If $c_0 = k$, $C(M) = 0$, properly skipped.
