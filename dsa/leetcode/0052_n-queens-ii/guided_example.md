# Guided Example: N-Queens II

We trace the step-by-step bitwise backtracking count evaluation on a representative $n = 4$ chessboard instance:

- **Input:** $n = 4$
- **Required output:** $2$

This instance demonstrates counting valid queen placements without allocating board strings, modeling attack lanes as integer bitmasks ($\text{cols}$, $\text{diag1}$, $\text{diag2}$), bitwise directional shifts ($\ll 1$ and $\gg 1$), isolated low-bit extraction via $p = \text{available} \ \& \ (-\text{available})$, and pruning dead-end branches.

---

## 1. Instance & Teaching Goal

Given an integer $n = 4$, return the total number of distinct solutions to the $n$-queens puzzle.

In contrast to N-Queens I (which requires reconstructing the $n \times n$ character grid for each solution), N-Queens II asks purely for the scalar count of legal configurations.
Allocating 2D arrays or string slices introduces substantial memory overhead. The optimal approach models column, anti-diagonal, and main-diagonal threats as three integer bitmasks. Each row transition updates threat bitmasks with single-instruction bitwise shifts, exploring the solution tree with zero heap allocations.

---

## 2. Conceptual Foundation & Invariants

### Bitmask Representation of Attack Lines
Let the $n$ columns be indexed by bits $0 \dots n - 1$.
- A full $n$-bit mask is $\text{limit} = (1 \ll n) - 1$. For $n = 4$, $\text{limit} = (1111)_2 = 15$.
- `cols`: Bit $c$ is 1 if column $c$ contains a queen.
- `diag1` (Anti-diagonal $/$): When moving from row $r$ to $r + 1$, an anti-diagonal threat moves left by 1 column:
  $$
  \text{diag1}_{\text{next}} = (\text{diag1} \mid p) \ll 1
  $$
- `diag2` (Main diagonal $\setminus$): When moving from row $r$ to $r + 1$, a main-diagonal threat moves right by 1 column:
  $$
  \text{diag2}_{\text{next}} = (\text{diag2} \mid p) \gg 1
  $$

### Available Columns Calculation
At any row, blocked columns are the bitwise OR of all three threat masks:
$$
\text{blocked} = \text{cols} \mid \text{diag1} \mid \text{diag2}
$$
Available columns are the inverted bits masked to $n$ positions:
$$
\text{available} = (\sim \text{blocked}) \ \& \ \text{limit}
$$

### Extracting Candidate Columns
While $\text{available} > 0$:
1. **Lowest Set Bit:** Extract the least significant set bit in $O(1)$:
   $$
   p = \text{available} \ \& \ (-\text{available})
   $$
2. **Recurse:** Call `dfs(row + 1, cols | p, (diag1 | p) << 1, (diag2 | p) >> 1)`.
3. **Clear Bit:** Remove the tried bit:
   $$
   \text{available} \leftarrow \text{available} \ \& \ (\text{available} - 1)
   $$

> **Invariant.** If $\text{row} == n$, a complete valid configuration has been achieved. The function returns 1, which sums along all branches to the exact number of distinct solutions.

---

## 3. Step-by-Step Worked Execution

We trace $n = 4$ ($\text{limit} = 1111_2 = 15$):

### Root State ($\text{row} = 0$)
- Initial masks: $\text{cols} = 0, \text{diag1} = 0, \text{diag2} = 0$.
- Available: $\text{available} = 1111_2$ (Columns 0, 1, 2, 3).

---

### Branch 1: Try Col 0 ($p = 0001_2$)
- **Row 1:**
  - $\text{cols} = 0001_2$.
  - $\text{diag1} = (0000 \mid 0001) \ll 1 = 0010_2$.
  - $\text{diag2} = (0000 \mid 0001) \gg 1 = 0000_2$.
  - Blocked: $0001 \mid 0010 \mid 0000 = 0011_2$.
  - Available: $(\sim 0011) \ \& \ 1111 = 1100_2$ (Columns 2 and 3).
  - *Attempt Col 2 ($p = 0100_2$):*
    - **Row 2:**
      - $\text{cols} = 0001 \mid 0100 = 0101_2$.
      - $\text{diag1} = (0010 \mid 0100) \ll 1 = 1100_2$.
      - $\text{diag2} = (0000 \mid 0100) \gg 1 = 0010_2$.
      - Blocked: $0101 \mid 1100 \mid 0010 = 1111_2$.
      - Available: $0000_2$.
      - *Dead end! Available is 0. Backtrack.*
  - *Attempt Col 3 ($p = 1000_2$):*
    - **Row 2:** Leads to Row 3 with all columns blocked.
