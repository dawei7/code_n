## General
**The height represented by one state**

For an upright orientation, let the state at `(r, c)` be the greatest fertile pyramid height whose apex is that cell. A barren apex has height zero. A fertile apex always supplies height one, but extending it by another level requires three supporting pyramids in the row below: those centered at columns `c - 1`, `c`, and `c + 1`.

Therefore an interior fertile cell satisfies

$$
\operatorname{height}(r,c)
= 1 + \min\!\bigl(
\operatorname{height}(r+1,c-1),
\operatorname{height}(r+1,c),
\operatorname{height}(r+1,c+1)
\bigr).
$$

A boundary column cannot extend beyond height one because an outside supporting cell is barren. Processing rows from bottom to top makes all three dependencies available.

**Why a maximum height contributes several plots**

If an apex supports maximum height $h$, then the nested shapes of heights $2,3,\ldots,h$ are all valid and distinct. Its contribution is therefore $h-1$. Summing that quantity over every apex counts each upright pyramid exactly once, at its unique topmost cell and chosen height.

**Reflecting the recurrence**

Inverse pyramids obey the identical recurrence with support in the row above. A second pass from top to bottom counts them. Only the immediately preceding support row is needed in either pass, so the two-dimensional state can be compressed to two length-$n$ arrays.

## Complexity detail
Each of the $mn$ cells is processed once per orientation with constant work, for $O(mn)$ time. A current row and one supporting row use $O(n)$ auxiliary space.

## Alternatives and edge cases
- **Expand every candidate height:** Testing every cell in every possible triangular plot repeats the same fertility checks and has polynomially slower worst-case growth.
- **Full two-dimensional DP:** Storing every height is correct and still uses $O(mn)$ time, but requires $O(mn)$ rather than $O(n)$ auxiliary space.
- **Prefix sums by row:** Row sums can test whether each horizontal level is fertile, yet every apex may still try many heights, so the worst case remains slower than the local recurrence.
- A single fertile cell and every height-one shape are excluded because a plot must contain more than one cell.
- Upright and inverse plots with the same cells are counted separately when both definitions are satisfied.
- A zero anywhere in a required base level limits every larger pyramid containing that level.
- One-row or one-column matrices cannot contain a height-two pyramid.
