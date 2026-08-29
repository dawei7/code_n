## General

**Tighten any chosen rectangle around its ones.** Suppose a particular group of ones is assigned to one rectangle. Extending that rectangle beyond the group's topmost, bottommost, leftmost, or rightmost occupied coordinate can only increase or preserve its area. Therefore an optimal answer uses the tight axis-aligned bounding box around the ones assigned to each rectangle.

The helper `f(i1, j1, i2, j2)` examines one inclusive grid region. It scans every cell in that region, records the four extreme coordinates containing a one, and returns

`(x2 - x1 + 1) * (y2 - y1 + 1)`.

This is the minimum rectangle area needed for the ones inside that region. Although the region itself may be large, zeros outside the occupied extremes do not contribute to the returned area.

If a region contains no one, the infinity sentinels remain unchanged and the arithmetic evaluates to positive infinity. Such a candidate cannot improve finite `ans`. The source thereby discards partitions with an empty one-group without an explicit branch. Given at least three ones, an optimal three-rectangle cover can assign at least one one to each rectangle.

**Reduce arbitrary non-overlapping rectangles to six partition families.** Three non-overlapping axis-aligned rectangles can be separated geometrically in one of these ways:

1. three horizontal strips, using two horizontal cuts;
2. three vertical strips, using two vertical cuts;
3. a top region split vertically into two parts, plus one full-width bottom region;
4. one full-width top region, plus a bottom region split vertically;
5. a left region split horizontally into two parts, plus one full-height right region;
6. one full-height left region, plus a right region split horizontally.

These are sometimes pictured as two parallel-strip layouts and four T-shaped layouts. To see why they suffice, consider one rectangle that is separable from the other two by a horizontal or vertical line. If the remaining pair is separated by a parallel line, the result is three strips. If it is separated by a perpendicular line, the result is one of the four T families. Axis alignment and non-overlap guarantee such relative ordering; rectangles may touch, so cuts may lie directly between adjacent cells.

The algorithm enumerates every possible placement of the relevant cut lines. For each resulting three grid regions, it replaces each region by the tight bounding box of the ones inside it through `f`. Those three boxes lie inside disjoint regions, so they cannot overlap.

**Enumerate three horizontal strips.** The first nested loops choose `i1` and `i2` with

$$
0\le i_1<i_2<m-1.
$$

They form row ranges `0..i1`, `i1+1..i2`, and `i2+1..m-1`, each spanning every column. The sum of the three helper results covers the horizontal-strip family.

**Enumerate three vertical strips.** The next loops choose two column cuts `j1` and `j2` and symmetrically evaluate full-height regions `0..j1`, `j1+1..j2`, and `j2+1..n-1`.

**Enumerate the four mixed orientations.** For each horizontal cut `i` and vertical cut `j`, the source evaluates four sums:

- top-left plus top-right plus the full bottom;
- the full top plus bottom-left plus bottom-right;
- top-left plus bottom-left plus the full right;
- the full left plus top-right plus bottom-right.

Together with the two strip loops, these are exactly the six families. `ans` begins at `m * n`, the area of the whole grid, and is replaced whenever one enumerated three-box sum is smaller.

**Why the enumeration returns a valid upper bound.** Each finite candidate has three subregions that are pairwise disjoint and have non-zero row and column dimensions. Each helper box is contained inside its own subregion, so the resulting rectangles are non-overlapping and have positive area. Every one lies in exactly one of the partition regions and therefore inside that region's helper box. Each finite sum is a legal cover.

**Why it cannot miss a better cover.** Begin with any optimal three-rectangle cover. Its relative layout belongs to one of the six separation families. Extend the separating lines to grid boundaries; this assigns every cell, and hence every covered one, to one of the three enumerated regions for some loop indices. When the algorithm evaluates those cuts, `f` returns the tightest box around the ones in each region. That box is no larger than the corresponding rectangle from the chosen optimal cover. The evaluated sum is therefore no greater than the supposed optimum, while the previous paragraph shows it is itself legal. Hence the minimum enumerated sum equals the true optimum.

