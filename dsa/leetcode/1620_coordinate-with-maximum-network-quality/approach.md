## General

**Turn the geometric question into a finite search**

The result must be an integral, non-negative coordinate. Every tower coordinate is also between 0 and 50. The implementation therefore checks every coordinate `(i, j)` in the fixed square from `(0, 0)` through `(50, 50)`. This is only $51 \times 51 = 2601$ candidate positions, so trying all of them is both simple and comfortably small.

Why is it safe not to examine a non-negative coordinate beyond 50? Every tower has both coordinates at most 50. Suppose a candidate has $x > 50$. Moving its $x$-coordinate left to 50 cannot increase its distance from any tower, because every tower lies at $x \le 50$. Consequently, no tower contribution decreases. The same reasoning applies to $y > 50$. Thus, a maximizer exists inside the searched square. Negative coordinates are not eligible for the requested tie-breaking result, so they do not need to be searched.

The outer loop assigns `i` from 0 through 50, and the inner loop assigns `j` from 0 through 50. For each candidate, `t` starts at zero and accumulates that coordinate's total network quality.

**Score one candidate exactly as the statement defines**

For a tower `[x, y, q]`, the code computes

$$
d = \sqrt{(x-i)^2 + (y-j)^2}.
$$

This is the Euclidean distance from the tower at $(x,y)$ to the candidate at $(i,j)$. The exponent `0.5` performs the square root after the two squared coordinate differences have been added.

The condition `d <= radius` is important. A tower exactly on the boundary is reachable because the contract says “less than or equal to,” not merely “less than.” If the condition is false, that tower contributes nothing. If it is true, the implementation adds

$$
\left\lfloor\frac{q}{1+d}\right\rfloor
$$

to `t`. The added 1 makes the denominator nonzero at the tower's own location. In that case $d=0$, so the tower contributes its entire integer quality $q$. As distance grows, the denominator grows and the contribution can only fall. Calling `floor` is necessary because ordinary division can produce a fractional value, while the required signal contribution is the greatest integer no larger than that value.

The contribution is calculated independently for every tower and then summed. This matters because flooring the individual contributions and flooring the final sum are not equivalent. For example, two separate contributions of 2.7 count as $2+2=4$, not $\lfloor 5.4\rfloor=5$. The source follows the required per-tower rule by applying `floor` inside the tower loop.

**Keep the best score and obtain the lexicographic tie break for free**

The variables `mx` and `ans` hold the greatest score seen so far and its coordinate. Both begin at zero, with `ans = [0, 0]`. Once `t` has been fully computed, the candidate replaces the answer only when `t > mx`. An equal score deliberately does not replace it.

That strict comparison works together with the traversal order. The loops visit coordinates in this sequence:

`(0,0), (0,1), ..., (0,50), (1,0), ..., (50,50)`.

This is precisely increasing lexicographic order: a smaller first coordinate comes first, and among equal first coordinates, a smaller second coordinate comes first. Therefore, the first coordinate encountered with a particular maximum score is the lexicographically smallest one. Later ties must be ignored, which is exactly what the strict `>` comparison does.

The zero initialization also handles the case where every candidate has quality zero. Since no score is greater than zero, `ans` stays `[0, 0]`. That is correct: every non-negative coordinate ties at quality zero, and `[0, 0]` is lexicographically smallest. More commonly, at least one tower has positive quality and its own location obtains at least that quality, causing an update.

**Why the exhaustive result is correct**

Every eligible maximizer can be represented by a point inside the searched `0..50` square, as established by the projection argument above. For each point in that square, the inner loop considers every tower. It adds a contribution exactly when that tower is reachable and uses the required floored formula, so `t` equals the true network quality of that point.

Whenever a score is greater than all earlier scores, the algorithm saves it. Hence, after the final candidate, `mx` is the maximum score over the entire search square. Because equal scores never overwrite an earlier answer and the search order is lexicographic, `ans` is the lexicographically smallest coordinate attaining that score. These facts cover both parts of the return contract: maximum quality and the required tie break.

## Complexity detail

Let $T$ be the number of towers, and let $C=51$ be the number of allowed coordinate values examined on each axis by this implementation.

There are $C^2$ candidate coordinates. At each candidate, the code visits all $T$ towers and performs a constant amount of arithmetic. Its time complexity is therefore

$$
O(C^2T).
$$

Because the problem fixes $C$ at 51, $C^2=2601$ is a constant, so this simplifies to $O(T)$ with respect to the varying input size. This explains the manifest's `O(T)` bound, but retaining $O(C^2T)$ makes the work performed by the loops explicit. With at most 50 towers, the source evaluates at most $2601 \times 50=130{,}050$ tower-candidate pairs.

The algorithm stores only the best coordinate, the best score, the current score, and a few loop and arithmetic values. It does not allocate a grid or a collection proportional to $T$. Its auxiliary space complexity is $O(1)$. The input list and the returned two-element list are not counted as growing auxiliary storage.

Floating-point square roots are used for `d`. Under the small integer coordinate bounds, these computations are well within ordinary numeric range. The mathematical target remains the exact Euclidean formula; the implementation follows it directly rather than comparing squared distances for the contribution, because the actual distance is also needed in the denominator.

## Alternatives and edge cases

- **Search only tower-centered bounding limits:** One can compute the maximum input $x$ and $y$ and search `0..max_x` by `0..max_y`. That may reduce constant work, but the fixed `0..50` search is simpler and remains tiny under the stated constraints.
- **Search the union of reachable disks:** Points outside every radius have score zero, so candidates could be generated only near towers. Managing integer disk bounds and still preserving tie behavior adds complexity without improving the asymptotic result for a 51-by-51 domain.
- **Precompute a quality grid:** Each tower could add its signal to all reachable grid cells, producing the same $O(C^2T)$ upper bound while using $O(C^2)$ memory. The source instead computes one scalar score at a time and needs constant auxiliary space.
- **Squared-distance reachability only:** Comparing `(x-i)**2 + (y-j)**2 <= radius**2` avoids a square root for the reachability test, but the square root is still required to calculate `q / (1 + d)`. It can be a minor numerical refinement, not a different algorithm.
- **Several coordinates have the same best quality:** The row-major traversal is lexicographic, and the strict update condition preserves the first best coordinate. Replacing `>` with `>=` would incorrectly retain the last tied coordinate.
- **A tower lies exactly `radius` away:** The `<=` check includes it, as required. Using `<` would lose a valid boundary contribution.
- **The candidate equals a tower location:** The distance is zero and the denominator is one, so that tower contributes exactly `q`.
- **A tower's floored contribution is zero:** The tower may be reachable yet add zero when its quality is too small relative to its distance. Adding zero is harmless and accurately follows the formula.
- **All qualities are zero:** No candidate improves `mx = 0`, so the method returns `[0, 0]`, the lexicographically smallest non-negative coordinate.
- **Flooring at the wrong time:** Each tower's quotient must be floored before summation. Flooring only the combined real-valued sum can produce a different and invalid score.
