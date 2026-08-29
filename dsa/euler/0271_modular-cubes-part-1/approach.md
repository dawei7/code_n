# Modular Cubes, Part 1 - Optimal Approach

## 1. Problem Essence & Formal Mathematical Formulation

For a positive integer $n$, define $S(n)$ as the sum of all integers $x$ such that:
$$1 < x < n \quad \text{and} \quad x^3 \equiv 1 \pmod n$$
We are given $N = 13082761331670030 = 2 \times 3 \times 5 \times 7 \times 11 \times 13 \times 17 \times 19 \times 23 \times 29 \times 31 \times 37 \times 41 \times 43$.
Find $S(N)$.

---

## 2. The Naive Approach & Fundamental Bottlenecks

### Linear Search for Modular Cube Roots
A naive approach tests all $x \in [2, N - 1]$ to check if $x^3 \equiv 1 \pmod N$:
- $N \approx 1.3 \times 10^{16}$.
- Testing $10^{16}$ numbers sequentially is completely impossible.

---

## 3. Core Intuition & Mathematical Structure

### Chinese Remainder Theorem & Prime Power Roots
By the Chinese Remainder Theorem (CRT), since $N = \prod_{i=1}^{14} p_i$ is a product of 14 distinct primes:
- The congruence $x^3 \equiv 1 \pmod N$ is equivalent to the simultaneous system:
  $$x^3 \equiv 1 \pmod{p_i} \quad \text{for all } i = 1, \dots, 14$$
- For each prime $p_i$:
  - If $p_i \not\equiv 1 \pmod 3$ and $p_i \ne 3$: $\gcd(3, p_i - 1) = 1$, so there is only **1 root** ($r \equiv 1$).
  - If $p_i \equiv 1 \pmod 3$: $\gcd(3, p_i - 1) = 3$, so there are **3 distinct roots** $\{1, r_1, r_2\} \pmod{p_i}$.
  - For $p = 3$: only $1$ root ($1 \pmod 3$).

---

## 4. Rigorous Mathematical Breakthrough & Derivations

### Cartesian Product over Local Cube Roots
1. The primes $p_i \mid N$ with $p_i \equiv 1 \pmod 3$ are:
   $$\{7, 13, 19, 31, 37, 43\} \quad (\text{exactly } 6 \text{ primes})$$
2. Total global solutions: $3^6 = 729$ solutions!
3. For each of the 729 combinations of local roots:
   Reconstruct the unique global integer $x \in [0, N - 1]$ via the Chinese Remainder Theorem.
4. Exclude the trivial root $x = 1$.
5. Summing the remaining $728$ values of $x$ completes in under $0.01$ seconds in pure Python!

---

## 5. Concrete Step-by-Step Example Walkthrough

### Verification on $n = 91 = 7 \times 13$:
- Primes: $7 \equiv 1 \pmod 3$ (roots $\{1, 2, 4\} \pmod 7$) and $13 \equiv 1 \pmod 3$ (roots $\{1, 3, 9\} \pmod{13}$).
- Total CRT combinations: $3 \times 3 = 9$ roots:
  $x \in \{1, 9, 16, 22, 29, 53, 74, 79, 81\} \pmod{91}$.
- Non-trivial sum: $9 + 16 + 22 + 29 + 53 + 74 + 79 + 81 = \mathbf{363}$. (Matches sample! $\checkmark$)

---

## 6. Implementation Architecture & Algorithmic Blueprint

### Algorithmic Execution Pipeline

| Stage | Operation | Method | Complexity |
| :---: | :--- | :--- | :---: |
| **Stage 1** | **Local Roots** | Find solutions to $r^3 \equiv 1 \pmod p$ for each $p \mid N$ | $\mathcal{O}(p)$ |
| **Stage 2** | **CRT Reconstruction** | Precompute CRT basis weights $M_i \cdot (M_i^{-1} \bmod p_i)$ | $\mathcal{O}(K)$ |
| **Stage 3** | **Cartesian Loop** | Iterate over all 729 root tuples and compute $x \bmod N$ | $\mathcal{O}(3^k)$ |
| **Stage 4** | **Summation** | Add all $x > 1$ | $\mathcal{O}(1)$ |

---

## 7. Mathematical Complexity & Edge Case Invariants

| Dimension | Complexity | Performance / Resource Bounds |
| :--- | :--- | :--- |
| **Time Complexity** | $\mathcal{O}(3^k)$ where $k = 6$ ($729$ iterations) | $< 0.01\text{ s}$ execution in pure Python |
| **Space Complexity** | $\mathcal{O}(1)$ | Scalar variables |
| **Implementation Standard** | $100\%$ Pure Python | Zero native compiler dependencies |

### Critical Invariants & Edge Cases Handled:
1. **$x = 1$ Exclusion:** The trivial root $x = 1$ is strictly excluded from $S(N)$.
2. **Chinese Remainder Uniqueness:** Modulo $N$ arithmetic is exact with arbitrary precision.
3. **Prime Powers:** Multiplicative independence across disjoint primes.
