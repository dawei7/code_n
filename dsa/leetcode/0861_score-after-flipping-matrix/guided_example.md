# Guided Example: Score After Flipping Matrix

We trace the step-by-step most significant bit dominance proof, row inversion normalization, column bit frequency counting, greedy column flipping, and binary positional weight summation on representative binary matrices:

- **Input:**
  $$
  grid = \begin{bmatrix}
  0 & 0 & 1 & 1 \\
  1 & 0 & 1 & 0 \\
  1 & 1 & 0 & 0
  \end{bmatrix}
  $$
- **Required output:** `39`
  - Matrix score rules:
    - Dimensions: $m = 3$ rows, $n = 4$ columns.
    - We can toggle all bits in any row any number of times ($0 \leftrightarrow 1$).
    - We can toggle all bits in any column any number of times ($0 \leftrightarrow 1$).
    - Each row is interpreted as an unsigned binary integer with column $0$ as the most significant bit (MSB, weight $2^{n-1} = 2^3 = 8$) and column $n - 1$ as the least significant bit (LSB, weight $2^0 = 1$).
    - Objective: Maximize the total sum of all $m$ row integers.
- **Most Significant Bit Dominance & Decoupled Greed Invariant:**
  - **The MSB Priority Lemma:**
    - The place value of the leftmost bit is:
      $$
      2^{n-1} > \sum_{k=0}^{n-2} 2^k = 2^{n-1} - 1
      $$
    - Having a $1$ at column $0$ is strictly greater than having $1$s at every remaining bit position combined!
    - Therefore, **every single row must have its leftmost bit set to $1$**.
    - If row $i$ has $grid[i][0] == 0$, we **must flip row $i$**. If $grid[i][0] == 1$, we must not flip row $i$.
    - This uniquely fixes the row flip decision for all $m$ rows!
  - **Independent Column Flipping:**
    - Once row orientations are fixed, each column $j$ ($j \in [0, n - 1]$) can be flipped independently of all other columns.
    - A column flip toggles every bit in column $j$ across all $m$ rows.
    - Let $cnt$ be the number of $1$s currently in column $j$. If we flip the column, the number of $1$s becomes $m - cnt$.
    - To maximize column $j$'s contribution to the total score, we choose:
      $$
      \text{ones}(j) = \max(cnt, m - cnt)
      $$
    - Total contribution of column $j$ is $\text{ones}(j) \times 2^{n - 1 - j}$.

---

## 1. Instance & Teaching Goal

Given the $3 \times 4$ binary matrix:
$$
\begin{bmatrix}
0 & 0 & 1 & 1 \\
1 & 0 & 1 & 0 \\
1 & 1 & 0 & 0
\end{bmatrix}
$$
Derive the row and column operations that maximize the score.

```text
Initial Matrix:
Row 0: [0, 0, 1, 1]  (MSB is 0 -> MUST FLIP)
Row 1: [1, 0, 1, 0]  (MSB is 1 -> Keep)
Row 2: [1, 1, 0, 0]  (MSB is 1 -> Keep)

After Row Flips:
Row 0: [1, 1, 0, 0]
Row 1: [1, 0, 1, 0]
Row 2: [1, 1, 0, 0]

Column 0 (weight 8): count(1) = 3 -> 3 * 8 = 24
Column 1 (weight 4): count(1) = 2, count(0) = 1 -> keep (2 ones) -> 2 * 4 = 8
Column 2 (weight 2): count(1) = 1, count(0) = 2 -> flip (2 ones) -> 2 * 2 = 4
Column 3 (weight 1): count(1) = 0, count(0) = 3 -> flip (3 ones) -> 3 * 1 = 3

Total Max Score = 24 + 8 + 4 + 3 = 39
```

The teaching goal is to show how binary positional arithmetic decouples row-level decisions from column-level optimizations.

---

## 2. Conceptual Foundation & Invariants

### 1. Row Inversion Vector:
For each row $i \in [0, m - 1]$:
$$
\text{flip\_row}[i] = (grid[i][0] == 0)
$$
Under this rule, after row normalization, every element at $(i, j)$ has effective value:
$$
grid'[i][j] = grid[i][j] \oplus \text{flip\_row}[i]
$$
where $\oplus$ is the bitwise XOR (toggle) operator.

### 2. Column-Wise Optimal Majority:
For column $j$:
$$
cnt_j = \sum_{i=0}^{m-1} grid'[i][j]
$$
$$
\text{best\_ones}_j = \max(cnt_j, m - cnt_j)
$$

### 3. Positional Score Accumulation:
$$
\text{Total Score} = \sum_{j=0}^{n-1} \text{best\_ones}_j \times 2^{n - 1 - j}
$$

---

## 3. Step-by-Step Worked Execution

We trace the $3 \times 4$ matrix:

---

### Step 1: Normalize Rows by MSB
- **Row 0: `[0, 0, 1, 1]`**
  - First element is $0$.
  - Flip row: $0 \to 1, 0 \to 1, 1 \to 0, 1 \to 0$.
  - Transformed: `[1, 1, 0, 0]`.
