# Guided Example: Edit Distance

We trace the step-by-step 2D Levenshtein dynamic programming matrix evaluation on a representative string transformation:

- **Input:** $\text{word1} = \text{"horse"}$, $\text{word2} = \text{"ros"}$
- **Required output:** $3$

This instance demonstrates string edit operations (insert, delete, replace), constructing the 2D prefix distance table, identifying diagonal match carryovers ($\text{word1}[i-1] == \text{word2}[j-1]$), and tracing the optimal 3-step transformation sequence.

---

## 1. Instance & Teaching Goal

Given two strings $\text{word1}$ of length $M = 5$ (`"horse"`) and $\text{word2}$ of length $N = 3$ (`"ros"`), find the minimum number of operations required to convert $\text{word1}$ into $\text{word2}$.

The permitted operations are:
1. **Insert** a character.
2. **Delete** a character.
3. **Replace** a character.

For `"horse"` and `"ros"`, the minimal conversion takes 3 operations:
1. Replace `'h'` with `'r'` $\longrightarrow$ `"rorse"`
2. Remove middle `'r'` $\longrightarrow$ `"rose"`
3. Remove trailing `'e'` $\longrightarrow$ `"ros"`

A naive recursive exploration evaluates branching choices of size $3^{M+N}$.
Dynamic programming builds the optimal solution by defining prefix subproblems over prefixes $\text{word1}[0 \dots i-1]$ and $\text{word2}[0 \dots j-1]$, solving the problem in $O(M \cdot N)$ time.

---

## 2. Conceptual Foundation & Invariants

### 2D Levenshtein Recurrence
Let $DP[i][j]$ be the minimum edit distance between prefix $\text{word1}[0 \dots i-1]$ (length $i$) and prefix $\text{word2}[0 \dots j-1]$ (length $j$).

#### Base Cases
- Transforming any string of length $i$ to an empty string requires $i$ deletions:
  $$
  DP[i][0] = i \quad \forall i \in [0, M]
  $$
- Transforming an empty string to a string of length $j$ requires $j$ insertions:
  $$
  DP[0][j] = j \quad \forall j \in [0, N]
  $$

#### General State Transitions ($i \ge 1, j \ge 1$)
1. **Matching Characters ($\text{word1}[i-1] == \text{word2}[j-1]$):**
   No operation is needed for the current characters; carry over previous diagonal cost:
   $$
   DP[i][j] = DP[i - 1][j - 1]
   $$
2. **Mismatched Characters ($\text{word1}[i-1] \ne \text{word2}[j-1]$):**
   Choose the minimum of the three valid edit operations, plus cost 1:
   $$
   DP[i][j] = 1 + \min \begin{cases}
   DP[i - 1][j] & \text{(Deletion of } \text{word1}[i-1]\text{)} \\
   DP[i][j - 1] & \text{(Insertion of } \text{word2}[j-1]\text{)} \\
   DP[i - 1][j - 1] & \text{(Replacement of } \text{word1}[i-1] \text{ with } \text{word2}[j-1]\text{)}
   \end{cases}
   $$

> **Invariant.** Entry $DP[i][j]$ holds the strictly minimal edit distance between the first $i$ letters of `word1` and the first $j$ letters of `word2`.

---

## 3. Step-by-Step Worked Execution

We construct the $6 \times 4$ DP table for $\text{word1} = \text{"horse"}$ and $\text{word2} = \text{"ros"}$:

### Base Row & Column Initialization
- Row 0 ($\text{word1} = \text{""}$): $[0, 1, 2, 3]$ (pure insertions).
- Column 0 ($\text{word2} = \text{""}$): $DP[0][0]=0, DP[1][0]=1, DP[2][0]=2, DP[3][0]=3, DP[4][0]=4, DP[5][0]=5$ (pure deletions).

---

