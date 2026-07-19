## General
**Track paths that are still inside**

Let the current grid store how many direction sequences place the ball at each cell after exactly the moves processed so far without having left the board. Initially only the starting cell has count one.

**Advance one move layer**

For every nonzero cell count, consider the four orthogonal directions. Add the count to the corresponding cell in a fresh next grid when the destination remains inside. When the destination is outside, add the count directly to the answer because that direction sequence has now produced a valid path.

**Stop extending escaped paths**

An exited path is accumulated once and never placed into the next grid. Consequently, every counted sequence is classified at its first boundary crossing and cannot be counted again on later layers. Repeating this transition through `maxMove` layers includes exits after any permitted number of moves.

**Why every valid path is counted exactly once**

Before each layer, the grid count at a cell equals the number of still-inside direction prefixes ending there. Extending each prefix by all four possible directions generates every next prefix once. Inside extensions preserve the state invariant; outside extensions are precisely the newly completed valid paths. Induction over the move layers therefore covers every allowed path and no invalid or duplicate path.

## Complexity detail
Each of at most `maxMove` layers scans `m n` cells and four constant directions, for $O(m n maxMove)$ time. The current and next grids use $O(m n)$ space. Counts are reduced modulo `1,000,000,007` throughout.

## Alternatives and edge cases
- **Top-down memoization:** cache the number of exits from each `(row, column, movesRemaining)` state; it has the same time bound but uses $O(m n maxMove)$ cache space and recursion.
- **Full three-dimensional table:** makes every move layer explicit but uses $O(m n maxMove)$ space unnecessarily.
- **Unmemoized path enumeration:** is correct for tiny inputs but can explore `4 ** maxMove` direction sequences.
- **Recompute every exact path length separately:** avoids exponential enumeration but repeats earlier layers and takes $O(m n maxMove^2)$ time.
- **Zero moves:** no boundary can be crossed, so the answer is zero.
- **One-cell grid:** each of the four first moves exits immediately; escaped paths are not extended further.
- **Corner and edge starts:** multiple first directions may leave the grid and must each contribute separately.
- **Modulo reduction:** apply it during transitions to keep all intermediate counts bounded.
