## General

**Why an ordinary binary search is not immediately available**

Every row and every column is sorted in non-decreasing order, but the entire matrix is not stored as one sorted array. Moving to the next physical cell in row-major order does not necessarily move to the next larger value. Flattening all $n^2$ entries and sorting them would make the rank easy to find, but it would cost $O(n^2)$ extra storage and would ignore most of the structure promised by the problem.

The exact solution instead binary-searches the range of possible values. The smallest matrix value is `matrix[0][0]`, because it is first in both its row and column. For the same reason, the largest value is `matrix[n - 1][n - 1]`. The required answer must lie between those two values, even when it appears more than once.

For any candidate value `mid`, ask the yes-or-no question:

> Are there at least `k` matrix entries whose values are less than or equal to `mid`?

If the answer is yes, the $k^{\text{th}}$ smallest value cannot be greater than `mid`; there are already enough entries at or below it. If the answer is no, the desired value must be strictly greater than `mid`. This monotone question supplies exactly the direction needed for binary search.

**The rank predicate**

Let

$$
C(v) = \#\{(r,c) : \texttt{matrix}[r][c] \le v\}.
$$

As $v$ increases, $C(v)$ can only stay the same or increase. Therefore the predicate $C(v) \ge k$ is false for values that are too small and true from the answer onward. The algorithm is looking for the smallest integer $v$ for which this predicate is true.

This definition also explains why duplicates are handled correctly. The question asks for sorted position, not the $k^{\text{th}}$ distinct value. If a number occurs several times, every occurrence contributes separately to $C(v)$. The count can jump by more than one at that value, and the first value where the count reaches `k` is still precisely the value occupying rank `k` in the sorted multiset.

**Counting entries at or below `mid` in linear time**

A direct scan would count correctly but would inspect all $n^2$ cells during every binary-search iteration. The helper `check` uses both sorting directions to count in $O(n)$ time.

It begins at the bottom-left cell with `i = n - 1` and `j = 0`. At any moment, `(i, j)` is the bottommost unresolved cell in column `j`.

- If `matrix[i][j] <= mid`, then every entry above it in the same column is also at most `mid`, because columns are non-decreasing from top to bottom. The cells in rows `0` through `i` contribute `i + 1` entries at once. After adding that amount to `count`, the algorithm moves right with `j += 1`; that column is completely resolved.
- If `matrix[i][j] > mid`, then this cell cannot be counted. Moreover, every cell to its right in the same row is at least as large, because rows are non-decreasing. Those right-side cells will never qualify either. Moving up with `i -= 1` discards this row’s unresolved suffix and searches for a smaller value.

Each step moves either one column right or one row up. Neither pointer ever reverses direction. There can be at most $n$ right moves and $n$ upward moves, so the traversal is linear rather than quadratic.

It helps to visualize the qualifying cells as a staircase-shaped region in the upper-left of the matrix. In each column, some prefix may be at most `mid`. The bottom-left walk traces the boundary of that region and adds an entire qualifying column prefix whenever it finds the boundary’s lower edge.

The helper finally returns `count >= k`, not the count itself, because binary search needs only the predicate. It is safe that the implementation does not stop as soon as `count` reaches `k`; completing the remaining walk changes no result and preserves the same $O(n)$ bound.

**Maintaining the binary-search interval**

The initial inclusive value interval is

```text
left  = matrix[0][0]
right = matrix[n - 1][n - 1]
```

The central invariant is that the actual $k^{\text{th}}$ smallest value always belongs to `[left, right]`.

While `left < right`, the solution computes `mid = (left + right) >> 1`, which is integer floor division by two for this sum in Python. If `check(...)` is true, at least `k` entries are no greater than `mid`. The answer is therefore at most `mid`, so the solution keeps `mid` and everything below it by assigning `right = mid`.

If `check(...)` is false, fewer than `k` entries are at most `mid`. Consequently, `mid` itself and every smaller value are impossible answers. The solution discards them with `left = mid + 1`.

These two updates deliberately differ. A true `mid` may be the first value satisfying the predicate, so it must remain in the interval. A false `mid` can never be the answer, so it is excluded. Since the interval consists of integers, either update makes it strictly smaller. Eventually `left == right`, leaving one possible value, which the method returns.

**Why the returned boundary must be a matrix element**

Binary search considers numerical candidates that might not occur in the matrix. That does not make the result approximate. The count $C(v)$ changes only when $v$ reaches an actual matrix value. Between two consecutive values present in the matrix, the predicate is constant. Therefore the first integer for which $C(v) \ge k$ must be a value at which the count jumps, and such a jump can happen only at a matrix entry.

