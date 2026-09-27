# Guided Example: Maximal Rectangle

We trace the step-by-step reduction of a 2D binary matrix to row-by-row histogram evaluation on a representative matrix:

- **Input:**
  $$\text{matrix} = \begin{pmatrix} \text{'1'} & \text{'0'} & \text{'1'} & \text{'0'} & \text{'0'} \\ \text{'1'} & \text{'0'} & \text{'1'} & \text{'1'} & \text{'1'} \\ \text{'1'} & \text{'1'} & \text{'1'} & \text{'1'} & \text{'1'} \\ \text{'1'} & \text{'0'} & \text{'0'} & \text{'1'} & \text{'0'} \end{pmatrix}$$
- **Required output:** $6$

This instance demonstrates reducing 2D maximal rectangle discovery to dynamic column height accumulation, resetting heights to $0$ on `'0'`, running the monotonic stack histogram solver across each row, and identifying the maximal $2 \times 3 = 6$ submatrix in $O(M \cdot N)$ time.

---

## 1. Instance & Teaching Goal

Given an $M \times N$ binary matrix ($M = 4, N = 5$) filled with `'0'`s and `'1'`s:
$$
\begin{pmatrix}
1 & 0 & 1 & 0 & 0 \\
1 & 0 & \mathbf{1} & \mathbf{1} & \mathbf{1} \\
1 & 1 & \mathbf{1} & \mathbf{1} & \mathbf{1} \\
1 & 0 & 0 & 1 & 0
\end{pmatrix}
$$
find the largest rectangle containing only `'1'`s and return its area.

The maximal rectangle occupies rows $1 \dots 2$ across columns $2 \dots 4$:
- Height = $2$ rows
- Width = $3$ columns
- Total Area = $2 \times 3 = 6$

A naive brute-force search checking all $O(M^2 N^2)$ submatrices takes $O(M^3 N^3)$ time.
By viewing each row as the base of a dynamic histogram where bar heights represent consecutive vertical `'1'`s reaching upward, we can apply LeetCode 84's monotonic stack solver on each row. This reduces overall complexity to $O(M \cdot N)$ time and $O(N)$ space.

---

## 2. Conceptual Foundation & Invariants

### 2D-to-1D Histogram Reduction
Maintain a 1D array $\text{heights}$ of size $N$, initially filled with zeroes.
For each row $r \in [0, M - 1]$:
1. **Update Histogram Heights:**
   For each column $c \in [0, N - 1]$:
   - If $\text{matrix}[r][c] == \text{'1'}$:
     $$
     \text{heights}[c] \leftarrow \text{heights}[c] + 1
     $$
   - If $\text{matrix}[r][c] == \text{'0'}$:
     $$
     \text{heights}[c] \leftarrow 0
     $$
     *(A zero breaks consecutive vertical ones, resetting the column height to 0).*
2. **Solve Largest Rectangle in Histogram:**
   Pass the updated $\text{heights}$ array into the monotonic stack histogram algorithm:
   $$
   \text{row\_max} = \text{largestRectangleArea}(\text{heights})
   $$
   $$
   \text{global\_max} = \max(\text{global\_max}, \, \text{row\_max})
   $$

> **Invariant.** After processing row $r$, $\text{heights}[c]$ equals the exact number of contiguous `'1'` cells in column $c$ ending at row $r$. Any rectangle with base on row $r$ corresponds directly to a valid rectangle in the histogram $\text{heights}$.

---

## 3. Step-by-Step Worked Execution

We trace the $4 \times 5$ matrix:

### Row 0: `["1", "0", "1", "0", "0"]`
- Column heights updated:
  - $\text{heights} = [1, 0, 1, 0, 0]$.
- Monotonic stack evaluation:
  - Bars of height 1 exist at columns 0 and 2 (each width 1).
  - Maximum area for Row 0: $1 \times 1 = 1$.
- Running global max: $1$.

---

### Row 1: `["1", "0", "1", "1", "1"]`
- Column heights updated:
  - Col 0: `'1'` $\implies 1 + 1 = 2$.
  - Col 1: `'0'` $\implies 0$.
  - Col 2: `'1'` $\implies 1 + 1 = 2$.
  - Col 3: `'1'` $\implies 0 + 1 = 1$.
  - Col 4: `'1'` $\implies 0 + 1 = 1$.
  - $\text{heights} = [2, 0, 2, 1, 1]$.