- Subtree 1 returns **0**.

---

### Branch 2: Try Col 1 ($p = 0010_2$)
- **Row 1:**
  - $\text{cols} = 0010_2$.
  - $\text{diag1} = 0010 \ll 1 = 0100_2$.
  - $\text{diag2} = 0010 \gg 1 = 0001_2$.
  - Blocked: $0010 \mid 0100 \mid 0001 = 0111_2$.
  - Available: $1000_2$ (Only Column 3 is safe!).
- **Place Col 3 at Row 1 ($p = 1000_2$):**
  - **Row 2:**
    - $\text{cols} = 0010 \mid 1000 = 1010_2$.
    - $\text{diag1} = (0100 \mid 1000) \ll 1 = 1000_2$ (masked).
    - $\text{diag2} = (0001 \mid 1000) \gg 1 = 0100_2$.
    - Blocked: $1010 \mid 1000 \mid 0100 = 1110_2$.
    - Available: $0001_2$ (Only Column 0 is safe!).
  - **Place Col 0 at Row 2 ($p = 0001_2$):**
    - **Row 3:**
      - Blocked calculates to $1011_2$.
      - Available: $0100_2$ (Column 2 is safe!).
    - **Place Col 2 at Row 3 ($p = 0100_2$):**
      - **Row 4:** Reached terminal row! Return **1**.
- Subtree 2 yields **1 valid solution** (`[1, 3, 0, 2]`).

---

### Branch 3: Try Col 2 ($p = 0100_2$)
- Symmetrical to Branch 2.
- Traverses $[2, 0, 3, 1]$ safely down to Row 4.
- Subtree 3 yields **1 valid solution**.

---

### Branch 4: Try Col 3 ($p = 1000_2$)
- Symmetrical to Branch 1.
- All leaf branches dead-end.
- Subtree 4 yields **0**.

Total count: $0 + 1 + 1 + 0 = 2$.

---

## 4. Complete Execution Trace

| Recursion Depth | Queen Placement (Bit) | Blocked Mask $\text{cols} \mid \text{diag1} \mid \text{diag2}$ | Available Bits | Lowest Set Bit $p$ | Action / Subtree Result |
|:---:|:---:|:---:|:---:|:---:|:---|
| Row 0 | $p = 0001_2$ (Col 0) | $0000_2$ | $1111_2$ | $0001_2$ | Dead ends at Row 2 / Row 3 ($+0$) |
| Row 0 | **$p = 0010_2$ (Col 1)** | $0000_2$ | $1111_2$ | $0010_2$ | Enters Subtree 2 |
| Row 1 | $p = 1000_2$ (Col 3) | $0111_2$ | $1000_2$ | $1000_2$ | Advances to Row 2 |
| Row 2 | $p = 0001_2$ (Col 0) | $1110_2$ | $0001_2$ | $0001_2$ | Advances to Row 3 |
| Row 3 | $p = 0100_2$ (Col 2) | $1011_2$ | $0100_2$ | $0100_2$ | Advances to Row 4 |
| Row 4 | Base Case | - | - | - | **Count +1 (`[1, 3, 0, 2]`)** |
| Row 0 | **$p = 0100_2$ (Col 2)** | $0000_2$ | $1111_2$ | $0100_2$ | **Count +1 (`[2, 0, 3, 1]`)** |
| Row 0 | $p = 1000_2$ (Col 3) | $0000_2$ | $1111_2$ | $1000_2$ | Dead ends ($+0$) |

---

## 5. Algorithmic Correctness

