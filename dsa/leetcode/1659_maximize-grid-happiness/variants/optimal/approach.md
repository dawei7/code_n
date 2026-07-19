## General
**Reduce the frontier by orienting the grid.** Rotate the dimensions conceptually so the shorter side has $c$ cells. Process the resulting $r \times c$ grid in row-major order. When deciding the current cell, only its left neighbor and the cell directly above can already be occupied; interactions with right and lower neighbors will be counted when those cells are processed.

**Encode the preceding cells in base three.** Store the last $c$ cell types as a ternary mask: 0 for empty, 1 for introvert, and 2 for extrovert. The oldest ternary digit identifies the person above the current cell, while the newest digit identifies the left neighbor except at a row boundary. Appending the current type and discarding the oldest digit produces the next frontier mask.

**Memoize placement resources and position.** A state consists of the row-major position, frontier mask, and remaining introvert and extrovert counts. Try leaving the cell empty. When the corresponding count is positive, also try placing either person type, adding its base happiness plus the complete pair effect with the already processed upper and left neighbors. Memoization merges all partial layouts that expose the same future-relevant state.

**Why local pair scoring yields the global total.** Every resident's base happiness is added exactly when that resident is placed. Every horizontal or vertical neighboring pair is encountered exactly once, when its later row-major endpoint is placed, and the pair adjustment already combines both people's reactions. Thus each completed DP path has precisely the happiness of its represented grid. Taking the maximum across all empty, introvert, and extrovert choices includes every legal partial placement, including choices that leave available people unused.

## Complexity detail
There are $rc$ positions, $3^c$ frontier masks, and at most $(I+1)(E+1)$ remaining-count pairs. Each state considers at most three constant-time choices, giving $O(rc3^c(I+1)(E+1))$ time. The memo table and recursion stack are bounded by $O(rc3^c(I+1)(E+1))$ space.

## Alternatives and edge cases
- **Row-state dynamic programming:** Precompute each ternary row's residents, internal happiness, and compatibility with every preceding row. This has the same profile-DP principle but trades simpler transitions for a $3^c \times 3^c$ compatibility table.
- **Enumerate complete grids:** Trying empty, introvert, and extrovert for every cell costs $O(3^{mn})$ before count pruning and repeats equivalent frontiers.
- **Greedy placement by base happiness:** Always preferring introverts or locally favorable cells misses pair effects and the benefit of leaving a person unplaced.
- With no available people, the maximum is zero.
- When both types are available for one cell, placing the introvert is better than placing the extrovert, and leaving the other person unused is legal.
- Two diagonal occupants are not neighbors and cause no pair adjustment.
- A mixed adjacent pair changes total happiness by $-10$, not by either participant's individual change alone.
- Rotating the dimensions changes no adjacency relation and minimizes the exponential mask width.
- Counts may exceed the number worth placing; the empty transition ensures negative marginal placements are never forced.
