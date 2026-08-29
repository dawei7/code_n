# Number Spiral Diagonals - Optimal Approach

## 1. Problem Essence & Formal Mathematical Formulation

Starting with the number $1$ at the center and moving to the right in a clockwise direction, an $N \times N$ number spiral ($N = 1001$ with $N \equiv 1 \pmod 2$) is constructed.

Let $S(N)$ denote the sum of all numbers lying on the two main diagonals of the $N \times N$ spiral grid.

The objective is to evaluate $S(1001)$.

---

## 2. The Naive Approach & Fundamental Bottlenecks

### 2D Matrix Simulation
A naive algorithm allocates an $N \times N$ grid, populates all $N^2$ numbers along the spiral trajectory, and then sums the diagonal coordinates $(i, i)$ and $(i, N-1-i)$:
```python
def naive_spiral_diagonals(n):
    # Allocates N x N grid and simulates spiral filling
    # ...
```

### Computational Inefficiencies
1. **Memory & Time Overhead $\mathcal{O}(N^2)$**: Allocating a $1001 \times 1001$ matrix requires over $1$ million array writes ($\approx 8$ MB).
2. **Superiority of Closed-Form Algebra**: The four corners of each square shell follow an exact quadratic formula, enabling $\mathcal{O}(1)$ closed-form evaluation.

---

## 3. Core Intuition & Mathematical Structure

An $N \times N$ odd spiral consists of concentric square shells $j = 1, 2, \dots, m$ where $m = (N - 1) / 2 = 500$, centered around the initial $1 \times 1$ core with value $1$.

For each shell $j$ of side length $k = 2j + 1$:
- Top-Right corner: $C_1(j) = (2j + 1)^2$
- Top-Left corner: $C_2(j) = (2j + 1)^2 - 2j$
- Bottom-Left corner: $C_3(j) = (2j + 1)^2 - 4j$
- Bottom-Right corner: $C_4(j) = (2j + 1)^2 - 6j$

### Shell Corner Formulas & Partial Sums

| Shell $j$ | Dimension $k = 2j+1$ | Corner Values | Corner Sum $S(j) = 16j^2 + 4j + 4$ | Running Diagonal Total |
| :---: | :---: | :---: | :---: | :---: |
| **Core ($0$)** | $1 \times 1$ | $\{1\}$ | $1$ | $1$ |
| **$1$** | $3 \times 3$ | $\{9, 7, 5, 3\}$ | $16(1) + 4(1) + 4 = 24$ | $1 + 24 = \mathbf{25}$ |
| **$2$** | $5 \times 5$ | $\{25, 21, 17, 13\}$ | $16(4) + 4(2) + 4 = 76$ | $25 + 76 = \mathbf{101}$ |
| **$3$** | $7 \times 7$ | $\{49, 43, 37, 31\}$ | $16(9) + 4(3) + 4 = 160$ | $101 + 160 = \mathbf{261}$ |
| **$500$** | $1001 \times 1001$ | Shell $500$ corners | $16(500^2) + 4(500) + 4$ | **$669\,171\,001$** |

---

## 4. Rigorous Mathematical Breakthrough & Derivations

### Closed-Form Polynomial Summation
Summing the 4 corners of shell $j$:
$$S(j) = 4(2j+1)^2 - 12j = 4(4j^2 + 4j + 1) - 12j = 16j^2 + 4j + 4$$

Summing across all $m = (N - 1) / 2$ shells:
$$S(N) = 1 + \sum_{j=1}^m (16j^2 + 4j + 4) = 1 + 16 \sum_{j=1}^m j^2 + 4 \sum_{j=1}^m j + 4m$$

Substituting Faulhaber's formulas $\sum j^2 = \frac{m(m+1)(2m+1)}{6}$ and $\sum j = \frac{m(m+1)}{2}$:
$$\begin{aligned}
S(N) &= 1 + \frac{8m(m+1)(2m+1)}{3} + 2m(m+1) + 4m \\
&= \frac{3 + 8m(2m^2 + 3m + 1) + 6m^2 + 6m + 12m}{3} \\
&= \boxed{\frac{16m^3 + 30m^2 + 26m + 3}{3}}
\end{aligned}$$

---

## 5. Concrete Step-by-Step Example Walkthrough

### Example 1: Evaluation for $5 \times 5$ Spiral ($N = 5 \implies m = 2$)
Using the closed-form cubic polynomial:
$$\begin{aligned}
S(5) &= \frac{16(2^3) + 30(2^2) + 26(2) + 3}{3} \\
&= \frac{16(8) + 30(4) + 52 + 3}{3} \\
&= \frac{128 + 120 + 55}{3} = \frac{303}{3} = \mathbf{101}
\end{aligned}$$
Matches problem statement sample value **101**! $\checkmark$

### Example 2: Exact Evaluation for $1001 \times 1001$ Spiral ($m = 500$)
$$\begin{aligned}
S(1001) &= \frac{16(500^3) + 30(500^2) + 26(500) + 3}{3} \\
&= \frac{16(125\,000\,000) + 30(250\,000) + 13\,000 + 3}{3} \\
&= \frac{2\,000\,000\,000 + 7\,500\,000 + 13\,003}{3} \\
&= \frac{2\,007\,513\,003}{3} = \mathbf{669\,171\,001}
\end{aligned}$$

---

## 6. Implementation Architecture & Algorithmic Blueprint

### Algorithmic Execution Pipeline

| Stage | Operation | Code / Formula Action | Complexity |
| :---: | :--- | :--- | :---: |
| **Stage 1** | **Shell Count Mapping** | $m = (\text{size} - 1) // 2 = 500$ | $\mathcal{O}(1)$ |
| **Stage 2** | **Cubic Polynomial** | `(16*m**3 + 30*m**2 + 26*m + 3) // 3` | $\mathcal{O}(1)$ |
| **Stage 3** | **Return Total** | Return scalar integer $669171001$ | $\mathcal{O}(1)$ |

---

## 7. Mathematical Complexity & Edge Case Invariants

| Dimension | Complexity | Performance / Resource Bounds |
| :--- | :--- | :--- |
| **Time Complexity** | $\mathcal{O}(1)$ | $\approx 0.00001$ seconds |
| **Space Complexity** | $\mathcal{O}(1)$ | In-place integer arithmetic |
| **Dynamic Execution** | $100\%$ Inline | Closed-form cubic evaluation |

### Critical Invariants & Edge Cases Handled:
1. **Exact Integer Division**: The polynomial $16m^3 + 30m^2 + 26m + 3$ is always divisible by 3 for all integer $m$.
2. **Boundary $N=1$ ($m=0$)**: For $N=1$, formula gives $3 // 3 = 1$, matching the center single cell.
