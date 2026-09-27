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

---

## 5. Algorithmic Correctness

**Soundness.** Mathematical transposition maps cell $(r, c)$ to $(c, r)$. In the script, element $(r, c)$ is appended to `row[c]`, ordered strictly by input row index $r$. Printing `row[1] \dots row[C]` in the `END` block outputs the transposed rectangular grid accurately.

**Completeness.** Since the problem guarantees that every row has the same number of columns, $NF$ is constant across all rows. Every cell in the grid is processed and printed.

---

## 6. Traps This Instance Exposes

- **Leading or Trailing Whitespace:** Appending `" " $i$"` unconditionally creates a leading space on row 1 (e.g. `" name alice"`). Branching on `if (NR == 1)` ensures the first element is unpadded.
- **Unequal Column Counts:** While the problem guarantees equal column count, a general script can track $\max(NF)$ across lines.
- **Large Files:** For large tables, buffering $R \times C$ words in memory is required because transposition cannot be completed until the final row is read.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(R \cdot C)$, where $R$ is the number of rows and $C$ is the number of columns in `file.txt`. Every word in the matrix is visited exactly once during ingestion and once during printing.
- **Auxiliary Space Complexity:** $O(R \cdot C)$ auxiliary memory to buffer the transposed strings in the `row` array.
