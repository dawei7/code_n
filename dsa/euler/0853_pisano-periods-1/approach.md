# Pisano Periods 1 - Optimal Approach

## 1. Problem Essence & Formal Mathematical Formulation

For any positive integer $n$, let $\pi(n)$ denote the Pisano period of the Fibonacci sequence modulo $n$.
Given:
- For period 18: $n \in \{19, 38, 76\}$. Sum of $n < 50$ is $57$.

Find the sum of all $n < 1\,000\,000\,000$ for which $\pi(n) = 120$.

---

## 2. The Naive Approach & Fundamental Bottlenecks

### Direct Period Simulation
- Simulating the Fibonacci sequence modulo $n$ for all $1 \le n < 10^9$ requires iterating $> 10^{11}$ steps, taking days of computation.

---

## 3. Core Intuition & Mathematical Structure

### Divisibility Criterion for Pisano Periods
A modulus $n$ has Pisano period dividing $L$ if and only if the period cycle restarts at step $L$:
$$F_L \equiv 0 \pmod n \quad \text{and} \quad F_{L+1} \equiv 1 \pmod n$$
This holds if and only if $n$ divides both $F_L$ and $F_{L+1} - 1$, which is equivalent to:
$$n \mid G_L = \gcd(F_L, F_{L+1} - 1)$$

---

## 4. Rigorous Mathematical Breakthrough & Derivations

### Exact Period Identification
For $L = 120$:
$$G_{120} = \gcd(F_{120}, F_{121} - 1) = 1548008755920 = 2^4 \cdot 3^2 \cdot 5 \cdot 11 \cdot 31 \cdot 41 \cdot 61 \cdot 2521$$

$G_{120}$ has exactly $(4+1)(2+1)(2)(2)(2)(2)(2)(2) = 960$ divisors.

A divisor $n \mid G_{120}$ has period **exactly** 120 (and not a proper divisor of 120) if and only if:
$$n \nmid G_d \quad \text{for all maximal proper divisors } d \in \{60, 40, 24\} \text{ of } 120$$
Testing this condition on each of the 960 divisors takes under 1 millisecond.

---

## 5. Concrete Step-by-Step Example Walkthrough

### Walkthrough for Period $L = 18$:
- $F_{18} = 2584$, $F_{19} - 1 = 4180$.
- $G_{18} = \gcd(2584, 4180) = 76 = 2^2 \cdot 19$.
- Divisors of 76: $\{1, 2, 4, 19, 38, 76\}$.
- Maximal proper divisors of 18: $d \in \{9, 6\}$.
  - $F_9 = 34, F_{10} - 1 = 54 \implies G_9 = \gcd(34, 54) = 2$.
  - $F_6 = 8, F_7 - 1 = 12 \implies G_6 = \gcd(8, 12) = 4$.
- Eliminating divisors of $G_9$ and $G_6$ ($\{1, 2, 4\}$) leaves exact period 18 moduli: $\{19, 38, 76\}$.
- Sum $< 50$: $19 + 38 = \mathbf{57}$. (Matches problem specification! $\checkmark$)

---

## 6. Implementation Architecture & Algorithmic Blueprint

| Stage | Operation | Description | Complexity |
| :---: | :--- | :--- | :---: |
| **Stage 1** | **Fibonacci Evaluation** | Compute $F_{120}, F_{121}$ via dynamic recurrence | $\mathcal{O}(L)$ |
| **Stage 2** | **GCD & Prime Factorization** | Compute $G_{120} = \gcd(F_{120}, F_{121} - 1)$ and factor | $\mathcal{O}(\sqrt{G_{120}})$ |
| **Stage 3** | **Divisor Tree Generation** | Enumerate all 960 divisors of $G_{120}$ | $\mathcal{O}(d(G_{120}))$ |
| **Stage 4** | **Sub-period Filtering** | Filter $n < 10^9$ with $n \nmid G_{60}, G_{40}, G_{24}$ | $\mathcal{O}(d(G_{120}))$ |

---

## 7. Mathematical Complexity & Edge Case Invariants

| Dimension | Complexity | Performance / Resource Bounds |
| :--- | :--- | :--- |
| **Time Complexity** | $\mathcal{O}(L + d(G_L)) \approx 0.001\text{ s}$ | Instantaneous execution |
| **Space Complexity** | $\mathcal{O}(d(G_L)) \le 10\text{ KB}$ | 960 integer entries |
| **Implementation Standard** | $100\%$ Pure Python | Zero external dependencies |

### Critical Invariants Handled:
1. **Maximal Sub-period Sufficiency**: To prove $\pi(n) = L$, it suffices to check only the maximal proper divisors $L/p$ for prime factors $p \mid L$, eliminating redundant checks on composite sub-divisors.
2. **Exact Divisor Bounds**: All candidates are guaranteed divisors of $G_L$, avoiding any linear modulus search.
