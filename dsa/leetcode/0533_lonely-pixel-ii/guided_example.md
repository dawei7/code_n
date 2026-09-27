# Guided Example: Lonely Pixel II

We trace the step-by-step row black pixel counting ($rows[i]$), column inverted index grouping ($g[j] = \{i \mid picture[i][j] == \text{'B'}\}$), target quota validation ($rows[i] == target \land |g[j]| == target$), row vector equality verification ($\forall i_2 \in g[j], picture[i_2] == picture[i_1]$), and qualified column pixel summation ($ans \mathrel{+}= target$) on representative matrices:

- **Input:**
  $$
  picture = \begin{bmatrix}
  W & B & W & B & B & W \\
  W & B & W & B & B & W \\
  W & B & W & B & B & W \\
  W & W & B & W & B & W
  \end{bmatrix}, \quad target = 3
  $$
- **Required output:** `6`
  - Dimensions: $m = 4$ rows, $n = 6$ columns.
  - Black lonely pixel rule (with integer $target$): A black pixel `'B'` at $(r, c)$ qualifies if and only if:
    1. Row $r$ has **exactly $target$** black pixels.
    2. Column $c$ has **exactly $target$** black pixels.
    3. Every row containing a black pixel in column $c$ is **completely identical** to row $r$.
- **Two-Phase Grouping & Validation Trace:**
  - **Phase 1: Compute Row Sums & Inverted Column Index:**
    - Row 0: `["W", "B", "W", "B", "B", "W"]` $\implies rows[0] = \mathbf{3}$ (columns 1, 3, 4)
    - Row 1: `["W", "B", "W", "B", "B", "W"]` $\implies rows[1] = \mathbf{3}$ (columns 1, 3, 4)
    - Row 2: `["W", "B", "W", "B", "B", "W"]` $\implies rows[2] = \mathbf{3}$ (columns 1, 3, 4)
    - Row 3: `["W", "W", "B", "W", "B", "W"]` $\implies rows[3] = \mathbf{2}$ (columns 2, 4)
    - Column inverted index $g[j]$ (which rows have `'B'` in column $j$):
      - Col 0: $g[0] = []$
      - Col 1: $g[1] = [0, 1, 2]$
      - Col 2: $g[2] = [3]$
      - Col 3: $g[3] = [0, 1, 2]$
      - Col 4: $g[4] = [0, 1, 2, 3]$
      - Col 5: $g[5] = []$
  - **Phase 2: Evaluate Columns with Active `'B'` Pixels:**
    - **Column 1 ($g[1] = [0, 1, 2]$):**
      - Number of `'B'`s in column 1: $|g[1]| = 3 == target$ (Pass!).
      - Inspect row 0: $rows[0] = 3 == target$ (Pass!).
      - Test row equality:
        - Row 0: `W B W B B W`
        - Row 1: `W B W B B W` (Identical!)
        - Row 2: `W B W B B W` (Identical!)
      - All rows in $g[1]$ are identical!
      - All $3$ pixels at $(0, 1), (1, 1), (2, 1)$ are valid lonely pixels:
        $$
        ans \leftarrow 0 + target = 0 + 3 = \mathbf{3}
        $$
    - **Column 2 ($g[2] = [3]$):**
      - $|g[2]| = 1 \ne target (3) \implies$ Fails column count check. Skip.
    - **Column 3 ($g[3] = [0, 1, 2]$):**
      - $|g[3]| = 3 == target$ (Pass!).
      - $rows[0] = 3 == target$ (Pass!).
      - Rows $0, 1, 2$ are identical (Pass!).
      - Add $3$ pixels:
        $$
        ans \leftarrow 3 + 3 = \mathbf{6}
        $$
    - **Column 4 ($g[4] = [0, 1, 2, 3]$):**
      - $|g[4]| = 4 \ne target (3) \implies$ Overloaded column (contains 4 black pixels). Skip.
  - Columns 0 and 5 have no `'B'` pixels.
  - Final total black lonely pixels: **`6`** (from columns 1 and 3).
- **Heterogeneous Row Mismatch Instance:**
  - If a column has $target$ black pixels across rows $A$ and $B$, but row $A$ has `'B'` at col 0 while row $B$ has `'B'` at col 1 $\implies picture[A] \ne picture[B] \implies$ Rejected.
- **Single Match with $target = 1$:**
  - Identical to Lonely Pixel I: only single isolated pixels without conflicting rows qualify.

This instance demonstrates equivalence relation clustering on 2D boolean matrices, mathematically proves why column-wise row vector congruence checks avoid per-pixel pairwise redundancy, and derives $O(M \cdot N)$ runtime and $O(M \cdot N)$ space bounds.

---

## 1. Instance & Teaching Goal

Given an $m \times n$ picture with pixels `'B'` and `'W'` and an integer $target$:
A black pixel $(r, c)$ is a **black lonely pixel** if:
1. Row $r$ contains exactly $target$ black pixels.
2. Column $c$ contains exactly $target$ black pixels.
3. Every row that contains a black pixel in column $c$ is **identical** to row $r$.
Find the total number of black lonely pixels.

```text
Target = 3
Picture:
  Row 0: [ W, [B], W, [B],  B,  W ]  (3 'B's)
  Row 1: [ W, [B], W, [B],  B,  W ]  (3 'B's, identical to Row 0)
  Row 2: [ W, [B], W, [B],  B,  W ]  (3 'B's, identical to Row 0)
  Row 3: [ W,  W,  B,  W,   B,  W ]  (2 'B's)
           |   |   |   |    |   |
  Col 'B': 0   3   1   3    4   0

Col 1: exactly 3 'B's, rows 0,1,2 identical -> 3 lonely pixels
Col 3: exactly 3 'B's, rows 0,1,2 identical -> 3 lonely pixels
Col 4: has 4 'B's != target (3) -> Rejected

Total = 3 + 3 = 6
```

