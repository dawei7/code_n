# Guided Example: Paint House II

We trace the step-by-step $O(N \cdot K)$ state transition optimization, dual-minimum tracking ($\text{min}_1, \text{idx}_1, \text{min}_2$), and color exclusion dispatch on representative $K$-color house painting matrices:

- **Input:** $\text{costs} = [[1, 5, 3], [2, 9, 4]]$
- **Required output:** $5$ (House 0 painted Color 0 (cost $1$); House 1 painted Color 2 (cost $4$) $\implies 1 + 4 = 5$)
- **Two-Color Minimal Instance:** $\text{costs} = [[1, 3], [2, 4]] \implies 5$ (Must alternate colors)
- **Equal Cost Ties:** $\text{costs} = [[2, 2, 2], [3, 3, 3]] \implies 5$ (Identical min1 and min2 values with distinct indices)

This instance demonstrates dynamic programming optimization from $O(N K^2)$ down to strictly optimal $O(N K)$ time, proves why tracking only the two smallest values ($\text{min}_1$ and $\text{min}_2$) of the previous house suffices to determine the cheapest valid transition for all $K$ colors in $O(1)$ time, and operates in $O(1)$ auxiliary space.

---

## 1. Instance & Teaching Goal

Given an $N \times K$ cost matrix for painting $N$ houses with $K$ colors ($N = 2, K = 3$):
$$
\text{costs} = \begin{bmatrix}
1 & 5 & 3 \\
2 & 9 & 4
\end{bmatrix}
$$
Paint all houses such that **no two adjacent houses share the same color**, minimizing total cost.

### The Complexity Bottleneck: $O(N K^2)$ vs $O(N K)$
Let $DP[i][c]$ be the minimum cost to paint houses $0 \dots i$ ending with color $c$.
The standard recurrence is:
$$
DP[i][c] = \text{costs}[i][c] + \min_{j \ne c} DP[i-1][j]
$$
- Finding $\min_{j \ne c}$ naively takes $O(K)$ per cell, totaling $O(N \cdot K^2)$ time. When $K = 1,000$ and $N = 1,000$, $N K^2 = 10^9$ operations, causing Time Limit Exceeded (TLE).
- **The Dual-Minimum Insight:**
  For any row, the minimum value among all $j \ne c$ is either:
  1. The **global minimum** $\text{min}_1$ (if $c \ne \text{idx}_1$).
  2. The **second global minimum** $\text{min}_2$ (if $c == \text{idx}_1$, because picking $\text{idx}_1$ is forbidden by adjacency).
By tracking only $\text{min}_1$, $\text{idx}_1$, and $\text{min}_2$ from row $i - 1$, row $i$ can be computed in strictly $O(1)$ time per color, reducing total complexity to **$O(N \cdot K)$**.

---

## 2. Conceptual Foundation & Invariants

### State Variables for Row $i - 1$
We maintain three scalar quantities summarizing the previous house:
- $\text{min}_1$: The minimum cost to paint houses up to $i - 1$.
- $\text{idx}_1$: The color index that achieved $\text{min}_1$.
- $\text{min}_2$: The second minimum cost to paint houses up to $i - 1$ (achieved at some color $\ne \text{idx}_1$).

### Transition Rule for House $i$, Color $c$
$$
\text{prev\_cost} = \begin{cases}
\text{min}_1, & \text{if } c \ne \text{idx}_1 \\
\text{min}_2, & \text{if } c == \text{idx}_1
\end{cases}
$$
$$
\text{current\_cost}[c] = \text{costs}[i][c] + \text{prev\_cost}
$$

### Rolling Update Protocol
While iterating through colors $c \in [0 \dots K - 1]$ for house $i$, simultaneously find the new $\text{new\_min}_1, \text{new\_idx}_1,$ and $\text{new\_min}_2$ in a single forward pass:
- If $\text{current\_cost}[c] < \text{new\_min}_1$:
  - $\text{new\_min}_2 \leftarrow \text{new\_min}_1$
  - $\text{new\_min}_1 \leftarrow \text{current\_cost}[c]$
  - $\text{new\_idx}_1 \leftarrow c$
- Else if $\text{current\_cost}[c] < \text{new\_min}_2$:
  - $\text{new\_min}_2 \leftarrow \text{current\_cost}[c]$

At the end of all $N$ houses, the answer is $\text{min}_1$.

> **Invariant.** For any color $c$, the cheapest allowable coloring of the preceding house is $\text{min}_1$ whenever $c \ne \text{idx}_1$, and $\text{min}_2$ otherwise. No other predecessor value can ever be strictly better.

---

## 3. Step-by-Step Worked Execution

We trace the algorithm on $\text{costs} = [[1, 5, 3], [2, 9, 4]]$ ($N = 2, K = 3$):

### Step 1: Base Case — House 0 ($\text{costs}[0] = [1, 5, 3]$)
Find the two smallest costs in row 0:
- Color 0: Cost $= 1$.
- Color 1: Cost $= 5$.
- Color 2: Cost $= 3$.

Values:
- Smallest: $\text{min}_1 = 1$, at index $\text{idx}_1 = 0$.
- Second smallest: $\text{min}_2 = 3$, at index $2$.
State after House 0: $(\text{min}_1 = 1, \; \text{idx}_1 = 0, \; \text{min}_2 = 3)$.

