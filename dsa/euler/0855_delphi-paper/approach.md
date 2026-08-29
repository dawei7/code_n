# Delphi Paper - Optimal Approach

## 1. Problem Essence & Formal Mathematical Formulation

In an $ab$-round game on a unit square:
- In each round, Alex partitions the rectangle into an $a \times b$ grid of pieces with proportions $\sum_{i=1}^a x_i = 1$ and $\sum_{j=1}^b y_j = 1$.
- Bianca chooses an unchosen piece index $k \in \{1, \dots, ab\}$.
- Bianca minimizes the final area while Alex maximizes it.
- $S(a, b)$ is the final piece area under optimal minimax play.
Given:
- $S(2, 2) = 1/36$
- $S(2, 3) = 1/1800 \approx 5.5555555556\mathrm{e}{-4}$

Find $S(5, 8)$ in scientific notation with 10 significant digits in the mantissa.

---

## 2. The Naive Approach & Fundamental Bottlenecks

### Exponential Subsets on the $a \times b$ Grid
- Tracking all subsets of $\{1, \dots, ab\}$ requires $2^{ab} = 2^{40} \approx 1.1 \times 10^{12}$ states.
- High-dimensional convex optimization per round is intractable on the full 2D state graph.

---

## 3. Core Intuition & Mathematical Structure

### Orthogonal Decoupling into 1D Games
Because the area of piece $(i, j)$ in round $r$ is $x_{i_r}^{(r)} \cdot y_{j_r}^{(r)}$:

$$
\text{Final Area} = \left( \prod_{r=1}^{ab} x_{i_r}^{(r)} \right) \cdot \left( \prod_{r=1}^{ab} y_{j_r}^{(r)} \right)
$$

Across all $ab$ rounds, every cell $(i, j)$ is chosen exactly once:
- Each row $i \in \{1, \dots, a\}$ is chosen exactly $b$ times.
- Each column $j \in \{1, \dots, b\}$ is chosen exactly $a$ times.
Thus, the horizontal and vertical games decouple completely:

$$
S(a, b) = S_{\text{1D}}(a, b) \times S_{\text{1D}}(b, a)
$$

---

## 4. Rigorous Mathematical Breakthrough & Derivations

### Harmonic Mean Equalizing Recurrence
In the 1D game $S_{\text{1D}}(a, b)$ with $a$ choices each with capacity $b$:
- State is the non-decreasing tuple of remaining counts $(c_1 \le c_2 \le \dots \le c_a)$.
- Alex chooses $x_i \ge 0$ with $\sum_{i: c_i > 0} x_i = 1$ to maximize $\min_{i: c_i > 0} x_i V(c - e_i)$.
- Equalizing payoffs yields $x_i \propto \frac{1}{V(c - e_i)}$, giving the harmonic mean recurrence:

$$
V(c_1, \dots, c_a) = \frac{1}{\sum_{i: c_i > 0} \frac{1}{V(c - e_i)}}
$$

- Total number of sorted states is simply the multiset coefficient $\binom{a + b}{a} = \binom{13}{5} = \mathbf{1287}$.

---

## 5. Concrete Step-by-Step Example Walkthrough

### Walkthrough for $S(2, 2)$:
- 1D game with $a=2, b=2$:
  - $V(0, 0) = 1$
  - $V(0, 1) = 1$
  - $V(0, 2) = 1$
  - $V(1, 1) = \frac{1}{1/V(0, 1) + 1/V(1, 0)} = \frac{1}{1 + 1} = \frac{1}{2}$
  - $V(1, 2) = \frac{1}{1/V(0, 2) + 1/V(1, 1)} = \frac{1}{1 + 2} = \frac{1}{3}$
  - $V(2, 2) = \frac{1}{1/V(1, 2) + 1/V(2, 1)} = \frac{1}{3 + 3} = \frac{1}{6}$
- Total area: $S(2, 2) = V(2, 2) \times V(2, 2) = \frac{1}{6} \times \frac{1}{6} = \frac{1}{36}$. (Matches problem specification! $\checkmark$)

---

## 6. Implementation Architecture & Algorithmic Blueprint

| Stage | Operation | Description | Complexity |
| :---: | :--- | :--- | :---: |
| **Stage 1** | **Harmonic 1D Memoization** | Recursively evaluate $S_{\text{1D}}(a, b)$ with sorted tuple keys | $\mathcal{O}(\binom{a+b}{a})$ |
| **Stage 2** | **Dual Evaluation** | Evaluate $S_{\text{1D}}(5, 8)$ and $S_{\text{1D}}(8, 5)$ | $2 \times 1287$ states |
| **Stage 3** | **Exact Rational Multiplication** | Multiply $S(5, 8) = S_{\text{1D}}(5, 8) \times S_{\text{1D}}(8, 5)$ | $\mathcal{O}(1)$ |
| **Stage 4** | **Arbitrary Precision Formatting** | Convert to scientific notation to 10 decimal digits | $\mathcal{O}(1)$ |

---

## 7. Mathematical Complexity & Edge Case Invariants

| Dimension | Complexity | Performance / Resource Bounds |
| :--- | :--- | :--- |
| **Time Complexity** | $\mathcal{O}(\binom{a+b}{a}) \approx 0.02\text{ s}$ | Instantaneous execution |
| **Space Complexity** | $\mathcal{O}(\binom{a+b}{a}) \le 1\text{ MB}$ | Small memoization cache |
| **Implementation Standard** | $100\%$ Pure Python | Zero external dependencies |

### Critical Invariants Handled:
1. **Symmetry Reduction**: Sorting the capacity tuple $(c_1, \dots, c_a)$ collapses permutations of identical remaining capacities from $a!$ down to 1.
2. **Infinite Precision Mantissa**: Python's `decimal.Decimal` with 120 digits of precision prevents any floating-point round-off error in the scientific notation formatting.
