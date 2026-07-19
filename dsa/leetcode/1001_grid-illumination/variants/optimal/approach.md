## General
**Index every illuminated line:** Maintain counters for active lamps in each row, column, main diagonal `row - col`, and anti-diagonal `row + col`. Also keep a set of active coordinates. Insert a listed lamp only if its coordinate is not already active, preventing duplicates from inflating the counters.

**Answer a query from four counters:** A query cell is illuminated exactly when at least one of its row, column, or two diagonal counters is positive. Record that answer before changing any lamp state, preserving the required query order.

**Remove only the local neighborhood:** Examine the query cell and its eight neighboring coordinates. When one is active, remove it from the set and decrement all four corresponding line counters. There are always only nine candidate shutdown positions, so no grid-sized work is needed. The counters remain equal to the active-lamp incidence on every indexed line, which proves each subsequent answer is accurate.

## Complexity detail
Deduplicating and indexing the $L$ listed lamps takes $O(L)$ time. Each of the $Q$ queries performs constant-time counter lookups and at most nine set removals, so total time is $O(L+Q)$. The active set and line counters use $O(L)$ space.

## Alternatives and edge cases
- **Scan every active lamp per query:** Directly testing all rows, columns, and diagonals is correct but takes $O(LQ)$ time when shutdowns remove nothing.
- **Materialize the grid:** The side length can be $10^9$, so an $n\times n$ matrix is infeasible and unnecessary.
- **Duplicate lamp positions:** Count a coordinate once; one shutdown removes that lamp completely.
- **Answer-before-shutdown order:** A lamp in the queried cell illuminates that query before being turned off.
- **Repeated queries:** Their answers may change because earlier queries mutate the active lamp set.
