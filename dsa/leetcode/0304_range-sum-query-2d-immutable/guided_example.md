# Guided Example: Range Sum Query 2D - Immutable

We trace the step-by-step 2D prefix sum table construction, four-term inclusion-exclusion geometric derivation, zero-boundary sentinel padding, and $O(1)$ subgrid query evaluation on representative matrix instances:

- **Input:**
  $$
  \text{matrix} = \begin{bmatrix}
  3 & 0 \\
  1 & 2
  \end{bmatrix}, \quad \text{queries} = [\text{sumRegion}(0, 0, 1, 1), \; \text{sumRegion}(1, 1, 1, 1)]
  $$
- **Required outputs:**
  - $\text{sumRegion}(0, 0, 1, 1) = 3 + 0 + 1 + 2 = 6$ (Entire matrix)
  - $\text{sumRegion}(1, 1, 1, 1) = 2$ (Single cell)
- **Non-Square Multi-Row Matrix Instance:**
  $$
  \text{matrix} = \begin{bmatrix}
  3 & 0 & 1 & 4 & 2 \\
  5 & 6 & 3 & 2 & 1 \\
  1 & 2 & 0 & 1 & 5 \\
  4 & 1 & 0 & 1 & 7 \\
  1 & 0 & 3 & 0 & 5
  \end{bmatrix}, \quad \text{sumRegion}(2, 1, 4, 3) = 8
  $$
- **Single Row / Single Column Queries:** Inclusion-exclusion handles edge rectangles seamlessly without conditional checks

This instance demonstrates 2D cumulative prefix area decomposition, provides a geometric proof of the inclusion-exclusion formula ($A + B - \text{overlap} + \text{cell}$), explains why an $(M+1) \times (N+1)$ padded table eliminates index bounds checking, and achieves $O(M \times N)$ preprocessing with $O(1)$ query time and $O(M \times N)$ space.

---

## 1. Instance & Teaching Goal

Given a 2D integer matrix:
$$
\text{matrix} = \begin{bmatrix}
3 & 0 \\
1 & 2
\end{bmatrix} \quad (M = 2, N = 2)
$$
We need to process queries $\text{sumRegion}(r_1, c_1, r_2, c_2) = \sum_{i=r_1}^{r_2} \sum_{j=c_1}^{c_2} \text{matrix}[i][j]$.

```text
Matrix:
(0,0)=3   (0,1)=0
(1,0)=1   (1,1)=2

Query (0, 0) to (1, 1): All 4 cells -> 3 + 0 + 1 + 2 = 6
Query (1, 1) to (1, 1): Single cell -> 2
```

### Why a Naive Double Loop is Inefficient
- Evaluating each query by nested loops over $[r_1, r_2] \times [c_1, c_2]$ costs $O((r_2 - r_1 + 1)(c_2 - c_1 + 1)) = O(M N)$ time per query.
- For $Q = 10^4$ queries on a $200 \times 200$ grid, naive iteration requires up to $4 \times 10^8$ operations.
- By precomputing a 2D prefix sum table in $O(M N)$ time, any rectangular region sum can be extracted using **four arithmetic lookups in $O(1)$ time**!

---

## 2. Conceptual Foundation & Invariants

### 2D Prefix Sum Definition
Define an $(M + 1) \times (N + 1)$ table $s$ where $s[i][j]$ stores the sum of the subgrid from origin $(0, 0)$ down to $(i - 1, j - 1)$:
- Boundary: $s[0][j] = 0$ for all $j$, and $s[i][0] = 0$ for all $i$.
- Recurrence for cell $(i, j)$ ($0 \le i < M, 0 \le j < N$):
  $$
  s[i + 1][j + 1] = s[i][j + 1] + s[i + 1][j] - s[i][j] + \text{matrix}[i][j]
  $$

```text
Visualizing 2D Construction:
+-------------------+---+
|                   |   |  s[i][j+1] covers top rectangle
|      s[i][j]      |   |  s[i+1][j] covers left rectangle
|     (overlap)     |   |  s[i][j] is counted twice -> subtract once
+-------------------+---+
|                   | X |  X = matrix[i][j] -> add once
+-------------------+---+
```

