## General

A stamp placement is legal only when its entire `stampHeight` by `stampWidth` rectangle lies inside the grid and contains no occupied cell. Every empty cell must belong to at least one legal placement. Since stamps may overlap and there is no limit on their number, placing one legal stamp can never make another legal stamp harmful. This removes any need to choose an optimal subset: conceptually, place every legal stamp, then ask whether their union covers every zero.

The challenge is doing both rectangle tests and union coverage without scanning every stamp-sized area cell by cell.

**Build a prefix sum of occupied cells**

The matrix `s` has dimensions $(m+1)$ by $(n+1)$. Its extra top row and left column remain zero. The code uses one-based coordinates for grid cells and fills

$$
s[i][j]=s[i-1][j]+s[i][j-1]-s[i-1][j-1]+\texttt{grid}[i-1][j-1].
$$

Thus `s[i][j]` equals the number of occupied cells in the rectangle from the original top-left corner through one-based cell $(i,j)$.

For a proposed stamp whose top-left corner is $(i,j)$ and bottom-right corner is $(x,y)$, inclusion-exclusion gives its number of occupied cells:

$$
s[x][y]-s[x][j-1]-s[i-1][y]+s[i-1][j-1].
$$

The full prefix rectangle contributes first. The area above the stamp and the area left of it are subtracted, and their overlap was subtracted twice, so it is added back. A result of zero means every cell under that placement is empty. The query costs $O(1)$ regardless of the stamp’s area.

**Enumerate exactly the placements that stay inside**

The top row `i` ranges from `1` through `m - stampHeight + 1`, expressed by `range(1, m - stampHeight + 2)`. Likewise, `j` ranges through `n - stampWidth + 1`. For each top-left corner, the code computes

`x = i + stampHeight - 1` and `y = j + stampWidth - 1`.

These formulas include exactly `stampHeight` rows and `stampWidth` columns. If a stamp dimension is larger than the grid’s corresponding dimension, the relevant range is empty, so no illegal out-of-bounds placement is considered.

**Record a whole valid rectangle with four updates**

When the occupied-cell sum is zero, every cell in the proposed rectangle is legally coverable. Marking all of those cells immediately would cost the stamp area per placement and could become far too slow. Instead, the solution uses a two-dimensional difference matrix `d`.

For an inclusive rectangle from $(i,j)$ through $(x,y)$, it performs:

- `d[i][j] += 1` to start a contribution;
- `d[i][y + 1] -= 1` to stop it after the right edge;
- `d[x + 1][j] -= 1` to stop it after the bottom edge;
- `d[x + 1][y + 1] += 1` to repair the corner that both negative updates affect.

The extra padding in the $(m+2)$ by $(n+2)$ matrix makes `x + 1` and `y + 1` safe even when a stamp touches the bottom or right border.

These four values are not coverage counts yet. They are boundaries whose two-dimensional prefix sum will later add one to exactly the cells inside the rectangle.

**Recover combined coverage and verify zeros**

In the final nested loop, the code converts `d` in place into actual coverage counts:

$$
d[i][j] \mathrel{+}= d[i-1][j]+d[i][j-1]-d[i-1][j-1].
$$

After this update, `d[i][j]` is the number of legal stamp placements covering that cell. Overlap is naturally allowed, so a count greater than one is harmless.

If the original value `v` is zero and `d[i][j] == 0`, that empty cell belongs to no legal stamp. No possible selection can cover it, so the method immediately returns false. Occupied cells are not required to be covered; in fact, the earlier rectangle query guarantees that no recorded stamp covers them. If the scan finds no uncovered zero, every empty cell is covered by at least one recorded legal stamp, and returning true is justified.

**Why placing every legal stamp proves correctness**

Every rectangle recorded in `d` stays inside the grid and has occupied-cell sum zero, so it obeys all restrictions. If their union covers all empty cells, using all those placements is a valid construction. Conversely, if an empty cell is outside the union of all legal placements, it cannot be covered by any valid solution because every stamp that could be chosen is already represented in that union. Therefore the final coverage test is both sufficient and necessary.

## Complexity detail

Let $m$ and $n$ be the grid dimensions. Building `s` visits all $mn$ cells once. There are at most $(m-\textit{stampHeight}+1)(n-\textit{stampWidth}+1)$ in-bounds placements, which is at most $mn$, and each uses one constant-time prefix query plus at most four difference updates. Reconstructing `d` and checking coverage visits all $mn$ cells once. Total time is $O(mn)$.

The occupied-cell prefix matrix uses $(m+1)(n+1)$ entries, and the difference matrix uses $(m+2)(n+2)$ entries. Together they require $O(mn)$ auxiliary space. The input grid is read but never modified.

This is linear in the number of grid cells, which is essential because the legal bound allows $mn$ up to $2\cdot10^5$, while a per-placement scan of a large stamp could multiply two large areas.

## Alternatives and edge cases

- **Scan every stamp rectangle directly:** This is easy to describe but may cost $O(mn \cdot \textit{stampHeight}\cdot\textit{stampWidth})$. The occupied-cell prefix sum reduces each legality test to $O(1)$.
- **Paint every valid rectangle directly:** Even with constant-time legality checks, writing every covered cell for every stamp can be superlinear. The difference grid records each rectangle in four operations.
- **Greedy placement around uncovered cells:** Choosing a stamp locally is unnecessary and can be difficult near obstacles. Because overlap is allowed and stamps do not consume resources, the union of all legal placements is the complete feasibility test.
- **Stamp larger than the grid:** No placement loop iteration occurs. The result is true only when there are no empty cells requiring coverage; otherwise the final scan finds an uncovered zero.
- **Grid with no empty cells:** No stamp is required. The final condition checks only cells where `v == 0`, so it correctly returns true.
- **All-empty grid:** Every in-bounds stamp position is legal. The result depends solely on whether those rectangles cover every border and interior cell.
- **One-by-one stamp:** Every empty cell has its own legal placement, so all zeros become covered and occupied cells are skipped.
- **One-row or one-column grid:** The same rectangle formulas work because the padded prefix matrices eliminate special boundary branches.
- **Overlapping stamps:** Difference counts may exceed one, but the test needs only positive versus zero coverage. Overlap never invalidates a placement.
- **Occupied cells:** They may have zero coverage and are deliberately ignored in the final rejection condition.
- **Bottom and right borders:** The $(m+2)$ by $(n+2)$ padding safely receives the difference updates just outside a border-touching stamp.
- **Off-by-one coordinates:** `grid` is zero-based, while `s` and `d` are used with one-based cell coordinates. The enumerations with `enumerate(..., 1)` maintain this mapping consistently.
- **Early false return:** Once an uncovered empty cell is found after all valid placements have been accumulated, later cells cannot change its coverage, so stopping is conclusive.
