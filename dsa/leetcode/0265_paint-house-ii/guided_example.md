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

### State Evolution on a Four-House Instance

The representative instance uses one transition; a longer instance where
$\text{idx}_1$ changes from row to row shows what the tracked pair must survive.
Take $\text{costs} = [[1, 4, 6], [1, 3, 5], [2, 1, 4], [1, 2, 3]]$, whose
authored answer is $7$.

| House $i$ | $\text{costs}[i]$ | DP row after the transition | $\text{min}_1$ ($\text{idx}_1$) | $\text{min}_2$ | What this row teaches |
|:---:|:---|:---|:---:|:---:|:---|
| 0 | `[1, 4, 6]` | `[1, 4, 6]` | 1 (color 0) | 4 (color 1) | The base row is the raw cost row, and the second minimum sits at a *different* index |
| 1 | `[1, 3, 5]` | `[5, 4, 6]` | 4 (color 1) | 5 (color 0) | $\text{idx}_1$ moves: color 1 pays $3$ plus the previous second minimum $4$, undercutting color 0, which must pay $1 + 4$ |
| 2 | `[2, 1, 4]` | `[6, 6, 8]` | 6 (color 0) | 6 (color 1) | A genuine tie: the cheapest base cost ($1$ at color 1) must add $5$, while color 0 adds $4$, and both land on $6$ |
| 3 | `[1, 2, 3]` | `[7, 8, 9]` | 7 (color 0) | 8 (color 1) | Colors 0 and 1 may each reuse the value $6$: excluding color 0 leaves $\text{min}_2 = 6$, and excluding color 1 leaves $\text{min}_1 = 6$ |

The optimum behind the final $7$ is the coloring $(1, 0, 1, 0)$ with per-house
costs $4, 1, 1, 1$. Row two is the row that makes the dual-minimum bookkeeping
necessary: because the two smallest values are equal but sit at different
indices, excluding one of them still leaves a minimum of $6$, and any method that
recorded only a value without its index would either forbid a legal color or
allow an illegal one.

---

## 5. Algorithmic Correctness

**Soundness.** For any color $c$, the only restriction from the previous house is that color $c$ cannot be chosen. Among all $K - 1$ allowed colors in row $i - 1$, the minimum cost is $\text{min}_1$ if $\text{idx}_1 \ne c$, and $\text{min}_2$ if $\text{idx}_1 == c$. Since $\text{min}_2$ is defined as the minimum over all colors other than $\text{idx}_1$, no legal choice could have a lower cost.

**Completeness.** By mathematical induction on house index $i$, $\text{min}_1$ is the exact minimum cost to paint houses $0 \dots i$ legally. All $K$ colors are evaluated at each house, guaranteeing that the global optimum is preserved.

---

## 6. Traps This Instance Exposes

- **$O(N K^2)$ TLE Trap:** Scanning all $K - 1$ elements for each color causes Time Limit Exceeded when $K$ is large. Precomputing the top two minimums reduces the inner transition to $O(1)$.
- **Identical Minimum Values:** If two different colors both yield the same minimal cost (e.g. costs $[2, 2, 5]$), $\text{min}_1 = 2$ and $\text{min}_2 = 2$ with different indices. If the next house chooses $\text{idx}_1$, it can transition to the other color at cost $\text{min}_2 = 2$.
- **$K = 1$ Edge Case:** If $K = 1$ and $N > 1$, it is impossible to paint adjacent houses with different colors. The problem guarantees $K \ge 2$ when $N > 1$.

### Why the Cheapest Color at Each House Is Not the Answer

A learner's first instinct is to paint every house its locally cheapest allowed
color. The four-house instance punishes that instinct, and the table follows both
strategies step by step on the same data.

| House $i$ | Greedy choice (cheapest color allowed by the previous row) | Greedy running total | Optimal cumulative from the DP row | Divergence |
|:---:|:---|:---:|:---:|:---|
| 0 | Color 0 at cost $1$ | 1 | 1 (color 0) | None yet: color 0 is genuinely best for a single house |
| 1 | Color 0 is forbidden, so color 1 at cost $3$ | 4 | 4 (color 1) | Still level, but greedy has already spent its cheap color |
| 2 | Color 1 is forbidden, so color 0 at cost $2$ | 6 | 6 (colors 0 and 1 tied) | Level again, and the tie hides the coming split |
| 3 | Color 0 is forbidden, so color 1 at cost $2$ | **8** | **7** (color 0, reusing the value $6$) | The optimum finishes on color 0 at cost $1$; greedy is locked out of it |

The failure is visible only at the last house, which is exactly why a local rule
cannot repair it: choosing color $0$ for house $0$ saves $3$ immediately but
forces color $1$ at house $3$, where the price is $2$ instead of $1$, and the
same asymmetry repeats through the middle houses. A second instance shows the
same trap with a wider margin: on
$\text{costs} = [[1, 1, 20], [1, 20, 20]]$ the greedy rule pays $1$ then $20$ for
a total of $21$, while the optimal coloring pays $1$ for color $1$ and then $1$
for color $0$, for a total of $2$. Keeping both minima lets the method accept a
slightly worse color now whenever it unlocks a much cheaper color next.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N \cdot K)$, where $N$ is the number of houses and $K$ is the number of colors. For each of the $N$ houses, we iterate through the $K$ colors exactly once, performing $O(1)$ comparisons and arithmetic operations per cell.
- **Auxiliary Space Complexity:** $O(1)$ auxiliary space. Only three scalar variables ($\text{min}_1$, $\text{idx}_1$, $\text{min}_2$) are maintained across rows.

### Alternatives and Their Costs

The follow-up asks for $O(nk)$ runtime, so every row below is judged against that
target rather than against the loose sizes used to motivate it. With the stated
limits $n \le 100$ and $k \le 20$, the naive inner scan performs at most
$(n - 1) \cdot k \cdot (k - 1) = 37{,}620$ exclusion lookups.

| Strategy | Mechanism | Time | Auxiliary space | Tradeoff or failure mode |
|:---|:---|:---:|:---:|:---|
| Exclusion scan per cell | For each color, scan every other color of the previous row for its minimum | $O(n k^2)$ | $O(k)$ for the previous row | Simple and obviously correct, but it is the form the follow-up asks to remove |
| Dual-minimum tracking (the method traced) | Carry only $\text{min}_1$, $\text{idx}_1$, and $\text{min}_2$ from the previous row | $O(n k)$ | $O(1)$ beyond two rolling rows | Needs $\text{min}_2$ to be the best value at an index other than $\text{idx}_1$, and both minima must come from the same unchanged row |
| Prefix and suffix minima per row | Precompute $\min$ over the row's prefix and suffix, then each color reads the two neighbours around it | $O(n k)$ | $O(k)$ | Same asymptotic time, but two extra passes and $k$ extra cells, and the arrays must be rebuilt for every house |
| Sort each row | Sort the previous row's value-index pairs and keep the two smallest | $O(n k \log k)$ | $O(k)$ | Converts a linear scan into a sort; more work than carrying two scalars |
| Min-heap over the previous row | Pop the smallest; if its index equals the current color, pop the next | $O(n k \log k)$ | $O(k)$ | Handles ties correctly, but pays a logarithm for a comparison that a linear pass already answers |

The dual-minimum method is the only $O(nk)$ strategy that also keeps auxiliary
space constant, which matters because the state it summarises is exactly two
numbers per row: the best value and the best value that is still legal when the
best one is forbidden.
