## General

**Accumulate vertical one-runs into a reusable histogram**

The list `heights` has one entry per matrix column. After processing row `i`, `heights[j]` equals the number of consecutive `"1"` cells ending at that row in column `j`.

The update `heights[j] + 1 if matrix[i][j] == '1' else 0` has both required cases. A one extends the vertical run from the previous row; a zero breaks it completely and resets the possible height to zero. The same list is reused for every row, so no full matrix of dynamic states is needed.

Each updated height list is treated as a histogram. The helper finds the largest consecutive-column rectangle supported by those heights, and `result` keeps the best across all bottom rows.

**Why a histogram rectangle is a matrix rectangle**

Suppose consecutive columns `a` through `b` have histogram heights at least `h`. In every one of those columns, the `h` cells ending at the current row are all ones. Together they form an all-one rectangle of height `h` and width `b - a + 1`.

Conversely, any all-one matrix rectangle has a bottom row. At that moment, each spanned column's height is at least the rectangle height. The helper can represent its area in that row's histogram. Since every row becomes a bottom once, no valid matrix rectangle is missed.

This reduction is the crucial idea; the remaining helper is the one-dimensional largest-rectangle algorithm.

**Keep unresolved histogram bars on a monotonic stack**

`largestRectangleArea` uses a stack of indices with sentinel `-1` at the bottom. Real stacked bars have increasing heights after processing each position. They remain unresolved because no shorter-or-equal bar has yet fixed their right boundary.

When a new height is less than or equal to the stack top's height, the top is popped. The new stack top after popping is the nearest lower boundary on the left under the helper's tie convention, while the current index is the first blocking position on the right.

The popped rectangle covers indices `stk[-1] + 1` through `i - 1`. The source writes its width as `(i - 1) - stk[-1]`, then multiplies by the popped height. `result` inside the helper records the maximum finalized area.

**Why a single position may trigger many pops**

A low height can terminate several taller candidate rectangles. Each popped bar has a different newly exposed left boundary, so each width is evaluated separately. The nested loop is still linear in aggregate because an index, once popped, never returns to the stack.

Equal heights are also popped because of `>=`. The newer equal index replaces the older one and can inherit a farther-left lower boundary. At least one equal-height representative therefore captures the widest plateau.

**Flush unresolved bars with a virtual end index**

The helper loops over `range(len(heights) + 1)`. At `i == len(heights)`, there is no real bar, but the condition treats the position as lower than every remaining height and pops the stack to its sentinel.

Logical `or` short-circuits, so `heights[i]` is not read at the out-of-range virtual index. Bars popped there have no smaller real bar to their right, and the formula correctly lets them extend through the last column.

The virtual index is appended after the flush but never used again. The initialization `i = 0` in `stk, result, i = ...` is redundant because the loop immediately assigns `i`; it does not affect behavior.

**Trace the area-six rectangle**

For a row histogram with a suffix such as heights `3, 2, 2`, the equal-height logic eventually lets a height-two representative cover all three positions. Its width is three and area is six. In the matrix, those values certify two consecutive one-cells above each of three columns, exactly the two-by-three rectangle from the example.

If a following row contains zero in the middle column, that height resets to zero and flushes rectangles crossing the column for the new bottom row. Previously discovered area six remains safely stored in outer `result`.

**A correctness invariant across rows and stack calls**

Before calling the helper for a row, `heights` exactly describes vertical one-runs ending there. Within the helper, stacked bars have no known right blocker, and every pop computes the maximal supported interval for that bar or an equal-height representative. The virtual end ensures every remaining bar is eventually considered.

Therefore the helper returns exactly the largest all-one rectangle ending at that row. Taking the maximum with all prior row results makes the outer `result` exactly the largest rectangle among all processed bottom rows. After the final row, every possible bottom edge has been included.

**Empty outer input handling**

Although the contract says the matrix is nonempty, `if not matrix: return 0` safely handles zero rows before reading `matrix[0]`. It does not separately guard an empty first row, which is acceptable because the column count is guaranteed positive.

## Complexity detail

Let the matrix have $m$ rows and $n$ columns. Updating `heights` is $O(n)$ per row. In each helper call, every index is pushed and popped at most once, so histogram work is also $O(n)$. Total time is $O(mn)$, matching the manifest. The source comment's `O(n^2)` is a square-matrix shorthand and is less precise for rectangular input.

The height array and per-call stack each use $O(n)$ space. Other state is scalar, so peak auxiliary space is $O(n)$, matching the manifest. The matrix is never modified.

## Alternatives and edge cases

- **Two boundary passes:** Compute nearest strictly lower positions on both sides for every histogram bar, then evaluate areas. It is equally linear per row but allocates more arrays.
- **Row-DP boundaries:** Maintain height, left, and right limits across rows without calling a separate histogram helper. It has the same asymptotic bounds but more update invariants.
- **Brute force over rectangles:** Enumerating corners and verifying cells is far too expensive for 200 by 200 input.
- **Empty outer matrix:** The defensive guard returns zero.
- **All zeroes:** Heights reset to zero on every row and result remains zero.
- **All ones:** Heights grow each row, and the full-width area eventually reaches `m * n`.
- **One cell:** Histogram result is zero or one according to the string value.
- **One column:** The maximum is the longest consecutive vertical run of ones.
- **Equal heights:** `>=` pops older equals, allowing a later representative to span the plateau.
- **Virtual end:** It finalizes increasing suffixes that encounter no real lower bar.
- **String-versus-integer values:** The update must compare with `'1'`; integer `1` would not match the input representation.
- **Rectangular matrices:** Complexity and storage use separate row and column quantities, despite the source's square shorthand comment.
- **Input preservation:** Only `heights`, stacks, and scalar results are changed.
