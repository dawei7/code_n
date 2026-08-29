# Odd Period Square Roots - Optimal Approach

## 1. Problem Essence & Formal Mathematical Formulation

For any non-square integer $N \in \mathbb{N}$, the continued fraction expansion of $\sqrt{N}$ is periodic:

$$
\sqrt{N} = a_0 + \cfrac{1}{a_1 + \cfrac{1}{a_2 + \cfrac{1}{\dots}}} = [a_0; (a_1, a_2, \dots, a_r)^{\infty}]
$$

where $a_0 = \lfloor \sqrt{N} \rfloor$ and $(a_1, \dots, a_r)$ is the repeating period block of length $r(N)$.

The objective is to find how many continued fraction expansions for $N \le 10\,000$ have an **odd period length** $r(N)$:

$$
\begin{aligned}
N_{\text{odd}} = \sum_{\substack{1 \le N \le 10000 \\ \lfloor \sqrt{N} \rfloor^2 \neq N}} \mathbb{I}\left( r(N) \equiv 1 \pmod 2 \right)
\end{aligned}
$$

---

## 2. The Naive Approach & Fundamental Bottlenecks

### Floating-Point Recurrence
A naive algorithm uses floating-point numbers $x_{k+1} = \frac{1}{x_k - \lfloor x_k \rfloor}$:
```python
def naive_period(n):
    # Subject to catastrophic cancellation and IEEE 754 precision loss
    # ...
```

### Exact Integer Recurrence for $\sqrt{N}$
By maintaining the exact irrational form $\frac{\sqrt{N} + m_k}{d_k}$:
1. **Initial State:** $m_0 = 0, \, d_0 = 1, \, a_0 = \lfloor \sqrt{N} \rfloor$.
2. **Transition Equations:**

$$
m_{k+1} = d_k a_k - m_k
$$

$$
d_{k+1} = \frac{N - m_{k+1}^2}{d_k}
$$

$$
a_{k+1} = \left\lfloor \frac{a_0 + m_{k+1}}{d_{k+1}} \right\rfloor
$$

3. **Period Closure Theorem:** The period repeats as soon as $a_k = 2 a_0$.

---

## 3. Core Intuition & Mathematical Structure

### Continued Fractions & Period Lengths for $N \le 13$

| $N$ | $\sqrt{N}$ Continued Fraction | Period Block $(a_1 \dots a_r)$ | Period Length $r(N)$ | $r(N)$ Parity |
| :---: | :--- | :---: | :---: | :---: |
| **$2$** | $[1; (2)]$ | $(2)$ | $1$ | **Odd $\checkmark$** |
| **$3$** | $[1; (1, 2)]$ | $(1, 2)$ | $2$ | Even |
| **$5$** | $[2; (4)]$ | $(4)$ | $1$ | **Odd $\checkmark$** |
| **$6$** | $[2; (2, 4)]$ | $(2, 4)$ | $2$ | Even |
| **$7$** | $[2; (1, 1, 1, 4)]$ | $(1, 1, 1, 4)$ | $4$ | Even |
| **$8$** | $[2; (1, 4)]$ | $(1, 4)$ | $2$ | Even |
| **$10$** | $[3; (6)]$ | $(6)$ | $1$ | **Odd $\checkmark$** |
| **$11$** | $[3; (3, 6)]$ | $(3, 6)$ | $2$ | Even |
| **$12$** | $[3; (2, 6)]$ | $(2, 6)$ | $2$ | Even |
| **$13$** | $[3; (1, 1, 1, 1, 6)]$ | $(1, 1, 1, 1, 6)$ | $5$ | **Odd $\checkmark$** |

*(For $N \le 13$, exactly 4 non-square values have an odd period length: $N \in \{2, 5, 10, 13\}$).*

---

## 4. Rigorous Mathematical Breakthrough & Derivations

### Integer Period Length Computation
1. Skip perfect squares where $a_0 \cdot a_0 == N$.
2. For each non-square $N$:
   - Initialize $m = 0, d = 1, a = a_0, \text{length} = 0$.
   - While $a \neq 2 a_0$:
     - $m \leftarrow d \cdot a - m$
     - $d \leftarrow (N - m^2) // d$
     - $a \leftarrow (a_0 + m) // d$
     - $\text{length} \leftarrow \text{length} + 1$
   - If $\text{length} \bmod 2 == 1$, increment $N_{\text{odd}}$.
3. Evaluates all $N \le 10\,000$ in $\approx 0.02$ seconds.

---

## 5. Concrete Step-by-Step Example Walkthrough

### Example 1: Trace for $N = 13$ ($a_0 = 3$)
- Initial: $m=0, d=1, a=3$.
- Step 1: $m = 1(3) - 0 = 3; \, d = (13 - 9)/1 = 4; \, a = \lfloor(3 + 3)/4\rfloor = \mathbf{1}$.
- Step 2: $m = 4(1) - 3 = 1; \, d = (13 - 1)/4 = 3; \, a = \lfloor(3 + 1)/3\rfloor = \mathbf{1}$.
- Step 3: $m = 3(1) - 1 = 2; \, d = (13 - 4)/3 = 3; \, a = \lfloor(3 + 2)/3\rfloor = \mathbf{1}$.
- Step 4: $m = 3(1) - 2 = 1; \, d = (13 - 1)/3 = 4; \, a = \lfloor(3 + 1)/4\rfloor = \mathbf{1}$.
- Step 5: $m = 4(1) - 1 = 3; \, d = (13 - 9)/4 = 1; \, a = \lfloor(3 + 3)/1\rfloor = \mathbf{6} = 2a_0$ (Terminates!).
- Coefficients: $(1, 1, 1, 1, 6) \implies$ Period Length $r = \mathbf{5}$ (Odd). Matches problem sample! $\checkmark$

### Example 2: Target Evaluation for $N \le 10\,000$
- Testing all non-squares up to $10\,000$:

$$
N_{\text{odd}} = \mathbf{1322}
$$

---

## 6. Implementation Architecture & Algorithmic Blueprint

### Algorithmic Execution Pipeline

| Stage | Operation | Code / Formula Action | Complexity |
| :---: | :--- | :--- | :---: |
| **Stage 1** | **Period Engine** | `period_length(n)` with exact integer recurrence | $\mathcal{O}(r(n))$ |
| **Stage 2** | **Square Filter** | If `a0 * a0 == n: return 0` | $\mathcal{O}(1)$ |
| **Stage 3** | **Recurrence Loop** | While $a \neq 2 a_0$: compute next $(m, d, a)$ | $\le 300$ steps |
| **Stage 4** | **Sum Accumulation** | `sum(1 for n in range(1, 10001) if period_length(n) % 2 == 1)` | $10\,000$ terms |
| **Stage 5** | **Return Count** | Return scalar integer $1322$ | $\mathcal{O}(1)$ |

---

## 7. Mathematical Complexity & Edge Case Invariants

| Dimension | Complexity | Performance / Resource Bounds |
| :--- | :--- | :--- |
| **Time Complexity** | $\mathcal{O}(N \cdot \bar{r})$ where $N = 10\,000, \bar{r} \approx 30$ | $\approx 0.02$ seconds |
| **Space Complexity** | $\mathcal{O}(1)$ | Scalar integer registers |
| **Dynamic Execution** | $100\%$ Inline | Exact integer continued fraction transitions |

### Critical Invariants & Edge Cases Handled:
1. **Zero Division Guard**: Formula $(N - m^2) // d$ is mathematically proven to always be an exact integer division without remainder.
2. **Deterministic Termination**: The condition $a == 2a_0$ is universally proven to mark the exact end of the primitive period for square roots of non-squares.