## General

**Validate constraints; do not try to solve the puzzle**

A partially filled board is valid when no filled digit is repeated in its row, column, or $3\times3$ box. Empty cells may remain, and validity does not guarantee that some completion exists. The selected implementation therefore performs one pass over existing cells and records what has already appeared; it does no backtracking.

**Give every row, column, and box nine digit flags**

The source allocates three $9\times9$ Boolean tables:

```python
row = [[False] * 9 for _ in range(9)]
col = [[False] * 9 for _ in range(9)]
sub = [[False] * 9 for _ in range(9)]
```

`row[i][d]` means digit index `d` has appeared in row `i`. `col[j][d]` has the analogous meaning for column `j`, and `sub[k][d]` for box `k`.

The actual characters range from `'1'` through `'9'`. Converting with `int(c) - 1` maps them to indices zero through eight: digit one uses flag zero and digit nine uses flag eight. The contract guarantees no other filled character, so every index is valid.

**Ignore dots because they impose no uniqueness requirement**

When `c == '.'`, the loop uses `continue`. Multiple empty cells in the same unit are allowed and must not be recorded as repeated values. Treating dot like a tenth symbol would incorrectly reject nearly every partial board.

**Map a cell to one of nine boxes**

Rows zero, one, and two share box-row zero because integer division by three gives zero. Rows three through five give one, and rows six through eight give two. Columns group the same way.

The expression

```python
k = i // 3 * 3 + j // 3
```

turns box coordinates `(i // 3, j // 3)` into a flat index. Multiplying the box-row by three skips its three earlier boxes; adding the box-column selects left, middle, or right. The resulting indices are:

```text
0 1 2
3 4 5
6 7 8
```

Every cell maps to exactly one row, one column, and one box.

**Check all three constraints before recording the digit**

For a filled cell, the condition

```python
if row[i][num] or col[j][num] or sub[k][num]:
    return False
```

asks whether the same digit has already appeared in any relevant unit. A true flag proves a duplicate and makes the board invalid immediately.

If all flags are false, the source sets all three to true. Checking before setting is crucial: setting first would make the current cell appear to duplicate itself.

Python short-circuits `or`, but that affects only how many flag reads occur; any one duplicate is sufficient for rejection.

**Maintain a precise scan invariant**

Before processing cell `(i, j)`, each table describes exactly the filled cells encountered earlier in row-major order. Empty cells contributed nothing. If a current flag is already set, the earlier corresponding cell and current cell violate the rule. Otherwise, setting the flags preserves the invariant.

If all 81 cells are processed without rejection, no pair of equal filled digits shares a row, column, or box. Those are exactly the three validity rules, so returning `True` is correct.

**Trace the invalid example's two eights**

The top-left `8` at `(0,0)` maps to digit index seven and box zero, setting `row[0][7]`, `col[0][7]`, and `sub[0][7]`. The later `8` at `(2,2)` maps to the same box zero. Even though it is in a different row and column, `sub[0][7]` is already true, so the method returns `False`.

This illustrates why checking only rows and columns is insufficient.

**The original board remains unchanged**

All writes go to auxiliary Boolean tables. Characters in `board` are only read. Early return is safe because the function promises only a Boolean result, not diagnostic details or a transformed board.

## Complexity detail

For the fixed $9\times9$ contract:

- **Time complexity: $O(1)$.** Exactly 81 cells exist, a constant independent of any input-size parameter.
- **Auxiliary space: $O(1)$.** The three tables always contain exactly 243 Boolean entries.

If generalized to an $N\times N$ board with $N$ symbols and suitable boxes, this table design would take $O(N^2)$ time and $O(N^2)$ space. The manifest uses the problem's fixed-size interpretation.

## Alternatives and edge cases

- **Sets per unit:** More direct membership semantics, but still fixed storage here and generalized $O(N^2)$ entries.
- **Bit masks:** Store nine seen flags in one integer per row, column, and box, reducing constants while preserving the same logic.
- **Rescan each unit per cell:** Avoids tables but repeats work unnecessarily.
- **All dots:** Every cell is skipped and the board is valid.
- **Incomplete but conflict-free board:** Returns true even if it has no possible solution; solvability is not requested.
- **Duplicate in one row:** `row[i][num]` detects it.
- **Duplicate in one column:** `col[j][num]` detects it.
- **Duplicate only in a box:** `sub[k][num]` detects it.
- **Same digit in unrelated units:** Allowed when row, column, and box are all different.
- **Input shape and symbols:** The exact fixed table sizes rely on the guaranteed $9\times9$ board and characters `1-9` or dot.
