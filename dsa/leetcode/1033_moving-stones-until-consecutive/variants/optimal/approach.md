## General

**Sort the three positions conceptually**

The input names `a`, `b`, and `c` do not indicate left-to-right order. The method derives:

- `x` as the minimum position.
- `z` as the maximum position.
- `y = a + b + c - x - z` as the remaining middle position.

The three positions are distinct, so this guarantees `x < y < z`. Only their sorted gaps matter to the game.

Let the left gap be `g_1 = y - x` and the right gap be `g_2 = z - y`. The stones are consecutive exactly when both gaps equal one, which is equivalent to `z - x = 2`.

**Already finished**

Three distinct integer positions cannot have span smaller than two. Therefore, if `z - x` is not greater than two, it must equal two, and the positions are `x, x + 1, x + 2`.

No unoccupied integer lies between the endpoints, so no legal move exists. The initialized values `mi = mx = 0` are returned.

This explains the outer condition `if z - x > 2`. All nonterminal configurations have a larger span.

**Minimum moves when one gap is small**

The test `y - x < 3 or z - y < 3` means at least one gap has size one or two.

If `y - x = 1`, the left pair is already consecutive. Move the right endpoint `z` to `y + 1`. Because the overall configuration was not already complete, `y + 1 < z`, so the target lies strictly between the old endpoints and is unoccupied. The result is three consecutive stones.

If `y - x = 2`, position `x + 1` is the single hole between the left pair. Move endpoint `z` into that hole. The new positions are `x, x + 1, x + 2`.

The two symmetric arguments apply when the right gap is one or two: move the left endpoint next to the right pair or into its one-cell hole.

Thus at least one move is necessary because the current state is nonterminal, and one move is sufficient. The minimum is one.

**Minimum moves when both gaps are large**

Now suppose `y - x >= 3` and `z - y >= 3`.

One move cannot finish the game. If the left endpoint is moved, the unchanged stones `y` and `z` remain at least three positions apart. Two members of a consecutive triple can differ by at most two, so they cannot both belong to a finished configuration. The same argument applies if the right endpoint moves: unchanged `x` and `y` are too far apart.

Two moves are sufficient. Move `x` to `y + 1`. This target lies strictly before `z` because the right gap is at least three, and it is unoccupied. The positions become `y, y + 1, z`. Then move endpoint `z` to `y + 2`, completing the triple.

Therefore, the minimum is two. The expression

`mi = 1 if y - x < 3 or z - y < 3 else 2`

implements exactly these cases.

**Maximum moves as empty positions**

Between endpoints `x` and `z` inclusive there are `z - x + 1` integer positions. Three contain stones, so the number of empty positions inside the span is

$$
(z-x+1)-3=z-x-2.
$$

This quantity is zero precisely at the terminal configuration. The code assigns it to `mx`.

Every legal move takes an endpoint and places it strictly inside the old span. As a result, the new outer span is smaller. Because positions are integers, it shrinks by at least one, so the number of interior empty positions decreases by at least one. No play sequence can therefore contain more than `z - x - 2` moves.

**Why that upper bound can be achieved**

To maximize moves, shrink an outer gap only one position at a time.

If `x + 1` is unoccupied, move the left endpoint from `x` to `x + 1`. The new position is strictly inside the old endpoints, and the total span decreases by exactly one.

Repeat while the left gap has holes. Once the left stone is adjacent to `y`, use the symmetric move on the right: move `z` to `z - 1` whenever that position is unoccupied. Each move again decreases the span by exactly one.

This process continues until both gaps are one. It uses one move for every initial empty position, exactly `z - x - 2` moves. The upper bound is attainable and is therefore the maximum.

The endpoint labels are recomputed after each move. Moving the current left endpoint one step inward remains legal as long as that position is not occupied.

**Trace `1, 2, 5`**

The sorted positions are `x = 1`, `y = 2`, and `z = 5`. The span is four, so play is not finished.

The left gap is one, which is below three. For the minimum, move five directly to three, obtaining `1, 2, 3` in one move.

For the maximum, there are `5 - 1 - 2 = 2` empty positions inside the span. Move five to four, producing `1, 2, 4`, then move four to three. This uses two moves.

**Why the formulas cover all states**

Distinct sorted integer positions give span at least two. Span two is exactly the zero-move state. Every larger span has a minimum of either one or two: one exactly when some adjacent gap is at most two, otherwise two. The maximum is determined solely by initial empty positions and is always attainable one unit at a time.

No simulation is needed because there are only three stones and these gap arguments completely characterize optimal short and long play.

## Complexity detail

The method computes one minimum, one maximum, several additions and subtractions, and a constant number of comparisons. It does not loop over the coordinate range. Time complexity is `O(1)`.

It stores only `x`, `y`, `z`, `mi`, and `mx`. The two-element returned list is constant-sized. Space complexity is `O(1)`. Both match the manifest.

The numeric coordinate limit of 100 does not drive the complexity; the same formulas work for arbitrarily distant integer positions.

## Alternatives and edge cases

- **Breadth-first search over configurations:** Enumerating every legal move can find the minimum for small coordinates, but state count grows and it gives no simple maximum proof. Gap formulas solve both objectives directly.
- **Recursive game simulation:** Exploring move sequences repeats configurations and obscures why maximum play is finite. The empty-position potential gives an exact bound.
- **Sort a three-element list:** `sorted([a, b, c])` is equally correct and still constant time. The exact solution derives the middle through the sum to avoid allocating the temporary list.
- **Input already sorted or reversed:** Minimum, maximum, and total-sum recovery produce the same `x, y, z` regardless of argument order.
- **Three consecutive positions:** Span equals two, so both answers remain zero.
- **One adjacent pair:** A gap of one guarantees a one-move finish by placing the opposite endpoint beside that pair.
- **A one-position hole:** A gap of two also gives a one-move finish by filling the hole with the opposite endpoint.
- **Both gaps at least three:** One move is impossible because whichever endpoint remains paired with the middle is still too far away; exactly two moves suffice.
- **Highly unbalanced gaps:** Minimum may still be one if the small gap is one or two, while maximum counts holes across both gaps.
- **Strictly interior target rule:** The one-move constructions always place the moved endpoint between the old endpoints, not outside or on an occupied location.
- **Dynamic endpoints:** After a move, the lowest and highest stones may be different physical stones. The maximum construction reasons about positions, not stone identities.
- **Why maximum is not the larger gap alone:** Empty positions in both gaps can be consumed one at a time, so the total `(g_1 - 1) + (g_2 - 1)` equals `z - x - 2`.
- **Distinct-value guarantee:** It ensures strict order and prevents zero gaps. Duplicate positions would not describe three separate stones under the source contract.
