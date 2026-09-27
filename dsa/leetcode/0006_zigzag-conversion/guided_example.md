# Guided Example: Zigzag Conversion

We trace the step-by-step execution of the optimal simulation method on a representative instance:

- **Input:** $s = \text{"PAYPALISHIRING"}$, $\text{numRows} = 3$
- **Required output:** $\text{"PAHNAPLSIIGYIR"}$

This instance demonstrates vertical bouncing across multiple rows, boundary direction reversal at row extremes, and final linear concatenation.

---

## 1. Instance & Teaching Goal

Given a string $s$ of length $N = 14$ and a row constraint $\text{numRows} = 3$, we arrange the characters along a vertical zigzag path and read off the resulting matrix row by row.

Visually, the zigzag path forms a periodic bouncing wave:

```text
Row 0: P       A       H       N
Row 1:   A   P   L   S   I   I   G
Row 2:     Y       I       R
```

Reading across rows horizontally produces:
- Row 0: $\text{"PAHN"}$
- Row 1: $\text{"APLSIIG"}$
- Row 2: $\text{"YIR"}$

Concatenating rows $0$, $1$, and $2$ yields $\text{"PAHNAPLSIIGYIR"}$.

A naive approach allocates a full 2D sparse matrix of dimensions $\text{numRows} \times N$, wasting $O(\text{numRows} \cdot N)$ memory on empty filler cells. The optimal approach maintains $\text{numRows}$ string buffers and simulates only the vertical cursor position, consuming strictly $O(N)$ auxiliary space.

The three candidate representations differ only in what they record per character, and the difference decides the auxiliary space:

| Representation | State Kept Per Step | Auxiliary Space | Extra Work Beyond the Single Pass | Why It Is Not the Representation Used Here |
|:---|:---|:---|:---|:---|
| Dense character grid | Cursor $(r, c)$ plus blank-filled cells | $O(\text{numRows} \cdot N)$, i.e. $3 \times 14 = 42$ allocated cells | A second sweep to collect the non-blank cells one row at a time | Only $N = 14$ of those cells ever hold a character; the padding is allocated and re-scanned for nothing |
| $(r, c, i)$ placement records | A list of row, column, and source-index triples | $O(N) = 14$ records | A lexicographic comparison sort by $(r, c)$ before joining | Correct, but the sort costs $O(N \log N)$ for an ordering that the bouncing cursor already produces automatically |
| One buffer per row plus a bouncing cursor | $r$, $d$, and $\text{numRows}$ buffers | $O(N) = 14$ characters, no padding | None; concatenation is one linear join | Chosen: every append lands at its final relative position inside its row |

---

## 2. Conceptual Foundation & Invariants

### Bouncing Wave Dynamics
The row cursor $r$ moves between $0$ and $\text{numRows} - 1$:
- We start at row $r = 0$ with initial vertical velocity $d = +1$ (moving downward).
- Whenever $r = 0$, the cursor reflects downward: $d = +1$.
- Whenever $r = \text{numRows} - 1$, the cursor reflects upward: $d = -1$.
- At each character $s[i]$, we append $s[i]$ to buffer $B[r]$, then update $r \leftarrow r + d$.

### Cycle Length
The vertical wave repeats every $2 \times (\text{numRows} - 1)$ steps:
$$
\text{Cycle Period} = 2 \times (3 - 1) = 4
$$
Within each cycle of length 4, the visited row sequence is:
$$
0 \to 1 \to 2 \to 1
$$

> **Invariant.** At step $k$, all characters $s[0 \dots k-1]$ have been appended to their respective row buffers in their original relative horizontal order, and the cursor $r$ accurately reflects the vertical position of $s[k]$.

---

## 3. Step-by-Step Worked Execution

We process the string $s = \text{"PAYPALISHIRING"}$ character by character:

### Cycle 1 (Indices 0–3)
- **Step 0 ($i=0$):** Character `'P'`. Current row $r = 0$. Append `'P'` to Row 0. At top boundary, set $d = +1$. Next row $r = 1$.
- **Step 1 ($i=1$):** Character `'A'`. Current row $r = 1$. Append `'A'` to Row 1. Maintain $d = +1$. Next row $r = 2$.
- **Step 2 ($i=2$):** Character `'Y'`. Current row $r = 2$. Append `'Y'` to Row 2. At bottom boundary ($r = \text{numRows} - 1$), reflect $d = -1$. Next row $r = 1$.
- **Step 3 ($i=3$):** Character `'P'`. Current row $r = 1$. Append `'P'` to Row 1. Maintain $d = -1$. Next row $r = 0$.

