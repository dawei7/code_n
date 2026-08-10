## General

**Turn a path through one required point into two independent chains.** A valid path must have strictly increasing $x$-coordinates and strictly increasing $y$-coordinates. The path is also required to contain `coordinates[k]`. Write that required point as $(x_k,y_k)$. Any point appearing before it must satisfy both $x<x_k$ and $y<y_k$; being smaller in only one coordinate is not enough. Similarly, every point after it must satisfy both $x>x_k$ and $y>y_k$. Therefore the source partitions the useful points into `lower` and `upper`. Points equal to the target in one coordinate, or lying on opposite sides in the two coordinates, cannot belong to any increasing path through the target and are deliberately discarded.

This partition is more than a convenient filter. It proves that the two sides can be optimized independently. Every increasing chain made from `lower` can be followed by the required point, because its last point is smaller than the target in both coordinates. Every increasing chain made from `upper` can follow the target for the symmetric reason. Moreover, every lower point is smaller than every upper point through the target inequalities: its coordinates are below $(x_k,y_k)$ while the upper point's coordinates are above them. Consequently, joining an optimal lower chain, the target, and an optimal upper chain always creates a valid complete path. The answer is therefore

$$
\text{bestLower}+1+\text{bestUpper}.
$$

The middle $1$ counts `coordinates[k]` itself. This reasoning also covers an empty side: an empty lower or upper chain contributes zero, while the required point still contributes one.

**Reduce each two-dimensional chain to a one-dimensional LIS.** The helper `longest_chain(points)` must find the largest subset that is strictly increasing in both coordinates. It first sorts points by increasing $x$. Once points are processed in that order, the remaining task seems to be a longest strictly increasing subsequence of their $y$-values. There is one subtle obstacle: two different points can have the same $x$, and a valid chain may not choose both because $x$ must increase strictly.

The tie rule solves exactly that obstacle. The sorting key is `(point[0], -point[1])`, so equal-$x$ points appear in decreasing $y$ order. A strictly increasing subsequence of $y$ cannot take two values from that decreasing block. Thus any subsequence selected by the LIS logic automatically uses strictly increasing $x$ as well as strictly increasing $y$. Without the negative second component, equal-$x$ points could appear in increasing-$y$ order and be incorrectly counted as a valid chain.

**What the `tails` list means.** After processing some sorted points, `tails[length - 1]` is the smallest possible ending $y$ among all valid chains of the given `length` seen so far. It does not store one final path, and replacing an entry does not discard a needed answer. A smaller ending value is always at least as useful as a larger ending value for extending the chain later.

For each current $y$, `bisect_left(tails, y)` finds the first position whose stored value is at least $y$. If no such position exists, $y$ is larger than every tail, so it extends the longest known chain and is appended. Otherwise, the source replaces that position with $y$. The use of `bisect_left` is essential for strict increase: an equal $y$ replaces an existing tail rather than extending the length. Had the code used `bisect_right`, equal $y$-coordinates could incorrectly increase the answer.

For example, suppose sorted $y$-values are $2,5,3,7$. The tails states are `[2]`, `[2,5]`, `[2,3]`, and `[2,3,7]`. Replacing $5$ by $3$ does not say the old point vanished from every real chain. It records that a length-two chain ending at $3$ gives later points more room to extend. Only the length of `tails` is needed, because the problem asks for the maximum path length rather than the actual coordinates.

**Why the returned length is exact.** Whenever the helper appends, it has found a real chain one element longer: the current $y$ exceeds the smallest tail of the previous length, and sorted order plus the tie rule ensures a strictly smaller earlier $x$. Replacements never invent a longer chain; they only improve an existing length's ending value. Conversely, for any valid chain of length $r$, processing its points in sorted order causes the LIS structure to maintain at least $r$ attainable levels. Therefore `len(tails)` can be neither larger nor smaller than the best two-dimensional chain length.

Finally, the source calls this exact helper separately for `lower` and `upper` and adds the results around the target. It uses `sorted(points, ...)` rather than sorting `coordinates` itself, so the caller's input order is not modified. The filtered lists and sorting copies are implementation details that matter for space, but they do not change the geometric argument.

## Complexity detail

Let $n$ be the number of coordinates, let $\ell$ be the number of points in `lower`, and let $u$ be the number in `upper`. Filtering scans all $n$ points and costs $O(n)$ time. Sorting the two groups costs $O(\ell\log\ell+u\log u)$. Every point in a sorted group performs one binary search in a tails list, adding another $O(\ell\log\ell+u\log u)$ time. Since $\ell+u\le n$, the total is $O(n\log n)$ time.

The two filtered lists hold at most $n$ point references in total. `sorted` creates sorted list objects, and the two `tails` lists can together grow to at most $\ell+u$. Thus the auxiliary space is $O(n)$. Python's sorting implementation may also use temporary memory bounded by the number of sorted elements; this remains inside $O(n)$. The algorithm does not construct the path itself, so no additional predecessor table is required.

## Alternatives and edge cases

- **Quadratic dynamic programming:** Sort with the same tie discipline and compute the best chain ending at every point by checking all earlier points. This is conceptually direct but costs $O(n^2)$ time, which is unsuitable for $n$ up to $10^5$.
- **A full two-dimensional partial-order data structure:** Coordinate compression with a Fenwick tree or segment tree can also query the best chain below a point. It is more machinery than necessary here because sorting one coordinate reduces the other coordinate to the standard strict LIS problem.
- **Sorting both coordinates ascending:** This is a tempting but incorrect shortcut. Equal-$x$ points with increasing $y$ could both enter the LIS even though the path requires a strict increase in $x$; decreasing $y$ within each $x$ tie is what prevents that error.
- **Using `bisect_right`:** That version computes a non-decreasing subsequence and would allow repeated $y$-coordinates. The contract requires strict increase in both dimensions, so `bisect_left` is the correct boundary operation.
- **Points incomparable with the required point:** A point with $x<x_k$ but $y>y_k$, or the reverse, cannot occur on either side of the target in a valid path. Ignoring it is required, not a lost optimization opportunity.
- **Equal coordinate on one axis:** Even though complete points are distinct, two points may share an $x$ or a $y$. Strict inequalities exclude a point sharing either coordinate with the target, and the sort/LIS rules prevent equal coordinates inside either side's chain.
- **Target is already the only usable point:** If both filtered groups are empty, both helper calls return zero and the method returns one, correctly representing the path containing only `coordinates[k]`.
- **Only one useful side exists:** If the target is minimal or maximal relative to all comparable points, one chain length is zero. The additive decomposition remains valid without special-case code.
- **Negative or large coordinate values:** The algorithm depends only on comparisons. Negative values and large magnitudes require no normalization, and negating $y$ in the sort key is safe with Python's arbitrary-precision integers.
- **Recovering the actual path:** The current `tails` array is sufficient only for the length. Returning the coordinates would require predecessor links and the index represented by every tails entry, increasing implementation complexity while retaining the same asymptotic bounds.
