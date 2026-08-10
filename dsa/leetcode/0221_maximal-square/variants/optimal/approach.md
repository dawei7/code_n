## General

**Choose a state that identifies each possible square unambiguously**

Many squares can overlap, so merely counting nearby `"1"` cells does not tell
whether they form a solid square. Dynamic programming becomes simple when each
candidate square is identified by its bottom-right corner.

The exact solution defines `dp[i + 1][j + 1]` as the side length of the largest
all-`"1"` square whose bottom-right cell is `matrix[i][j]`. A side length is
stored rather than an area because extending a square changes its side by one,
and the neighboring states naturally describe side lengths. The area is
computed only once at the end.

The `+1` offsets leave row 0 and column 0 of `dp` filled with zeros. Those
sentinel borders represent the absence of cells above the first matrix row or
left of the first matrix column. They let every real cell use the same
three-neighbor formula without special branches for edges and corners.

**A zero cell cannot end a positive square**

If `matrix[i][j] == '0'`, any square ending at that cell contains a zero and
therefore cannot consist entirely of ones. Its maximum side length is zero.
The source does not assign the DP entry in that case, because the entire table
was initialized to zero.

The matrix entries are strings, so the comparison must be against `'1'`, not
integer `1`.

**A one cell looks at top, left, and top-left**

For a current `"1"` cell, consider these already computed values:

- `dp[i][j + 1]` is the largest square ending directly above the current cell;
- `dp[i + 1][j]` is the largest square ending directly to its left;
- `dp[i][j]` is the largest square ending diagonally above-left.

If the smallest of those side lengths is $q$, the current cell can extend an
all-one region to side $q+1$. The diagonal state supplies the inner
$q \times q$ block, while the top and left states guarantee that the new
bottom-excluded column and right-excluded row have enough consecutive ones to
complete the larger square. The current cell fills its final corner.

That yields the exact transition

$$
\texttt{dp[i+1][j+1]}
= 1 + \min(\texttt{dp[i][j+1]},\texttt{dp[i+1][j]},\texttt{dp[i][j]}).
$$

The minimum is necessary because a square must be complete in both dimensions.
A large square above cannot compensate for a short run on the left, and a
large left square cannot compensate for missing cells above. The weakest of
the three neighboring regions limits how far the current square can extend.

**Why the recurrence is neither too small nor too large**

Let the three neighboring state values have minimum $q$. Each is at least
$q$, so their certified all-one regions overlap to cover every cell of a
$(q+1) \times (q+1)$ square ending at the current one cell. Therefore the
transition can safely produce at least $q+1$.

Conversely, suppose a square of side $r$ ends at the current cell. If
$r > 1$, removing its bottom row leaves a square of side $r-1$ ending above,
removing its right column leaves one ending to the left, and removing both
leaves one ending above-left. All three neighboring DP values must be at least
$r-1$. Hence $r$ cannot exceed one plus their minimum. Combining both
directions shows that the recurrence gives the exact maximum side length for
this bottom-right corner.

**Row-major order makes every dependency available**

The outer loop processes rows from top to bottom, and the inner loop processes
columns from left to right. When cell `(i, j)` is reached, the entire previous
row and the current row's left portion have already been computed. Therefore
the top, left, and top-left states used by the transition are final.

The variable `mx` stores the greatest side length encountered anywhere. A
square can end at any matrix position, so updating `mx` after every positive DP
entry considers all possible bottom-right corners. The answer asks for area,
not side length, so the final return is `mx * mx`.

**Trace a local obstruction**

Imagine the top, left, and diagonal states around a current one cell are 3, 1,
and 3. Although two neighboring directions support side 3, the left state of
1 reveals that a needed boundary contains a zero too close to the current
corner. The recurrence gives `1 + min(3, 1, 3) = 2`; a side-2 square is valid,
but side 3 or 4 is not.

In the first reference example, scanning eventually creates DP entries of 2
where four ones form a `2 x 2` block. No entry reaches 3, so `mx` is 2 and the
returned area is 4. In an all-zero matrix every DP entry remains zero, `mx`
never changes, and the returned area is 0.

**The exact implementation uses a full table**

The manifest says the branch stores one DP line over the shorter dimension and
claims $O(\min(m,n))$ space. The exact source allocates
`(m + 1) x (n + 1)` entries and never compresses rows or transposes dimensions.
Its actual auxiliary space is $O(mn)$. A one-row recurrence is a valid
optimization discussed below, but it is not the executable code documented
here.

The source safely evaluates `len(matrix[0])` because the reference guarantees
at least one row and at least one column. It also assumes `List` is available
for the type annotation.

## Complexity detail

Let $m$ be the number of rows and $n$ the number of columns. The two nested
loops visit each of the $mn$ cells exactly once, and every visit performs a
constant number of comparisons and assignments. Initializing the DP table also
takes $O(mn)$ work, so total time is $O(mn)$.

The table contains $(m+1)(n+1)$ integers, which is $O(mn)$ auxiliary space.
The remaining variables use $O(1)$ space. This is the exact source bound, not
the compressed $O(\min(m,n))$ bound currently stated by the manifest. The
input matrix is not modified.

## Alternatives and edge cases

- **One-row dynamic programming:** Keep one padded row, save the old diagonal value before overwriting, and apply the same recurrence. Choosing the shorter matrix dimension for storage achieves $O(\min(m,n))$ auxiliary space and matches the manifest, but requires more careful update ordering.
- **Two DP rows:** Retain the previous and current rows. It reduces space to $O(n)$ while remaining easier to reason about than one-row in-place updates.
- **Expand every square from each one cell:** Check newly added bottom rows and right columns as a candidate grows. It uses little extra space but can revisit many cells and become prohibitively expensive.
- **Prefix-sum rectangle queries:** A 2D prefix sum can test whether a chosen square contains all ones in constant time, but searching many side lengths and positions adds complexity and still uses $O(mn)$ storage.
- **One cell containing `"1"`:** The sentinel neighbors are all zero, so the recurrence stores side 1 and returns area 1.
- **One cell containing `"0"`:** The DP entry stays zero and the method returns 0.
- **A single row or column:** No square larger than side 1 can exist. Sentinel padding and the minimum recurrence enforce that automatically.
- **All ones:** The DP values grow by one along diagonals until reaching side $\min(m,n)$, and the returned area is $\min(m,n)^2$.
- **Zeros inside a large region:** Every zero resets its endpoint state to zero, and the minimum propagates that obstruction only as far as it genuinely limits later squares.
- **Area versus side length:** `mx` is a length. Returning `mx` directly would be wrong whenever the largest square is larger than `1 x 1`; squaring it produces the requested number of cells.
- **Input preservation:** The separate DP table records derived lengths, leaving all string entries in `matrix` unchanged.
