## General

The tightest axis-aligned rectangle is completely determined by four indices:

- `u`: the first row containing at least one black pixel;
- `d`: the last row containing at least one black pixel;
- `l`: the first column containing at least one black pixel;
- `r`: the last column containing at least one black pixel.

Once those inclusive boundaries are known, the height is `d - u + 1`, the width is `r - l + 1`, and their product is the required area.

A full matrix scan could find all four bounds in $O(mn)$ time, but the problem requires less than that. The source instead tests entire rows or columns only at binary-search pivots.

**Projecting the image conceptually**

Call a row black when it contains at least one `1`; otherwise call it white. If each row is represented by that one Boolean, the image has a one-dimensional row projection. Define a column projection in the same way.

The source never allocates these projection arrays. To test whether row `mid` is black, it starts `c = 0` and advances while `image[mid][c] == '0'`. If it stops with `c < n`, it found a black pixel. If it reaches `c == n`, the whole row is white.

Likewise, to test column `mid`, it scans row index `r` until it either finds `image[r][mid] == '1'` or reaches `m`.

This on-demand projection is what avoids inspecting all $mn$ pixels up front.

**Why the black projections are contiguous**

All black pixels belong to one horizontally and vertically connected component. Suppose two black rows had a completely white row between them. Any path from a black pixel above that white row to a black pixel below it would have to change its row coordinate one step at a time, so it would have to pass through the intermediate row. Because that row contains no black pixel, no all-black path could cross it. This contradicts connectivity.

Therefore, every row between the first and last black rows is also black. The row projection has the form

`white ... white, black ... black, white ... white`.

The same argument applies to columns: an entirely white column between two black columns would separate the component horizontally. Thus, black columns also form one contiguous interval.

**Why the known black pixel matters**

The complete projection is not monotone; it may change from white to black and later from black to white. A single ordinary binary search cannot locate both transitions without an anchor.

The input guarantees `image[x][y] == '1'`. Hence row `x` lies inside the black row interval and column `y` lies inside the black column interval. Splitting at these known black coordinates produces four monotone searches:

- rows from 0 through `x`: white followed by black, so find the first black row;
- rows from `x` through `m - 1`: black followed by white, so find the last black row;
- columns from 0 through `y`: white followed by black, so find the first black column;
- columns from `y` through `n - 1`: black followed by white, so find the last black column.

The known black row and column also guarantee that each search interval contains at least one black position, so a valid boundary always exists.

**Finding the upper boundary**

The first search starts with `left = 0` and `right = x`. Its invariant is that the first black row lies somewhere in the inclusive interval `[left, right]`.

It chooses the lower midpoint `mid = (left + right) >> 1`, which is integer floor division by two.

- If row `mid` contains black, `mid` may be the first black row, so the source keeps it by setting `right = mid`.
- If row `mid` is white, every row at or before `mid` in this monotone half is white, so the first black row must be later. It sets `left = mid + 1`.

Each update preserves the possible boundary and shrinks the interval. When `left == right`, that single index is the first black row, stored as `u`.

**Finding the lower boundary**

The second row search starts with `[x, m - 1]` and seeks the last black row. Here the pattern is black followed by white.

It uses the upper midpoint

`mid = (left + right + 1) >> 1`.

The added one matters when two candidates remain. It chooses the right candidate; otherwise, assigning `left = mid` after a black test could leave `left` unchanged and make the loop stall.

- If row `mid` is black, it may be the last black row, and a later black row may exist, so set `left = mid`.
- If it is white, the last black row must be earlier, so set `right = mid - 1`.

When the interval collapses, `left` is stored as `d`.

**Finding the left and right boundaries**

The next two loops repeat exactly the same lower-bound and upper-bound patterns on columns.

The left-boundary search uses `[0, y]`, a lower midpoint, and a full vertical scan of the pivot column. A black pivot keeps `right = mid`; a white pivot moves `left = mid + 1`. The converged value is `l`.

The right-boundary search uses `[y, n - 1]`, an upward-biased midpoint, and another vertical scan. A black pivot moves `left = mid`; a white pivot moves `right = mid - 1`. The converged value is `r`.

