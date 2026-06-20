# N-Queen (Branch and Bound)

| | |
|---|---|
| **ID** | `bb_05` |
| **Category** | branch_and_bound |
| **Complexity (required)** | $O(N!)$ Worst Case |
| **Difficulty** | 5/10 |
| **Interview relevance** | 7/10 |
| **Wikipedia** | [Eight queens puzzle](https://en.wikipedia.org/wiki/Eight_queens_puzzle) |

## Problem statement

The N-Queens puzzle is the problem of placing N chess queens on an N x N chessboard so that no two queens threaten each other.
This means no two queens can share the same row, column, or diagonal.
While this is classically solved using Backtracking, you can drastically optimize the constraint-checking step using an array-based **Branch and Bound** state tracker.

**Input:** An integer N.
**Output:** The number of valid distinct solutions (or the list of board configurations).

## When to use it

- When asked to optimize standard Backtracking code. A naive backtracking solution iterates through the board array to check if a Queen attack is valid, taking $O(N)$ time per placement. Branch and Bound uses pre-calculated hash arrays to validate constraints in strict $O(1)$ time!

## Approach

The classic backtracking approach places a queen in row r, column c, and then calls a function `is_safe(r, c)`. That function scans the entire row, column, and two diagonals, taking $O(N)$ time.

**The Branch and Bound Optimization ($O(1)$ Checks):**
Instead of manually scanning the board, we can maintain four "Bound" arrays.
1. `cols_taken[N]`: True if a queen is anywhere in that column.
2. `rows_taken[N]`: True if a queen is anywhere in that row.
3. `diag1_taken[2N-1]`: The primary diagonals (top-left to bottom-right). Notice a mathematical invariant: for any cell (r, c) on the exact same primary diagonal, the value **r - c is always constant**! (We offset it by +N-1 so array indices aren't negative).
4. `diag2_taken[2N-1]`: The secondary diagonals (top-right to bottom-left). For any cell on the same secondary diagonal, the value **r + c is always constant**!

By tracking these invariants, `is_safe(r, c)` becomes a simple $O(1)$ check:
`if not cols_taken[c] and not diag1_taken[r - c + N - 1] and not diag2_taken[r + c]: place_queen()`

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for bb_05: N-Queen (Branch and Bound).

Place N queens on an N x N board so that no two
"""


def solve(n):
    """N-queen via branch and bound (column-by-column with
    O(1) row/diagonal lookups)."""
    if n <= 0:
        return []
    row_used = [False] * n
    # / diagonal: r + c. backslash diagonal: c - r + (n - 1).
    slash = [False] * (2 * n - 1)
    backslash = [False] * (2 * n - 1)
    placement = []                        # list of (row, col)
    found = []

    def dfs(col):
        if col == n:
            found.extend(placement)
            return True
        for r in range(n):
            si = r + col
            bi = col - r + (n - 1)
            if row_used[r] or slash[si] or backslash[bi]:
                continue
            row_used[r] = True
            slash[si] = True
            backslash[bi] = True
            placement.append((r, col))
            if dfs(col + 1):
                return True
            placement.pop()
            row_used[r] = False
            slash[si] = False
            backslash[bi] = False
        return False

    dfs(0)
    return sorted(found)
```

</details>

## Walk-through

`N = 4`.
Start `row = 0`.
- Try `col = 0`.
  - `d1_id = 0 - 0 + 3 = 3`. `d2_id = 0 + 0 = 0`.
  - Free? Yes. Place Queen at `(0,0)`.
  - State: `cols[0]=T`, `diag1[3]=T`, `diag2[0]=T`.

Recurse `row = 1`.
- Try `col = 0`: `cols[0]` is True. Blocked!
- Try `col = 1`: `d1_id = 1 - 1 + 3 = 3`. `diag1[3]` is True! (Threatened by 0,0 on primary diagonal). Blocked!
- Try `col = 2`: `d1_id = 1 - 2 + 3 = 2`, `d2_id = 1 + 2 = 3`. All Free!
  - Place Queen at `(1,2)`.
  - State: `cols[2]=T`, `diag1[2]=T`, `diag2[3]=T`.

Recurse `row = 2`... (If all columns block, the function returns, popping the call stack back up, triggering the `False` un-marks, and trying the next column at the previous level. This is the essence of backtracking with bounds!)

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(N!)$ | $O(N)$ |
| **Average** | $O(N!)$ | $O(N)$ |
| **Worst** | $O(N!)$ | $O(N)$ |

The time complexity remains $O(N!)$ in the absolute worst-case tree exploration because we iterate N columns, then N-1, etc. However, replacing the $O(N)$ loop inside `is_safe` with an $O(1)$ array lookup reduces the overall operations by a factor of N, massively speeding up the wall-clock execution time.
Space complexity is $O(N)$ for the recursion call stack and the constraint arrays.

## Variants & optimizations

- **Bitmasking:** Instead of using boolean arrays, you can use raw bitwise integers to track the taken columns and diagonals! Shifting the integer `(diag1 >> 1)` instantly passes the state to the next row. This is the most legendary and heavily optimized way to solve N-Queens, running entirely in CPU registers.

## Real-world applications

- **Constraint Satisfaction Problems (CSP):** The math of assigning physical frequencies to cellular towers so that overlapping ranges do not interfere is directly analogous to non-threatening queens.

## Related algorithms in cOde(n)

- **[backtrack_01 - N-Queens](../backtracking/backtrack_01_n-queens.md)** — The classic backtracking version, without the mathematical $O(1)$ bounding arrays.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
