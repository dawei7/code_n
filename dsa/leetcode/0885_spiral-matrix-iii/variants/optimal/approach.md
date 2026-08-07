## General
Given You start at the cell `(rStart, cStart)` of an `rows x cols` grid facing east. The northwest corner is at the first row and column in the grid, and the southeast corner is at the last row and column, the algorithm executes a single-pass linear scan through input elements. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O(m^2)$ — Operation count bound.
- **Space Complexity**: $O(\texttt{rows} \cdot \texttt{cols})$ — Auxiliary memory allocation bound.
