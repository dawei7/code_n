# Largest Prime Factor - Optimal Approach

## 1. Problem Essence & Formal Mathematical Formulation

By the Fundamental Theorem of Arithmetic, every integer $N > 1$ admits a unique prime factorization:

$$
N = \prod_{i=1}^k p_i^{e_i} = p_1^{e_1} p_2^{e_2} \cdots p_k^{e_k}
$$

where $p_1 < p_2 < \dots < p_k$ are distinct prime numbers ($p_i \in \mathbb{P}$) and $e_i \ge 1$.

The objective is to compute the largest prime factor of $N$:

$$
P_{\text{max}}(N) = \max \{ p \in \mathbb{P} \mid p \mid N \} = p_k
$$

We must evaluate $P_{\text{max}}(600\,851\,475\,143)$.

---

## 2. The Naive Approach & Fundamental Bottlenecks

### Naive Unreduced Trial Division
A naive approach tests all integers $d \in [2, N]$ for divisibility and primality:
```python
def is_prime(x):
    return x > 1 and all(x % i != 0 for i in range(2, int(x**0.5) + 1))

def naive_largest_factor(n):
    for d in range(n, 1, -1):
        if n % d == 0 and is_prime(d):
            return d
```

### Computational Inefficiencies
1. **Unbounded Iteration $\mathcal{O}(N)$**: For $N \approx 6.0 \times 10^{11}$, element-wise search requires hundreds of billions of division steps.
2. **Repeated Primality Tests**: Testing primality on every divisor candidate creates redundant nested computations.

---

## 3. Core Intuition & Mathematical Structure

Instead of testing primality separately, we use **Dynamic Factor Extraction**:
Whenever we find the smallest divisor $d \ge 2$ that divides the remaining dividend $M$, **$d$ is guaranteed to be prime** because all smaller composite multiples have already been divided out.

### Factorization Reduction Table for $N = 600\,851\,475\,143$

| Step | Divisor $d$ | Divisibility $d \mid M$ | Remaining Dividend $M \leftarrow M / d^{v_d(M)}$ | Dynamic Bound $\sqrt{M}$ |
| :---: | :---: | :---: | :---: | :---: |
| **Start** | — | — | $600\,851\,475\,143$ | $775\,146$ |
| **1** | $71$ | $71 \mid 600\,851\,475\,143$ | $8\,462\,696\,833$ | $91\,992$ |
| **2** | $839$ | $839 \mid 8\,462\,696\,833$ | $10\,086\,647$ | $3\,175$ |
| **3** | $1471$ | $1471 \mid 10\,086\,647$ | $6857$ | $82$ |
| **End** | $d > 82$ | $d^2 > M$ halts loop | **$6857$** (Remaining prime) | — |

---

## 4. Rigorous Mathematical Breakthrough & Derivations

### A. Square Root Bound on Composite Dividends
If $M$ is composite, it must have at least one prime factor $p \le \sqrt{M}$.
*Proof:* If every prime factor $p_i > \sqrt{M}$, then $M = \prod p_i \ge p_1 p_2 > \sqrt{M} \sqrt{M} = M$, a contradiction.

### B. In-Place Division & Automatic Primality
By dividing out all occurrences of $d$ via:

$$
M \leftarrow \frac{M}{d^{v_d(M)}}
$$

1. No composite multiple of $d$ can ever divide the reduced $M$.
2. The next divisor discovered is strictly prime.
3. The upper bound threshold $d \le \sqrt{M}$ shrinks dynamically, enabling super-fast termination.

---

## 5. Concrete Step-by-Step Example Walkthrough

### Example 1: Trace on $N = 13195$
1. Initial $M = 13195$.
2. $d = 2, 3, 4$: Do not divide $13195$.
3. $d = 5$: $13195 / 5 = 2639 \implies M = 2639, P_{\text{max}} = 5$.
4. $d = 7$: $2639 / 7 = 377 \implies M = 377, P_{\text{max}} = 7$.
5. $d = 13$: $377 / 13 = 29 \implies M = 29, P_{\text{max}} = 13$.
6. For $d \ge 15$, $d^2 \ge 225 > 29$, loop terminates.
7. Residual $M = 29 > 1 \implies P_{\text{max}} = 29$. Matches sample! $\checkmark$

### Example 2: Target Evaluation for $N = 600\,851\,475\,143$
- $M \div 71 = 8\,462\,696\,833$
- $M \div 839 = 10\,086\,647$
- $M \div 1471 = 6857$
- Residual prime factor $= \mathbf{6857}$.

---

## 6. Implementation Architecture & Algorithmic Blueprint

### Algorithmic Execution Pipeline

| Stage | Operation | Code / Formula Action | Complexity |
| :---: | :--- | :--- | :---: |
| **Stage 1** | **State Initialization** | $M = N, P_{\text{max}} = 1, d = 2$ | $\mathcal{O}(1)$ |
| **Stage 2** | **Dynamic Trial Loop** | Iterate while $d^2 \le M$ | $\mathcal{O}(\sqrt{p_{\text{max}}})$ |
| **Stage 3** | **Exhaustive Division** | While $d \mid M$: $M \leftarrow M // d, P_{\text{max}} = d$ | $\mathcal{O}(\log_d N)$ |
| **Stage 4** | **Wheel Step** | $d \leftarrow d + 1$ if $d == 2$ else $d + 2$ | $\mathcal{O}(1)$ |
| **Stage 5** | **Residual Capture** | If $M > 1$: $P_{\text{max}} = M$ | $\mathcal{O}(1)$ |

---

## 7. Mathematical Complexity & Edge Case Invariants

| Dimension | Complexity | Performance / Resource Bounds |
| :--- | :--- | :--- |
| **Time Complexity** | $\mathcal{O}(\sqrt{p_k})$ | $\approx 0.0001$ seconds ($d$ halts at $1471$) |
| **Space Complexity** | $\mathcal{O}(1)$ | In-place integer registers |
| **Dynamic Execution** | $100\%$ Inline | Trial division with dynamic bound reduction |

### Critical Invariants & Edge Cases Handled:
1. **Prime Inputs ($N \in \mathbb{P}$)**: If $N$ is prime, loop finishes with $M = N > 1$, correctly returning $P_{\text{max}} = N$.
2. **Even Factor Elimination**: The special step $d=2$ removes all powers of 2 before odd stepping begins.