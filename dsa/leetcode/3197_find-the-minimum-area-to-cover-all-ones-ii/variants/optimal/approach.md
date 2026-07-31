## General

**Reduce each region to its tight bounding rectangle**

For any rectangular region of the grid, the cheapest rectangle covering all
of its `1`s is determined uniquely: its top, bottom, left, and right sides pass
through the extreme occupied rows and columns. Empty regions contribute zero
during enumeration; because the input has at least three `1`s, an optimal
three-rectangle cover is represented by a partition whose three occupied
pieces are all nonempty.

Build prefix sums along every row and column. They let us test whether a row
or column segment contains a `1` in constant time. Scanning inward from the
four sides therefore finds the tight bounding area of any queried region in
$O(R+C)$ time. Cache these region queries because the same pieces recur for
different cuts.

**Why six partition families are sufficient**

Shrink every rectangle in an optimal answer to its occupied bounding box.
Since the three boxes do not overlap, a horizontal or vertical line separates
one box from at least one other box. If two parallel cuts separate all three,
the layout is three horizontal stripes or three vertical stripes.

Otherwise, one cut separates a single box from the other two. The two boxes
on the remaining side can be separated by a perpendicular cut. Choosing which
side contains that pair gives four mixed layouts: two boxes above, below, left,
or right of the single box. These two stripe layouts and four mixed layouts
cover every possible relative placement of three disjoint axis-aligned boxes.

Enumerate both ordered pairs of horizontal cuts, both ordered pairs of
vertical cuts, and every horizontal/vertical cut pair for the four mixed
orientations. For each candidate, sum the three cached tight bounding areas
and retain the minimum. Every evaluated candidate is a valid non-overlapping
cover, and the classification above guarantees that one candidate represents
an optimal cover, so the minimum is optimal.

## Complexity detail

There are $O(R^2)$ horizontal-stripe region queries, $O(C^2)$ vertical-stripe
queries, and $O(RC)$ mixed-layout queries. Each distinct bounding-area query
scans at most $R+C$ boundary lines after the $O(RC)$ prefix construction.
The total time is therefore
$O((R+C)(R^2+RC+C^2))$.

The row and column prefix tables use $O(RC)$ space. The cache holds
$O(R^2+RC+C^2)$ region results, for total auxiliary space
$O(RC+R^2+C^2)$.

## Alternatives and edge cases

- **Scan every cell for every region:** This keeps the same six-layout proof,
  but finding each bounding box costs $O(RC)$ and raises the worst-case time.
- **Enumerate arbitrary rectangle triples:** Trying all coordinate choices
  obscures the separation structure and is prohibitively expensive even for
  the $30 \times 30$ limit.
- Empty enumeration regions contribute zero internally. An optimal cover can
  still be represented by a partition in which all three regions contain a
  `1`, because every required rectangle may be shrunk around the `1`s assigned
  to it.
- A single row or column is handled by the three-parallel-stripe family in the
  other direction.
- Rectangles may share edges or corners; only overlap is forbidden.
- Zeros inside a tight bounding rectangle still count toward its area.