For the grid `[[1,0,1],[1,1,1]]`, one useful mixed partition uses a vertical separation between columns $0$ and $1$ while splitting the right side horizontally. The left full-height region has a tight area of two, the top-right region covers the one at $(0,2)$ with area one, and the remaining lower-right ones can be bounded appropriately. Considering all cut locations and orientations finds the stated minimum of five without guessing which individual one belongs to which rectangle.

## Complexity detail

Let $R$ be the number of rows and $C$ the number of columns. The helper does not use prefix sums or caching. A call over a region of height $h$ and width $w$ costs $O(hw)$ time and $O(1)$ auxiliary space.

There are $O(R^2)$ horizontal two-cut candidates. For one candidate, its three regions partition the grid, so their helper scans total $RC$ cells. This part costs $O(R^3C)$. The vertical-strip part symmetrically costs $O(RC^3)$. There are $O(RC)$ mixed cut pairs; four constant configurations are tested, and the three regions of each configuration total $RC$ scanned cells. This costs $O(R^2C^2)$.

Combining them gives

$$
O\bigl(RC(R^2+RC+C^2)\bigr)
$$

time. On an $N\times N$ grid, that is $O(N^4)$. Only boundary variables and loop indices are stored, so auxiliary space is $O(1)$.

These facts materially disagree with the manifest. Its summary claims “cached prefix-assisted bounding boxes,” but `f` is a fresh nested scan on every call and has no decorator, memo table, or prefix structure. Its stated time $O((R+C)(R^2+RC+C^2))$ and space $O(RC+R^2+C^2)$ do not describe the checked-in source. The exact bounds are the repeated-scan time above and $O(1)$ auxiliary space. The small constraint $R,C\le30$ makes the quartic square-grid behavior bounded enough for this implementation.

## Alternatives and edge cases

- **Precompute every subregion's bounding area:** Cache `f` by its four boundaries or precompute the particular strip/corner areas used by the six families. This trades memory for avoiding repeated cell scans and is closer to the manifest's description.
- **Prefix-assisted boundary queries:** Ordinary sums can reveal whether a band contains a one, allowing boundary searches or precomputed directional boxes. A carefully designed version can reduce repeated work, but it is not present in the exact source.
- **Rotate the grid:** The editorial implements fewer orientations on the original grid and repeats them after a $90^\circ$ rotation. The exact source writes all six orientations explicitly instead.
- **Assign each one to one of three labels:** Enumerating $3^K$ assignments for $K$ ones and bounding each label is correct for tiny $K$ but exponential.
- **Only three horizontal or vertical strips:** These miss T-shaped layouts, which can be strictly smaller when two clusters share one side of the grid and a third lies across it.
- **Empty partition region:** `f` returns infinity through its sentinels, so that candidate is ignored. This enforces that each selected piece contains at least one one in the source's model.
- **At least three ones:** This guarantee supports three nonempty one-groups. Without it, three positive-area rectangles might include rectangles covering no one, requiring different empty-region handling.
- **One row:** Horizontal and mixed loops have no candidates, but two vertical cuts can separate at least three occupied cells because the at-least-three-ones guarantee implies at least three columns.
- **One column:** The horizontal-strip loop handles the symmetric case.
- **Rectangles may touch:** The partition ranges are adjacent, such as ending at `i` and beginning at `i+1`. Their boxes can share a boundary line geometrically but never a grid cell.
- **Inclusive bounds:** Both loops in `f` include `i2` and `j2`, and the area formula includes `+1` in both dimensions.
- **Zeros between ones:** The tight box includes any intervening zeros; rectangles need only cover all ones, not consist solely of ones.
- **Initial upper bound:** `R * C` is finite and at least the optimum for a valid instance. Every accepted candidate can only lower it.
- **No input mutation:** The source repeatedly reads `grid` but never changes it.
- **Manifest mismatch:** Do not attribute prefix sums, caching, the manifest time, or its space bound to this implementation; none is visible in `solution.py`.
