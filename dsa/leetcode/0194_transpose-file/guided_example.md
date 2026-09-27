# Guided Example: Transpose File

We trace the step-by-step rectangular matrix transposition via `awk` field buffering and column concatenation on representative space-delimited text files:

- **Input File `file.txt`:**
  ```text
  name age
  alice 21
  ryan 30
  ```
- **Required output:**
  ```text
  name alice ryan
  age 21 30
  ```
- **Two-Row Minimal Instance:** `name age\nalice 21` $\implies$ `name alice\nage 21`
- **Single Column Instance:** `a\nb\nc` $\implies$ `a b c` (Columns become rows)
- **Single Row Instance:** `a b c` $\implies$ `a\nb\nc` (Rows become columns)

This instance demonstrates matrix dimension swapping ($(R \times C) \to (C \times R)$) using Unix stream processing, details field aggregation (`row[i] = row[i] " " $i`), manages delimiter spacing without trailing whitespace, and runs in linear $O(R \cdot C)$ time.

---

## 1. Instance & Teaching Goal

Given a rectangular text file `file.txt` where each row has the exact same number of columns, separated by single spaces:
$$
\begin{pmatrix}
\text{name} & \text{age} \\
\text{alice} & 21 \\
\text{ryan} & 30
\end{pmatrix}
$$
Transpose its content so that rows become columns and columns become rows:
$$
\begin{pmatrix}
\text{name} & \text{alice} & \text{ryan} \\
\text{age} & 21 & 30
\end{pmatrix}
$$
In output text format:
```text
name alice ryan
age 21 30
```

In standard Unix utilities, files are read line by line (row by row). Because output must be printed row by row, we cannot stream the first transposed line until the entire file has been read (to obtain elements from every row).
`awk` provides native field parsing (`$1, $2, \dots, $NF`) and associative arrays:
- As each input row $r$ is read, its $c$-th field `$c` is appended to buffer `row[c]`.
- When all rows are ingested, the `END` block prints the $C$ accumulated strings.

---

## 2. Conceptual Foundation & Invariants

### The `awk` Transposition Protocol
```bash
awk '{
    for (i = 1; i <= NF; i++) {
        if (NR == 1) {
            row[i] = $i
        } else {
            row[i] = row[i] " " $i
        }
    }
} END {
    for (i = 1; i <= NF; i++) {
        print row[i]
    }
}' file.txt
```

#### Variables and Logic:
1. `NR` (Number of Records): Current 1-based row number.
2. `NF` (Number of Fields): Number of space-separated columns in the current line.
3. `$i`: Value of the $i$-th column in the current row.
4. Initialization on `NR == 1`:
   Each `row[i]` begins with its first element without a leading space:
   $$
   \text{row}[i] \leftarrow \$i
   $$
5. Concatenation on `NR > 1`:
   Subsequent rows append a space delimiter followed by the field:
   $$
   \text{row}[i] \leftarrow \text{row}[i] \mathbin{\Vert} \text{" "} \mathbin{\Vert} \$i
   $$
6. Emitting in `END`:
   Iterate $i$ from $1$ to $NF$, printing each completed transposed row.

> **Invariant.** After processing row $r$, `row[c]` contains the exact space-separated string of the first $r$ elements of column $c$.

---

## 3. Step-by-Step Worked Execution

We trace the script on `file.txt`:
```text
Row 1: name age
Row 2: alice 21
Row 3: ryan 30
```

### Row 1: `NR = 1`, Content: `"name age"`
- $NF = 2$.
- $i = 1$: `NR == 1` $\implies \text{row}[1] = \$1 = \mathbf{\text{"name"}}$.
- $i = 2$: `NR == 1` $\implies \text{row}[2] = \$2 = \mathbf{\text{"age"}}$.
- Buffers:
  - `row[1] = "name"`
  - `row[2] = "age"`

---

