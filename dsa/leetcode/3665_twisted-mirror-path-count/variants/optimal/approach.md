## General

**Direction matters when entering a mirror**

In an ordinary right/down path count, one number per cell is enough: paths from above and left are added because their future choices are identical.

A mirror changes that. A path arriving horizontally is redirected downward, while a path arriving vertically is redirected rightward. The algorithm must therefore keep the two arrival directions separate until it knows whether the current cell is empty or a mirror.

The source represents those directional flows with:

- `from_left`: number of paths entering the current cell from its left, equivalently moving right.
- `from_above[column]`: number of paths entering the current cell from above, equivalently moving down.

After processing the cell, the same variables are reused as outgoing flows:

- Updated `from_left` travels right to the next column.
- Updated `from_above[column]` travels down to the same column in the next row.

This rolling interpretation reduces a full `m x n` directional DP to one array of `n` column values plus one scalar.

**Process cells in row-major order**

The outer loop moves from the top row to the bottom row, and the inner loop moves left to right.

Before cell `(row, column)` is processed:

- `from_left` was produced by cell `(row, column - 1)`, if that cell exists.
- `from_above[column]` was produced by cell `(row - 1, column)`, if that cell exists.

Both predecessors are already processed, and no legal move comes from below or the right. This order is a topological traversal of all right/down movement and reflected movement, because every reflection still advances one row or one column.

At the beginning of each new row, `from_left = 0`. No path can enter the first column from outside the grid’s left boundary.

**Initialize the starting cell**

The top-left cell is guaranteed empty. There is exactly one way to be at the starting point before making any move.

The source sets `total = 1` and writes that value into both outgoing channels:

`from_left = 1`

and

`from_above[0] = 1`.

This does not count the empty starting path twice. It represents its two possible next directions: one path flow may leave right and one may leave down. Those choices lead to distinct full routes.

Boundary overflow is handled naturally. If the start were on an edge, an outgoing channel that points outside would simply never be consumed by another cell.

**Empty cells merge arrivals and allow both directions**

For an empty cell, every path arriving from either direction reaches the cell normally. Once there, it may choose right or down, so both outgoing directions receive the same total:

`total = (from_left + from_above[column]) mod MOD`.

The source assigns `total` back to both channels.

This is the familiar unique-path recurrence, except that the two input counts have remained separate long enough to handle mirrors correctly.

Modulo `1,000,000,007` is applied when counts are added. Every stored channel therefore remains reduced, and later swaps need no additional arithmetic.

**Mirror cells swap directional flows**

Suppose a path approaches a mirror from the left. It was trying to move right, so the mirror turns it downward. That count must leave through the vertical channel.

Suppose a path approaches from above. It was trying to move down, so the mirror turns it right. That count must leave through the horizontal channel.

The exact transition is therefore

`new_from_left = old_from_above`

and

`new_from_above = old_from_left`.

The source performs this with simultaneous assignment:

`from_left, from_above[column] = from_above[column], from_left`.

Python evaluates both right-hand values before either assignment, so neither old count is lost.

The robot is described as reflecting before entering the mirror cell, but representing the mirror as a direction-swapping transition at that coordinate gives the same next cell and path count.

**Consecutive mirrors require no special loop**

After one mirror swaps the channels, its outgoing flow reaches the adjacent cell in the reflected direction. If that next cell is another mirror, row-major processing applies another swap there.

For example, a horizontal arrival reflected down by one mirror becomes a vertical arrival at the mirror below. That second mirror then turns it right, exactly as the note specifies.

There is no need to trace a chain in a separate while loop. The grid traversal processes every mirror encounter once in topological order.

**Invalid reflections disappear at boundaries**

If a mirror in the last column turns a downward arrival to the right, `from_left` receives the count, but there is no next column to consume it. At the start of the next row, `from_left` resets to zero, so the out-of-bounds path vanishes.

If a mirror in the last row turns a rightward arrival downward, the count is stored in `from_above[column]`, but there is no next row to read it.

The same principle applies to ordinary choices that leave the grid. The rolling DP does not create states outside the valid matrix, so invalid paths are discarded without explicit boundary tests.

**Why every valid path is counted once**

At an empty cell, every incoming path is placed into both possible outgoing choices, matching the two voluntary moves. At a mirror, each incoming path has exactly one forced outgoing direction, matching the swap.

Every transition advances right or down, so a path reaches each coordinate in one directional state at a definite point in row-major order. Different sequences of voluntary moves or reflections remain separate counts until they reach an identical state, where adding them is valid because their future behavior is the same.

No transition invents an illegal direction, and out-of-bounds flows are never consumed. By induction over the processing order, the two channels contain exactly all valid partial paths.

The bottom-right cell is guaranteed empty. After it is processed, `from_left` equals the sum of arrivals from its left and above, which is the total number of valid complete paths. The source returns that value.

**Trace an empty `2 x 2` grid**

The start emits one path right and one down. The top-right cell receives one from the left; the bottom-left receives one from above. At the target, those two flows add, giving two paths.

**Trace a mirror turn**

If the robot reaches a mirror from the left, that count does not continue to the next column. The swap places it in `from_above[column]`, so it appears at the cell below during the next row. A simultaneous vertical arrival, if any, is independently moved into `from_left` and continues right.

## Complexity detail

Let the grid have `m` rows and `n` columns. Every cell is processed exactly once, and each transition performs constant work. Total time is `O(mn)`.

`from_above` contains `n` integers. `from_left`, `total`, and loop variables use constant space, so auxiliary space is `O(n)`.

If the grid has more columns than rows, an implementation could transpose the interpretation to use `O(min(m, n))` rolling space, but the exact source allocates by the original column count.

The input grid is read but never modified. Counts are reduced modulo `MOD` as they are added, preventing unbounded growth.

## Alternatives and edge cases

- **Full three-dimensional DP:** Store a count for every cell and both directions. It is conceptually explicit but uses `O(mn)` space instead of the rolling `O(n)` state.
- **One total per cell:** It loses arrival direction, which is necessary to know how a mirror reflects the path.
- **Treat mirrors as blocked cells:** Paths do not stop at mirrors; they are redirected and may continue through chains.
- **Add arrivals at a mirror:** A mirror does not let each arrival choose both directions. It swaps the two flows without addition.
- **Process columns before rows without changing state layout:** The rolling dependencies would no longer align with `from_left` and `from_above`. A different traversal needs a correspondingly transposed representation.
- **Consecutive mirrors:** Each cell-level swap naturally applies the next reflection.
- **Mirror on the last row or column:** A direction turned outside the grid is invalid and is discarded because no future cell reads that channel.
- **Starting and target mirrors:** The constraints guarantee both are empty, so the special initialization and final merge are valid.
- **Modulo after every cell:** Empty-cell additions are reduced immediately; mirror swaps preserve already-reduced counts.
- **No mirrors:** The method becomes the standard rolling unique-path DP.
- **All available routes reflected out:** No flow reaches the target and the returned value is zero.
- **Distinct path definition:** Paths are distinguished by their sequence of moves and reflections, and DP addition counts each sequence once.
- **Input preservation:** The source stores only counts and does not mutate `grid`.
