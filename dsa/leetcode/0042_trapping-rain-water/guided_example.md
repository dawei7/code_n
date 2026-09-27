# Guided Example: Trapping Rain Water

We trace the step-by-step water trapping elevation calculation on a representative terrain profile:

- **Input:** $\text{height} = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]$
- **Required output:** $6$

This instance demonstrates column-by-column water level physics, prefix and suffix elevation boundary dominance ($\min(L_i, R_i)$), the two-pointer bottleneck elimination technique, and exact trapped volume summation.

---

## 1. Instance & Teaching Goal

Given an elevation map represented by an array of $N = 12$ bar heights:
$$
[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
$$
where each bar has width 1, we must determine the total volume of water trapped between the bars after rain.

Physical Principle:
At any coordinate $i$, water is constrained by the highest wall to its left and the highest wall to its right. Water spills over whichever wall is shorter. Therefore, the water level at column $i$ is strictly capped by:
$$
\text{Water Level}(i) = \min(L_i, R_i)
$$
where $L_i = \max_{0 \le k \le i}(\text{height}[k])$ and $R_i = \max_{i \le k < N}(\text{height}[k])$.
The volume trapped directly above bar $i$ is:
$$
\text{Trapped Water}(i) = \max(0, \, \min(L_i, R_i) - \text{height}[i])
$$

For our instance, water pools at indices 2, 4, 5, 6, and 9, totaling $1 + 1 + 2 + 1 + 1 = 6$ units of water.

---

## 2. Conceptual Foundation & Invariants

### 1. Dynamic Programming Precomputation ($O(N)$ Space)
We construct two arrays of size $N$:
- $\text{left\_max}[i]$: Running maximum from left to right:
  $$
  \text{left\_max}[i] = \max(\text{left\_max}[i-1], \text{height}[i])
  $$
- $\text{right\_max}[i]$: Running maximum from right to left:
  $$
  \text{right\_max}[i] = \max(\text{right\_max}[i+1], \text{height}[i])
  $$
- The trapped water at each column $i$ is simply $\min(\text{left\_max}[i], \text{right\_max}[i]) - \text{height}[i]$.

### 2. Two-Pointer Space Optimization ($O(1)$ Space)
Instead of allocating two arrays, we use pointers $l = 0$ and $r = N - 1$, maintaining scalar variables $\text{left\_max}$ and $\text{right\_max}$:
- If $\text{left\_max} \le \text{right\_max}$: The bottleneck for column $l$ is definitively $\text{left\_max}$ (because we know there exists some bar on the right of height at least $\text{right\_max} \ge \text{left\_max}$). Water at $l$ is $\text{left\_max} - \text{height}[l]$. We process $l$ and increment $l \leftarrow l + 1$.
- Else: The bottleneck for column $r$ is definitively $\text{right\_max}$. Water at $r$ is $\text{right\_max} - \text{height}[r]$. We process $r$ and decrement $r \leftarrow r - 1$.

> **Invariant.** At each step, whichever side has the smaller maximum wall is limited entirely by its own side's peak; the taller peak on the opposite side ensures water will not spill across.

---

## 3. Step-by-Step Worked Execution

We compute the water trapped above every index $i \in [0, 11]$:

```text
Elevation Profile Diagram:
       3 |                      #
       2 |          # ~ ~ ~ ~ ~ # # ~ #
       1 |    # ~ # # ~ # # ~ # # # # #
       0 |  _ # _ # # _ # # # # # # # #
Index i:    0 1 2 3 4 5 6 7 8 9 10 11
Trapped:    0 0 1 0 1 2 1 0 0 1 0  0  -> Total = 6
```

### Detailed Index-by-Index Evaluation

- **Index 0 ($\text{height} = 0$):** $L_0 = 0, R_0 = 3 \implies \min(0, 3) - 0 = 0$.
- **Index 1 ($\text{height} = 1$):** $L_1 = 1, R_1 = 3 \implies \min(1, 3) - 1 = 0$.
- **Index 2 ($\text{height} = 0$):** $L_2 = 1, R_2 = 3 \implies \min(1, 3) - 0 = 1 - 0 = \mathbf{1}$.
- **Index 3 ($\text{height} = 2$):** $L_3 = 2, R_3 = 3 \implies \min(2, 3) - 2 = 0$.
- **Index 4 ($\text{height} = 1$):** $L_4 = 2, R_4 = 3 \implies \min(2, 3) - 1 = 2 - 1 = \mathbf{1}$.
- **Index 5 ($\text{height} = 0$):** $L_5 = 2, R_5 = 3 \implies \min(2, 3) - 0 = 2 - 0 = \mathbf{2}$.
- **Index 6 ($\text{height} = 1$):** $L_6 = 2, R_6 = 3 \implies \min(2, 3) - 1 = 2 - 1 = \mathbf{1}$.
- **Index 7 ($\text{height} = 3$):** Global peak! $L_7 = 3, R_7 = 3 \implies \min(3, 3) - 3 = 0$.
- **Index 8 ($\text{height} = 2$):** $L_8 = 3, R_8 = 2 \implies \min(3, 2) - 2 = 0$.
- **Index 9 ($\text{height} = 1$):** $L_9 = 3, R_9 = 2 \implies \min(3, 2) - 1 = 2 - 1 = \mathbf{1}$.
- **Index 10 ($\text{height} = 2$):** $L_{10} = 3, R_{10} = 2 \implies \min(3, 2) - 2 = 0$.
- **Index 11 ($\text{height} = 1$):** $L_{11} = 3, R_{11} = 1 \implies \min(3, 1) - 1 = 0$.

Total trapped water: $1 + 1 + 2 + 1 + 1 = 6$.

---

## 4. Complete Execution Trace

| Index $i$ | Bar Height | Left Max $L_i$ | Right Max $R_i$ | Limiting Boundary $\min(L_i, R_i)$ | Trapped Water at Column | Cumulative Volume |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 0 | 0 | 0 | 3 | 0 | $0 - 0 = 0$ | 0 |
| 1 | 1 | 1 | 3 | 1 | $1 - 1 = 0$ | 0 |
| 2 | 0 | 1 | 3 | 1 | $1 - 0 = 1$ | 1 |
| 3 | 2 | 2 | 3 | 2 | $2 - 2 = 0$ | 1 |
| 4 | 1 | 2 | 3 | 2 | $2 - 1 = 1$ | 2 |
| 5 | 0 | 2 | 3 | 2 | $2 - 0 = 2$ | 4 |
| 6 | 1 | 2 | 3 | 2 | $2 - 1 = 1$ | 5 |
| 7 | 3 | 3 | 3 | 3 | $3 - 3 = 0$ | 5 |
| 8 | 2 | 3 | 2 | 2 | $2 - 2 = 0$ | 5 |
| 9 | 1 | 3 | 2 | 2 | $2 - 1 = 1$ | **6** |
| 10 | 2 | 3 | 2 | 2 | $2 - 2 = 0$ | 6 |
| 11 | 1 | 3 | 1 | 1 | $1 - 1 = 0$ | 6 |

### Two-Pointer Walk with Constant Auxiliary Space

The previous table uses the precomputed arrays. The same total must emerge from the pointer method, and the next table records the frontier state before each decision so the elimination rule can be checked column by column. Here $\text{left\_max}$ and $\text{right\_max}$ are the scalar running maxima held by the two pointers.

| Step | $l$ | $r$ | $\text{left\_max}$ before | $\text{right\_max}$ before | Comparison | Column retired | Height | Water added | Cumulative |
|:---:|:---:|:---:|:---:|:---:|:---|:---:|:---:|:---:|:---:|
| 1 | 0 | 11 | 0 | 0 | $0 \le 0$, so the left side is the bottleneck | $l = 0$ | 0 | $0 - 0 = 0$ | 0 |
| 2 | 1 | 11 | 0 | 0 | $0 \le 0$, left side | $l = 1$ | 1 | $1 - 1 = 0$ | 0 |
| 3 | 2 | 11 | 1 | 0 | $1 \le 0$ is false, so the right side is the bottleneck | $r = 11$ | 1 | $1 - 1 = 0$ | 0 |
| 4 | 2 | 10 | 1 | 1 | $1 \le 1$, left side | $l = 2$ | 0 | $1 - 0 = 1$ | 1 |
| 5 | 3 | 10 | 1 | 1 | $1 \le 1$, left side | $l = 3$ | 2 | $2 - 2 = 0$ | 1 |
| 6 | 4 | 10 | 2 | 1 | $2 \le 1$ is false, right side | $r = 10$ | 2 | $2 - 2 = 0$ | 1 |
| 7 | 4 | 9 | 2 | 2 | $2 \le 2$, left side | $l = 4$ | 1 | $2 - 1 = 1$ | 2 |
| 8 | 5 | 9 | 2 | 2 | $2 \le 2$, left side | $l = 5$ | 0 | $2 - 0 = 2$ | 4 |
| 9 | 6 | 9 | 2 | 2 | $2 \le 2$, left side | $l = 6$ | 1 | $2 - 1 = 1$ | 5 |
| 10 | 7 | 9 | 2 | 2 | $2 \le 2$, left side | $l = 7$ | 3 | $3 - 3 = 0$ | 5 |
| 11 | 8 | 9 | 3 | 2 | $3 \le 2$ is false, right side | $r = 9$ | 1 | $2 - 1 = 1$ | **6** |
| 12 | 8 | 8 | 3 | 2 | $3 \le 2$ is false, right side | $r = 8$ | 2 | $2 - 2 = 0$ | 6 |

The retired columns in order are $0, 1, 11, 2, 3, 10, 4, 5, 6, 7, 9, 8$: all twelve indices exactly once, with no column revisited. The positive contributions land on columns $2, 4, 5, 6, 9$ and total $1 + 1 + 2 + 1 + 1 = 6$, matching the array-based evaluation. Step 11 is the decisive one for the right half: once $\text{right\_max} = 2$ is known to be below $\text{left\_max} = 3$, column $9$ cannot hold more than $2$ units, so the left peak no longer constrains it.

---

## 5. Algorithmic Correctness

**Soundness.** Water cannot rise above the shorter of its enclosing boundaries without overflowing. Because $L_i$ and $R_i$ represent the maximal physical obstacles on either side of coordinate $i$, $\min(L_i, R_i)$ is the exact height of the water surface. Subtracting $\text{height}[i]$ gives the exact depth of water supported by the ground at that column.

**Completeness.** Every column from $0$ to $N - 1$ is evaluated. Because columns have unit width $1$, the total volume is the exact sum of individual column depths. No pooling region is overlooked.

---

## 6. Traps This Instance Exposes

- **Using Global Max Instead of Local Boundaries:** Water does not pool up to $\max(\text{all heights})$. It pools only to the local enclosing peaks $\min(L_i, R_i)$.
- **Negative Water Depths:** If a bar is higher than an adjacent valley, $\min(L_i, R_i) - \text{height}[i]$ could theoretically be negative if $L_i$ did not include $\text{height}[i]$. Defining $L_i = \max(L_{i-1}, \text{height}[i])$ ensures $\min(L_i, R_i) \ge \text{height}[i]$, naturally preventing negative depths.
- **Monotonic Stack Alternative:** Water can also be computed horizontally in layers using a monotonic decreasing stack of indices. When a taller bar is found, valleys are popped and filled layer by layer. The two-pointer / DP column method is mathematically equivalent and simpler to reason about.

### Boundary terrain profiles

Each profile below is evaluated by the same $\min(L_i, R_i) - \text{height}[i]$ rule; the last column records which side's pointer retires the columns, which is where an off-by-one in the tie-break would show up.

| Elevation map | $N$ | Trapped volume | Why no water is held or how it is held | Pointer behaviour |
|:---|:---:|:---:|:---|:---|
| $[0]$ | $1$ | $0$ | A single column has no enclosing wall on either side, so $\min(L_0, R_0) = 0 = \text{height}[0]$ | The lone column is retired once and contributes $0$ |
| $[1, 2, 3, 4]$ | $4$ | $0$ | Strictly increasing: the left maximum at each column equals that column's own height, so the surface never rises above the bar | The left pointer retires every column |
| $[4, 3, 2, 1]$ | $4$ | $0$ | Strictly decreasing: the mirrored case, where the right maximum equals the column height | The right pointer retires every column |
| $[3, 3, 3]$ | $3$ | $0$ | Equal boundaries: $\min(L_i, R_i) = 3 = \text{height}[i]$ everywhere, so every depth is zero | Both maxima stay equal, so ties are resolved by the left branch |
| $[5, 0, 0, 0, 5]$ | $5$ | $15$ | A flat basin: the three interior columns each hold $5 - 0 = 5$ units | The two walls give equal maxima, and the left branch retires the interior columns |
| $[100000, 0, 100000]$ | $3$ | $100000$ | The largest legal wall bounds a single interior column, holding $100000 - 0$ units | The interior column is retired by the left branch after the wall maxima match |

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N$ is the number of bars. Precomputing $\text{left\_max}$ and $\text{right\_max}$ requires two linear passes, and summation requires one pass ($3N = O(N)$). The two-pointer approach solves it in a single pass of $N$ steps.
- **Auxiliary Space Complexity:** $O(1)$ when using the two-pointer approach, maintaining only scalar variables ($\text{left\_max}$, $\text{right\_max}$, $l$, $r$, $\text{ans}$).

### Cost of each equivalent method

All three methods below produce the same total; they differ in what they must remember in order to know $\min(L_i, R_i)$.

| Method | Time | Auxiliary space | State it maintains | Why it still yields the exact total |
|:---|:---:|:---:|:---|:---|
| Prefix and suffix maximum arrays | $O(N)$ across two build passes plus one summation pass | $O(N)$ | A full $\text{left\_max}$ array and a full $\text{right\_max}$ array | For each column the two arrays hold exactly $L_i$ and $R_i$, so the per-column formula is applied directly |
| Two pointers with running maxima | $O(N)$ in a single pass | $O(1)$ | Two indices and two scalar maxima | The smaller of the two running maxima is provably the true bottleneck for the column on its own side, so the taller opposite peak cannot raise the surface |
| Monotonic decreasing stack | $O(N)$ amortized, since each index is pushed and popped at most once | $O(N)$ | A stack of indices whose heights are non-increasing | Water is filled in horizontal layers between each popped valley floor and the taller bar that closes it, which sums to the same vertical depths |