### Cycle 2 (Indices 4–7)
- **Step 4 ($i=4$):** Character `'A'`. Current row $r = 0$. Append `'A'` to Row 0. At top boundary, reflect $d = +1$. Next row $r = 1$.
- **Step 5 ($i=5$):** Character `'L'`. Current row $r = 1$. Append `'L'` to Row 1. Next row $r = 2$.
- **Step 6 ($i=6$):** Character `'I'`. Current row $r = 2$. Append `'I'` to Row 2. Bottom boundary reached; reflect $d = -1$. Next row $r = 1$.
- **Step 7 ($i=7$):** Character `'S'`. Current row $r = 1$. Append `'S'` to Row 1. Next row $r = 0$.

### Cycle 3 (Indices 8–11)
- **Step 8 ($i=8$):** Character `'H'`. Current row $r = 0$. Append `'H'` to Row 0. Top boundary reached; reflect $d = +1$. Next row $r = 1$.
- **Step 9 ($i=9$):** Character `'I'`. Current row $r = 1$. Append `'I'` to Row 1. Next row $r = 2$.
- **Step 10 ($i=10$):** Character `'R'`. Current row $r = 2$. Append `'R'` to Row 2. Bottom boundary reached; reflect $d = -1$. Next row $r = 1$.
- **Step 11 ($i=11$):** Character `'I'`. Current row $r = 1$. Append `'I'` to Row 1. Next row $r = 0$.

### Cycle 4 (Indices 12–13)
- **Step 12 ($i=12$):** Character `'N'`. Current row $r = 0$. Append `'N'` to Row 0. Top boundary reached; reflect $d = +1$. Next row $r = 1$.
- **Step 13 ($i=13$):** Character `'G'`. Current row $r = 1$. Append `'G'` to Row 1. String exhausted.

---

## 4. Complete Execution Trace

The complete state table tracing each character assignment:

| Step $i$ | Character $s[i]$ | Active Row $r$ | Boundary Action / Velocity $d$ | Next Row | Row 0 Buffer | Row 1 Buffer | Row 2 Buffer |
|:---:|:---:|:---:|:---:|:---:|:---|:---|:---|
| 0 | `P` | 0 | Top boundary $\implies d = +1$ | 1 | `["P"]` | `[]` | `[]` |
| 1 | `A` | 1 | Descending ($d = +1$) | 2 | `["P"]` | `["A"]` | `[]` |
| 2 | `Y` | 2 | Bottom boundary $\implies d = -1$ | 1 | `["P"]` | `["A"]` | `["Y"]` |
| 3 | `P` | 1 | Ascending ($d = -1$) | 0 | `["P"]` | `["A", "P"]` | `["Y"]` |
| 4 | `A` | 0 | Top boundary $\implies d = +1$ | 1 | `["P", "A"]` | `["A", "P"]` | `["Y"]` |
| 5 | `L` | 1 | Descending ($d = +1$) | 2 | `["P", "A"]` | `["A", "P", "L"]` | `["Y"]` |
| 6 | `I` | 2 | Bottom boundary $\implies d = -1$ | 1 | `["P", "A"]` | `["A", "P", "L"]` | `["Y", "I"]` |
| 7 | `S` | 1 | Ascending ($d = -1$) | 0 | `["P", "A"]` | `["A", "P", "L", "S"]` | `["Y", "I"]` |
| 8 | `H` | 0 | Top boundary $\implies d = +1$ | 1 | `["P", "A", "H"]` | `["A", "P", "L", "S"]` | `["Y", "I"]` |
| 9 | `I` | 1 | Descending ($d = +1$) | 2 | `["P", "A", "H"]` | `["A", "P", "L", "S", "I"]` | `["Y", "I"]` |
| 10 | `R` | 2 | Bottom boundary $\implies d = -1$ | 1 | `["P", "A", "H"]` | `["A", "P", "L", "S", "I"]` | `["Y", "I", "R"]` |
| 11 | `I` | 1 | Ascending ($d = -1$) | 0 | `["P", "A", "H"]` | `["A", "P", "L", "S", "I", "I"]` | `["Y", "I", "R"]` |
| 12 | `N` | 0 | Top boundary $\implies d = +1$ | 1 | `["P", "A", "H", "N"]` | `["A", "P", "L", "S", "I", "I"]` | `["Y", "I", "R"]` |
| 13 | `G` | 1 | Descending ($d = +1$) | 2 | `["P", "A", "H", "N"]` | `["A", "P", "L", "S", "I", "I", "G"]` | `["Y", "I", "R"]` |

