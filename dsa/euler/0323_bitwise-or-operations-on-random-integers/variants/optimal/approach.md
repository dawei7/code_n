# Bitwise-OR Operations on Random Integers - Optimal Approach

## 1. Problem Essence & Formal Mathematical Formulation

Let $y_0, y_1, y_2, \dots$ be a sequence of 32-bit random integers where each bit is $0$ or $1$ with equal probability $1/2$.
Define the bitwise-OR sequence $x_n$ by:
- $x_0 = 0$
- $x_n = x_{n-1} \mid y_n$ for $n \ge 1$
Let $N$ be the random variable denoting the index $n$ at which $x_n = 2^{32} - 1$ (all 32 bits become 1).

Find the expected value $\mathbb{E}[N]$ rounded to $10$ decimal places behind the decimal point.

---

## 2. The Naive Approach & Fundamental Bottlenecks

### Monte Carlo Simulation
A naive simulation generates random bitwise-OR sequences:
- To achieve 10 decimal places of accuracy (standard error $< 10^{-11}$), a Monte Carlo simulation requires at least $10^{22}$ trials.
- This demands decades of supercomputer execution.

---

## 3. Core Intuition & Mathematical Structure

### Bit Independence & Cumulative Distribution Function
Because each bit evolves independently across operations:
- For a single bit, the probability that it remains $0$ after $n$ independent OR operations is $\left(\frac{1}{2}\right)^n$.
- Thus, the probability that a single bit has become $1$ after $n$ operations is $1 - 2^{-n}$.
- For all 32 bits to be $1$ after $n$ operations:
  $$\mathbb{P}(N \le n) = \left( 1 - 2^{-n} \right)^{32}$$

---

## 4. Rigorous Mathematical Breakthrough & Derivations

### Tail-Sum Formula for Non-Negative Integer Random Variables
By the tail-sum formula for discrete expectations:
$$\mathbb{E}[N] = \sum_{n=0}^{\infty} \mathbb{P}(N > n) = \sum_{n=0}^{\infty} \left( 1 - \mathbb{P}(N \le n) \right) = \sum_{n=0}^{\infty} \left( 1 - (1 - 2^{-n})^{32} \right)$$

### Geometric Convergence & Truncation:
Since $1 - (1 - 2^{-n})^{32} \approx 32 \cdot 2^{-n}$ decays exponentially, evaluating the series up to $n = 100$ guarantees an error $< 10^{-28}$, which is well beyond the required 10 decimal places.

---

## 5. Concrete Step-by-Step Example Walkthrough

### Numerical Partial Sum Progression:
1. $n = 0$: $1 - (1 - 1)^{32} = 1.0$.
2. $n = 1$: $1 - (1 - 0.5)^{32} = 1 - 2^{-32} \approx 0.999999999767$.
3. $n = 2$: $1 - (3/4)^{32} \approx 0.999899$.
4. Summing terms $n = 0 \dots 100$ yields:
   $$\mathbb{E}[N] \approx \mathbf{6.3551758451}$$

---

## 6. Implementation Architecture & Algorithmic Blueprint

### Algorithmic Execution Pipeline

| Stage | Operation | Formula Action | Complexity |
| :---: | :--- | :--- | :---: |
| **Stage 1** | **Tail Sum Loop** | Loop $n = 0 \dots 100$ | $\mathcal{O}(1)$ |
| **Stage 2** | **Term Evaluation** | Compute $1 - (1 - 2^{-n})^{32}$ with high precision | $\mathcal{O}(1)$ |
| **Stage 3** | **Accumulation** | Add to running total | $\mathcal{O}(1)$ |
| **Stage 4** | **Formatting** | Format as 10-decimal float string `f"{ans:.10f}"` | $\mathcal{O}(1)$ |

---

## 7. Mathematical Complexity & Edge Case Invariants

| Dimension | Complexity | Performance / Resource Bounds |
| :--- | :--- | :--- |
| **Time Complexity** | $\mathcal{O}(1)$ | $< 0.001\text{ s}$ execution in pure Python |
| **Space Complexity** | $\mathcal{O}(1)$ | Scalar variables |
| **Implementation Standard** | $100\%$ Pure Python | Zero external dependencies |

### Critical Invariants & Edge Cases Handled:
1. **$n = 0$ Term Inclusion:** $\mathbb{P}(N > 0) = 1$ is correctly included.
2. **Double Precision Limit:** Python 64-bit float precision has 53 bits of mantissa ($\approx 15-17$ significant decimal digits), completely sufficient for 10 decimal places.
3. **Exponential Convergence:** Terms for $n > 100$ are $< 10^{-28}$.