### Why Column-Centric Evaluation is Optimal
- If column $c$ satisfies the conditions:
  - All $target$ black pixels in column $c$ simultaneously qualify!
  - Because all rows with a black pixel in column $c$ must be identical, checking column $c$ once determines the qualification of all its $target$ pixels in one step.
  - Adding $target$ for each valid column solves the problem in a single column pass.

---

## 2. Conceptual Foundation & Invariants

### 1. Inverted Column Index:
- Let $rows[i]$ be the count of `'B'` in row $i$.
- Let $g[j]$ be the list of row indices that have `'B'` in column $j$:
  $$
  g[j] = \{i \mid picture[i][j] == \text{'B'}\}
  $$

### 2. The Column Qualification Test:
For each column $j$ with $g[j] \ne \emptyset$:
Let $i_1 = g[j][0]$ be the first row in $g[j]$:
1. Check row quota: $rows[i_1] == target$.
2. Check column quota: $|g[j]| == target$.
3. Check row congruence:
   $$
   \forall i_2 \in g[j], \quad picture[i_2] == picture[i_1]
   $$
If all three conditions hold:
$$
ans \leftarrow ans + target
$$

> **Column Homogeneity Invariant.** When all rows having `'B'` in column $c$ are identical, each of those rows has the exact same black pixel pattern, ensuring mutual and symmetric compliance with the lonely pixel rule.

---

## 3. Step-by-Step Worked Execution

We trace the $4 \times 6$ matrix with $target = 3$:

---

### Step 1: Precompute Row Counts and Column Groups
- $rows = [3, 3, 3, 2]$.
- $g[1] = [0, 1, 2]$
- $g[2] = [3]$
- $g[3] = [0, 1, 2]$
- $g[4] = [0, 1, 2, 3]$
- $ans = 0$.

---

### Step 2: Test Columns

1. **Column 1 ($g[1] = [0, 1, 2]$):**
   - First row $i_1 = 0 \implies rows[0] = 3 == 3$.
   - Column size $|g[1]| = 3 == 3$.
   - Check rows $0, 1, 2$:
     - $picture[0] == picture[1]$: True
     - $picture[0] == picture[2]$: True
   - All conditions hold!
   - $ans \leftarrow 0 + 3 = \mathbf{3}$.

2. **Column 2 ($g[2] = [3]$):**
   - $|g[2]| = 1 \ne 3 \implies$ Skip.

3. **Column 3 ($g[3] = [0, 1, 2]$):**
   - $rows[0] = 3 == 3$.
   - $|g[3]| = 3 == 3$.
   - Rows $0, 1, 2$ are identical: True.
   - All conditions hold!
   - $ans \leftarrow 3 + 3 = \mathbf{6}$.

4. **Column 4 ($g[4] = [0, 1, 2, 3]$):**
   - $|g[4]| = 4 \ne 3 \implies$ Skip.

---

### Step 3: Result
$$
ans = \mathbf{6}
$$

---

## 4. Complete Execution Trace

| Column $j$ | Rows Containing `'B'` ($g[j]$) | Column Count $|g[j]|$ | First Row Count $rows[i_1]$ | Rows Identical? | Valid Column? | Contribution to $ans$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **$1$** | $[0, 1, 2]$ | $3$ | $3$ | **Yes** | **Yes** | $+3$ (Total: 3) |
| $2$ | $[3]$ | $1$ | $2$ | — | No ($|g| \ne 3$) | $0$ |
| **$3$** | $[0, 1, 2]$ | $3$ | $3$ | **Yes** | **Yes** | $+3$ (Total: 6) |
| $4$ | $[0, 1, 2, 3]$ | $4$ | $3$ | No ($rows[3] \ne rows[0]$) | No ($|g| \ne 3$) | $0$ |
| **Final** | — | — | — | — | — | **Result: $6$** |

---

## 5. Boundary Cases & Failure Modes

- **$target > \min(m, n)$:** Impossible to have $target$ pixels in a row/column $\implies \mathbf{0}$.
- **All Rows Identical with Exactly $target$ `'B'`s:** Every column containing `'B'` satisfies the conditions $\implies$ all $m \times target$ black pixels qualify.
- **Rows Have Equal Counts but Different Patterns:** If row 0 is `[B, B, W]` and row 1 is `[W, B, B]`, both have 2 `'B'`s, but `picture[0] != picture[1]`. Column 1 fails the row congruence test $\implies$ correctly returns 0.

---

## 6. Traps & Common Anti-Patterns

- **Comparing Only the Black Pixel Positions:** Rule 2 requires that the *entire rows* are identical, not just that they have `'B'` in column $c$. Checking `picture[i2] == picture[i1]` guarantees full row equality.
- **Per-Pixel Iteration with Redundant Congruence Checks:** Iterating through all $M \times N$ cells and re-checking row equality each time takes $O(M^2 \cdot N)$ time. Processing per-column tests each group of $target$ rows exactly once in $O(M \cdot N)$ time.
- **Missing the $|g[j]| == target$ Check:** If $|g[j]| > target$, there are too many black pixels in that column, which must be rejected even if the first row has $rows[i_1] == target$.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Building row counts and inverted column lists takes $O(M \cdot N)$ time.
  - For each column with $\le target$ rows, row equality checks compare strings of length $N$.
  - At most $N$ columns, each doing at most $target$ string comparisons.
  - Total Time: $\mathcal{O}(M \cdot N)$. For $N, M \le 200$, completes in $< 10$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(M \cdot N)$ space to store the column inverted lists $g$.
