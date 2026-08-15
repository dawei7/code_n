# Ordered Fractions - Optimal Approach

## 1. Problem Essence & Formal Mathematical Formulation

Consider the set of all reduced proper fractions $\frac{n}{d}$ where $n < d \le 1\,000\,000$ and $\gcd(n, d) = 1$, ordered by increasing size (the Farey sequence $\mathcal{F}_{1000000}$).

For $d \le 8$, listing the fractions in order:
$$\frac{1}{8}, \frac{1}{7}, \frac{1}{6}, \frac{1}{5}, \frac{1}{4}, \frac{2}{7}, \frac{1}{3}, \frac{3}{8}, \frac{2}{5}, \mathbf{\frac{3}{7}}, \frac{1}{2}, \frac{4}{7}, \frac{3}{5}, \frac{5}{8}, \frac{2}{3}, \frac{5}{7}, \frac{3}{4}, \frac{4}{5}, \frac{5}{6}, \frac{6}{7}, \frac{7}{8}$$
The fraction immediately to the left of $\frac{3}{7}$ is $\frac{2}{5}$ (numerator is $2$).

The objective is to find the numerator of the fraction immediately to the left of $\frac{3}{7}$ for all denominators $d \le 1\,000\,000$:
$$n^* = \operatorname{num}\left( \max \left\{ \frac{n}{d} \in \mathbb{Q} \;\middle|\; 1 \le n < d \le 10^6, \, \gcd(n, d) = 1, \, \frac{n}{d} < \frac{3}{7} \right\} \right)$$

---

## 2. The Naive Approach & Fundamental Bottlenecks

### Full Farey Sequence Generation & Sorting
A naive approach generates all $\sum_{d=1}^{10^6} \phi(d) \approx \frac{3}{\pi^2} 10^{12} \approx 3 \times 10^{11}$ fractions and sorts them:
```python
def naive_ordered_fractions():
    # Attempting to sort 300 billion fractions requires terabytes of RAM!
    # ...
```

### The Mediant & Farey Neighbor Theorem
1. In any Farey sequence, if $\frac{a}{b} < \frac{c}{d}$ are consecutive adjacent neighbors, they satisfy the cross-multiplication determinant equation:
   $$b c - a d = 1$$
2. For $\frac{c}{d} = \frac{3}{7}$:
   $$3b - 7a = 1 \implies 3b \equiv 1 \pmod 7 \implies b \equiv 5 \pmod 7$$
3. To make $\frac{a}{b}$ as close to $\frac{3}{7}$ as possible, we choose the maximum possible denominator $b \le 1\,000\,000$ satisfying $b \equiv 5 \pmod 7$:
   $$d^* = 999\,997$$
4. The numerator is:
   $$n^* = \frac{3 d^* - 1}{7} = \frac{3(999997) - 1}{7} = \mathbf{428\,570}$$

---

## 3. Core Intuition & Mathematical Structure

### Farey Neighbor Approximations to $\frac{3}{7}$

| Bound $N$ | Maximum $d \le N$ with $d \equiv 5 \pmod 7$ | Best Numerator $n = \frac{3d - 1}{7}$ | Closest Fraction $\frac{n}{d}$ | Difference to $\frac{3}{7}$ ($\frac{1}{7d}$) |
| :---: | :---: | :---: | :---: | :---: |
| **$N = 8$** | $d = 5$ | $n = \frac{15 - 1}{7} = \mathbf{2}$ | $\mathbf{\frac{2}{5}}$ | $\frac{1}{35} \approx 0.02857$ (Sample) |
| **$N = 20$** | $d = 19$ | $n = \frac{57 - 1}{7} = 8$ | $\frac{8}{19}$ | $\frac{1}{133} \approx 0.00752$ |
| **$N = 100$** | $d = 96$ | $n = \frac{288 - 1}{7} = 41$ | $\frac{41}{96}$ | $\frac{1}{672} \approx 0.00148$ |
| **$N = 10^6$** | $\mathbf{d = 999\,997}$ | $\mathbf{n = 428\,570}$ | $\mathbf{\frac{428\,570}{999\,997}}$ | $\mathbf{\frac{1}{6\,999\,979}} \approx 1.4 \times 10^{-7}$ |

---

## 4. Rigorous Mathematical Breakthrough & Derivations

### $\mathcal{O}(1)$ Closed-Form Derivation
1. For any denominator $d$, the strictly largest numerator $n$ satisfying $\frac{n}{d} < \frac{3}{7}$ is:
   $$n(d) = \left\lfloor \frac{3d - 1}{7} \right\rfloor$$
2. The difference to $\frac{3}{7}$ is:
   $$\frac{3}{7} - \frac{n(d)}{d} = \frac{3d - 7 n(d)}{7d} = \frac{(3d \bmod 7)}{7d}$$
3. This difference is minimized when $(3d \bmod 7) = 1$ (i.e. $d \equiv 5 \pmod 7$) and $d$ is maximized ($d = 999\,997$).
4. Cross-multiplication confirms:
   $$3(999997) - 7(428570) = 2\,999\,991 - 2\,999\,990 = 1$$
5. Thus, $\gcd(428570, 999997) = 1$ automatically!

---

## 5. Concrete Step-by-Step Example Walkthrough

### Example 1: Trace for $d \le 8$
- $d = 5 \equiv 5 \pmod 7$.
- $n = \frac{3(5) - 1}{7} = \frac{14}{7} = \mathbf{2}$.
- Preceding fraction: $\frac{2}{5}$, numerator is $\mathbf{2}$. Matches problem statement sample! $\checkmark$

### Example 2: Target Evaluation for $d \le 1\,000\,000$
- $1\,000\,000 \bmod 7 = 1$.
- To get residue $5 \pmod 7$: subtract $3 \implies d^* = 999\,997$.
- Numerator:
  $$n^* = \frac{3(999997) - 1}{7} = \frac{2999990}{7} = \mathbf{428\,570}$$

---

## 6. Implementation Architecture & Algorithmic Blueprint

### Algorithmic Execution Pipeline

| Stage | Operation | Code / Formula Action | Complexity |
| :---: | :--- | :--- | :---: |
| **Stage 1** | **Scan Range** | For $d \in [1000000, 999993]$ step $-1$ | $7$ steps |
| **Stage 2** | **Numerator Upper Bound** | $n = (3 \cdot d - 1) // 7$ | $\mathcal{O}(1)$ |
| **Stage 3** | **Cross-Multiplication** | If $n \cdot d_{\text{best}} > n_{\text{best}} \cdot d$: update $(n_{\text{best}}, d_{\text{best}})$ | $\mathcal{O}(1)$ |
| **Stage 4** | **Return Value** | Return scalar integer $428570$ | $\mathcal{O}(1)$ |

---

## 7. Mathematical Complexity & Edge Case Invariants

| Dimension | Complexity | Performance / Resource Bounds |
| :--- | :--- | :--- |
| **Time Complexity** | $\mathcal{O}(1)$ | $\approx 0.0000$ seconds |
| **Space Complexity** | $\mathcal{O}(1)$ | Scalar integer registers |
| **Dynamic Execution** | $100\%$ Inline | Farey neighbor cross-multiplication comparison |

### Critical Invariants & Edge Cases Handled:
1. **Coprimality Invariant**: Because $3(999997) - 7(428570) = 1$, Bézout's identity guarantees $\gcd(428570, 999997) = 1$ without computing GCD.
2. **Strict Inequality**: Formula $(3d - 1) // 7$ strictly ensures $\frac{n}{d} < \frac{3}{7}$, avoiding $\frac{3}{7}$ itself when $7 \mid d$.