- **Row 1: `[1, 0, 1, 0]`**
  - First element is $1$. Keep unchanged.
  - Transformed: `[1, 0, 1, 0]`.
- **Row 2: `[1, 1, 0, 0]`**
  - First element is $1$. Keep unchanged.
  - Transformed: `[1, 1, 0, 0]`.

Matrix after Step 1:
$$
\begin{bmatrix}
1 & 1 & 0 & 0 \\
1 & 0 & 1 & 0 \\
1 & 1 & 0 & 0
\end{bmatrix}
$$

---

### Step 2: Evaluate Column 0 ($j = 0$, Weight $2^{4-1-0} = 2^3 = 8$)
- Column values: $[1, 1, 1]$.
- Count of $1$s: $cnt_0 = 3$.
- Count of $0$s: $m - cnt_0 = 0$.
- $\max(3, 0) = 3$.
- Contribution: $3 \times 8 = \mathbf{24}$.
- Running sum: $24$.

---

### Step 3: Evaluate Column 1 ($j = 1$, Weight $2^{4-1-1} = 2^2 = 4$)
- Column values: $[1, 0, 1]$.
- Count of $1$s: $cnt_1 = 2$.
- Count of $0$s: $m - cnt_1 = 1$.
- Comparison: $2 > 1 \implies$ do not flip column.
- $\max(2, 1) = 2$.
- Contribution: $2 \times 4 = \mathbf{8}$.
- Running sum: $24 + 8 = 32$.

---

### Step 4: Evaluate Column 2 ($j = 2$, Weight $2^{4-1-2} = 2^1 = 2$)
- Column values: $[0, 1, 0]$.
- Count of $1$s: $cnt_2 = 1$.
- Count of $0$s: $m - cnt_2 = 2$.
- Comparison: $2 > 1 \implies$ **flip column 2!**
- Toggled values become $[1, 0, 1]$, giving $2$ ones.
- Contribution: $2 \times 2 = \mathbf{4}$.
- Running sum: $32 + 4 = 36$.

---

### Step 5: Evaluate Column 3 ($j = 3$, Weight $2^{4-1-3} = 2^0 = 1$)
- Column values: $[0, 0, 0]$.
- Count of $1$s: $cnt_3 = 0$.
- Count of $0$s: $m - cnt_3 = 3$.
- Comparison: $3 > 0 \implies$ **flip column 3!**
- Toggled values become $[1, 1, 1]$, giving $3$ ones.
- Contribution: $3 \times 1 = \mathbf{3}$.
- Running sum: $36 + 3 = \mathbf{39}$.

---

## 4. Complete Execution Trace

| Column $j$ | Bit Weight ($2^{n-1-j}$) | Normalized Column Bits | Number of $1$s ($cnt$) | Number of $0$s ($m - cnt$) | Column Action | Optimal Ones Count | Column Score Contribution | Running Total Score |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| $0$ | $2^3 = 8$ | $[1, 1, 1]$ | $3$ | $0$ | Keep | $3$ | $3 \times 8 = 24$ | $24$ |
| $1$ | $2^2 = 4$ | $[1, 0, 1]$ | $2$ | $1$ | Keep | $2$ | $2 \times 4 = 8$ | $32$ |
| $2$ | $2^1 = 2$ | $[0, 1, 0]$ | $1$ | $2$ | **Flip** | $2$ | $2 \times 2 = 4$ | $36$ |
| **$3$** | **$2^0 = 1$** | $[0, 0, 0]$ | $0$ | $3$ | **Flip** | $3$ | $3 \times 1 = 3$ | **`39`** |

---

## 5. Boundary Cases & Failure Modes

- **$1 \times 1$ Matrix (e.g. `[[0]]`):** Single cell with $0$. Flip row $\to [1]$. Weight $2^0 = 1$. Returns $1$.
- **All Rows Already Start with $1$:** No row flips needed; immediately evaluates optimal column majorities.
- **Ties in Column Bit Counts ($m$ is even, $cnt = m / 2$):** Both keeping and flipping produce $m/2$ ones; score contribution is identical either way.

---

## 6. Traps & Common Anti-Patterns

- **Trying All $2^m$ Row Flip Combinations:** Exploring all possible row toggle subsets takes $\mathcal{O}(2^m \cdot n)$ time. When $m = 20$, $2^{20} > 10^6$ iterations causes TLE. The MSB dominance lemma proves the first column greedily determines all row flips.
- **Flipping Column 0:** Flipping column 0 after setting all rows to 1 would turn all MSBs to 0, destroying the highest possible value.
- **Modifying the Grid In-Place Unnecessarily:** Calculating effective bits mathematically via `(grid[i][j] == grid[i][0])` allows finding the answer in $\mathcal{O}(1)$ auxiliary space without mutating inputs.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Inverting rows based on column 0: $\mathcal{O}(m \cdot n)$.
  - Tallying ones across all $n$ columns: $\mathcal{O}(m \cdot n)$.
  - Total Time: $\mathcal{O}(m \cdot n)$, running in $< 1$ ms for $m, n \le 20$.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(1)$ additional memory if computing virtual bit states on the fly.
