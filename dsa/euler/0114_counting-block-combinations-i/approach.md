# Counting Block Combinations I - Optimal Approach

## 1. Problem Essence & Formal Mathematical Formulation

A row measuring seven units in length has red blocks with a minimum length of three units placed on it, such that any two red blocks (which are allowed to be different lengths) are separated by at least one grey square. There are exactly seventeen ($17$) ways of doing this:
- $1$ way with no red blocks (all grey squares).
- $15$ ways with one red block (lengths $3, 4, 5, 6, 7$ in various positions).
- $1$ way with two red blocks ($3$ red, $1$ grey, $3$ red).
- Total $= 1 + 15 + 1 = 17$.

Let a row of length $n = 50$ be filled with grey unit squares and red blocks with minimum length $m = 3$, with at least one grey square between adjacent red blocks.

The objective is to find **how many ways the row of length $50$ can be filled**:

$$
N_{\text{ways}} = a_{50}
$$

---

## 2. The Naive Approach & Fundamental Bottlenecks

### Full Binary Coloring Tree
A naive approach tests all binary colorings (grey/red) of length $50$:
```python
def naive_block_combinations():
    # 2^50 ≈ 1.12 x 10^15 configurations is computationally infeasible
    # ...
```

### 1D Dynamic Programming Recurrence
1. Let $a_i$ be the total number of valid block configurations for a row of length $i$.
2. **Transition Rules for cell $i$:**
   - **Cell $i$ is grey:** Inherits all $a_{i-1}$ configurations.
   - **Cell $i$ is the end of a red block of length $\ell \in [m, i]$:**
     - The red block occupies cells $[i - \ell + 1 \dots i]$.
     - If $i - \ell - 1 \ge 0$, cell $i - \ell$ must be grey, leaving $a_{i - \ell - 1}$ configurations for the preceding prefix.
     - If $i - \ell - 1 < 0$ (the block starts at the very beginning of the row), it contributes $1$ configuration.
3. **Combined Recurrence:**

$$
a_i = a_{i-1} + \sum_{\ell=m}^i \begin{cases} a_{i - \ell - 1} & \text{if } i - \ell - 1 \ge 0 \\ 1 & \text{otherwise} \end{cases}
$$

4. For $n = 50$, the DP table fills in $\mathcal{O}(n^2)$ operations in $\approx 0.0001$ seconds.

---

## 3. Core Intuition & Mathematical Structure

### DP Table Step-by-Step Values for $n = 0 \dots 7$ ($m = 3$)

| Row Length $i$ | Grey End $a_{i-1}$ | Red End Contributions $\sum a_{i-\ell-1}$ | Total Combinations $a_i$ |
| :---: | :---: | :--- | :---: |
| **$0$** | — | Base Case | **$1$** |
| **$1$** | $1$ | None ($\ell \ge 3 > 1$) | **$1$** |
| **$2$** | $1$ | None ($\ell \ge 3 > 2$) | **$1$** |
| **$3$** | $1$ | $\ell=3 \implies +1$ | **$2$** |
| **$4$** | $2$ | $\ell=3 \implies +1, \, \ell=4 \implies +1$ | **$4$** |
| **$5$** | $4$ | $\ell=3 \implies a_1=1, \, \ell=4 \implies +1, \, \ell=5 \implies +1$ | **$7$** |
| **$6$** | $7$ | $\ell=3 \implies a_2=1, \, \ell=4 \implies a_1=1, \, \ell=5 \implies +1, \, \ell=6 \implies +1$ | **$11$** |
| **$7$** | $11$ | $\ell=3 \implies a_3=2, \, \ell=4 \implies a_2=1, \, \ell=5 \implies a_1=1, \, \ell=6 \implies +1, \, \ell=7 \implies +1$ | **$17$ (Sample)** |

---

## 4. Rigorous Mathematical Breakthrough & Derivations

### Linear Recurrence Execution Pipeline
1. Allocate array `dp = [0] * (n + 1)` with `dp[0] = 1`.
2. For $i = 1 \dots 50$:
   - `dp[i] = dp[i-1]`
   - For $\ell \in [3, i]$:
     - If $i - \ell - 1 \ge 0$: `dp[i] += dp[i - \ell - 1]`
     - Else: `dp[i] += 1`
3. Return `dp[50]`.

---

## 5. Concrete Step-by-Step Example Walkthrough

### Example 1: Trace for $n = 7, m = 3$
- $a_0 = 1, a_1 = 1, a_2 = 1, a_3 = 2, a_4 = 4, a_5 = 7, a_6 = 11$.
- At $i = 7$:
  - Grey end: $a_6 = 11$.
  - Red ends: $\ell=3 \implies a_3=2$, $\ell=4 \implies a_2=1$, $\ell=5 \implies a_1=1$, $\ell=6 \implies 1$, $\ell=7 \implies 1$.
  - Red sum: $2 + 1 + 1 + 1 + 1 = 6$.
  - Total $a_7 = 11 + 6 = \mathbf{17}$. Matches problem statement sample! $\checkmark$

### Example 2: Target Evaluation for $n = 50$
- Advancing DP to $i = 50$:

$$
a_{50} = \mathbf{16\,475\,640\,049}
$$

---

## 6. Implementation Architecture & Algorithmic Blueprint

### Algorithmic Execution Pipeline

| Stage | Operation | Code / Formula Action | Complexity |
| :---: | :--- | :--- | :---: |
| **Stage 1** | **DP Init** | `dp = [0] * (n + 1); dp[0] = 1` | $\mathcal{O}(n)$ |
| **Stage 2** | **Length Loop $i$** | For $i \in [1, 50]$ | $50$ steps |
| **Stage 3** | **Grey Propagation** | `dp[i] = dp[i-1]` | $\mathcal{O}(1)$ |
| **Stage 4** | **Red Block Inner** | For $\ell \in [3, i]$: add prefix configurations | $\mathcal{O}(i)$ |
| **Stage 5** | **Return Value** | Return `dp[50] = 16475640049` | $\mathcal{O}(1)$ |

---

## 7. Mathematical Complexity & Edge Case Invariants

| Dimension | Complexity | Performance / Resource Bounds |
| :--- | :--- | :--- |
| **Time Complexity** | $\mathcal{O}(n^2)$ where $n = 50$ | $\approx 0.0001$ seconds ($1275$ additions) |
| **Space Complexity** | $\mathcal{O}(n)$ | Array of $51$ integer values $\approx 1$ KB |
| **Dynamic Execution** | $100\%$ Inline | 1D dynamic programming recurrence |

### Critical Invariants & Edge Cases Handled:
1. **Mandatory Grey Separator**: Slicing at index `i - length - 1` naturally enforces that two red blocks can never touch directly.
2. **Arbitrary Red Lengths**: Summing $\ell$ from $m$ up to $i$ allows red blocks to take any length $\ge 3$.