### Row 2: `NR = 2`, Content: `"alice 21"`
- $NF = 2$.
- $i = 1$: `NR > 1` $\implies \text{row}[1] = \text{"name"} + \text{" "} + \$1 = \mathbf{\text{"name alice"}}$.
- $i = 2$: `NR > 1` $\implies \text{row}[2] = \text{"age"} + \text{" "} + \$2 = \mathbf{\text{"age 21"}}$.
- Buffers:
  - `row[1] = "name alice"`
  - `row[2] = "age 21"`

---

### Row 3: `NR = 3`, Content: `"ryan 30"`
- $NF = 2$.
- $i = 1$: `NR > 1` $\implies \text{row}[1] = \text{"name alice"} + \text{" "} + \$1 = \mathbf{\text{"name alice ryan"}}$.
- $i = 2$: `NR > 1` $\implies \text{row}[2] = \text{"age 21"} + \text{" "} + \$2 = \mathbf{\text{"age 21 30"}}$.
- Buffers:
  - `row[1] = "name alice ryan"`
  - `row[2] = "age 21 30"`

---

### End Block: Output Emission
File reading finishes. Execute `END` block:
- Print `row[1]`: `name alice ryan`
- Print `row[2]`: `age 21 30`

Execution complete!

---

## 4. Complete Execution Trace

```text
Input File:
Row 1: name age
Row 2: alice 21
Row 3: ryan 30

Accumulation States:
After Row 1: row[1] = "name"              row[2] = "age"
After Row 2: row[1] = "name alice"        row[2] = "age 21"
After Row 3: row[1] = "name alice ryan"   row[2] = "age 21 30"

Output:
name alice ryan
age 21 30
```

| Row Number `NR` | Line Text | Field `$1` | Field `$2` | Accumulator `row[1]` | Accumulator `row[2]` |
|:---:|:---|:---:|:---:|:---|:---|
| 1 | `name age` | `"name"` | `"age"` | `"name"` | `"age"` |
| 2 | `alice 21` | `"alice"` | `"21"` | `"name alice"` | `"age 21"` |
| **3** | **`ryan 30`** | **`"ryan"`** | **`"30"`** | **`"name alice ryan"`** | **`"age 21 30"`** |
| **END** | - | - | - | **Emit line 1** | **Emit line 2** |

### Shape Boundaries of the Same Protocol

Transposition changes the dimensions, so the degenerate shapes are not special cases in the script but consequences of two numbers: $R$ (how many times the seeding branch can run) and the final $NF$ (what the `END` loop counts to).

| Instance file | Input shape $R \times C$ | Output shape $C \times R$ | Printed output | Which detail of the protocol decides the result |
|:---|:---:|:---:|:---|:---|
| `name age` then `alice 21` | $2 \times 2$ | $2 \times 2$ | `name alice` then `age 21` | The seeding branch runs once per field on row 1, so row 2 appends exactly one space per column and no delimiter is ever doubled. |
| `a b c` | $1 \times 3$ | $3 \times 1$ | `a`, `b`, `c` on three lines | With $R = 1$ the append branch never executes; every accumulator holds a single word, and the `END` loop bound of 3 turns one input row into three output rows. |
| `a` then `b` then `c` | $3 \times 1$ | $1 \times 3$ | `a b c` on one line | Here $NF = 1$ on every row, so only `row[1]` is ever created and exactly one output line exists. No branch suppresses the other columns; there simply are none. |
| `a b c d`, `1 2 3 4`, `w x y z` | $3 \times 4$ | $4 \times 3$ | `a 1 w`, `b 2 x`, `c 3 y`, `d 4 z` | Rectangularity is what makes the `END` bound correct: $NF$ read after the last record still equals the true column count. |

The last row isolates the one assumption the script truly depends on. The `END` block takes its loop bound from the most recently read record, so it prints the number of fields of the **final** row, not the maximum over all rows. The equal-column guarantee is exactly what makes those two quantities identical, and it is why the protocol needs no bookkeeping of a running maximum.

