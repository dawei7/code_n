# Guided Example: Pascal's Triangle

We trace the step-by-step mathematical additive recurrence and row generation for Pascal's Triangle:

- **Input:** $\text{numRows} = 5$
- **Required output:** `[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]`
- **Base Instance:** $\text{numRows} = 1 \implies [[1]]$

This instance demonstrates row boundary anchoring ($T(r, 0) = T(r, r) = 1$), adjacent-pair parent summation ($T(r, c) = T(r-1, c-1) + T(r-1, c)$), combinatorial binomial equivalence ($\binom{r}{c}$), and generating the complete lower-triangular matrix in $O(N^2)$ time.

---

## 1. Instance & Teaching Goal

Given an integer $\text{numRows} = 5$, construct the first $5$ rows of Pascal's triangle:
$$
\begin{matrix}
\text{Row 0:} & & & & 1 & & & \\
\text{Row 1:} & & & 1 & & 1 & & \\
\text{Row 2:} & & 1 & & 2 & & 1 & \\
\text{Row 3:} & 1 & & 3 & & 3 & & 1 \\
\text{Row 4:} & 1 & 4 & & 6 & & 4 & 1
\end{matrix}
$$
Every entry in Pascal's triangle is defined by the rule that each number is the sum of the two numbers directly above it:
- The outer boundaries are always $1$.
- Any interior number at row $r$, column $c$ ($0 < c < r$) equals the sum of column $c-1$ and column $c$ from row $r-1$.

Each row $r$ corresponds to the binomial coefficients of $(x + y)^r$, with entry $(r, c)$ representing $\binom{r}{c} = \frac{r!}{c!(r-c)!}$.

Constructing each subsequent row from the previously completed row runs in time proportional to the total number of entries: $\sum_{r=1}^N r = \frac{N(N+1)}{2} = O(N^2)$.

---

## 2. Conceptual Foundation & Invariants

### Additive Generation Protocol
Let $T(r, c)$ denote the element at 0-indexed row $r$ and column $c$ ($0 \le c \le r$):

1. **Boundary Values:**
   The first and last elements of every row are identically $1$:
   $$
   T(r, 0) = 1, \quad T(r, r) = 1
   $$
2. **Interior Summation Recurrence:**
   For $1 \le c < r$:
   $$
   T(r, c) = T(r - 1, c - 1) + T(r - 1, c)
   $$
3. **Iterative Row Synthesis:**
   Initialize `triangle = [[1]]`.
   For $r$ from $1$ to $\text{numRows} - 1$:
   - Let `prev = triangle[r - 1]`.
   - Initialize `row = [1]`.
   - For $c$ from $1$ to $r - 1$:
     $$
     \text{row.append}(\text{prev}[c - 1] + \text{prev}[c])
     $$
   - `row.append(1)`.
   - `triangle.append(row)`.

> **Invariant.** After row $r$ is synthesized, every element $T(r, c)$ exactly matches $\binom{r}{c}$ and depends strictly on the validated contents of row $r-1$.

---

## 3. Step-by-Step Worked Execution

We trace row creation for $\text{numRows} = 5$:

### Row $r = 0$:
- Base row with single element:
  $$
  \text{Row}_0 = [1]
  $$
- $\text{triangle} = [[1]]$.

---

### Row $r = 1$:
- Length $= 2$. Boundaries only: $c = 0$ and $c = 1$.
- $\text{Row}_1 = [1, 1]$.
- $\text{triangle} = [[1], [1, 1]]$.

---

### Row $r = 2$ (Prior Row: $[1, 1]$):
- Boundary: $\text{Row}_2[0] = 1$.
- Interior $c = 1$:
  $$
  T(2, 1) = T(1, 0) + T(1, 1) = 1 + 1 = 2
  $$
- Boundary: $\text{Row}_2[2] = 1$.
- $\text{Row}_2 = [1, 2, 1]$.

---

### Row $r = 3$ (Prior Row: $[1, 2, 1]$):
- Boundary: $\text{Row}_3[0] = 1$.
- Interior $c = 1$:
  $$
  T(3, 1) = T(2, 0) + T(2, 1) = 1 + 2 = 3
  $$
- Interior $c = 2$:
  $$
  T(3, 2) = T(2, 1) + T(2, 2) = 2 + 1 = 3
  $$
- Boundary: $\text{Row}_3[3] = 1$.
- $\text{Row}_3 = [1, 3, 3, 1]$.

---

### Row $r = 4$ (Prior Row: $[1, 3, 3, 1]$):
- Boundary: $\text{Row}_4[0] = 1$.
- Interior $c = 1$:
  $$
  T(4, 1) = T(3, 0) + T(3, 1) = 1 + 3 = 4
  $$
- Interior $c = 2$:
  $$
  T(4, 2) = T(3, 1) + T(3, 2) = 3 + 3 = 6
  $$
- Interior $c = 3$:
  $$
  T(4, 3) = T(3, 2) + T(3, 3) = 3 + 1 = 4
  $$
- Boundary: $\text{Row}_4[4] = 1$.
- $\text{Row}_4 = [1, 4, 6, 4, 1]$.

Generation complete.
Output: `[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]`.

---

## 4. Complete Execution Trace

| Row Index $r$ | Row Length | Boundary Anchor | Interior Element Calculations | Emitted Row |
|:---:|:---:|:---:|:---|:---|
| 0 | 1 | $1$ | None | `[1]` |
| 1 | 2 | $1, 1$ | None | `[1, 1]` |
| 2 | 3 | $1, 1$ | $c=1: 1 + 1 = 2$ | `[1, 2, 1]` |
| 3 | 4 | $1, 1$ | $c=1: 1 + 2 = 3$, $c=2: 2 + 1 = 3$ | `[1, 3, 3, 1]` |
| 4 | 5 | $1, 1$ | $c=1: 1 + 3 = 4$, $c=2: 3 + 3 = 6$, $c=3: 3 + 1 = 4$ | `[1, 4, 6, 4, 1]` |

