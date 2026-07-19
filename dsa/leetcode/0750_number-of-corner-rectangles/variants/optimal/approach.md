## General
**Let a pair of columns identify two corners**

Within one row, every pair of columns containing `1` can be the lower corners of a rectangle. It completes one rectangle with each earlier row that contained `1` in the same column pair. Maintain how many previous rows have supplied every pair: add that count to the answer, then increment it for the current row.

**Orient the grid around its smaller dimension**

Pair generation is quadratic in the number of columns. If the original grid has more columns than rows, transpose it first. The working column count is then $\min(m,n)$, while transposition does not change which four cells define a rectangle.

**Why each rectangle is counted exactly once**

Fix a rectangle and consider its later working row. Its two corner columns generate one pair in that row, and the earlier row has already contributed exactly once to the pair's counter, so the rectangle is added. No other row or column pair represents those same four corners. Conversely, every prior counter contribution and current pair share two distinct rows and columns with `1` at all four intersections, so every counted object is valid.

## Complexity detail
Let $m$ and $n$ be the original dimensions and $s=\min(m,n)$. After orientation there are $\max(m,n)$ rows, and a row generates at most $O(s^2)$ column pairs. The time is $O(mn\min(m,n))$. The pair-frequency table contains $O(s^2)$ entries, which is also the auxiliary-space bound.

## Alternatives and edge cases
- **Intersect each pair of rows:** Count their common `1` columns and add $k(k - 1) / 2$; after orienting the smaller dimension as rows, this has the same asymptotic time and can use $O(1)$ extra counting space.
- **Enumerate every row pair and column pair:** Testing all four corners directly is simple but costs $O(m^2 n^2)$ time.
- **Sparse pair-frequency map:** Store only column pairs that actually occur; this can save memory on sparse grids while retaining the same worst-case bounds.
- **Fewer than two usable rows or columns:** No rectangle can be formed, and the pair process naturally returns `0`.
- **All-one matrix:** The answer is $\binom{m}{2} \cdot \binom{n}{2}$; this is a useful dense boundary check.
- **Interior cells:** They never affect whether the four selected corners form a valid rectangle.
