## General
**Only three recent geometric configurations can create the first crossing**

Before the first self-intersection, the counterclockwise path is either expanding outward, contracting inward, or making the single transition between those phases. That structure means the current segment can first meet only the segment three, four, or five steps behind it; older segments remain shielded by those recent boundaries.

At index `i`, the ordinary inward-spiral crossing with segment $i - 3$ occurs when the current length reaches at least across segment $i - 2$ and the intervening segment is no longer than $i - 3$:
`distance[i] >= distance[i - 2]` and `distance[i - 1] <= distance[i - 3]`.

**Touching and transition cases need inclusive comparisons**

The current segment can meet segment $i - 4$ when the two intervening parallel segments are equal and the current plus segment $i - 4$ reaches segment $i - 2$. This includes edge touching, not only a proper crossing.

During an outward-to-inward transition, segment `i` can reach segment $i - 5$. The two surrounding pairs must overlap in both axes: segment $i - 2$ must reach at least segment $i - 4$, the current segment plus $i - 4$ must reach $i - 2$, and the analogous inequalities must hold for segments $i - 1$, $i - 3$, and $i - 5$.

Checking the configurations in order at every index detects a crossing as soon as it becomes possible. Each condition uses only six recent lengths and includes equality so shared endpoints and collinear contact count as self-crossing.

**The first crossing must match one of the configurations**

If the path is still expanding, the current segment remains outside all earlier boundaries. Once a segment stops expanding, the path either crosses the third-back segment immediately, lies flush with the fourth-back segment, or enters the bounded transition where the fifth-back segment becomes exposed. After contraction begins, the third-back test covers subsequent inward crossings.

These exhaust the geometry at the first intersection. Therefore rejecting all three patterns for every segment proves the path never self-intersects, while every accepted inequality describes actual overlap in both coordinate axes.

## Complexity detail
The scan examines each segment once and evaluates a constant number of inequalities, giving $O(n)$ time. It reads only a fixed window of recent array values and uses $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Construct coordinates and compare every segment pair:** is straightforward but takes $O(n^2)$ time and $O(n)$ path storage.
- **Check only the segment three steps back:** misses the flush four-step case and the outward-to-inward transition case.
- **Use strict inequalities:** misses paths that touch at an endpoint or overlap along a boundary.
- Fewer than four segments cannot cross a nonconsecutive segment. Positive lengths avoid zero-length degeneracies.