- Monotonic stack evaluation:
  - Height 2 at col 0: area $2 \times 1 = 2$.
  - Height 2 at col 2: area $2 \times 1 = 2$.
  - Height 1 across cols $2 \dots 4$: width $3 \implies 1 \times 3 = 3$.
  - Maximum area for Row 1: $3$.
- Running global max: $\max(1, 3) = 3$.

---

### Row 2: `["1", "1", "1", "1", "1"]`
- Column heights updated:
  - All cells are `'1'`, so every column height increments by 1:
  - $\text{heights} = [3, 1, 3, 2, 2]$.
- Monotonic stack evaluation on $[3, 1, 3, 2, 2]$:
  - Height 3 at col 0: width 1 $\implies 3 \times 1 = 3$.
  - Height 1 spanning cols $0 \dots 4$: width 5 $\implies 1 \times 5 = 5$.
  - Height 3 at col 2: width 1 $\implies 3 \times 1 = 3$.
  - **Height 2 spanning cols $2 \dots 4$ ($[3, 2, 2]$):**
    - Both cols 2, 3, 4 have height $\ge 2$.
    - Width: $4 - 2 + 1 = 3$.
    - Area: $2 \times 3 = \mathbf{6}$!
  - Maximum area for Row 2: $6$.
- Running global max: $\max(3, 6) = \mathbf{6}$.

---

### Row 3: `["1", "0", "0", "1", "0"]`
- Column heights updated:
  - Col 0: `'1'` $\implies 3 + 1 = 4$.
  - Col 1: `'0'` $\implies 0$.
  - Col 2: `'0'` $\implies 0$.
  - Col 3: `'1'` $\implies 2 + 1 = 3$.
  - Col 4: `'0'` $\implies 0$.
  - $\text{heights} = [4, 0, 0, 3, 0]$.
- Monotonic stack evaluation:
  - Col 0 has height 4, width 1 $\implies 4 \times 1 = 4$.
  - Col 3 has height 3, width 1 $\implies 3 \times 1 = 3$.
  - Maximum area for Row 3: $4$.
- Running global max: $\max(6, 4) = 6$.

All rows evaluated. Final maximal rectangle area is $6$.

### Per-Column Run Ledger

Reading the same data column-first exposes the vertical half of the reduction. Each
column's height series is its run of consecutive `'1'`s ending at the current row, and a
`'0'` cell truncates that series:

| Column $c$ | Heights down rows $0 \dots 3$ | Longest vertical run of `'1'`s | Rows where the height is reset to $0$ |
|:---:|:---:|:---:|:---:|
| 0 | $1, 2, 3, 4$ | 4 (rows $0 \dots 3$) | none |
| 1 | $0, 0, 1, 0$ | 1 (row $2$) | 0, 1, 3 |
| 2 | $1, 2, 3, 0$ | 3 (rows $0 \dots 2$) | 3 |
| 3 | $0, 1, 2, 3$ | 3 (rows $1 \dots 3$) | 0 |
| 4 | $0, 1, 2, 0$ | 2 (rows $1 \dots 2$) | 0, 3 |

The answer cannot be read off the longest run alone: column 0 supports a run of $4$ but
is isolated horizontally, so its tallest rectangle is only $4 \times 1 = 4$. Conversely
the winning rectangle needs columns $2 \dots 4$ simultaneously, and their height series
agree on the value $2$ exactly at rows $1 \dots 2$, which is why the maximal area is
$2 \times 3 = 6$ rather than $3 \times 1$ or $1 \times 5$.

---

## 4. Complete Execution Trace

| Row $r$ | Matrix Row Content | Updated Column Heights $\text{heights}$ | Best Histogram Interval $[c_L, c_R]$ | Limiting Height $h$ | Width $w$ | Row Max Area | Global Max Area |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 0 | `["1", "0", "1", "0", "0"]` | `[1, 0, 1, 0, 0]` | $[0, 0]$ or $[2, 2]$ | 1 | 1 | 1 | 1 |
| 1 | `["1", "0", "1", "1", "1"]` | `[2, 0, 2, 1, 1]` | $[2, 4]$ | 1 | 3 | 3 | 3 |
| **2** | **`["1", "1", "1", "1", "1"]`** | **`[3, 1, 3, 2, 2]`** | **$[2, 4]$** | **2** | **3** | **6** | **6 (Max)** |
| 3 | `["1", "0", "0", "1", "0"]` | `[4, 0, 0, 3, 0]` | $[0, 0]$ | 4 | 1 | 4 | 6 |

