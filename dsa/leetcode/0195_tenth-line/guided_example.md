# Guided Example: Tenth Line

We trace the step-by-step stream filtering, numeric line addressing, and early termination on representative text files:

- **Input File `file.txt`:**
  ```text
  Line 1
  Line 2
  Line 3
  Line 4
  Line 5
  Line 6
  Line 7
  Line 8
  Line 9
  Line 10
  Line 11
  ```
- **Required output:**
  ```text
  Line 10
  ```
- **Fewer Than 10 Lines Instance:** `file.txt` contains 7 lines $\implies$ Empty output (prints nothing)
- **Exactly 10 Lines Instance:** `file.txt` contains 10 lines $\implies$ Prints Line 10

This instance explores line-addressed stream processing, analyzes the three foundational Unix tools (`sed`, `awk`, `tail | head`), explains why suppression flags (`-n`) and record counting (`NR == 10`) avoid output pollution, and achieves $O(\min(N, 10))$ time with early termination.

---

## 1. Instance & Teaching Goal

Given a text file `file.txt`, print **just the 10th line** of the file to standard output. If the file contains fewer than 10 lines, output nothing.

Evaluating `file.txt`:
- Lines 1 through 9: Read and discarded.
- Line 10: Selected and printed to stdout.
- Lines 11 and beyond: Discarded (or skipped via early termination `q` / `exit`).

A naive script might echo lines without checking total line count, erroneously printing blank lines when the file has fewer than 10 records.
Standard Unix tools solve this with precise record targeting and zero temporary file creation.

---

## 2. Conceptual Foundation & Invariants

### Method A: Stream Editor `sed` with Line Addressing (Recommended)
```bash
sed -n '10p' file.txt
```
Or with early termination to optimize for large files:
```bash
sed -n '10{p;q}' file.txt
```

#### Mechanics of `sed -n '10p'`:
1. **`-n` (Quiet Mode):**
   By default, `sed` prints every line in the pattern space after executing commands. The `-n` flag disables automatic echoing, ensuring that lines are printed only when explicitly requested.
2. **`10` (Address Selector):**
   Matches only the 10th input line. For lines $1 \dots 9$ and $11 \dots \infty$, the address condition is false.
3. **`p` (Print Action):**
   Prints the current line buffer.
4. **`q` (Quit):**
   Immediately terminates execution after line 10, preventing unnecessary I/O on large files.

### Method B: Pattern Scanning with `awk`
```bash
awk 'NR == 10 {print; exit}' file.txt
```
- `NR` is `awk`'s built-in record number (1-based line counter).
- When `NR == 10`, it executes `{print; exit}`.
- If $NR < 10$ at EOF, the block never executes, naturally producing an empty output.

### Method C: Pipeline with `tail` and `head`
```bash
tail -n +10 file.txt | head -n 1
```
- `tail -n +10`: Begins output at line 10 (1-indexed) and streams to the end of the file. If the file has fewer than 10 lines, it outputs nothing.
- `head -n 1`: Takes only the first line of that incoming stream (line 10).

> **Invariant.** An output line is emitted if and only if the current 1-based record index equals 10.

---

## 3. Step-by-Step Worked Execution

We trace the streaming evaluation line by line across `file.txt`:

### Records 1 to 9:
- `NR = 1` (`"Line 1"`): Address $10$ matches? `False`. Quiet mode suppresses output.
- `NR = 2` (`"Line 2"`): Address $10$ matches? `False`. Quiet mode suppresses output.
- `NR = 3 \dots 9`: Address $10$ matches? `False`. Discarded.

---

### Record 10 (`"Line 10"`):
- `NR = 10`: Address $10$ matches? **`True!`**
- Execute `p`:
  Emits `"Line 10"` to standard output.
- If early exit `q` is specified:
  Stream closes immediately without reading line 11!

---

### Records 11+ (Without `q`):
- `NR = 11`: Address $10$ matches? `False`. Discarded.
- Stream finishes at EOF.

Final output:
```text
Line 10
```

---

## 4. Complete Execution Trace

```text
file.txt Stream:
Line 1  -> NR = 1  != 10 -> Suppressed
Line 2  -> NR = 2  != 10 -> Suppressed
...
Line 9  -> NR = 9  != 10 -> Suppressed
Line 10 -> NR = 10 == 10 -> PRINT ("Line 10") -> QUIT
Line 11 -> (Skipped if early quit used)

Output: Line 10
```

| Line Counter `NR` | Line Content | Address Match (`NR == 10`) | `sed -n` Action | Emitted to Stdout |
|:---:|:---|:---:|:---:|:---|
| 1 | `Line 1` | `False` | Suppress | - |
| 2 | `Line 2` | `False` | Suppress | - |
| ... | ... | `False` | Suppress | - |
| 9 | `Line 9` | `False` | Suppress | - |
| **10** | **`Line 10`** | **`True`** | **Print (`p`)** | **`Line 10`** |
| 11 | `Line 11` | `False` | Suppress / Quit | - |