---

### Step 2: Transition — House 1 ($\text{costs}[1] = [2, 9, 4]$)
Previous state: $\text{idx}_1 = 0$ (cost $1$), alternative $\text{min}_2 = 3$.

- **Color $c = 0$ (Cost $= 2$):**
  - Check adjacency: $c == \text{idx}_1$ ($0 == 0$).
  - Conflict! Cannot use House 0's best color (0).
  - Must use second best: $\text{prev} = \text{min}_2 = 3$.
  $$
  \text{val}_0 = 2 + 3 = \mathbf{5}
  $$

- **Color $c = 1$ (Cost $= 9$):**
  - Check adjacency: $c \ne \text{idx}_1$ ($1 \ne 0$).
  - Free to use House 0's global best: $\text{prev} = \text{min}_1 = 1$.
  $$
  \text{val}_1 = 9 + 1 = \mathbf{10}
  $$

- **Color $c = 2$ (Cost $= 4$):**
  - Check adjacency: $c \ne \text{idx}_1$ ($2 \ne 0$).
  - Free to use House 0's global best: $\text{prev} = \text{min}_1 = 1$.
  $$
  \text{val}_2 = 4 + 1 = \mathbf{5}
  $$

Row 1 costs: $[5, 10, 5]$.
Find new minimums:
- Smallest: $\text{new\_min}_1 = 5$ at $\text{new\_idx}_1 = 0$.
- Second smallest: $\text{new\_min}_2 = 5$ at index $2$.

---

### Step 3: Terminal Extraction
All $N = 2$ houses evaluated.
The global minimum cost is $\text{min}_1 = \mathbf{5}$.

---

## 4. Complete Execution Trace

```text
House 0: [1, 5, 3]
  min1 = 1 (idx 0), min2 = 3 (idx 2)

House 1: [2, 9, 4]
  c = 0: c == idx1 (0 == 0) -> use min2 (3) -> 2 + 3 = 5
  c = 1: c != idx1 (1 != 0) -> use min1 (1) -> 9 + 1 = 10
  c = 2: c != idx1 (2 != 0) -> use min1 (1) -> 4 + 1 = 5
  new costs: [5, 10, 5]
  new min1 = 5, new min2 = 5

Final Answer: 5
```

| House $i$ | Color $c$ | Base Cost $\text{costs}[i][c]$ | Condition ($c == \text{idx}_1$)? | Predecessor Cost Used | Total Transition Cost | Running New $\text{min}_1, \text{min}_2$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| 0 | 0, 1, 2 | $[1, 5, 3]$ | - | - | $[1, 5, 3]$ | $\text{min}_1 = 1 \, (c=0), \; \text{min}_2 = 3$ |
| 1 | 0 | 2 | **Yes ($0 == 0$)** | $\text{min}_2 = 3$ | $2 + 3 = 5$ | $\text{new\_min}_1 = 5 \, (c=0)$ |
| 1 | 1 | 9 | No ($1 \ne 0$) | $\text{min}_1 = 1$ | $9 + 1 = 10$ | $\text{new\_min}_2 = 10$ |
| 1 | 2 | 4 | No ($2 \ne 0$) | $\text{min}_1 = 1$ | $4 + 1 = 5$ | $\text{new\_min}_2 = 5$ |
| **End** | - | - | - | - | - | **$\mathbf{5}$ (Final Cost)** |

---

## 5. Algorithmic Correctness

**Soundness.** For any color $c$, the only restriction from the previous house is that color $c$ cannot be chosen. Among all $K - 1$ allowed colors in row $i - 1$, the minimum cost is $\text{min}_1$ if $\text{idx}_1 \ne c$, and $\text{min}_2$ if $\text{idx}_1 == c$. Since $\text{min}_2$ is defined as the minimum over all colors other than $\text{idx}_1$, no legal choice could have a lower cost.

**Completeness.** By mathematical induction on house index $i$, $\text{min}_1$ is the exact minimum cost to paint houses $0 \dots i$ legally. All $K$ colors are evaluated at each house, guaranteeing that the global optimum is preserved.

---

## 6. Traps This Instance Exposes

- **$O(N K^2)$ TLE Trap:** Scanning all $K - 1$ elements for each color causes Time Limit Exceeded when $K$ is large. Precomputing the top two minimums reduces the inner transition to $O(1)$.
- **Identical Minimum Values:** If two different colors both yield the same minimal cost (e.g. costs $[2, 2, 5]$), $\text{min}_1 = 2$ and $\text{min}_2 = 2$ with different indices. If the next house chooses $\text{idx}_1$, it can transition to the other color at cost $\text{min}_2 = 2$.
- **$K = 1$ Edge Case:** If $K = 1$ and $N > 1$, it is impossible to paint adjacent houses with different colors. The problem guarantees $K \ge 2$ when $N > 1$.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N \cdot K)$, where $N$ is the number of houses and $K$ is the number of colors. For each of the $N$ houses, we iterate through the $K$ colors exactly once, performing $O(1)$ comparisons and arithmetic operations per cell.
- **Auxiliary Space Complexity:** $O(1)$ auxiliary space. Only three scalar variables ($\text{min}_1$, $\text{idx}_1$, $\text{min}_2$) are maintained across rows.