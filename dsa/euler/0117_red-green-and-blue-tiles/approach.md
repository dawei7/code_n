# Red, Green, and Blue Tiles - Optimal Approach

## 1. Problem Essence & Formal Mathematical Formulation

Using a combination of grey square tiles (length $1$) and oblong tiles chosen from:
- **Red tiles:** length $2$
- **Green tiles:** length $3$
- **Blue tiles:** length $4$

It is possible to tile a row measuring five ($5$) units in length in exactly fifteen ($15$) different ways.
Unlike Problem 116, colors MAY be freely mixed within the same row!

The objective is to find **how many different ways a row measuring fifty ($50$) units in length can be tiled**:

$$
N_{\text{ways}} = a_{50}
$$

---

## 2. The Naive Approach & Fundamental Bottlenecks

### 4-Way Branching Recursion Tree
A naive approach recursively branches on each of the 4 tile choices:
```python
def naive_mixed_tiles(n):
    # Explores 4^50 ≈ 1.26 x 10^30 states
    # ...
```

### 4th-Order Linear Dynamic Programming Recurrence
1. Let $a_i$ be the total number of ways to tile a row of length $i$.
2. The last tile ending at position $i$ can be:
   - Grey tile (length 1): contributes $a_{i-1}$ ways.
   - Red tile (length 2): contributes $a_{i-2}$ ways (if $i \ge 2$).
   - Green tile (length 3): contributes $a_{i-3}$ ways (if $i \ge 3$).
   - Blue tile (length 4): contributes $a_{i-4}$ ways (if $i \ge 4$).
3. **4th-Order Linear Recurrence (Tetranacci-like):**

$$
a_i = a_{i-1} + a_{i-2} + a_{i-3} + a_{i-4} \quad \text{for } i \ge 4
$$

   with base cases $a_0 = 1, a_1 = 1, a_2 = 2, a_3 = 4$.
4. For $n = 50$, the DP table evaluates in $\mathcal{O}(n)$ time ($\approx 0.0000$ seconds).

---

## 3. Core Intuition & Mathematical Structure

### Step-by-Step DP Values for $n = 0 \dots 5$

| Length $i$ | Grey Tile ($1$) | Red Tile ($2$) | Green Tile ($3$) | Blue Tile ($4$) | Total Ways $a_i$ |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **$0$** | — | — | — | — | **$1$ (Base)** |
| **$1$** | $a_0 = 1$ | — | — | — | **$1$** |
| **$2$** | $a_1 = 1$ | $a_0 = 1$ | — | — | **$2$** |
| **$3$** | $a_2 = 2$ | $a_1 = 1$ | $a_0 = 1$ | — | **$4$** |
| **$4$** | $a_3 = 4$ | $a_2 = 2$ | $a_1 = 1$ | $a_0 = 1$ | **$8$** |
| **$5$** | $a_4 = 8$ | $a_3 = 4$ | $a_2 = 2$ | $a_1 = 1$ | **$15$ (Sample)** |

---

## 4. Rigorous Mathematical Breakthrough & Derivations

### Linear Recurrence Pipeline
1. Allocate array `dp = [0] * (n + 1)` with `dp[0] = 1`.
2. For $i = 1 \dots 50$:

$$
a_i = a_{i-1} + \mathbb{I}(i \ge 2)a_{i-2} + \mathbb{I}(i \ge 3)a_{i-3} + \mathbb{I}(i \ge 4)a_{i-4}
$$

3. Return `dp[50]`.

---

## 5. Concrete Step-by-Step Example Walkthrough

### Example 1: Trace for $n = 5$
- $a_0 = 1, a_1 = 1, a_2 = 2, a_3 = 4, a_4 = 8$.
- At $i = 5$:

$$
a_5 = a_4 + a_3 + a_2 + a_1 = 8 + 4 + 2 + 1 = \mathbf{15}
$$

- Matches problem statement sample! $\checkmark$

### Example 2: Target Evaluation for $n = 50$
- Advancing DP to $i = 50$:

$$
a_{50} = \mathbf{100\,808\,458\,816\,927}
$$

---

## 6. Implementation Architecture & Algorithmic Blueprint

### Algorithmic Execution Pipeline

| Stage | Operation | Code / Formula Action | Complexity |
| :---: | :--- | :--- | :---: |
| **Stage 1** | **DP Init** | `dp = [0] * (n + 1); dp[0] = 1` | $\mathcal{O}(n)$ |
| **Stage 2** | **Recurrence Loop** | For $i \in [1, 50]$ | $50$ steps |
| **Stage 3** | **4-Way Sum** | `dp[i] = dp[i-1] + dp[i-2] + dp[i-3] + dp[i-4]` | $\mathcal{O}(1)$ |
| **Stage 4** | **Return Value** | Return scalar integer $100808458816927$ | $\mathcal{O}(1)$ |

---

## 7. Mathematical Complexity & Edge Case Invariants

| Dimension | Complexity | Performance / Resource Bounds |
| :--- | :--- | :--- |
| **Time Complexity** | $\mathcal{O}(n)$ where $n = 50$ | $\approx 0.0000$ seconds ($200$ additions) |
| **Space Complexity** | $\mathcal{O}(n)$ | Array of $51$ integer values $\approx 1$ KB |
| **Dynamic Execution** | $100\%$ Inline | 4th-order linear dynamic programming recurrence |

### Critical Invariants & Edge Cases Handled:
1. **Base Case $a_0 = 1$**: Representing the empty tiling of length $0$ as $1$ way ensures that a tile covering the entire prefix correctly adds $1$.
2. **Boundary Guards**: Checking $i \ge 2, 3, 4$ prevents negative index access for small $i$.