### Final Concatenation
- **Row 0:** $\text{"PAHN"}$
- **Row 1:** $\text{"APLSIIG"}$
- **Row 2:** $\text{"YIR"}$
- **Combined Result:** $\text{"PAHN"} + \text{"APLSIIG"} + \text{"YIR"} = \text{"PAHNAPLSIIGYIR"}$.

---

## 5. Algorithmic Correctness

**Soundness.** The zigzag layout specifies that letters are placed down the columns and diagonally up to the top. By tracking the vertical row coordinate $r$ with direction variable $d \in \{+1, -1\}$, each character is assigned to its exact mathematical row index. Since characters are added to each row buffer in temporal order, the horizontal relative ordering within each row is preserved without needing coordinate sorting.

**Completeness.** Every character in $s$ is processed in sequence exactly once. Because the row buffers partition the characters of $s$, concatenating rows $0$ through $\text{numRows}-1$ includes all $N$ characters without omission or duplication.

---

## 6. Traps This Instance Exposes

- **Single Row Degeneracy ($\text{numRows} = 1$):** If $\text{numRows} = 1$, the top and bottom boundaries coincide ($0 = \text{numRows} - 1$). The direction cannot oscillate properly, leading to out-of-bounds indexing if not guarded by an early exit returning $s$ directly.
- **Short Input ($N \le \text{numRows}$):** When the string length does not exceed $\text{numRows}$, no zigzag bounce occurs; the string is placed straight down the first column and returned unchanged.
- **Memory Overhead of Sparse Matrix:** Simulating the 2D grid with full whitespace padding requires $O(\text{numRows} \cdot N)$ storage and additional scanning time. Using dynamic row buffers eliminates grid padding completely.

The degenerate rail counts are worth tabulating, because each one turns off part of the bounce mechanism rather than requiring a different mechanism:

| Boundary Regime | Instance | Behaviour of $r$ and $d$ | Rail Contents | Returned Value |
|:---|:---|:---|:---|:---|
| Single rail | `s = "ABCD"`, $\text{numRows} = 1$ | $r$ is pinned at $0$, since $0 = \text{numRows} - 1$; the upward and downward reflections coincide, so $d$ never produces a legal move | Rail 0 absorbs the whole string | `"ABCD"`, the input unchanged |
| Rails equal to the character count | `s = "ABCD"`, $\text{numRows} = 4$ | $r$ walks $0 \to 1 \to 2 \to 3$ and lands exactly on the bottom rail at the last character, so no diagonal step is ever taken | Four rails of one character each | `"ABCD"` |
| More rails than characters | `s = "ABC"`, $\text{numRows} = 5$ | $r$ reaches only $2 < \text{numRows} - 1 = 4$; the direction remains $d = +1$ for the entire traversal | Rails 0, 1, 2 hold one character each; rails 3 and 4 stay empty | `"ABC"` |
| Two rails | `s = "ABCDE"`, $\text{numRows} = 2$ | Cycle period shrinks to $2 \cdot (2 - 1) = 2$, so every index is a turning point: $r$ visits $0, 1, 0, 1, 0$ | Rail 0 = `"ACE"`, rail 1 = `"BD"` | `"ACEBD"` |
| Maximum rail count | `s = "Z"`, $\text{numRows} = 1000$ | One append to rail 0, then the traversal ends immediately | Rail 0 = `"Z"`; the other 999 rails contribute the empty string | `"Z"` |
| Non-letter characters | `s = "A,B.C"`, $\text{numRows} = 3$ | Cycle period $4$; $r$ visits $0, 1, 2, 1, 0$ exactly as for letters | Rail 0 = `"AC"`, rail 1 = `",."`, rail 2 = `"B"` | `"AC,.B"` |

No regime above needs a separate rule: in each case the boundary tests plus the final row concatenation already produce the stated output, which is why the guard for $\text{numRows} = 1$ is the only genuine special case.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. We iterate through the string of length $N$ once, performing $O(1)$ operations per character (buffer append and pointer updates). Concatenating the $\text{numRows}$ row buffers takes $O(N)$ time. The overall runtime is strictly $O(N)$.
- **Auxiliary Space Complexity:** $O(N)$. The row buffers store exactly the $N$ characters of the input string across $\text{numRows}$ lists.
