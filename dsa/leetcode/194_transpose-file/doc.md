# Transpose File

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 194 |
| Difficulty | Medium |
| Category | Shell |
| Topics | Shell |
| Supported Languages | bash |
| Official Link | [LeetCode](https://leetcode.com/problems/transpose-file/) |

## Problem Description
### Goal
The file `file.txt` contains a rectangular table: each input row has the same positive number of whitespace-separated fields. Transform the table so original rows become output columns and original columns become output rows.

Write the transposed table to standard output with one output row per original column and fields separated by single spaces. Preserve every field value exactly while changing only its position. If the input has `m` rows and `n` fields per row, the output must have `n` rows with `m` fields each. Do not print labels or expose this Bash task as function-return data.

### Function Contract
**Inputs**

- `file.txt`: rows containing the same positive number of whitespace-separated fields

**Return value**

Write one output row per original column, with fields separated by single spaces.

### Examples
**Example 1**

- File: rows `name age` and `alice 21`
- Output: rows `name alice` and `age 21`

**Example 2**

- File contains one row: `a b c`
- Output: three one-field rows

**Example 3**

- File contains one column
- Output: one row containing all original rows

### Required Complexity

- **Time:** $O(rc)$
- **Space:** $O(rc)$

<details>
<summary>Approach</summary>

#### General

The file arrives in row-major order, but each output line needs one value from every input row. An `awk` program can accumulate one output string per original column.

For every input record, loop from field `1` through `NF`. On the first row, initialize `output[column]` with that field. On later rows, append one space followed by the field. Record the first row's field count so the `END` block can print columns in numeric order rather than relying on unspecified associative-array iteration order.

For input

```text
name age
alice 21
```

the first record initializes `output[1] = "name"` and `output[2] = "age"`. The second extends them to `"name alice"` and `"age 21"`; printing those strings gives the transpose.

After processing `r` input rows, accumulator `c` contains exactly fields `(1,c), (2,c), ..., (r,c)` separated by single spaces. Each new row appends the next value to every column accumulator, preserving this statement until end-of-file.

Every source cell at row `r`, column `c` is visited once and appended to accumulator `c` after all earlier-row values in that same column. Thus accumulator `c` contains original column `c` in row order. Printing accumulators from `1` through the column count maps every source coordinate `(r,c)` to output coordinate `(c,r)`, which is exactly matrix transposition.

#### Complexity detail

For `r` rows and `c` columns, the loop visits all `rc` fields once, giving $O(rc)$ logical work. The accumulated output contains all `rc` fields and uses $O(rc)$ space. Repeated string concatenation may have implementation-dependent copying costs, but the intended `awk` solution is linear in the data emitted under ordinary string-buffer behavior.

#### Alternatives and edge cases

- Re-reading the file once per column with `cut` or `awk` can reduce retained state but performs repeated file scans and requires discovering the column count.
- Printing while reading cannot finish an output row until values from all later input rows are known.
- A one-row file becomes one output line per field; a one-column file becomes one line containing all rows.
- The contract guarantees a nonempty rectangular table. Ragged rows would require an explicit missing-field policy.
- Default `awk` field splitting normalizes arbitrary runs of whitespace to single spaces in the output.

</details>
