# Tidying Up B - Optimal Approach

## 1. Problem Essence & Formal Mathematical Formulation

A random permutation of $N$ jigsaw pieces numbered $1 \dots N$ is assembled.
Whenever a piece merges into a contiguous segment of length $k$, the $k$-th hexagonal number $H(k) = k(2k - 1)$ is recorded.
$E(N)$ is the expected product of all $N$ recorded hexagonal numbers.
Given:
- $E(4) = 994$

Find $E(100) \bmod 987654319$.

---

## 2. The Naive Approach & Fundamental Bottlenecks

### Permutation Expectation
- Summing over all $N! = 100! \approx 9.33 \times 10^{157}$ permutations is completely impossible.

---

## 3. Core Intuition & Mathematical Structure

### Backward Induction & Independence of Sub-segments
Consider the final step when the full caterpillar of length $N$ is completed:
- The very last piece placed is uniformly distributed among positions $i \in \{1, \dots, N\}$ with probability $1/N$.
- The length of the newly merged segment at this final step is always $N$, recording the factor $H(N) = N(2N - 1)$.
- Conditional on the last piece being at index $i$, the assembly processes for the subsegments $\{1, \dots, i-1\}$ (length $i-1$) and $\{i+1, \dots, N\}$ (length $N-i$) are **mutually independent**.

---

## 4. Rigorous Mathematical Breakthrough & Derivations

### Convolutional Recurrence
By linearity of expectation and multiplicative independence of sub-intervals:
$$E(N) = H(N) \cdot \frac{1}{N} \sum_{i=1}^N E(i - 1) E(N - i)$$
Substituting $H(N) = N(2N - 1)$:
$$E(N) = (2N - 1) \sum_{i=1}^N E(i - 1) E(N - i)$$
with initial condition $E(0) = 1$.

The factor $1/N$ cancels the $N$ in $H(N)$, proving why the expectation is always an exact integer.

---

## 5. Concrete Step-by-Step Example Walkthrough

### Walkthrough for $N = 1 \dots 4$:
- $E(0) = 1$
- $E(1) = (2(1) - 1) \cdot (E(0) E(0)) = 1 \times 1 = \mathbf{1}$.
- $E(2) = (2(2) - 1) \cdot (E(0) E(1) + E(1) E(0)) = 3 \times (1 + 1) = \mathbf{6}$.
- $E(3) = (2(3) - 1) \cdot (E(0)E(2) + E(1)E(1) + E(2)E(0)) = 5 \times (6 + 1 + 6) = 5 \times 13 = \mathbf{65}$.
- $E(4) = (2(4) - 1) \cdot (E(0)E(3) + E(1)E(2) + E(2)E(1) + E(3)E(0)) = 7 \times (65 + 6 + 6 + 65) = 7 \times 142 = \mathbf{994}$. (Matches problem specification! $\checkmark$)

---

## 6. Implementation Architecture & Algorithmic Blueprint

| Stage | Operation | Description | Complexity |
| :---: | :--- | :--- | :---: |
| **Stage 1** | **DP Table Allocation** | Allocate array $E[0 \dots N]$ with $E[0] = 1$ | $\mathcal{O}(N)$ |
| **Stage 2** | **Convolution Step** | Compute $\text{conv} = \sum_{i=1}^k E[i-1] E[k-i] \pmod{\text{MOD}}$ | $\mathcal{O}(k)$ per step |
| **Stage 3** | **Hexagonal Scaling** | Multiply by $(2k - 1) \pmod{\text{MOD}}$ | $\mathcal{O}(1)$ |
| **Stage 4** | **Result Output** | Return $E[100]$ | $\mathcal{O}(N^2) < 0.001\text{ s}$ |

---

## 7. Mathematical Complexity & Edge Case Invariants

| Dimension | Complexity | Performance / Resource Bounds |
| :--- | :--- | :--- |
| **Time Complexity** | $\mathcal{O}(N^2) \approx 0.001\text{ s}$ | Instantaneous execution |
| **Space Complexity** | $\mathcal{O}(N) \le 1\text{ KB}$ | 100 elements in memory |
| **Implementation Standard** | $100\%$ Pure Python | Zero external dependencies |

### Critical Invariants Handled:
1. **Integer Divisibility**: The structural cancellation of $1/N$ by $N(2N - 1)$ guarantees that all DP transitions remain strictly in $\mathbb{Z}$.
2. **Convolution Completeness**: The symmetric sum $i = 1 \dots N$ accounts for all $N$ possible partition points of the final merge.