### Row 1: $\text{word1}[0] = \text{'h'}$
- $j = 1$ (`'r'`): Mismatch. $1 + \min(DP[0][1]=1, DP[1][0]=1, DP[0][0]=0) = 1 + 0 = 1$.
- $j = 2$ (`'o'`): Mismatch. $1 + \min(DP[0][2]=2, DP[1][1]=1, DP[0][1]=1) = 1 + 1 = 2$.
- $j = 3$ (`'s'`): Mismatch. $1 + \min(DP[0][3]=3, DP[1][2]=2, DP[0][2]=2) = 1 + 2 = 3$.
Row 1: `[1, 1, 2, 3]`.

---

### Row 2: $\text{word1}[1] = \text{'o'}$
- $j = 1$ (`'r'`): Mismatch. $1 + \min(DP[1][1]=1, DP[2][0]=2, DP[1][0]=1) = 1 + 1 = 2$.
- $j = 2$ (`'o'`): **Match!** Inherit diagonal $DP[1][1] = 1$.
- $j = 3$ (`'s'`): Mismatch. $1 + \min(DP[1][3]=3, DP[2][2]=1, DP[1][2]=2) = 1 + 1 = 2$.
Row 2: `[2, 2, 1, 2]`.

---

### Row 3: $\text{word1}[2] = \text{'r'}$
- $j = 1$ (`'r'`): **Match!** Inherit diagonal $DP[2][0] = 2$.
- $j = 2$ (`'o'`): Mismatch. $1 + \min(DP[2][2]=1, DP[3][1]=2, DP[2][1]=2) = 1 + 1 = 2$.
- $j = 3$ (`'s'`): Mismatch. $1 + \min(DP[2][3]=2, DP[3][2]=2, DP[2][2]=1) = 1 + 1 = 2$.
Row 3: `[3, 2, 2, 2]`.

---

### Row 4: $\text{word1}[3] = \text{'s'}$
- $j = 1$ (`'r'`): Mismatch. $1 + \min(DP[3][1]=2, DP[4][0]=4, DP[3][0]=3) = 1 + 2 = 3$.
- $j = 2$ (`'o'`): Mismatch. $1 + \min(DP[3][2]=2, DP[4][1]=3, DP[3][1]=2) = 1 + 2 = 3$.
- $j = 3$ (`'s'`): **Match!** Inherit diagonal $DP[3][2] = 2$.
Row 4: `[4, 3, 3, 2]`.

---

### Row 5: $\text{word1}[4] = \text{'e'}$
- $j = 1$ (`'r'`): Mismatch. $1 + \min(DP[4][1]=3, DP[5][0]=5, DP[4][0]=4) = 1 + 3 = 4$.
- $j = 2$ (`'o'`): Mismatch. $1 + \min(DP[4][2]=3, DP[5][1]=4, DP[4][1]=3) = 1 + 3 = 4$.
- $j = 3$ (`'s'`): Mismatch. $1 + \min(DP[4][3]=2, DP[5][2]=4, DP[4][2]=3) = 1 + 2 = \mathbf{3}$.
Row 5: `[5, 4, 4, 3]`.

Terminal minimum edit distance is $DP[5][3] = 3$.

---

## 4. Complete Execution Trace

### 2D Levenshtein DP Distance Table

| $\text{word1} \downarrow \setminus \text{word2} \to$ | $\emptyset$ | `'r'` | `'o'` | `'s'` |
|:---:|:---:|:---:|:---:|:---:|
| **$\emptyset$** | **0** | 1 | 2 | 3 |
| **`'h'`** | 1 | **1 (Replace)** | 2 | 3 |
| **`'o'`** | 2 | 2 | **1 (Match)** | 2 |
| **`'r'`** | 3 | 2 | 2 | **2 (Delete)** |
| **`'s'`** | 4 | 3 | 3 | **2 (Match)** |
| **`'e'`** | 5 | 4 | 4 | **3 (Delete / Target)** |

---

### Optimal Backtrace from the Target Cell

A filled table reports the cost, but the actual edit script is recovered by walking from $(M, N)$ back toward $(0, 0)$ and always stepping to a predecessor that attained the current cell's value. A tie between predecessors is harmless: each minimal predecessor yields an equally short script.

