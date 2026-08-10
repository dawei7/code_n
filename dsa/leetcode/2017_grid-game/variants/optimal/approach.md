## General

**A first-robot path is determined by one column**

In a grid with only two rows, a path begins on the top row, moves right some number of times, moves down exactly once, and then continues right on the bottom row. Choose the column `j` where the first robot moves down.

That path clears top-row columns zero through `j` and bottom-row columns `j` through the end.

The two cells in column `j` are both on the first robot's path: it arrives at the top cell and moves down into the bottom cell. This shared cleared column separates the surviving top-right and bottom-left regions, which is why neither remaining sum includes column `j`.

**Identify what remains for the second robot**

Only two positive regions can remain:

- the top-row suffix strictly after `j`;
- the bottom-row prefix strictly before `j`.

The second robot cannot collect both regions. To collect the bottom-left prefix it must move down early and can never move back up to the top-right suffix. To collect the top-right suffix it stays on top past the cut and misses the bottom-left prefix.

It can choose whichever region has the larger sum, so for a fixed first-robot turn column its optimal score is

$$
\max(\text{top suffix after }j,\text{bottom prefix before }j).
$$

**Maintain both sums with exact update order**

`s1` begins as the sum of the entire top row. `s2` begins at zero.

At column `j`, the source first executes `s1 -= grid[0][j]`. Now `s1` is the top suffix strictly after the turn column, excluding the cell cleared by the first robot.

It computes `max(s1,s2)` while `s2` still contains only bottom columns strictly before `j`. This is exactly the second robot's best response.

Only afterward does `s2 += grid[1][j]` prepare the bottom prefix for the next turn column.

Changing this order would incorrectly leave a turn-column cell available even though the first robot traverses both row cells at the downward move.

**Apply the minimax choice**

The first robot knows that the second will select the larger remaining region. It therefore chooses the turn column minimizing that maximum.

`ans` starts at infinity and updates with

`ans = min(ans, max(s1, s2))`

for every possible `j`. This is the minimax structure directly: minimum over first-player choices of maximum second-player outcomes.

**Trace the first example**

For top row `[2,5,4]` and bottom row `[1,5,1]`:

- turning at zero leaves top suffix nine and bottom prefix zero, so the second gets nine;
- turning at one leaves top suffix four and bottom prefix one, so it gets four;
- turning at two leaves top suffix zero and bottom prefix six, so it gets six.

The first robot selects column one and limits the second robot to four.

**Why there is no third useful second path**

After the first path is cleared, any second path turns down at some column. If it turns no later than the first cut, its only nonzero opportunity lies in the bottom prefix; delaying within that side cannot exceed collecting the whole prefix. If it turns later, its only nonzero opportunity lies in the top suffix.

Thus every possible second path is bounded by one of the two region sums, and paths exist that collect each whole region. Their maximum is exact.

The second robot may traverse zeroed cells to connect its chosen region to the start and destination; zeroes block points, not movement.

**Why maximizing the first robot's own score is different**

The objective is adversarial denial, not the first robot's collected total. A path collecting many points may leave an even larger connected region for the second. The minimax expression evaluates the opponent's remaining options directly.

## Complexity detail

Let $N$ be the number of columns. Computing the initial top sum takes $O(N)$ and the loop takes $O(N)$, for total time $O(N)$.

Only `ans`, `s1`, `s2`, and loop variables are stored, so auxiliary space is $O(1)$. The grid is not modified despite the story describing cleared cells.

## Alternatives and edge cases

- **Simulate both paths:** Enumerating first and second turn columns takes $O(N^2)$ and is unnecessary after deriving the two regions.
- **Prefix-sum arrays:** Permit constant-time region queries for every cut but use $O(N)$ space; rolling sums are simpler.
- **Maximize first robot's points greedily:** Solves the wrong objective and can leave a larger score for the opponent.
- **One column:** The first robot clears both cells and the second receives zero.
- **Turn at first column:** Bottom prefix is empty and only top suffix can score.
- **Turn at last column:** Top suffix is empty and only bottom prefix can score.
- **Balanced regions:** The second may choose either; their equal value is still the fixed-cut outcome.
- **Positive cell values:** Ensure collecting an entire available region is never worse than skipping part of it.
- **Update order:** Remove current top, evaluate, then add current bottom.
- **Large sums:** Python integers avoid overflow across $5\cdot10^4$ columns.
- **No grid mutation:** Running sums model the cleared path without writing zeroes.
- **Minimax:** First chooses the smallest possible value of the second's best response.