---

## 5. Algorithmic Correctness

**Soundness.** Mathematical transposition maps cell $(r, c)$ to $(c, r)$. In the script, element $(r, c)$ is appended to `row[c]`, ordered strictly by input row index $r$. Printing `row[1] \dots row[C]` in the `END` block outputs the transposed rectangular grid accurately.

**Completeness.** Since the problem guarantees that every row has the same number of columns, $NF$ is constant across all rows. Every cell in the grid is processed and printed.

---

## 6. Traps This Instance Exposes

- **Leading or Trailing Whitespace:** Appending `" " $i$"` unconditionally creates a leading space on row 1 (e.g. `" name alice"`). Branching on `if (NR == 1)` ensures the first element is unpadded.
- **Unequal Column Counts:** While the problem guarantees equal column count, a general script can track $\max(NF)$ across lines.
- **Large Files:** For large tables, buffering $R \times C$ words in memory is required because transposition cannot be completed until the final row is read.

### What the First-Row Branch Actually Prevents

Unconditional concatenation is the natural first attempt, and it is not wrong by accident of arithmetic — it is wrong by one character per line. The comparison below uses the lesson instance, and the exact spacing is shown because the output is compared byte for byte.

| Stage | Accumulator with the `NR == 1` branch | Accumulator with unconditional concatenation | Why the two differ |
|:---|:---|:---|:---|
| After row 1 | `row[1] = name`, `row[2] = age` | `row[1] = " name"`, `row[2] = " age"` | The delimiter is emitted before the field even though nothing precedes it, so the very first append creates a leading space. |
| After row 2 | `row[1] = name alice` | `row[1] = " name alice"` | Every later append adds one space in both variants, so the extra leading character is never repaired. |
| After row 3 | `row[1] = name alice ryan` | `row[1] = " name alice ryan"` | The accumulated difference is still exactly one leading space; concatenation never removes it. |
| Printed line 1 | `name alice ryan` | ` name alice ryan` | The leading space survives into standard output and the line no longer matches the required format. |

The lesson generalises: a delimiter belongs **between** elements, so it must be emitted once per element except the first. Branching on `NR == 1` is the cheapest way to express that, because the first element of each column is always read on the first record.

### Transposition Strategies Compared

| Formulation | State retained while reading | Work | Auxiliary space | Tradeoff |
|:---|:---|:---|:---|:---|
| Per-column string accumulators (this protocol) | One partially built output line per column | One append per field, then $C$ print operations | $O(R \cdot C)$ characters | Chosen here: one pass over the input and no index arithmetic, but it must carry the first-row branch for delimiters and the final $NF$ for the print bound. |
| Two-dimensional cell array, printed column by column | One array slot per grid cell | One store per field, then $R \cdot C$ indexed reads in the `END` block | $O(R \cdot C)$ slots, with a higher constant than concatenated strings | Makes the mapping $(r, c) \to (c, r)$ explicit and removes all delimiter bookkeeping, at the cost of tracking the row count and a maximum field count instead of a simple final $NF$. |
| One output column per pass over the file | The words of a single column | Every record is re-split on every pass, so $O(R \cdot C^{2})$ character work because each of the $C$ passes scans each record to reach field $c$ | $O(R)$ for the column being printed, and no grid buffering at all | Needs no buffering, which suits a table too large to hold in memory, but it re-reads the whole input once per output line and its work grows quadratically in the column count. |

---

## 7. Complexity Derivation

- **Time Complexity:** $O(R \cdot C)$, where $R$ is the number of rows and $C$ is the number of columns in `file.txt`. Every word in the matrix is visited exactly once during ingestion and once during printing.
- **Auxiliary Space Complexity:** $O(R \cdot C)$ auxiliary memory to buffer the transposed strings in the `row` array.