| Step | Current cell $(i, j)$ | $DP[i][j]$ | `word1[i-1]` | `word2[j-1]` | Chosen predecessor | Operation | Next cell |
|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| 1 | $(5, 3)$ | 3 | `'e'` | `'s'` | $(4, 3)$ with $DP = 2$ | Delete `'e'` from `word1` | $(4, 3)$ |
| 2 | $(4, 3)$ | 2 | `'s'` | `'s'` | $(3, 2)$ with $DP = 2$ | Characters agree, so the diagonal is free | $(3, 2)$ |
| 3 | $(3, 2)$ | 2 | `'r'` | `'o'` | $(2, 2)$ with $DP = 1$ | Delete `'r'` from `word1` | $(2, 2)$ |
| 4 | $(2, 2)$ | 1 | `'o'` | `'o'` | $(1, 1)$ with $DP = 1$ | Characters agree, so the diagonal is free | $(1, 1)$ |
| 5 | $(1, 1)$ | 1 | `'h'` | `'r'` | $(0, 0)$ with $DP = 0$ | Replace `'h'` with `'r'` | $(0, 0)$ |

The walk lands on the origin after exactly three charged operations, which is consistent with $DP[5][3] = 3$. Read forward, it reproduces the script named at the top of the lesson: `"horse"` becomes `"rorse"`, then `"rose"`, then `"ros"`.

---

## 5. Algorithmic Correctness

**Soundness.** Any string alignment between $\text{word1}[0 \dots i-1]$ and $\text{word2}[0 \dots j-1]$ must align $\text{word1}[i-1]$ with $\text{word2}[j-1]$ (either matching or replacement), delete $\text{word1}[i-1]$, or insert $\text{word2}[j-1]$. By exploring the minimum of these three mutually exclusive choices at every cell, the optimal substructure is preserved.

**Completeness.** Computing cells in row-major order guarantees that the three predecessor cells $(i-1, j)$, $(i, j-1)$, and $(i-1, j-1)$ are fully resolved before cell $(i, j)$ is evaluated. Cell $(M, N)$ is provably the minimum global distance.

---

## 6. Traps This Instance Exposes

- **Base Column/Row Non-Zero Initialization:** Forgetting to initialize $DP[i][0] = i$ and $DP[0][j] = j$ causes conversions to/from empty prefixes to be miscounted as free ($0$).
- **Match Operation Has Cost 0:** When characters match, do not add $+1$. The cost is carried directly from the top-left diagonal without modification ($DP[i][j] = DP[i-1][j-1]$).
- **Space Optimization:** Since row $i$ depends only on row $i - 1$, the table can be computed using two 1D rows of length $N + 1$, reducing memory from $O(M \cdot N)$ to $O(N)$.

---

## 7. Complexity Derivation

### Variant Comparison

The same recurrence admits several state representations with different constant factors and different amounts of recoverable information.

| Variant | State retained | Time | Auxiliary space | Material failure mode |
|:---|:---|:---|:---|:---|
| Plain recursion on suffixes | Call stack only | $O(3^{M+N})$ | $O(M + N)$ stack | Re-solves each suffix pair exponentially many times |
| Memoized recursion | Cache keyed by $(i, j)$ | $O(M \cdot N)$ | $O(M \cdot N)$ | Needs $O(M + N)$ stack depth, so long inputs can exhaust the recursion limit |
| Full 2D bottom-up table (used here) | $(M+1) \times (N+1)$ matrix | $O(M \cdot N)$ | $O(M \cdot N)$ | Retains every row although only row $i - 1$ is ever read |
| Two rolling rows | Previous row and current row | $O(M \cdot N)$ | $O(N)$ | Discards earlier rows, so no row-major backtrace is possible afterwards |
| One row plus a saved diagonal scalar | Current row and one saved scalar | $O(M \cdot N)$ | $O(N)$ | Recovers the optimal cost but not the edit script unless predecessors are recorded separately |

- **Time Complexity:** $O(M \cdot N)$, where $M = |\text{word1}|$ and $N = |\text{word2}|$. The table has $(M + 1)(N + 1)$ cells, each taking $O(1)$ constant time.
- **Auxiliary Space Complexity:** $O(M \cdot N)$ for the full 2D table, or $O(N)$ with 1D row compression.