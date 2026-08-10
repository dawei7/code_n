## General

**Replace “empty rectangle” checks with a skyline.** A valid ordered placement uses Alice at an upper-left point $A=(x_A,y_A)$ and Bob at a lower-right point $B=(x_B,y_B)$. Hence

$$
x_A\le x_B
\quad\text{and}\quad
y_A\ge y_B.
$$

The axis-aligned rectangle between them, including all four boundaries, may contain no other point. Checking every third point for every candidate pair would take $O(N^3)$ time, which is too slow for $N$ up to 1000. The exact solution sorts the points so horizontal eligibility is automatic, then represents all possible blockers for a fixed Alice with one number.

**Use the exact tie order required by zero-width rectangles.** Points are sorted by

`(x, -y)`:

- increasing $x$ from left to right;
- decreasing $y$ when two points share $x$.

After selecting the point at index $i$ as Alice, every suffix point has $x\ge x_A$. Sorting equal-$x$ points from top to bottom is crucial because fences are allowed to be vertical lines. A higher same-column point must be considered as Alice before a lower same-column Bob, and an intermediate same-column point must appear early enough to block a longer vertical segment.

The source sorts `points` in place, so it changes the list's order.

**Scan the suffix while maintaining the visible height.** Fix Alice's height `y1`. Variable `max_y` starts at negative infinity. It represents the highest lower boundary already encountered among points at or below Alice that can block later candidates.

For every later point with height `y2`, the condition

`max_y < y2 <= y1`

decides validity. The right half, `y2 <= y1`, ensures Bob is not above Alice. The left half, `max_y < y2`, ensures no earlier suffix point lies within the candidate rectangle's vertical span.

When the condition succeeds, the pair is counted and `max_y` becomes `y2`.

**Why a height no greater than the frontier is invalid.** Assume a candidate Bob has `y2 <= max_y`. The point that established `max_y` was encountered earlier in the sorted suffix. Its $x$ is therefore between Alice and this Bob, allowing equality where a boundary is vertical. Its height lies at most at Alice and at least at Bob:

$$
y_B\le \texttt{max\_y}\le y_A.
$$

That point is inside the rectangle or on its boundary. It is a third person, so Alice would be sad. The candidate must not be counted.

The inequality is strict. If `y2 == max_y`, the earlier point lies on the horizontal boundary of the rectangle and still blocks it.

**Why a height above the frontier is valid.** Suppose `max_y < y2 <= y1`. Any point previously scanned with height in $[y2,y1]$ would have established a frontier at least $y2$, contradicting the strict inequality. Earlier points above $y1$ are outside the rectangle, while earlier points below $y2$ are below it. Points that appear later in sorted order have $x$ beyond Bob and cannot be inside the rectangle being tested. Thus no third point lies within or on the fence.

After counting this Bob, setting `max_y = y2` is correct because it is now the highest relevant blocking height seen. A later point below or level with it is hidden; a later point higher than it can define a smaller vertical interval that excludes this blocker.

**Why ignored points need no update.** A point above Alice cannot be inside any downward rectangle rooted at Alice. A point below or equal to the current frontier is already dominated by a higher blocker: remembering the lower point would not invalidate any candidate that the higher one does not already invalidate. Therefore the single maximum is a complete summary of the suffix history.

**A geometric trace.** Let Alice be at height 8. Suppose later heights, already ordered by $x$, are 3, 1, 6, 5, 6, and 7. Height 3 is visible and counted, setting the frontier to 3. Height 1 is blocked. Height 6 is visible and raises the frontier. Height 5 is blocked by that point. The repeated height 6 is also blocked because the earlier point would be on the new fence. Height 7 lies above the frontier but not above Alice, so it is visible and counted. Three pairs are valid for this Alice.

**Coverage and uniqueness.** Every legal Alice-Bob orientation has Alice no farther right than Bob. The sort places Alice before Bob, with the $y$ tie-break resolving same-column orientations. The outer loop eventually chooses that Alice, and the inner suffix loop reaches that Bob. The frontier proof decides exactly whether another point occupies their rectangle. The reversed placement is either geometrically illegal or considered separately only if it too satisfies the required upper-left/lower-right roles, so pairs are not accidentally doubled.

## Complexity detail

Sorting costs $O(N\log N)$ time. The nested loops inspect all suffix pairs, totaling $N(N-1)/2=O(N^2)$ iterations. The total time complexity is $O(N^2)$, which dominates sorting and is suitable for $N\le1000$.

At the algorithmic level, only a count and one frontier value are needed after sorting. In this exact Python source, however, `points[i + 1:]` allocates a new suffix list on every outer iteration. The largest such list contains $O(N)$ references, so peak auxiliary space is $O(N)$; the repeated slices also cause $O(N^2)$ cumulative allocation traffic. Python's in-place sort can require $O(N)$ temporary workspace as well.

Therefore the local manifest's $O(1)$ space description does not accurately describe this protected implementation. An index-based inner loop could avoid suffix slices, but that is a different source. The input list is mutated by sorting.

## Alternatives and edge cases

- **Third-point scan for every pair:** It directly implements the definition but takes $O(N^3)$ time.
- **Coordinate compression plus 2D prefix sums:** Rectangle population queries become constant time after preprocessing, but the compressed grid may use quadratic space and is unnecessary for the one-frontier insight.
- **Range trees or Fenwick structures:** More advanced geometric data structures can answer related dominance queries, but they add implementation complexity without improving this source's needed $O(N^2)$ pair traversal.
- **Index-based suffix traversal:** It preserves the exact skyline logic and time bound while removing slice allocations. The protected implementation uses slicing, so its real peak space remains linear.
- **Equal $x$ coordinates:** Descending $y$ order makes upper points precede lower points and correctly supports zero-width fences.
- **Equal $y$ coordinates:** Only the first visible point at that height can be Bob; a farther point is blocked by it on the fence boundary.
- **Bob above Alice:** The `y2 <= y1` condition rejects the orientation.
- **Third point exactly on an edge:** It blocks the pair. Strict frontier growth ensures equality is treated as blocked, not clear.
- **Third point below Bob:** It lies outside the rectangle and does not affect validity; a higher stored frontier already captures all relevant obstruction.
- **Point above Alice:** It is ignored for this Alice because it cannot enter any rectangle extending downward from her.
- **Distinct points but repeated coordinates:** Complete coordinate pairs are distinct, yet $x$ or $y$ alone may repeat, so both sort and strictness details remain necessary.
- **Input mutation:** The method returns only the count but leaves `points` sorted by $(x,-y)$.