### Query Formula by Inclusion-Exclusion
To compute the sum of rectangle from $(r_1, c_1)$ to $(r_2, c_2)$:
$$
\text{sumRegion}(r_1, c_1, r_2, c_2) = s[r_2 + 1][c_2 + 1] - s[r_1][c_2 + 1] - s[r_2 + 1][c_1] + s[r_1][c_1]
$$

```text
(0, 0) ------------------- (0, c2+1)
  |           Top Strip       |
  |            s[r1][c2+1]    |
(r1, 0) ----- + ------------- +
  |   Left    |   Target      |
  |   Strip   |   Region      |
  |           |               |
(r2+1, 0) --- + ------------- (r2+1, c2+1)
```
- Full rectangle from origin: $s[r_2 + 1][c_2 + 1]$.
- Subtract top unwanted strip: $- s[r_1][c_2 + 1]$.
- Subtract left unwanted strip: $- s[r_2 + 1][c_1]$.
- Add back doubly-subtracted top-left overlap: $+ s[r_1][c_1]$.

> **Invariant.** For any query bounds, the four-point formula cancels all elements outside the target bounding box and counts every element inside the box exactly once.

---

## 3. Step-by-Step Worked Execution

We trace the construction and queries on $\text{matrix} = \begin{bmatrix} 3 & 0 \\ 1 & 2 \end{bmatrix}$:
Matrix size: $M = 2, N = 2$.
Prefix table size: $3 \times 3$, initialized to $0$.

---

### Step 1: Populate 2D Prefix Table $s$

1. **Row $i = 0$:**
   - $j = 0$ ($\text{val} = 3$):
     $$
     s[1][1] = s[0][1] + s[1][0] - s[0][0] + 3 = 0 + 0 - 0 + 3 = \mathbf{3}
     $$
   - $j = 1$ ($\text{val} = 0$):
     $$
     s[1][2] = s[0][2] + s[1][1] - s[0][1] + 0 = 0 + 3 - 0 + 0 = \mathbf{3}
     $$

2. **Row $i = 1$:**
   - $j = 0$ ($\text{val} = 1$):
     $$
     s[2][1] = s[1][1] + s[2][0] - s[1][0] + 1 = 3 + 0 - 0 + 1 = \mathbf{4}
     $$
   - $j = 1$ ($\text{val} = 2$):
     $$
     s[2][2] = s[1][2] + s[2][1] - s[1][1] + 2 = 3 + 4 - 3 + 2 = \mathbf{6}
     $$

Completed prefix table $s$:
$$
s = \begin{bmatrix}
0 & 0 & 0 \\
0 & 3 & 3 \\
0 & 4 & 6
\end{bmatrix}
$$

---

### Step 2: Evaluate Query 1 — $\text{sumRegion}(0, 0, 1, 1)$
- Bounds: $r_1 = 0, c_1 = 0, r_2 = 1, c_2 = 1$.
- Shifted table indices:
  $$
  r_2 + 1 = 2, \quad c_2 + 1 = 2, \quad r_1 = 0, \quad c_1 = 0
  $$
- Apply formula:
  $$
  \text{Sum} = s[2][2] - s[0][2] - s[2][0] + s[0][0]
  $$
- Substitute values:
  $$
  \text{Sum} = 6 - 0 - 0 + 0 = \mathbf{6}
  $$

---

### Step 3: Evaluate Query 2 — $\text{sumRegion}(1, 1, 1, 1)$
- Bounds: $r_1 = 1, c_1 = 1, r_2 = 1, c_2 = 1$.
- Shifted table indices:
  $$
  r_2 + 1 = 2, \quad c_2 + 1 = 2, \quad r_1 = 1, \quad c_1 = 1
  $$
- Apply formula:
  $$
  \text{Sum} = s[2][2] - s[1][2] - s[2][1] + s[1][1]
  $$
- Substitute values:
  $$
  \text{Sum} = 6 - 3 - 4 + 3 = \mathbf{2}
  $$