The same rows can be read as a dependency graph over cell coordinates. Each
interior row lists the exact two parents it consumes, and the closed-form column
confirms that the recurrence and the binomial definition agree cell by cell:

| Target cell | Left parent $T(r-1,\,c-1)$ | Right parent $T(r-1,\,c)$ | Recurrence value $T(r,c)$ | Closed form $\binom{r}{c}$ |
|:---:|:---:|:---:|:---:|:---:|
| $T(2,1)$ | $T(1,0) = 1$ | $T(1,1) = 1$ | $2$ | $\binom{2}{1} = 2$ |
| $T(3,1)$ | $T(2,0) = 1$ | $T(2,1) = 2$ | $3$ | $\binom{3}{1} = 3$ |
| $T(3,2)$ | $T(2,1) = 2$ | $T(2,2) = 1$ | $3$ | $\binom{3}{2} = 3$ |
| $T(4,1)$ | $T(3,0) = 1$ | $T(3,1) = 3$ | $4$ | $\binom{4}{1} = 4$ |
| $T(4,2)$ | $T(3,1) = 3$ | $T(3,2) = 3$ | $6$ | $\binom{4}{2} = 6$ |
| $T(4,3)$ | $T(3,2) = 3$ | $T(3,3) = 1$ | $4$ | $\binom{4}{3} = 4$ |

Six interior cells are written for $\text{numRows} = 5$, and no cell is ever read
before its row has been completed, which is what makes the recursion a valid
bottom-up dynamic program rather than a cyclic dependency.

---

## 5. Algorithmic Correctness

**Soundness.** Pascal's identity states that for all integers $n, k \ge 1$:
$$
\binom{n}{k} = \binom{n-1}{k-1} + \binom{n-1}{k}
$$
Because the algorithm initializes the base cases $\binom{n}{0} = \binom{n}{n} = 1$ and computes all interior cells via Pascal's identity using the previous row, every generated value is mathematically identical to the corresponding binomial coefficient.

**Completeness.** Outer loops execute for $r = 0 \dots \text{numRows} - 1$, generating exactly $\text{numRows}$ rows. Each row $r$ generates exactly $r + 1$ elements, covering the complete triangular structure without omission.

---

## 6. Traps This Instance Exposes

- **1-based vs 0-based Row Counting:** `numRows` is the total count of rows (e.g. `numRows = 5` means 5 rows, indexed $0 \dots 4$).
- **Index Out of Bounds on Prior Row:** Interior index $c$ references `prev[c - 1]` and `prev[c]`. Since `prev` has length $r$ and $c < r$, `prev[c]` is always within bounds.
- **Symmetry Exploitation:** Note that $T(r, c) = T(r, r - c)$. While one could compute half the row and mirror it, simple sequential addition is so fast that direct accumulation is cleaner and avoids copying.

The boundary shapes below are all handled by the same two anchors and one
recurrence, so none of them needs a special branch:

| Scenario | Input | Required result | Why the recurrence still holds |
|:---|:---|:---|:---|
| Minimum input | `numRows = 1` | `[[1]]` | Row synthesis runs zero times; the seed already satisfies $T(0,0) = \binom{0}{0} = 1$ |
| Boundary-only row | $r = 1$ | `[1, 1]` | The interior range $1 \le c < r$ is empty, so only the anchors $T(1,0)$ and $T(1,1)$ are written |
| First interior cell | $r = 4$, $c = 1$ | $1 + 3 = 4$ | Its left parent $(r-1, c-1) = (3,0)$ is a row anchor and always exists |
| Last interior cell | $r = 4$, $c = 3$ | $3 + 1 = 4$ | Its right parent $(r-1, c) = (3,3)$ is a row anchor and always exists |
| Symmetric pair | $r = 3$, $c = 1$ and $c = 2$ | both $3$ | $T(r,c) = T(r, r-c)$ forces $\binom{3}{1} = \binom{3}{2}$ |
| One row past the instance | `numRows = 6` | sixth row `[1, 5, 10, 10, 5, 1]` | Row 5 derives from the completed row 4: $1+4=5$, $4+6=10$, $6+4=10$, $4+1=5$ |

These strategies all produce the identical triangle for $\text{numRows} = 5$;
they differ only in arithmetic volume and index discipline:

| Strategy | Additions for $\text{numRows} = 5$ | Auxiliary space | Trade-off |
|:---|:---:|:---|:---|
| Sequential additive recurrence (used above) | $6$ | $O(1)$ beyond the output; only the previous row is read | Simplest index arithmetic; each row is emitted the moment it is finished |
| Closed-form binomial evaluation per cell | $6$ evaluations, each needing products and exact division | $O(1)$ | More work per cell and a real risk of an inexact intermediate if the division order is chosen carelessly |
| Mirrored half-row | $4$, since only $c \le \lfloor r/2 \rfloor$ is computed | $O(1)$ | Saves two additions here but adds a mirroring step and a parity case when $r$ is even |

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N^2)$, where $N = \text{numRows}$. The algorithm calculates $1 + 2 + 3 + \dots + N = \frac{N(N+1)}{2}$ numbers, each taking $O(1)$ addition.
- **Auxiliary Space Complexity:** $O(1)$ beyond the required $O(N^2)$ output structure to store the rows.