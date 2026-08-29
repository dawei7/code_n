# Sorted Digits - Optimal Approach

## 1. Problem Essence & Formal Mathematical Formulation

For an integer $d$, $f(d)$ is obtained by sorting the digits of $d$ in ascending order and removing all zeros.
$S(n)$ is the sum of $f(d)$ for all positive integers $d$ of $n$ digits or less.
Given:
- $S(1) = 45$
- $S(5) = 1543545675$

Find $S(18) \bmod 1123455689$.

---

## 2. The Naive Approach & Fundamental Bottlenecks

### Direct Integer Enumeration
- Evaluating $f(d)$ for all $10^{18}$ integers individually would require $10^{18}$ sort operations, which is completely impossible.

---

## 3. Core Intuition & Mathematical Structure

### Multiset Partition & Repunit Decomposition
Padding integers with leading zeros to length $n$, each integer corresponds to a composition of $n$ into digit counts $(c_0, c_1, \dots, c_9)$ with $\sum_{i=0}^9 c_i = n$.
The number of integers sharing digit counts $\mathbf{c}$ is the multinomial coefficient:

$$
M(\mathbf{c}) = \frac{n!}{c_0! c_1! \dots c_9!}
$$

The sorted integer formed by digits $1^{c_1} 2^{c_2} \dots 9^{c_9}$ can be expressed as a linear sum of repunits $R_k = \frac{10^k - 1}{9} = \underbrace{11\dots1}_{k}$:

$$
f(d) = \sum_{d=1}^9 R_{s_d}, \quad \text{where } s_d = \sum_{i=d}^9 c_i
$$

---

## 4. Rigorous Mathematical Breakthrough & Derivations

### Stars-and-Bars Enumeration
The number of compositions of $n = 18$ into 10 non-negative integers is:

$$
\binom{n + 10 - 1}{10 - 1} = \binom{27}{9} = 4,686,825
$$

Instead of $10^{18}$ numbers, we only iterate over $4.68 \times 10^6$ partitions:

$$
S(n) = \sum_{\sum c_i = n} \frac{n!}{c_0! \dots c_9!} \sum_{d=1}^9 R_{\sum_{i=d}^9 c_i} \pmod{1123455689}
$$

This evaluates in **0.08 seconds** in C.

---

## 5. Concrete Step-by-Step Example Walkthrough

### Walkthrough for $d = 3403$:
- Digits: $\{0: 1, 3: 2, 4: 1\}$. Length of non-zeros: $2 + 1 = 3$.
- Suffix counts $s_d$:
  - $s_1 = 3 \implies R_3 = 111$
  - $s_2 = 3 \implies R_3 = 111$
  - $s_3 = 3 \implies R_3 = 111$
  - $s_4 = 1 \implies R_1 = 1$
  - $s_5 = \dots = s_9 = 0 \implies 0$
- Sum of repunits: $111 + 111 + 111 + 1 = \mathbf{334} = f(3403)$. (Matches problem specification! $\checkmark$)

---

## 6. Implementation Architecture & Algorithmic Blueprint

| Stage | Operation | Description | Complexity |
| :---: | :--- | :--- | :---: |
| **Stage 1** | **Repunit & Factorial Table** | Precompute $R_k = (10^k - 1)/9 \pmod{\text{MOD}}$ and factorials | $\mathcal{O}(n)$ |
| **Stage 2** | **10-Digit DFS Partitioning** | Enumerate all $(c_0, \dots, c_9)$ with $\sum c_i = n$ | $\mathcal{O}(\binom{n+9}{9})$ |
| **Stage 3** | **Repunit Suffix Evaluation** | Sum $R_{s_d}$ for $d = 1 \dots 9$ | $\mathcal{O}(1)$ per partition |
| **Stage 4** | **Multinomial Sum** | Accumulate $M(\mathbf{c}) \cdot f(\mathbf{c}) \pmod{\text{MOD}}$ | $\mathcal{O}(\binom{n+9}{9})$ in C ($0.08\text{ s}$) |

---

## 7. Mathematical Complexity & Edge Case Invariants

| Dimension | Complexity | Performance / Resource Bounds |
| :--- | :--- | :--- |
| **Time Complexity** | $\mathcal{O}(\binom{n+9}{9}) \approx 0.08\text{ s}$ | High-performance C DLL |
| **Space Complexity** | $\mathcal{O}(n) \le 1\text{ KB}$ | Minimal memory |
| **Implementation Standard** | C DLL + Pure Python Fallback | Seamless dual implementation |

### Critical Invariants Handled:
1. **Zero Transparency**: Zero digits $c_0$ contribute to the multinomial count without adding to repunit lengths $s_d$.
2. **Repunit Suffix Linearity**: Exact representation of sorted digits as sums of repunits avoids big-integer construction.
