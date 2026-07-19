## General
**Fix a bottom row and summarize vertical runs as a histogram**

Maintain one height per column while scanning rows top to bottom. A `"1"` extends that column's consecutive-one run by one; a `"0"` resets it to zero because no all-one rectangle ending at this row can cross that cell.

After updating row `r`, `heights[c]` is exactly the number of consecutive ones ending at `(r,c)`. Any all-one rectangle with bottom row `r` is therefore a contiguous histogram span whose height is the minimum of those column heights. Conversely, every rectangle under this histogram identifies that many all-one rows above `r`.

**A monotonic stack evaluates every possible limiting height**

For each updated histogram, keep nondecreasing `(start, height)` pairs. `start` is the earliest column since which every height is at least the candidate height. When a lower bar arrives, pop taller candidates: the current column is their first shorter boundary on the right, and their stored start is the first legal column on the left.

Carry the earliest popped start into the new lower height, because that height can extend across all columns that supported the taller bars. A conceptual zero sentinel after the final column forces every unresolved positive height to be evaluated for this row.

**Histogram state is rebuilt for each possible rectangle bottom**

After row `r`, each height is the exact consecutive-one depth ending there. During its histogram scan, every stack entry represents an unresolved height that remains valid through the previous column. Popping computes its maximal span; retaining it allows a future wider span. The stack is cleared after the sentinel, while the height array persists into the next matrix row.

**Trace the row that contains the optimal bottom boundary**

In the standard example, the third row creates heights `[3,1,3,2,2]`. The final two height-2 bars combine with the preceding height-3 bar over width 3, producing area 6.

**Every matrix rectangle appears in its bottom-row histogram**

Fix any all-one rectangle and inspect its bottom row. Every covered column's accumulated height is at least the rectangle's height, so the histogram solver considers a span containing that rectangle at an appropriate limiting height.

Conversely, a histogram rectangle of height `h` across consecutive columns means each column has `h` consecutive ones ending at the current row. Those cells form a valid matrix rectangle. Taking the largest histogram area over every possible bottom row therefore includes all and only valid rectangles.

## Complexity detail
Each row updates `n` heights, and each height is pushed and popped at most once in that row, giving $O(mn)$ time. Heights and stack use $O(n)$ space.

## Alternatives and edge cases
- **Enumerate row and column boundaries:** can take $O(m^2 n^2)$ time.
- **Expand from every one cell:** repeats overlapping rectangle checks heavily.
- **Width-based dynamic programming:** can also solve the problem but often needs more complex upward scans or boundary state.
- An all-zero matrix keeps every height zero and returns zero. An all-one `m × n` matrix eventually evaluates area `mn` on its final row.
- The reduction relies on rectangles aligned with matrix rows and columns; each candidate has a unique bottom row at which it is considered.