### Authored Instances at the Boundary

Selection by position has two independent boundaries: not enough records, and a tenth record that carries no text. The table separates them, because both end in empty-looking output.

| Instance file | Records in the file | Highest counter reached | Selection result | Observable output | What the instance proves |
|:---|:---:|:---:|:---|:---|:---|
| `Line 1` through `Line 12` | 12 | 12 without a quit, 10 with one | counter 10 is the only match | `Line 10` | Selection depends on position alone: records 11 and 12 are never candidates, whatever their text says. |
| `1` through `9`, then `ten` | 10 | 10 | counter 10 matches, and it is also the final record | `ten` | The test is `NR == 10`, not "ten records followed by one more"; reaching the end of the file right after the match changes nothing. |
| `1`, `2`, `3` | 3 | 3 | no record ever reaches counter 10 | nothing at all | Exhausting the input is not an error: the address never becomes true, the exit status still reports success, and the empty result is the required answer. |
| `1` through `9`, one empty line, then `11` | 11 | 11 | counter 10 matches, and its content is the empty string | one empty record, which normalizes to the same empty output | A blank line is still a record. The counter advances across it, so empty output alone cannot distinguish a short file from a file whose tenth line is blank. |

The last row is the decisive one for correctness reasoning. Any formulation that decides by looking at the text of a record — for instance, stopping when it reads something nonempty — would treat the blank tenth record as the end of the file and then print record 11. Position-based addressing is what makes the rule sound in both directions.

---

## 5. Algorithmic Correctness

**Soundness.** In `sed -n '10p'`, `-n` guarantees that non-matching lines produce zero output. The command `p` is invoked exclusively when the record counter reaches 10, ensuring that only line 10 is emitted.

**Completeness.** If the file contains $\ge 10$ lines, line 10 is guaranteed to be matched and printed. If the file contains $< 10$ lines, EOF is reached before line 10, leaving the output empty as required.

---

## 6. Traps This Instance Exposes

- **Forgetting `-n` in `sed`:** Running `sed '10p' file.txt` without `-n` prints *every* line once and line 10 *twice*! The `-n` flag is mandatory.
- **Off-by-One in `tail`:** Writing `tail -n 10` prints the *last 10 lines* of the file. The syntax to start from line 10 forward is `tail -n +10`.
- **Fewer Than 10 Lines:** If the file has 5 lines, `head -n 10 file.txt | tail -n 1` would erroneously print line 5! `sed -n '10p'` and `tail -n +10 | head -n 1` both correctly print nothing.

### Formulations Compared

All four correct forms agree on the answer; they differ in how much of the stream they consume and in which mistake each one invites.

| Formulation | How record 10 is recognized | Reads past record 10 | With fewer than ten records | With a blank tenth record | Characteristic failure |
|:---|:---|:---|:---|:---|:---|
| `sed -n '10p'` | the line address matches the tenth record | Yes; the remaining records are still read and discarded | no record is selected, so nothing is printed | the empty record is selected and emitted, giving empty visible output | dropping `-n` restores automatic echoing: every record is printed once, and record 10 is printed a second time. |
| `sed -n '10{p;q}'` | the same address, with a quit command inside the matched block | No; the editor stops reading immediately after the print | nothing is printed | the empty record is printed, then the editor quits | the `q` must sit inside the addressed block; outside it the quit applies to the first record, and the command prints nothing at all. |
| `awk 'NR == 10 {print; exit}'` | the built-in record counter `NR` compared with 10 | No; the exit statement stops after the print | the rule never fires, so nothing is printed | the empty record is printed | omitting the exit keeps the answer correct but reads the whole file, which is exactly the cost the early-exit form removes. |
| `tail -n +10 \| head -n 1` | a starting-line offset, then the first record of that stream | Only until the reader closes the pipe after one record | the first tool emits nothing, so the second emits nothing | the empty record is first on the stream and is emitted | `-n 10` instead of `-n +10` asks for the last ten records, which is a different question. |
| `head -n 10 \| tail -n 1` | the last record among the first ten | No | the final available record is printed, for example `3` from a three-record file | the empty record is tenth of the first ten and is printed | eliminated: it returns a line for a short file, so it cannot express the required condition. |

Two conclusions follow for the complexity analysis in the next section. The `-n` form touches every record and therefore runs in $O(C)$ over the whole file, while the quitting forms stop at record 10 and run in $O(\min(C, C_{10}))$. All correct forms keep only the current record in memory, so the auxiliary space is the length of one line rather than the size of the file.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - With early termination (`sed -n '10{p;q}'` or `awk 'NR==10{print;exit}'`): $O(\min(C, C_{10}))$ where $C_{10}$ is the character count up to line 10.
  - Standard pass: $O(C)$ where $C$ is total file character count.
- **Auxiliary Space Complexity:** $O(L)$ where $L$ is the character length of line 10 (constant buffer space).
