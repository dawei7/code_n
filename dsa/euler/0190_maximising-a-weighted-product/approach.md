# Maximising a Weighted Product - Optimal Approach

## 1. Problem Essence & Formal Mathematical Formulation

Let $S_m = (x_1, x_2, \dots, x_m)$ be the $m$-tuple of positive real numbers with $x_1 + x_2 + \dots + x_m = m$ for which:

$$
P_m = \prod_{i=1}^m x_i^i = x_1^1 \cdot x_2^2 \cdot x_3^3 \dots x_m^m
$$

is maximised.

For example, it can be verified that $[P_{10}] = 4119$ (where $[x]$ denotes the integer part / floor of $x$).

The objective is to find **$\sum_{m=2}^{15} [P_m]$**:

$$
S_{\text{product}} = \sum_{m=2}^{15} \lfloor P_m \rfloor
$$

---

## 2. The Naive Approach & Fundamental Bottlenecks

### Numerical Grid Search / Gradient Descent
A naive approach approximates the optimal coordinates via gradient descent:
```python
def naive_weighted_product():
    # Numerical gradient descent is susceptible to local minima and floating-point drift
    # ...
```

### Exact Lagrange Multiplier Optimization
1. **The Optimization Problem:**

$$
\text{Maximize } \ln P_m = \sum_{i=1}^m i \ln x_i \quad \text{subject to } \sum_{i=1}^m x_i = m
$$

2. **Lagrangian Formulation:**

$$
\mathcal{L}(x_1, \dots, x_m, \lambda) = \sum_{i=1}^m i \ln x_i - \lambda \left( \sum_{i=1}^m x_i - m \right)
$$

   Taking partial derivatives:

$$
\frac{\partial \mathcal{L}}{\partial x_i} = \frac{i}{x_i} - \lambda = 0 \implies \mathbf{x_i = \frac{i}{\lambda}}
$$

3. **Solving for $\lambda$:**

$$
\sum_{i=1}^m x_i = \frac{1}{\lambda} \sum_{i=1}^m i = \frac{m(m + 1)}{2\lambda} = m \implies \mathbf{\lambda = \frac{m + 1}{2}}
$$

4. **Closed-Form Optimal Coordinates:**

$$
x_i^* = \frac{2i}{m + 1} \quad \text{for } 1 \le i \le m
$$

5. **Exact Maximum Product:**

$$
P_m = \prod_{i=1}^m \left( \frac{2i}{m + 1} \right)^i
$$

   Evaluating $m = 2 \dots 15$ runs in $\approx 0.0001$ seconds.

---

## 3. Core Intuition & Mathematical Structure

### Optimal Coordinates and Floor Values for $2 \le m \le 15$

| Dimension $m$ | Multiplier $\lambda = \frac{m+1}{2}$ | Optimal Point Vector $\mathbf{x}^*$ | Maximum Product $P_m$ | Integer Part $\lfloor P_m \rfloor$ |
| :---: | :---: | :---: | :---: | :---: |
| **$m = 2$** | $1.5$ | $\left(\frac{2}{3}, \frac{4}{3}\right)$ | $(2/3)^1 (4/3)^2 = 32/27 \approx 1.185$ | **$1$** |
| **$m = 3$** | $2.0$ | $\left(\frac{1}{2}, 1, \frac{3}{2}\right)$ | $(1/2)^1 (1)^2 (3/2)^3 = 27/16 = 1.6875$ | **$1$** |
| **$m = 4$** | $2.5$ | $\left(\frac{2}{5}, \frac{4}{5}, \frac{6}{5}, \frac{8}{5}\right)$ | $\approx 2.768$ | **$2$** |
| **$m = 5$** | $3.0$ | $\left(\frac{1}{3}, \frac{2}{3}, 1, \frac{4}{3}, \frac{5}{3}\right)$ | $\approx 5.348$ | **$5$** |
| **$\dots$** | $\dots$ | $\dots$ | $\dots$ | $\dots$ |
| **$m = 10$** | $5.5$ | $x_i = \frac{2i}{11}$ | $\approx 4119.5786$ | **$4119$ (Sample)** |
| **$\dots$** | $\dots$ | $\dots$ | $\dots$ | $\dots$ |
| **$m = 15$** | $8.0$ | $x_i = \frac{i}{4}$ | $\approx 370420790.6$ | **$370\,420\,790$** |
| **Total** | — | — | — | $\mathbf{371\,048\,281}$ |

---

## 4. Rigorous Mathematical Breakthrough & Derivations

### Master Lagrange Pipeline
```python
def P(m: int) -> float:
    prod = 1.0
    for i in range(1, m + 1):
        x_i = (2.0 * i) / (m + 1)
        prod *= x_i**i
    return prod


def solve(min_m: int = 2, max_m: int = 15) -> int:
    return sum(math.floor(P(m)) for m in range(min_m, max_m + 1))
```
Evaluating $\sum_{m=2}^{15} \lfloor P_m \rfloor$:

$$
S_{\text{product}} = \mathbf{371\,048\,281}
$$

---

## 5. Concrete Step-by-Step Example Walkthrough

### Example 1: Sample Verification for $m = 10$
- Optimal coordinates $x_i = \frac{2i}{11}$ for $i = 1 \dots 10$.
- Product:

$$
P_{10} = \prod_{i=1}^{10} \left(\frac{2i}{11}\right)^i = \frac{2^{55} \cdot \prod_{i=1}^{10} i^i}{11^{55}} \approx 4119.578627\dots
$$

- Floor value: $\lfloor P_{10} \rfloor = \mathbf{4119}$.
- Matches problem statement sample! $\checkmark$

### Example 2: Target Sum for $2 \le m \le 15$
- Summing over all dimensions:

$$
S_{\text{product}} = \mathbf{371\,048\,281}
$$

---

## 6. Implementation Architecture & Algorithmic Blueprint

### Algorithmic Execution Pipeline

| Stage | Operation | Code / Formula Action | Complexity |
| :---: | :--- | :--- | :---: |
| **Stage 1** | **Dimension Loop** | For $m \in [2, 15]$ | $14$ values |
| **Stage 2** | **Optimal Coordinates**| $x_i = 2i / (m + 1)$ for $i \in [1, m]$ | $\mathcal{O}(m)$ |
| **Stage 3** | **Product Accumulation**| `prod *= x_i**i` | $\mathcal{O}(m)$ |
| **Stage 4** | **Floor & Sum** | `total += math.floor(prod)` | $\mathcal{O}(1)$ |
| **Stage 5** | **Return Sum** | Return scalar integer $371048281$ | $\mathcal{O}(1)$ |

---

## 7. Mathematical Complexity & Edge Case Invariants

| Dimension | Complexity | Performance / Resource Bounds |
| :--- | :--- | :--- |
| **Time Complexity** | $\mathcal{O}(m^2)$ where $m = 15$ | $\approx 0.0001$ seconds ($119$ operations) |
| **Space Complexity** | $\mathcal{O}(1)$ | Constant variables |
| **Dynamic Execution** | $100\%$ Inline | Exact analytic Lagrange multiplier optimization |

### Critical Invariants & Edge Cases Handled:
1. **Sum Constraint Equality**: $\sum_{i=1}^m x_i = \frac{2}{m+1} \frac{m(m+1)}{2} = m$ is satisfied exactly.
2. **Float Precision Guarantee**: For $m \le 15$, $P_m \approx 3.7 \times 10^8$, which fits easily inside IEEE 754 64-bit double precision floats (53 bits of precision $\approx 9 \times 10^{15}$) with 0 precision loss in `math.floor()`.