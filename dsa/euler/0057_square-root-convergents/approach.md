# Square Root Convergents - Optimal Approach

## 1. Problem Essence & Formal Mathematical Formulation

The square root of 2 can be expanded as an infinite continued fraction:
$$\sqrt{2} = 1 + \cfrac{1}{2 + \cfrac{1}{2 + \cfrac{1}{2 + \dots}}}$$

Let $\frac{n_k}{d_k}$ denote the $k$-th convergent fraction approximation of $\sqrt{2}$.

The first few expansions are:
- $k=1: 1 + \frac{1}{2} = \frac{3}{2} = 1.5$
- $k=2: 1 + \frac{1}{2 + 1/2} = \frac{7}{5} = 1.4$
- $k=3: 1 + \frac{1}{2 + 1/(2 + 1/2)} = \frac{17}{12} = 1.41666\dots$
- $k=4: \frac{41}{29} = 1.41379\dots$
- $k=8: \frac{1393}{985}$ (where $n_8$ has 4 digits and $d_8$ has 3 digits)

The objective is to find how many of the first $1000$ expansions have a numerator with strictly more decimal digits than the denominator:
$$N = \sum_{k=1}^{1000} \mathbb{I}\left( \text{length}(\operatorname{str}(n_k)) > \text{length}(\operatorname{str}(d_k)) \right)$$

---

## 2. The Naive Approach & Fundamental Bottlenecks

### Recursive Fraction Parsing
A naive approach re-evaluates the continued fraction recursively from scratch using rational fraction objects:
```python
def naive_sqrt2_convergents():
    # performs recursive rational fraction arithmetic
    # ...
```

### The Linear Matrix Recurrence
Using the continued fraction relation $\sqrt{2} + 1 = 2 + \frac{1}{\sqrt{2} + 1}$:
$$\frac{n_{k+1}}{d_{k+1}} = 1 + \frac{1}{1 + \frac{n_k}{d_k}} = 1 + \frac{d_k}{n_k + d_k} = \frac{n_k + 2d_k}{n_k + d_k}$$

The numerators and denominators evolve via the exact linear recurrence:
$$\begin{pmatrix} n_{k+1} \\ d_{k+1} \end{pmatrix} = \begin{pmatrix} 1 & 2 \\ 1 & 1 \end{pmatrix} \begin{pmatrix} n_k \\ d_k \end{pmatrix}$$
with initial state $n_1 = 3, d_1 = 2$.

---

## 3. Core Intuition & Mathematical Structure

### Early Convergents of $\sqrt{2}$

| Index $k$ | Convergent Fraction $\frac{n_k}{d_k}$ | Decimal Approx | Digits in $n_k$ | Digits in $d_k$ | $L(n_k) > L(d_k)$? |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **$1$** | $\frac{3}{2}$ | $1.5$ | $1$ | $1$ | No |
| **$2$** | $\frac{7}{5}$ | $1.4$ | $1$ | $1$ | No |
| **$3$** | $\frac{17}{12}$ | $1.4166\dots$ | $2$ | $2$ | No |
| **$4$** | $\frac{41}{29}$ | $1.4137\dots$ | $2$ | $2$ | No |
| **$5$** | $\frac{99}{70}$ | $1.4142\dots$ | $2$ | $2$ | No |
| **$6$** | $\frac{239}{169}$ | $1.4142\dots$ | $3$ | $3$ | No |
| **$7$** | $\frac{577}{408}$ | $1.4142\dots$ | $3$ | $3$ | No |
| **$8$** | $\mathbf{\frac{1393}{985}}$ | $1.4142\dots$ | **$4$** | **$3$** | **Yes ($\mathbf{4 > 3}$)** |

---

## 4. Rigorous Mathematical Breakthrough & Derivations

### Coprimality & Linear Transitions
1. The transition matrix $\mathbf{M} = \begin{pmatrix} 1 & 2 \\ 1 & 1 \end{pmatrix}$ has $\det(\mathbf{M}) = -1$.
2. Therefore, $\gcd(n_k, d_k) = 1$ for all $k \ge 1$, so the fractions are naturally always in lowest reduced terms without needing GCD simplifications.
3. Iterating $n, d \leftarrow n + 2d, n + d$ computes all 1000 terms in $\approx 0.002$ seconds.

---

## 5. Concrete Step-by-Step Example Walkthrough

### Example 1: Trace for Expansion $k = 8$
- $n_7 = 577, d_7 = 408$.
- $n_8 = 577 + 2(408) = 577 + 816 = \mathbf{1393}$ ($4$ digits).
- $d_8 = 577 + 408 = \mathbf{985}$ ($3$ digits).
- $4 > 3 \implies$ 1st convergent with more digits in numerator! Matches problem statement sample! $\checkmark$

### Example 2: Target Evaluation for $1 \le k \le 1000$
- Iterating the recurrence for 1000 expansions:
  $$N = \mathbf{153}$$

---

## 6. Implementation Architecture & Algorithmic Blueprint

### Algorithmic Execution Pipeline

| Stage | Operation | Code / Formula Action | Complexity |
| :---: | :--- | :--- | :---: |
| **Stage 1** | **State Init** | `n, d = 3, 2; count = 0` | $\mathcal{O}(1)$ |
| **Stage 2** | **Expansion Loop** | For step in range(1000) | $1000$ iterations |
| **Stage 3** | **Digit Length Check** | `if len(str(n)) > len(str(d)): count += 1` | $\mathcal{O}(\text{digits})$ |
| **Stage 4** | **Matrix Update** | `n, d = n + 2 * d, n + d` | $\mathcal{O}(1)$ BigInt additions |
| **Stage 5** | **Return Value** | Return scalar integer $153$ | $\mathcal{O}(1)$ |

---

## 7. Mathematical Complexity & Edge Case Invariants

| Dimension | Complexity | Performance / Resource Bounds |
| :--- | :--- | :--- |
| **Time Complexity** | $\mathcal{O}(K \cdot D)$ where $K = 1000, D \le 400$ | $\approx 0.002$ seconds |
| **Space Complexity** | $\mathcal{O}(D)$ | 400-digit BigInt registers $\approx 2$ KB |
| **Dynamic Execution** | $100\%$ Inline | 2D linear recurrence iteration |

### Critical Invariants & Edge Cases Handled:
1. **Coprimality Invariant**: $\det(\mathbf{M}) = -1$ guarantees $\gcd(n_k, d_k) = 1$, eliminating expensive GCD computations.
2. **Exact String Length Measurement**: Evaluates exact decimal digit counts without floating-point logarithm precision issues.
