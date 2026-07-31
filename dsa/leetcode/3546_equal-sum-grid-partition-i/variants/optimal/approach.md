## General

A legal equal partition must give each section exactly half of the sum of the whole grid. Compute that total once, then examine the only possible straight-cut boundaries.

For horizontal cuts, maintain `prefix` as the sum of every row above the current boundary. Iterating only through `grid[:-1]` prevents the lower section from becoming empty. At each boundary, `prefix * 2 == total` is equivalent to the upper and lower sums being equal because the lower sum is `total - prefix`.

If no horizontal boundary works, reset the prefix and scan columns from left to right. Add every entry of the current column before testing the boundary to its right. Again, stop before the final column so the right section remains nonempty. The accumulated prefix is exactly the sum on the left, and the same doubled-prefix comparison detects equality. These loops visit every legal horizontal and vertical cut, so returning `false` after both scans proves that no allowed partition exists.

## Complexity detail

Let $m$ be the row count and $n$ the column count. Computing the total, examining row prefixes, and examining column prefixes each visit at most all $mn$ entries, for $O(mn)$ time overall. Only scalar totals, indices, and the current row reference are stored, so auxiliary space is $O(1)$.

## Alternatives and edge cases

- **Stored row and column sums:** Precomputing both sets of sums also gives $O(mn)$ time, but uses $O(m+n)$ extra space that the direct scans avoid.
- **Recompute every candidate section:** Summing both sides independently for each boundary is correct but can take $O((m+n)mn)$ time.
- **Two-dimensional prefix table:** Rectangle queries are unnecessary for full-width or full-height sections and add $O(mn)$ space.
- **Single row:** There is no horizontal boundary, but every vertical boundary is still examined.
- **Single column:** There is no vertical boundary, but every horizontal boundary is still examined.
- **Odd total:** No integer prefix can equal half the total, so every comparison fails naturally.
- **Nonempty sections:** Excluding the final row and final column from candidate boundaries prevents a cut along the outer edge.
- **One cut only:** A horizontal success does not require any vertical cut, and vice versa; the task does not ask for four equal rectangles.