Although the variable name `r` is temporarily used as the row-scanning index inside each column test, the source assigns `r = left` after the final search. At the area calculation, `r` therefore holds the intended rightmost black column.

**Tracing the example**

For

`[["0","0","1","0"],["0","1","1","0"],["0","1","0","0"]]`,

the row projection is `[black, black, black]`, so `u = 0` and `d = 2`. The column projection is `[white, black, black, white]`, so `l = 1` and `r = 2`.

The rectangle has height

$$
2-0+1=3
$$

and width

$$
2-1+1=2.
$$

Its area is $3\cdot2=6$.

**Why the rectangle is both sufficient and minimal**

Every black pixel has a row between `u` and `d` by definition of the extreme black rows, and a column between `l` and `r` by definition of the extreme black columns. Therefore, the computed rectangle encloses every black pixel.

Any enclosing axis-aligned rectangle must include a pixel in row `u`, a pixel in row `d`, a pixel in column `l`, and a pixel in column `r`. It cannot move any side inward without excluding at least one of those extreme pixels. Thus, no smaller axis-aligned enclosing rectangle exists.

## Complexity detail

Let $m$ be the number of rows and $n$ the number of columns.

Each row binary search performs $O(\log m)$ iterations. Testing one pivot row may scan all $n$ columns, so the two row searches together cost $O(n\log m)$ time.

Each column binary search performs $O(\log n)$ iterations. Testing one pivot column may scan all $m$ rows, so the two column searches together cost $O(m\log n)$ time.

The total time complexity is therefore

$$
O(n\log m+m\log n).
$$

The source stores only dimensions, binary-search bounds, midpoints, scanning indices, and the four final boundaries. It allocates no projection array, visited matrix, queue, or recursion stack. Auxiliary space is $O(1)$.

The subquadratic benefit comes from inspecting only logarithmically many rows and columns. A particular pivot scan may still read an entire row or column, but the algorithm does not perform such a scan for every possible row and every possible column.

## Alternatives and edge cases

- **Scan the entire matrix:** Update four extrema whenever a `1` is found. This is simple and uses $O(1)$ space, but costs $O(mn)$ time and does not satisfy the requested subquadratic condition.
- **DFS or BFS from `(x, y)`:** Connectivity guarantees traversal reaches every black pixel, allowing boundary updates in $O(B)$ time for $B$ black pixels. In the worst case $B=mn$, and visited or recursion storage can also grow to $O(B)$.
- **Precompute row and column projections:** It makes boundary searches cheap but building the projections already costs $O(mn)$, losing the intended advantage.
- **One binary search over the whole projection:** The global pattern is white-black-white, not monotone. The known black coordinate must split it into a first-boundary half and a last-boundary half.
- **Downward-biased midpoint for the last boundary:** With two candidates, `mid` would equal `left`; a black test followed by `left = mid` would not shrink the interval. The `+1` upward bias prevents this infinite loop.
- **Treating boundaries as exclusive:** The exact source stores all four bounds inclusively, so both dimensions require `+1`. Omitting it makes a one-pixel span have size zero.
- **Single black pixel:** All four searches collapse to its row and column, and the area is $(0+1)(0+1)=1$.
- **Single row:** Both row searches may perform no iterations, giving `u = d = 0`. Column searches still find the horizontal span.
- **Single column:** Both column searches may perform no iterations, giving `l = r = 0`. Row searches find the vertical span.
- **Black component touches an image border:** A boundary may legitimately be 0, `m - 1`, or `n - 1`; the inclusive initial intervals retain those candidates.
- **White gaps inside a boundary row:** A row needs only one black pixel to be part of the projection. The horizontal scan correctly tests existence, not whether the row is entirely black.
- **Non-rectangular black component:** The black pixels may form any connected shape. Only their extreme rows and columns determine the enclosing rectangle.
- **Connectivity guarantee:** The monotone projection lemma depends on a single component. With disconnected black regions, an empty row or column could separate black projections and invalidate these binary searches.
- **Character representation:** Pixels are strings `'0'` and `'1'`, so the source compares against `'0'` rather than numeric zero.
- **Known pixel location:** The algorithm uses both `x` and `y` as guaranteed anchors. If either did not point to black, the corresponding search intervals would not necessarily contain the desired transition.
