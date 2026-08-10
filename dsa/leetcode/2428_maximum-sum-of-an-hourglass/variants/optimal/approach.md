## General

**Describe the seven-cell shape precisely**

An hourglass occupies a three-by-three bounding box. It includes all three cells in the top row, only the center cell in the middle row, and all three cells in the bottom row. The middle-left and middle-right cells do not belong to the shape.

The exact solution identifies an hourglass by its center `grid[i][j]`. A legal center cannot lie on the outer border because the shape needs one row above and below and one column to the left and right. Therefore `i` ranges from 1 through `m - 2` and `j` ranges from 1 through `n - 2`. Python expresses these intervals as `range(1, m - 1)` and `range(1, n - 1)`.

Every legal hourglass has exactly one center, and every center in those loops defines exactly one fully contained hourglass. Enumerating centers therefore visits every possible placement once.

**Reuse the surrounding three-by-three square**

For one center, the generator inside `sum` visits all nine cells with row indices `i-1` through `i+1` and column indices `j-1` through `j+1`. That total includes the seven hourglass cells plus the two unwanted middle-side cells `grid[i][j - 1]` and `grid[i][j + 1]`.

The code initializes

`s = -grid[i][j - 1] - grid[i][j + 1]`

and then adds the complete three-by-three total. Algebraically, the two unwanted cells occur once positively and once negatively, so they cancel. The remaining value is exactly

$$
\begin{aligned}
&\texttt{grid}[i-1][j-1]
+\texttt{grid}[i-1][j]
+\texttt{grid}[i-1][j+1] \\
&+\texttt{grid}[i][j] \\
&+\texttt{grid}[i+1][j-1]
+\texttt{grid}[i+1][j]
+\texttt{grid}[i+1][j+1].
\end{aligned}
$$

This “full square minus two cells” formulation is equivalent to spelling out all seven additions. It also makes the fixed mask visible: everything in the bounding square is selected except the two sides of the middle row.

**Keep the largest placement**

The accumulator `ans` starts at zero. This is safe because every matrix entry is non-negative, so every hourglass sum is also non-negative. After computing `s` for a center, `ans = max(ans, s)` retains the greatest sum among all placements examined so far.

After the first center, the invariant is that `ans` equals that first hourglass sum or zero; because the sum is non-negative, it equals the sum. Each later update compares the prior maximum with the newly encountered placement. By induction, after any loop prefix `ans` is the maximum over exactly those hourglasses already visited. When both loops finish, all legal centers have been visited, so `ans` is the global maximum.

For a three-by-three matrix, each range contains only the center index 1. The generator sums all nine cells and subtracts the two middle-side cells, producing the only hourglass. For `[[1,2,3],[4,5,6],[7,8,9]]`, the full square totals 45; subtracting 4 and 6 gives 35.

**Why no rotation or boundary case is missed**

The problem fixes the orientation, and the seven selected offsets match that orientation. The loops do not generate rotated variants. Because both dimensions are at least three, there is always at least one legal center. The smallest and largest center indices put the shape flush against a border but never outside the matrix.

The implementation uses the first row to obtain `n = len(grid[0])`. The contract guarantees a rectangular $m \times n$ matrix, so every later row supports the same column indices.

Although the manifest describes sliding a mask by its top-left position, the code uses the center. These are equivalent coordinates: a center at $(i,j)$ corresponds to a bounding-box top-left position $(i-1,j-1)$. The exact arithmetic is center-based.

## Complexity detail

There are $(m-2)(n-2)$ legal centers. For each one, the nested generator visits exactly nine cells, and the surrounding arithmetic is constant time. Nine is a fixed shape size, so total time is

$$
O(9(m-2)(n-2)) = O(mn).
$$

The algorithm stores dimensions, loop indices, the current sum, and the best sum. The generator is consumed immediately by `sum` and ranges over a constant nine cells, so auxiliary space is $O(1)$. The input is not modified, and the output is one integer.

If negative entries were permitted, the same enumeration would still be linear, but initializing `ans` to zero could be wrong when every hourglass sum is negative. The given lower bound of zero is what validates that initialization.

## Alternatives and edge cases

- **Write all seven additions explicitly:** This avoids summing the two excluded cells only to subtract them and may have a smaller constant factor. The asymptotic bounds are identical, while the exact source emphasizes the three-by-three mask.
- **Use two-dimensional prefix sums:** A prefix-sum matrix can obtain the top and bottom row segments quickly, but each segment already has fixed length three. Preprocessing adds $O(mn)$ space without improving the $O(mn)$ total time.
- **Sliding row sums:** Maintain length-three sums for the top and bottom rows as the center moves horizontally. It can reduce repeated additions but adds bookkeeping for a shape containing only seven cells.
- **Exactly three rows or columns:** There is only one legal center along that dimension. The ranges correctly include it once.
- **All zeros:** Every hourglass sum is zero, and the initialized answer remains the correct maximum.
- **Maximum values:** One sum contains only seven entries, so its mathematical maximum is $7 \cdot 10^6$. Python has no overflow concern.
- **Border centers:** A cell on row 0, row $m-1$, column 0, or column $n-1$ cannot be a center. The loop bounds exclude all of them.
- **Unrotated shape:** The two removed cells are specifically the horizontal neighbors of the center. Removing vertical neighbors would describe a rotated and invalid shape.
- **Rectangular rather than square grids:** Row and column loop bounds are independent, so $m$ and $n$ need not match.