For example, suppose the sorted multiset begins `1, 5, 9, 10, ...`. Candidates `6`, `7`, and `8` all have the same count as `5`. Binary search may inspect any of them, but none can be the first true boundary for a rank whose answer is `9`. The search eventually converges on `9` itself.

**Why the counting walk is exact**

When the walk accepts `matrix[i][j]`, it counts exactly rows `0` through `i` of column `j`. Sorted columns prove all of them qualify. Rows below `i` in that column have already been eliminated during earlier upward moves, so no cell is counted twice. When the walk rejects a cell and moves upward, sorted rows prove that the rejected cell and every still-unresolved cell to its right in that row are too large. Thus, no qualifying cell is discarded.

At termination, either every column has been resolved (`j == n`) or every row has been eliminated (`i < 0`). In both cases, every matrix cell has been either counted once or correctly excluded. The returned predicate is consequently exact. Combined with the lower-bound binary search, this proves that the final `left` is the value at one-based rank `k`.

## Complexity detail

Let $n$ be the number of rows and columns, and define the initial numerical range width as

$$
R = \texttt{matrix}[n-1][n-1] - \texttt{matrix}[0][0] + 1.
$$

Each call to `check` performs at most $2n$ pointer moves, so it takes $O(n)$ time. Binary search halves an integer value interval of width $R$ on every iteration, requiring $O(\log R)$ iterations. The total running time is therefore $O(n \log R)$.

This complexity depends on the spread of the values rather than on the number of cells. Under the stated bounds, values may range from $-10^9$ to $10^9$, so the number of binary-search iterations is still small. The logarithm is not $\log(n^2)$ because the method is not binary-searching cell indices.

The method uses only `left`, `right`, `mid`, the counter, and two matrix indices. The helper does not allocate a row-sized or matrix-sized structure, so the auxiliary space is $O(1)$. The input matrix itself is read-only and is not counted as extra space.

## Alternatives and edge cases

- **Min-heap merge of sorted rows:** Treat each row as a sorted list, place the first entry of up to `min(n, k)` rows in a min-heap, and pop/replace the smallest entry `k` times. This is intuitive and runs in $O(h + k\log h)$ time with $O(h)$ space for $h=\min(n,k)$. It does not meet the constant-extra-space follow-up, and it can be slower when `k` is large.

- **Flatten and sort:** Copying all $n^2$ entries into an array and sorting gives the answer directly in $O(n^2\log n)$ time and $O(n^2)$ extra space. It violates the requested memory improvement and wastes the row/column ordering.

- **Binary-search every row separately:** For each candidate `mid`, a standard upper-bound search in every row can compute the count in $O(n\log n)$ time. Combined with value binary search, that becomes $O(n\log n\log R)$. The bottom-left staircase walk removes the extra $\log n$ factor.

- **Duplicates:** Equal values must be counted as separate cells. Using `<= mid`, rather than `< mid`, makes the predicate correspond to the number of entries occupying ranks through that value. The lower-bound search then returns the repeated value whenever rank `k` falls inside its block.

- **One-cell matrix:** When `n = 1`, `left` and `right` are equal immediately. The loop is skipped and the sole entry is returned, including when it is negative.

- **Extreme ranks:** For `k = 1`, the answer is the top-left value. For `k = n^2`, it is the bottom-right value. The same predicate and interval updates handle both cases without special branches.

- **Negative and widely separated values:** The search operates on integer comparisons, so negative endpoints cause no conceptual problem. Computing the midpoint from the endpoints also works when zero lies inside the interval. Python integers avoid overflow; in a fixed-width language, use an overflow-safe midpoint expression or a wider integer type.

- **Non-decreasing rather than strictly increasing:** Rows and columns may contain equal adjacent values. The staircase proof requires only `<=` ordering, not uniqueness, so plateaus are valid.

- **Rectangular generalization:** The package contract is an $n \times n$ matrix. The staircase idea also works for a rectangular matrix if row and column limits are tracked separately, but the exact code intentionally uses `n` for both dimensions because the input is guaranteed square.

- **Advanced $O(n)$ selection:** Specialized algorithms can exploit sorted matrices to attain linear time, as mentioned by the follow-up, but they are substantially more complex. The value-space binary search is the practical optimal branch represented by the supplied solution and achieves constant auxiliary memory with a short, auditable invariant.
