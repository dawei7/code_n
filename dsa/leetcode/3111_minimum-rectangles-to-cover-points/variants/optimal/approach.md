## General

**Reduce the rectangles to horizontal intervals.** Every input point has a nonnegative $y$-coordinate, and a rectangle may choose any nonnegative height. Once a horizontal span has been chosen, its top can therefore be raised enough to cover every point whose $x$-coordinate lies in that span. Only the $x$-coordinates affect how many rectangles are required.

Sort the points by $x$-coordinate. Maintain `covered_through`, the inclusive right endpoint of the most recently placed rectangle. Points with $x \le \texttt{covered_through}$ are already covered. When the scan reaches a point at coordinate $a > \texttt{covered_through}$, that point is the leftmost one not yet covered, so start a new rectangle with horizontal span $[a,a+w]$.

**Starting at the leftmost uncovered point is optimal.** Any valid solution must use some rectangle that covers the point at $a$. If that rectangle begins to the left of $a$, shifting its left edge to $a$ and extending its right edge to $a+w$ cannot uncover an unprocessed point: no uncovered point lies to the left of $a$, and the shifted rectangle reaches at least as far to the right as any width-at-most-$w$ rectangle covering $a$. Thus an optimal solution exists whose first remaining rectangle is exactly the greedy rectangle.

After removing all points through $a+w$, the same argument applies to the next leftmost uncovered point. Repeating this exchange proves that each greedy placement is compatible with an optimal completion, so the final rectangle count is minimum.

## Complexity detail

Let $n$ be the number of points defined in the function contract. Sorting takes $O(n \log n)$ time, and the subsequent scan takes $O(n)$ time. The app-local implementation stores and sorts a copy of the points, requiring $O(n)$ auxiliary space; Python's in-place sort used by the native source may also use linear temporary storage in the worst case.

## Alternatives and edge cases

- **Sort only distinct x-coordinates:** Building a set first can reduce the number of scanned values when many points share an $x$-coordinate, but the worst-case time and space remain $O(n \log n)$ and $O(n)$.
- **Min-heap:** Heapify all $x$-coordinates and repeatedly pop covered values. This is also $O(n \log n)$ but has larger constants and does not simplify the greedy proof.
- **Repeated minimum search:** Find the smallest remaining $x$ and filter covered points after every rectangle. This is correct but takes $O(n^2)$ time when each rectangle covers only one point.
- **Zero width:** A rectangle then covers exactly one distinct $x$-coordinate, although it may cover many points at different heights on that vertical line.
- **Inclusive right boundary:** A point with $x=a+w$ is covered by the rectangle beginning at $a$; only a strictly larger coordinate starts the next rectangle.
- **Repeated x-coordinates:** Distinct points may share an $x$-coordinate because their $y$-coordinates differ, and all such points are covered together.
- **Vertical coordinates:** Large gaps in $y$ never force another rectangle because rectangle height has no upper bound.
