## General
**Expose each row's immediate neighbors**

Order by `seat_id` and use `LAG` and `LEAD` to attach the preceding and following identifiers and availability flags to every seat.

**Require a truly consecutive free neighbor**

Keep the current row only when it is free and either the previous row is free with identifier `seat_id - 1`, or the next row is free with identifier `seat_id + 1`. Checking identifiers makes the logic robust even if a data set has a gap.

**Why every qualifying seat is returned**

A seat belongs to a consecutive available pair exactly when one of its numeric neighbors exists and is free. The two window comparisons test those two possibilities directly. Runs longer than two satisfy the condition at their endpoints through one neighbor and at interior seats through both, so every run member appears exactly once.

## Complexity detail
For `n` seats, the window ordering generally costs $O(n \log n)$ time and $O(n)$ working space. Filtering and final output ordering fit within that bound.

## Alternatives and edge cases
- **Self-join adjacent identifiers:** join free seats on an absolute identifier difference of one and union both endpoints; it is correct but requires deduplication.
- **Windowed three-row sum:** works when seat identifiers are guaranteed gapless, but explicit identifier checks are more robust.
- **Correlated neighbor existence:** is direct but may rescan the table for every seat and take $O(n^2)$ time without an index.
- **Isolated free seat:** is excluded.
- **Exactly two free seats:** both are returned.
- **Long free run:** every seat in the run is returned.
- **Occupied seat between free seats:** breaks adjacency.
- **Identifier gap:** does not create a consecutive pair.
- **Output order:** must be ascending by seat identifier.
