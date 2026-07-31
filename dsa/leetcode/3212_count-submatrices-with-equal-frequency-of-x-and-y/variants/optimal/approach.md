## General

**Reduce the submatrix family to bottom-right corners**

Any rectangular submatrix containing `grid[0][0]` must start at row zero and column zero. It is therefore uniquely determined by its bottom-right cell $(i,j)$ and contains rows $0$ through $i$ and columns $0$ through $j$.

Represent each `"X"` as balance $+1$, each `"Y"` as $-1$, and each dot as zero. A rectangle has equal `"X"` and `"Y"` frequencies exactly when its total balance is zero. Track its `"X"` count separately to exclude the all-dot case.

**Accumulate vertical columns and horizontal prefixes**

Maintain for every column its balance and `"X"` count across all rows processed so far. When visiting a new row, update those column totals cell by cell.

Within that row, take running sums of the updated column totals from column zero through the current column. At column $j$, these running values describe exactly the anchored rectangle ending at the current row and $j$. Count it when the balance is zero and the `"X"` total is positive.

Every eligible anchored rectangle has one bottom-right corner visited by the scan. The vertical arrays contain exactly its rows, and the horizontal prefix contains exactly its columns, so the test uses its true frequencies. Conversely, every counted prefix is a rectangle containing `grid[0][0]` and satisfies both required frequency conditions.

## Complexity detail

Each of the $rc$ cells is processed once with constant work. Time complexity is $O(rc)$ and the two column arrays use $O(c)$ auxiliary space.

The answer can be as large as $rc$, since only anchored rectangles are considered rather than arbitrary pairs of row and column boundaries.

## Alternatives and edge cases

- **Two full 2D prefix tables:** Separate `"X"` and `"Y"` prefix sums also give $O(rc)$ time, but use $O(rc)$ space instead of one-dimensional column state.
- **Rescan each anchored rectangle:** Trying every bottom-right corner and recounting all enclosed cells can take $O(r^2c^2)$ time.
- **Count arbitrary submatrices:** Choosing independent top and left boundaries includes rectangles that do not contain `grid[0][0]` and solves a different problem.
- **All dots:** Balance is zero everywhere, but the positive-`"X"` condition rejects every rectangle.
- **Only one letter:** A rectangle containing only `"X"` or only `"Y"` cannot have equal frequencies.
- **Top-left dot:** Larger anchored rectangles may still qualify once they include matching `"X"` and `"Y"` cells.
- **Single row or column:** The same prefix logic counts qualifying one-dimensional anchored rectangles.
- **Dots inside a valid rectangle:** Dots do not alter either letter count and therefore do not disturb equality.