- Matches single cell $\text{matrix}[1][1] = 2$!

---

## 4. Complete Execution Trace

```text
Matrix:
[3, 0]
[1, 2]

Prefix Table s:
[0, 0, 0]
[0, 3, 3]
[0, 4, 6]

Query 1 (0, 0, 1, 1): s[2][2] - s[0][2] - s[2][0] + s[0][0] = 6 - 0 - 0 + 0 = 6
Query 2 (1, 1, 1, 1): s[2][2] - s[1][2] - s[2][1] + s[1][1] = 6 - 3 - 4 + 3 = 2
```

| Table Entry | Top Term $s[i][j+1]$ | Left Term $s[i+1][j]$ | Overlap $s[i][j]$ | $\text{matrix}[i][j]$ | Computed $s[i+1][j+1]$ |
|:---:|:---:|:---:|:---:|:---:|:---:|
| $s[1][1]$ | 0 | 0 | 0 | 3 | **3** |
| $s[1][2]$ | 0 | 3 | 0 | 0 | **3** |
| $s[2][1]$ | 3 | 0 | 0 | 1 | **4** |
| $s[2][2]$ | 3 | 4 | 3 | 2 | **6** |

| Query $(r_1, c_1, r_2, c_2)$ | $+ s[r_2+1][c_2+1]$ | $- s[r_1][c_2+1]$ | $- s[r_2+1][c_1]$ | $+ s[r_1][c_1]$ | Total Sum |
|:---:|:---:|:---:|:---:|:---:|:---:|
| $(0, 0, 1, 1)$ | $+6$ | $-0$ | $-0$ | $+0$ | **6** |
| $(1, 1, 1, 1)$ | $+6$ | $-3$ | $-4$ | $+3$ | **2** |

---

## 5. Algorithmic Correctness

**Soundness.** Let $R$ denote the set of cells $[r_1, r_2] \times [c_1, c_2]$. The four prefix regions partition the coordinate plane into four quadrants relative to $(r_1, c_1)$. By the Principle of Inclusion-Exclusion, every cell in $[0, r_1 - 1] \times [0, c_1 - 1]$ is counted $+1 - 1 - 1 + 1 = 0$ times. Every cell above or to the left of the rectangle is counted $+1 - 1 = 0$ times. Every cell inside $R$ is counted $+1$ time. Thus, the computed sum is mathematically exact.

**Completeness.** The $(M + 1) \times (N + 1)$ dimensions ensure that for any query with $0 \le r_1 \le r_2 < M$ and $0 \le c_1 \le c_2 < N$, all four queried table coordinates lie within $[0, M] \times [0, N]$. The zero sentinel boundaries naturally handle subgrids touching the top or left edges without requiring branch conditions.

---

## 6. Traps This Instance Exposes

- **Forgetting to Add the Top-Left Overlap:** Subtracting both the top strip $s[r_1][c_2 + 1]$ and the left strip $s[r_2 + 1][c_1]$ removes their intersection $s[r_1][c_1]$ twice. It must be added back ($+ s[r_1][c_1]$).
- **Off-by-One in Shifted Coordinates:** The bottom-right corner must use $r_2 + 1$ and $c_2 + 1$, while the upper-left boundaries use $r_1$ and $c_1$. Writing $r_1 - 1$ instead of $r_1$ introduces index out-of-bounds errors on 0-indexed rows.
- **Dynamic Updates:** This solution assumes the matrix is immutable. If cells were updated dynamically, updating a cell $(i, j)$ would require updating up to $O(M N)$ prefix entries, necessitating a 2D Fenwick Tree or 2D Segment Tree ($O(\log M \log N)$ update and query).

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Initialization: $O(M \times N)$ to compute all $(M + 1) \times (N + 1)$ prefix entries using dynamic programming.
  - `sumRegion`: $O(1)$ constant time per query, executing exactly four table reads and three additions/subtractions.
  - Total time for $Q$ queries: $O(M N + Q)$.
- **Auxiliary Space Complexity:** $O(M \times N)$ auxiliary memory to store the $(M + 1) \times (N + 1)$ prefix sum array $s$.
