# N-Queens

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 51 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Backtracking |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/n-queens/) |

## Problem Description
### Goal
Place exactly `n` chess queens on an $n \times n$ board. A valid placement must prevent every pair of queens from sharing a row, a column, or either diagonal, since queens attack along all of those lines.

Return every distinct valid board in any order. Represent each board as `n` strings of length `n`, using `Q` for a queen and `.` for an empty square. Each valid board must appear once. When no placement exists, return an empty collection.

### Function Contract
**Inputs**

- `n`: the board width and number of queens, with $1 \le n \le 9$

**Return value**

A `List[List[str]]` containing every distinct valid board.

### Examples
**Example 1**

- Input: `n = 4`
- Output: `[ [".Q..", "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."] ]`

**Example 2**

- Input: `n = 1`
- Output: `[["Q"]]`

**Example 3**

- Input: `n = 2`
- Output: `[]`

### Required Complexity

- **Time:** $O(n!)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**One queen per row reduces the board to column choices**

Search from the first row downward. The recursion depth itself enforces one queen per row, so a partial board needs only the chosen column for each earlier row. Three bit masks record occupied columns and the two diagonal directions attacked in the current row.

With `board_mask = (1 << n) - 1`, safe positions are:

```text
available = board_mask & ~(columns | descending | ascending)
```

Extract `bit = available & - available` to visit one safe column, remove it, and continue until no choices remain. The bit's index is the column recorded for board construction.

**Shift diagonal attacks when moving to the next row**

For the next row, one diagonal direction attacks a column one bit to the left and the other attacks one bit to the right. Thus the recursive state uses `(descending | bit) << 1` and `(ascending | bit) >> 1`. Masking the left-shifted value to `board_mask` is optional in an arbitrary-precision language when availability is masked later, but keeps the state explicitly within the board.

Column attacks do not shift: a queen continues to attack the same column in every lower row.

**Masks encode exactly the conflicts relevant to the current row**

Before searching a row, `columns` marks exactly the columns used above it, while the two diagonal masks mark exactly the squares attacked in that row. Therefore every free bit is a safe placement, and every unsafe placement is excluded before recursion.

**Materialize a board only at a complete placement**

Keep a path of selected column indices. When its length reaches `n`, convert each column into a row string containing one `Q` and $n - 1$ dots. Delaying string construction avoids rebuilding partial board rows at every failed search node.

**Trace a representative input**

For $n = 4$, choosing column 1 in row 0 removes that column and its shifted diagonal neighbors from row 1. Continuing with the only compatible choices yields `.Q.. / ...Q / Q... / ..Q.`. Backtracking restores the masks implicitly and discovers the reflected solution beginning in column 2.

**One safe-bit path represents each board**

Each recursion level represents a new row, and a chosen bit is absent from the occupied column and both diagonal masks. Every placed queen therefore avoids all earlier queens; reaching row `n` yields a valid board.

Conversely, any valid board specifies one column in each row. Because that queen conflicts with no earlier placement, its bit remains in the free-choice mask at every prefix, so the search follows the board's full path. Different row-column choices create different paths and rendered boards, making the enumeration complete and duplicate-free.

#### Complexity detail

The row-by-row search has an $O(n!)$ upper bound because available columns decrease with depth; diagonal pruning substantially reduces the explored tree. The position path and recursion depth use $O(n)$ auxiliary space, excluding returned boards.

#### Alternatives and edge cases

- **Enumerate all column permutations, then test diagonals:** avoids duplicate columns but explores all $n!$ permutations even when a prefix is already impossible.
- **Sets for columns and diagonals:** expresses the same pruning clearly but has more allocation and hashing overhead than bit masks.
- **Scan the partial board for every placement:** remains backtracking but adds an $O(n)$ conflict check at each node.
- $n = 1$ has one solution. $n = 2$ and $n = 3$ exhaust all safe prefixes without reaching depth `n`.
- Reflected or rotated boards count as distinct placements when their queen coordinates differ; the search should not symmetry-deduplicate the required output.

</details>
