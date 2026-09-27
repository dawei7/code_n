# Guided Example: Valid Sudoku

We trace the step-by-step single-pass constraint verification on a representative 9x9 Sudoku board instance:

- **Input:** A partially filled 9x9 grid $\text{board}$ with known digits and empty cells (`'.'`)
- **Required output:** $\text{True}$

This instance demonstrates simultaneous row, column, and $3 \times 3$ sub-box constraint checking, the 2D-to-1D sub-box index mapping formula $b = \lfloor r/3 \rfloor \times 3 + \lfloor c/3 \rfloor$, ignoring empty cells, and early-exit conflict detection.

---

## 1. Instance & Teaching Goal

A 9x9 Sudoku board is valid if and only if:
1. Each row contains digits `'1'` through `'9'` without repetition.
2. Each column contains digits `'1'` through `'9'` without repetition.
3. Each of the nine $3 \times 3$ sub-boxes contains digits `'1'` through `'9'` without repetition.

Only the already filled cells need to be validated. The board does not need to be solvable; it only needs to satisfy the local consistency rules.

A naive approach runs 27 separate passes over the board (9 row checks, 9 column checks, and 9 box checks). The optimal approach uses three collections of bitmasks or hash sets to validate row, column, and sub-box constraints simultaneously in a single pass over the 81 cells in $O(1)$ time and space.

---

## 2. Conceptual Foundation & Invariants

### The $3 \times 3$ Sub-box Indexing Formula
The 9x9 board is partitioned into nine $3 \times 3$ sub-boxes indexed from 0 to 8:
```text
Box 0 | Box 1 | Box 2
------+-------+------
Box 3 | Box 4 | Box 5
------+-------+------
Box 6 | Box 7 | Box 8
```
For any cell at row $r \in [0, 8]$ and column $c \in [0, 8]$:
- Row band: $\lfloor r / 3 \rfloor \in \{0, 1, 2\}$
- Column band: $\lfloor c / 3 \rfloor \in \{0, 1, 2\}$
- Sub-box index:
  $$
  b = \left\lfloor \frac{r}{3} \right\rfloor \times 3 + \left\lfloor \frac{c}{3} \right\rfloor
  $$

### Verification State Tracking
We maintain three structures:
- $\text{rows}[r]$: Set of digits observed in row $r$ ($0 \le r < 9$).
- $\text{cols}[c]$: Set of digits observed in column $c$ ($0 \le c < 9$).
- $\text{boxes}[b]$: Set of digits observed in sub-box $b$ ($0 \le b < 9$).

For each cell $(r, c)$:
1. If $\text{board}[r][c] == \text{'.'}$, skip the cell.
2. Let $d = \text{board}[r][c]$:
   - Check if $d \in \text{rows}[r]$ or $d \in \text{cols}[c]$ or $d \in \text{boxes}[b]$.
   - If any condition is met, a duplicate exists; return $\text{False}$ immediately.
   - Otherwise, insert $d$ into $\text{rows}[r]$, $\text{cols}[c]$, and $\text{boxes}[b]$.

> **Invariant.** After inspecting cell $(r, c)$, no row, column, or $3 \times 3$ sub-box among the processed cells contains duplicate digits.

---

## 3. Step-by-Step Worked Execution

We trace the first row and prominent cells of the standard valid board:

### Row 0 Trace ($r = 0$)
- **Cell $(0, 0) = \text{'5'}$:**
  - Sub-box: $b = \lfloor 0/3 \rfloor \times 3 + \lfloor 0/3 \rfloor = 0 \times 3 + 0 = 0$.
  - Check $\text{'5'}$ in $\text{rows}[0]$, $\text{cols}[0]$, $\text{boxes}[0]$: Absent.
  - Insert: $\text{rows}[0] \cup \{5\}, \text{cols}[0] \cup \{5\}, \text{boxes}[0] \cup \{5\}$.
- **Cell $(0, 1) = \text{'3'}$:**
  - Sub-box: $b = 0 \times 3 + 0 = 0$.
  - Check $\text{'3'}$: Absent.
  - Insert: $\text{rows}[0] \cup \{3\}, \text{cols}[1] \cup \{3\}, \text{boxes}[0] \cup \{3\}$.
- **Cells $(0, 2), (0, 3)$:**
  - Value is `'.'`. Ignored.
- **Cell $(0, 4) = \text{'7'}$:**
  - Sub-box: $b = \lfloor 0/3 \rfloor \times 3 + \lfloor 4/3 \rfloor = 0 + 1 = 1$.
  - Check $\text{'7'}$: Absent.
  - Insert: $\text{rows}[0] \cup \{7\}, \text{cols}[4] \cup \{7\}, \text{boxes}[1] \cup \{7\}$.

