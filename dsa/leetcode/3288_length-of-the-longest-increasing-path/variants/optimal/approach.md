## General

Let the required point be $(x_k, y_k)$. Every point before it in an increasing path must lie strictly down and to its left, so it must satisfy $x < x_k$ and $y < y_k$. Similarly, every point after it must satisfy $x > x_k$ and $y > y_k$. A point incomparable with the target can never belong to a path containing it.

This separates the answer into three compatible pieces: the longest increasing chain among the lower-left points, the required point itself, and the longest increasing chain among the upper-right points. Any optimal chain on either side can be joined through the target because all inequalities between that chain and the target are already strict.

To find a longest chain within one side, sort its points by ascending $x$. For equal $x$, sort by descending $y$. Then compute a strictly increasing longest subsequence of the resulting $y$-coordinates with the patience-sorting tails array. The descending tie order is essential: two equal-$x$ points appear with decreasing $y$, so a strictly increasing subsequence cannot select both. For each $y$, `bisect_left` finds the first tail at least as large and replaces it, or extends the tails array when no such position exists.

The tails array does not store one literal path. At length $j + 1$, it stores the smallest possible final $y$ among chains of that length seen so far. Replacing a tail preserves the chain length while making future extensions no harder. Consequently, its final length is the maximum number of points strictly increasing in both coordinates.

## Complexity detail

Let $n$ be the number of input points. Filtering both sides takes $O(n)$ time. Sorting dominates at $O(n \log n)$, and all binary searches together also take $O(n \log n)$. The filtered lists, sorting storage, and tails arrays use $O(n)$ auxiliary space.

## Alternatives and edge cases

- **Quadratic dynamic programming:** Sorting the points and testing every earlier predecessor is direct, but requires $O(n^2)$ time and is too slow for $n = 10^5$.
- **Fenwick tree with coordinate compression:** A range-maximum structure can also compute the chain lengths in $O(n \log n)$, but it needs careful batching for equal $x$ and is more machinery than the tails method.
- **Equal coordinates on one axis:** Strict increase forbids chaining points with equal $x$ or equal $y$; descending $y$ ties and `bisect_left` enforce these two restrictions.
- **No compatible point on one side:** That side contributes zero, while the required point still makes the answer at least one.
- **Input order:** The path depends only on coordinate comparisons, so sorting does not violate any ordering condition.
