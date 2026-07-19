## General
**Start where either move discards a region.** Begin at the top-right cell. If it is `0`, row sorting proves that every cell to its left in the same row is also `0`, so advance to the next row. If it is `1`, record that column implicitly by moving left; there may be an earlier `1`, but no column to the right can improve the answer.

**Walk only left or down.** Continue until the row index reaches $m$ or the column index becomes negative. The current column moves only left and the current row moves only down, so no cell is queried twice and at most $m+n$ interface calls are needed.

**Why the last feasible column is leftmost.** Whenever the scan moves down, the discarded row has no `1` at or left of the current column. Whenever it moves left, the observed `1` proves the current column is feasible. Therefore, after the walk ends, the last feasible column is the smallest one containing a `1`; if no feasible column was observed, the column remains $n-1$ after all rows are exhausted and the answer is `-1`.

## Complexity detail
The staircase walk makes at most $m$ downward moves and $n$ leftward moves, so it uses $O(m+n)$ time and `get` calls. Only row and column indices are stored, giving $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Binary search each row:** Finding each row's first `1` independently takes $O(m\log n)$ time and interface calls, which is slower when many rows must be examined.
- **Inspect every cell:** A full scan takes $O(mn)$ calls and can exceed the judge's query limit.
- **All zeroes:** The walk reaches the bottom without moving left and returns `-1`.
- **All ones:** The walk moves across the entire first row and returns column `0`.
- **Single row or column:** The same directional rules reduce to a one-dimensional scan.
- **Hidden storage:** Use only `get` and `dimensions`; the underlying matrix is not directly accessible.
