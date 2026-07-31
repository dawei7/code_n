## General

**Give every ordered subboard one optimal value**

Let `best[h][w]` be the greatest revenue obtainable from a piece whose height
is `h` and width is `w`. Initialize this value with the direct sale price for
`[h, w]`, or zero when that shape is not listed. Keeping the dimensions ordered
is essential because rotation is forbidden.

Process heights and widths from small to large. A horizontal cut at `cut`
produces pieces `cut x w` and `(h - cut) x w`; a vertical cut analogously
produces `h x cut` and `h x (w - cut)`. Both smaller dimensions have already
been solved, so their values can be added. Examine every cut and retain the
best result alongside the direct-sale option.

Every allowed first action is represented: sell the piece, leave it unsold, or
make one full horizontal or vertical cut. For a cut, the two resulting pieces
are independent, and their table entries already contain their best possible
continuations. Taking the maximum over all first actions therefore yields the
optimal value for the current shape. Induction over increasing dimensions
establishes that `best[m][n]` is the greatest obtainable revenue. Complementary
cut positions produce the same two dimensions, so only the first half of each
axis needs inspection.

## Complexity detail

For each of the $mn$ ordered dimensions, at most $m/2$ horizontal and $n/2$
vertical cut positions are examined. The total time is
$O(mn(m+n))$. The table has $(m+1)(n+1)$ entries, so auxiliary space is
$O(mn)$.

## Alternatives and edge cases

- **Top-down memoization:** The same recurrence can be evaluated on demand in $O(mn(m+n))$ time, but recursion and a memo table add control-flow overhead.
- **Evaluate paired cuts:** Trying a horizontal and vertical cut together remains correct because the four rectangles form a legal sequential partition, but considering every pair increases the bound to $O(m^2n^2)$.
- **Unmemoized recursion:** Re-solving identical subboards after different cut sequences causes exponential repetition.
- **Orientation:** Store and query `[height, width]` exactly as listed; never copy a price into the transposed table cell.
- **Repeated shapes:** Independent subboards may use the same price entry any number of times.
- **Unsold pieces:** A missing direct price contributes zero, which permits an unusable remainder to be left unsold.
- **Whole-board sale:** The initial direct price must remain a candidate even when cuts are possible.