### Candidate Intervals on the Decisive Row

Row 2 produces the winning rectangle, so it is worth enumerating its histogram
candidates exhaustively. Every maximal rectangle of a histogram has height equal to some
bar, and for each such height the best width is the widest interval whose minimum is at
least that height:

| Candidate interval | Limiting height $h$ | Columns spanned | Width $w$ | Area | Why this is the maximal span at that height |
|:---|:---:|:---:|:---:|:---:|:---|
| $[0, 0]$ | 3 | 0 | 1 | $3 \times 1 = 3$ | Column 1 has height $1 < 3$, so the height-$3$ block is capped immediately on the right. |
| $[0, 4]$ | 1 | $0 \dots 4$ | 5 | $1 \times 5 = 5$ | Every column has height $\ge 1$ and column 1 is the single minimum, so the span cannot grow. |
| $[2, 2]$ | 3 | 2 | 1 | $3 \times 1 = 3$ | Column 1 caps it on the left and column 3 (height $2$) caps it on the right. |
| $[2, 4]$ | 2 | $2 \dots 4$ | 3 | $2 \times 3 = \mathbf{6}$ | Columns 2, 3, 4 all have height $\ge 2$ while column 1 has height $1$, so this is the widest height-$2$ interval. |

The height-$2$ candidate is the largest of the four. Row 2 is the first row that admits a
height-$2$ interval of width $3$: on row 1 the same columns held heights $2, 1, 1$, so
their minimum was only $1$ and the identical span yielded just $1 \times 3 = 3$. Row 3
then destroys the span by resetting columns 2 and 4 to $0$, which is why the global
maximum stays at $6$.

---

## 5. Algorithmic Correctness

**Soundness.** Any contiguous all-ones rectangle has a defined bottom row $r$ and height $h$. Because $\text{heights}[c]$ tracks the number of consecutive ones ending at row $r$, every column $c$ spanned by the rectangle has $\text{heights}[c] \ge h$. The histogram subroutine is proven to find the maximal rectangle in any histogram, so it is guaranteed to discover this candidate.

**Completeness.** Every candidate all-ones rectangle in the matrix must have its bottom edge on some row $r \in [0, M - 1]$. Since all $M$ rows are tested, no maximal rectangle can be omitted.

---

## 6. Traps This Instance Exposes

- **Failing to Reset on `'0'`:** If $\text{matrix}[r][c] == \text{'0'}$, $\text{heights}[c]$ must be immediately set to $0$. Merely keeping the previous height would allow rectangles to jump across zero cells.
- **Empty Matrix Guards:** Matrices with zero rows ($M = 0$) or zero columns ($N = 0$) must return $0$ upfront to avoid out-of-bounds indexing.
- **Single Row Matrix:** If $M = 1$, the loop runs once, correctly evaluating the maximum run of consecutive `'1'`s.

### Boundary Instances and Their Verdicts

| Instance | `matrix` | Expected area | Boundary exercised | Why the reduction still answers correctly |
|:---|:---|:---:|:---|:---|
| Interior rectangle | `[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]` | 6 | Short bars capping a tall block | The block is exactly the height-$2$, width-$3$ interval found by the row-2 histogram pass. |
| No `'1'` cell | `[["0"]]` | 0 | Single zero cell | The only height is reset to $0$, so every histogram candidate has area $0$. |
| Single `'1'` cell | `[["1"]]` | 1 | Smallest non-empty rectangle | The height array becomes $[1]$ and the histogram pass returns $1 \times 1 = 1$. |
| All-one square | `[["1","1"],["1","1"]]` | 4 | No reset ever occurs | Heights grow to $[2, 2]$ on the second row, giving width $2$ at height $2$. |
| Zero splits wide rectangles | `[["1","1","0","1"],["1","1","0","1"],["1","1","1","1"]]` | 6 | A zero that forbids spanning | Heights reach $[3, 3, 1, 3]$ on row $2$; the left pair yields $3 \times 2 = 6$, and the zero column prevents any wider combination. |

---

## 7. Complexity Derivation

- **Time Complexity:** $O(M \cdot N)$. For each of the $M$ rows, updating the height array takes $O(N)$ time, and solving the histogram with a monotonic stack takes $O(N)$ time ($M \times O(N) = O(M \cdot N)$).
- **Auxiliary Space Complexity:** $O(N)$ to store the 1D $\text{heights}$ array and the monotonic stack.
