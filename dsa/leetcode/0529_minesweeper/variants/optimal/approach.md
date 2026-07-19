## General
**Handle a mine before starting a search**

If the clicked cell contains `M`, replace it with `X` and return immediately. No other square changes after a mine is selected.

**Reveal empty cells as a graph traversal**

Treat each empty square as a vertex connected to its up to eight surrounding squares. Start a queue at the clicked empty cell. When a cell is first scheduled, mark it `B` immediately so another neighbor cannot enqueue it again.

**Stop expansion at numbered boundaries**

For each queued square, inspect only its valid neighbors and count unrevealed mines. A positive count replaces the provisional `B` with the corresponding digit and stops that branch. A zero count remains `B`, and every still-unrevealed empty neighbor is marked and queued.

**Why the revealed region is exact**

Every expanded `B` square has zero adjacent mines, so revealing all of its neighboring empty squares follows the game rule. Numbered squares are revealed when reached but never expanded. The traversal therefore reaches every empty square connected to the click through zero-mine squares and nothing beyond a numbered boundary; immediate marking ensures each square is processed once.

## Complexity detail
Each of the `rows * cols` cells can enter the queue at most once, and processing examines at most eight neighbors. Time is $O(rows \cdot cols)$. The queue can hold $O(rows \cdot cols)$ cells in the worst case, and the board update is in place.

## Alternatives and edge cases
- **Recursive depth-first search:** implements the same reveal rule compactly but can exceed the call-stack limit on a large blank region.
- **Explicit depth-first stack:** has the same asymptotic bounds as breadth-first search and differs only in reveal order, which does not affect the final board.
- **Scan the whole board for every revealed cell:** counts adjacent mines correctly but can degrade to quadratic time in the number of cells.
- **Clicked mine:** changes only that cell from `M` to `X`.
- **Board boundary:** neighbor coordinates outside the rectangle must be ignored.
- **Diagonal mine:** counts as adjacent just like horizontal and vertical mines.
- **Numbered square:** is revealed but must not propagate the search farther.
- **Mine cells during expansion:** remain `M`; only a directly clicked mine becomes `X`.