**Soundness.** Because column, anti-diagonal, and main-diagonal threats are updated synchronously using exact bit shifts, an available bit at column $c$ is guaranteed to be conflict-free against all queens placed in rows $0 \dots \text{row}-1$. Every configuration reaching $\text{row} == n$ is provably valid.

**Completeness.** Clearing the lowest set bit via `available &= available - 1` exhausts all safe column choices in the current row before returning, guaranteeing no valid solution branch is omitted.

---

## 6. Traps This Instance Exposes

- **Missing $n$-Bit Truncation:** When shifting `diag1 << 1`, bits can overflow past bit $n - 1$. Applying $\& \ \text{limit}$ restricts the available mask strictly to the $n$ active columns of the board.
- **Two's Complement Lowest-Bit Trick:** $p = \text{available} \ \& \ (-\text{available})$ isolates the rightmost set bit in $O(1)$ operations via two's complement integer properties.
- **Symmetry Optimization:** The board is horizontally symmetric: the number of solutions starting with col $c$ equals the number starting with col $n - 1 - c$. For even $n$, searching only $c \in [0, n/2 - 1]$ and doubling the count cuts runtime in half.

### Boundary Instances and Verified Counts

The same recurrence is exercised against the smallest and largest legal boards, so the count is never a property of the mask arithmetic alone but of how quickly the threat lanes close. The mask width is $\text{limit} = 2^n - 1$; the returned value is exactly the number of branches that survive to a full row.

| Board size $n$ | $\text{limit} = 2^n - 1$ | Verified count | What decides the count |
|:---:|:---:|:---:|---|
| 1 | 1 | 1 | No threat lane is ever occupied, so the single set bit reaches the terminal row. |
| 2 | 3 | 0 | The two rows must use both columns, and either choice blocks the other row completely: both branches die at row 1. |
| 3 | 7 | 0 | Placing col 1 first blocks all of row 1; the outer openers leave only the opposite outer column, which then blocks all of row 2. |
| 4 | 15 | 2 | Exactly the two traced placements `[1, 3, 0, 2]` and `[2, 0, 3, 1]`. |
| 5 | 31 | 10 | Pruning is no longer immediate: several rows keep two or more safe columns, so ten branches reach row 5. |
| 6 | 63 | 4 | Strictly fewer than $n = 5$: the count is **not** monotone in the board size. |
| 9 | 511 | 352 | The largest legal board; the tally is a leaf count with no closed form, so it must be produced by the search. |

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n!)$. Pruning via bitwise operations reduces the search tree size dramatically compared to explicit arrays. All bitwise operations (`|`, `&`, `<<`, `>>`) run in $O(1)$ CPU cycles.
- **Auxiliary Space Complexity:** $O(n)$ recursion call stack depth. No heap arrays or string allocations are required.

### Alternative Encodings of the Same Search

Every candidate below explores the identical solution tree; they differ only in how the threat lanes are encoded and how early a dead branch is detected.

| Strategy | State carried per row | Cost | Tradeoff or failure mode |
|---|---|---|---|
| Three threat bitmasks (this lesson) | $\text{cols}, \text{diag1}, \text{diag2}$ as $n$-bit integers | $O(n!)$ time, $O(n)$ auxiliary space | Shifts must be truncated to $n$ bits, and the complement must be masked with $\text{limit}$, because an unmasked complement is negative. |
| Boolean per-column and per-diagonal occupancy arrays | $\text{cols}[j]$ plus the two diagonal arrays indexed by $i + j$ and $i - j + n$ | Same $O(n!)$ time, $O(n)$ auxiliary space | Simpler to read, but each row inspects several arrays instead of one bitwise combination, and the diagonal offsets must be kept inside their array bounds. |
| Enumerate all $n!$ column permutations, then test each board | The current permutation only | $O(n! \cdot n)$ time, $O(n)$ auxiliary space | No pruning: for $n = 9$ it examines $9! = 362\,880$ complete boards to find the same 352 valid ones. |
| Mirror-symmetry halving | Bitmasks plus a restricted first-row choice | Roughly half the $O(n!)$ traversal | Valid only when the doubled half excludes every self-symmetric placement; applying the doubling blindly on odd $n$ double counts the middle-column branches. |
