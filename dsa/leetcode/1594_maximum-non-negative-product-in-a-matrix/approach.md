## General

**Why one best product per cell is not enough**

Every path to a cell can continue only right or down, suggesting grid dynamic programming. The complication is multiplication by negative values.

A large positive product is best before multiplying by a positive number, but a very negative product can become the largest positive result after multiplying by a negative number. Tracking only the maximum would discard that useful negative extreme. The solution stores both the minimum and maximum path product at every cell.

For cell `(i, j)`:

- `f[i][j][0]` is the minimum product among all paths from the start to that cell;
- `f[i][j][1]` is the maximum product among those paths.

These are exact integer products. The modulus is deliberately not applied during the DP because modulo reduction destroys numerical ordering and sign information.

**Why the two extremes are sufficient**

To reach `(i, j)`, the previous cell must be `(i - 1, j)` or `(i, j - 1)`. Let the current grid value be `x`.

For one predecessor, all previous products lie between its stored minimum `a` and maximum `b`. Multiplication by the fixed `x` behaves in one of three ways:

- if `x > 0`, order is preserved, so the new extremes come from `a * x` and `b * x`;
- if `x < 0`, order reverses, but the new extremes still come from those same two endpoint products;
- if `x == 0`, both endpoint products are zero and every path product becomes zero.

Thus no interior previous product can produce a new value beyond both multiplied extremes. Checking each predecessor’s minimum and maximum is enough to recover the new global minimum and maximum.

**Initialization**

The DP table is an $M\times N$ matrix whose entries begin as `[0, 0]` pairs. At the top-left cell, the only path consists of that cell itself, so both extremes equal `grid[0][0]`.

The source handles this with:

`f[0][0][0] = x` and `f[0][0][1] = x`,

then uses `continue` so the start is not processed as though it had a predecessor.

**Collecting candidates from above and left**

For every other cell, `mn` begins at positive infinity and `mx` at negative infinity. These sentinels ensure the first real predecessor product replaces them.

If `i > 0`, the cell above exists. The assignment `a, b = f[i - 1][j]` retrieves its minimum and maximum. The source updates:

`mn = min(mn, a * x, b * x)`

`mx = max(mx, a * x, b * x)`.

If `j > 0`, it repeats the same operation with the left predecessor.

At least one predecessor exists for every cell other than the start, so no infinity is stored. Finally:

`f[i][j][0], f[i][j][1] = mn, mx`.

Unlike a sign-branch implementation, this uniform candidate method does not need separate positive, negative, and zero cases. Evaluating both extremes automatically handles every sign.

**A path-sign example**

Suppose two paths reach a predecessor with products negative eight and positive three, and the current cell contains negative two. Extending the former gives positive sixteen, while extending the latter gives negative six. The previous minimum becomes the new maximum. A DP that had retained only positive three would miss the optimal positive sixteen.

A zero cell collapses both extremes to zero. Later negative values cannot recover a nonzero product on that particular path, but paths arriving from another predecessor may still supply different candidates if that other route does not pass through the zero.

**Why the recurrence covers every path**

Every path to a non-start cell ends with exactly one move from above or left. By induction, each predecessor pair contains the true minimum and maximum over all paths to that predecessor. Multiplying by the current cell extends every such path.

For each predecessor, the extreme extended products occur at one of its stored endpoints because multiplication by a constant is monotone or order-reversing. Taking the minimum and maximum across both predecessors therefore gives the true extremes over every path to the current cell.

The base case is exact, so induction establishes every DP entry. In particular, `f[m - 1][n - 1][1]` is the maximum product over all complete paths.

**Final sign check and modulus**

The source names the destination maximum `ans`. If `ans < 0`, every path product is negative because `ans` is already the greatest one. No non-negative path exists, so the method returns `-1`.

If `ans == 0`, zero is a valid non-negative maximum and the method returns zero. If `ans > 0`, it returns `ans % (10**9 + 7)`.

Applying the modulus only after selecting the true maximum follows the problem statement. Two products can change relative order after modular reduction, so reducing intermediate states would invalidate the DP.

## Complexity detail

Let $M$ be the number of rows and $N$ the number of columns.

The nested loops visit all $MN$ cells once. Each cell inspects at most two predecessors and evaluates a constant number of products and comparisons. Time complexity is $O(MN)$.

The table `f` stores two integers for each cell, using $O(MN)$ auxiliary space. Loop variables and extrema use $O(1)$ additional state. The input grid is not modified.

Python integers safely preserve exact products. Under the stated dimensions and cell bounds the values are manageable, but exact arithmetic is conceptually necessary because the modulus must wait until the end.

## Alternatives and edge cases

- **Store only the maximum:** This fails when a negative current value turns the most negative predecessor product into the largest positive result.
- **Track only signs:** Sign reachability can tell whether a non-negative path exists but cannot determine the largest magnitude.
- **Enumerate all right/down paths:** The number of paths is combinatorial. DP merges paths sharing a cell into two sufficient extrema.
- **Recursive memoization:** It can compute the same min/max state, but the iterative table avoids recursion overhead and follows dependency order directly.
- **Rolling-row optimization:** Only the previous row and current left state are needed, so memory can be reduced to $O(N)$. The checked-in source retains the full $O(MN)$ table.
- **Single cell:** Both extrema equal that value. A negative value returns `-1`; zero or positive is returned modulo the constant.
- **Single row or column:** Each cell has only one predecessor, so there is exactly one path and both extrema remain equal.
- **Zero on a path:** That path’s product becomes and remains zero. Zero is valid and beats every negative product.
- **All path products negative:** The maximum endpoint product is still negative, triggering `-1`.
- **Negative start or destination:** No special case is needed; the min/max transitions handle sign changes across the full path.
- **Modulo timing:** Reducing inside the table would corrupt sign and ordering. The source reduces only the selected non-negative maximum.
- **Infinity sentinels:** They are temporary initialization values only. Every non-start cell has at least one valid predecessor that replaces them.
- **Input preservation:** All state is stored in `f`, so `grid` remains unchanged.