---

### Conflict Detection Demonstration (Invalid Variant)
Suppose cell $(0, 0)$ contains `'8'` and cell $(3, 0)$ also contains `'8'`:
1. At cell $(0, 0)$, `'8'` is inserted into $\text{cols}[0]$.
2. At cell $(3, 0)$, when checking $d = \text{'8'}$ against column $c = 0$:
   - $\text{'8'} \in \text{cols}[0]$ evaluates to $\text{True}$!
   - Conflict in column 0 detected!
   - Algorithm returns $\text{False}$ immediately.

---

## 4. Complete Execution Trace

| Cell Coordinate $(r, c)$ | Digit $d$ | Sub-box ID $b = \lfloor r/3 \rfloor \cdot 3 + \lfloor c/3 \rfloor$ | Membership Check ($\text{row}, \text{col}, \text{box}$) | Action Taken | State Status |
|:---:|:---:|:---:|:---:|:---|:---:|
| $(0, 0)$ | `'5'` | 0 | Not seen | Record in $\text{row}_0, \text{col}_0, \text{box}_0$ | Valid |
| $(0, 1)$ | `'3'` | 0 | Not seen | Record in $\text{row}_0, \text{col}_1, \text{box}_0$ | Valid |
| $(0, 4)$ | `'7'` | 1 | Not seen | Record in $\text{row}_0, \text{col}_4, \text{box}_1$ | Valid |
| $(1, 0)$ | `'6'` | 0 | Not seen | Record in $\text{row}_1, \text{col}_0, \text{box}_0$ | Valid |
| $(1, 3)$ | `'1'` | 1 | Not seen | Record in $\text{row}_1, \text{col}_3, \text{box}_1$ | Valid |
| $(1, 4)$ | `'9'` | 1 | Not seen | Record in $\text{row}_1, \text{col}_4, \text{box}_1$ | Valid |
| $(1, 5)$ | `'5'` | 1 | Not seen | Record in $\text{row}_1, \text{col}_5, \text{box}_1$ | Valid |
| $(2, 1)$ | `'9'` | 0 | Not seen | Record in $\text{row}_2, \text{col}_1, \text{box}_0$ | Valid |
| $(2, 2)$ | `'8'` | 0 | Not seen | Record in $\text{row}_2, \text{col}_2, \text{box}_0$ | Valid |

### Sub-box Mapping Grid Reference

| Row Range | Col Range $0 \dots 2$ | Col Range $3 \dots 5$ | Col Range $6 \dots 8$ |
|:---:|:---:|:---:|:---:|
| $0 \dots 2$ | Sub-box 0 | Sub-box 1 | Sub-box 2 |
| $3 \dots 5$ | Sub-box 3 | Sub-box 4 | Sub-box 5 |
| $6 \dots 8$ | Sub-box 6 | Sub-box 7 | Sub-box 8 |

---

## 5. Algorithmic Correctness

**Soundness.** A board is invalid if and only if some digit appears $\ge 2$ times in the same row, column, or sub-box. Checking set membership prior to insertion detects any second occurrence instantly, guaranteeing sound conflict detection.

**Completeness.** Every cell $(r, c)$ in the 9x9 grid is examined. Empty cells are skipped because they impose no uniqueness constraints. If all 81 cells are visited without triggering a conflict, the board is provably valid.

---

## 6. Traps This Instance Exposes

- **Sub-box Formula Division:** Using integer division $\lfloor r/3 \rfloor \times 3 + \lfloor c/3 \rfloor$ maps the 9 blocks correctly. A common bug is writing $r/3 + c/3$, which treats indices as fractions or conflates distinct boxes.
- **Solvability vs Validity:** A Sudoku board can be valid according to the current numbers even if it cannot be legally solved to completion. The problem explicitly asks for validity of the given cells, not solvability.
- **Bitmask Optimization:** Instead of hash sets, each unit's digits can be tracked using a single 9-bit integer where the $d$-th bit represents whether digit $d$ was seen: `mask & (1 << d)`. This reduces memory overhead to 27 integers and speeds up lookups to bitwise operations.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$. The board dimensions are fixed at $9 \times 9 = 81$ cells. Each cell requires $O(1)$ arithmetic operations and set lookups.
- **Auxiliary Space Complexity:** $O(1)$. Three arrays of 9 sets (or 9-bit integers) store at most $3 \times 9 \times 9 = 243$ entries, requiring constant memory.
