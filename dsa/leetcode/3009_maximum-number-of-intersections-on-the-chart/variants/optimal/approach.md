## General

**Turn every segment into a vertical interval**

A nonhorizontal line segment between heights $u$ and $v$ intersects a horizontal line at every height between them. If all segment intervals were simply closed at both ends, a chart vertex shared by two adjacent segments could be counted twice even though the horizontal line meets one geometric point there.

The solution assigns each segment a consistent half-open convention: include its left endpoint and exclude its right endpoint. The final chart point, which is no segment’s left endpoint, is then added separately.

**Why doubled coordinates encode open and closed endpoints**

Event coordinates use twice the real height. Ordinary vertex height $h$ is represented by `2*h`, while `2*h+1` represents a level infinitesimally above $h$ for sweep-order purposes.

For a rising segment from `first < second`, the left endpoint is the lower one. The events:

- add one at `2*first`;
- subtract one at `2*second`

encode interval $[\textit{first},\textit{second})$.

For a falling segment, the left endpoint is the higher one and the right endpoint is the lower one. The events:

- add one at `2*second + 1`;
- subtract one at `2*first + 1`

encode $(\textit{second},\textit{first}]$: exclude the lower right endpoint and include the higher left endpoint.

Both formulas implement “left chart endpoint included, right chart endpoint excluded,” expressed in vertical order.

**Add the last vertex**

Every segment accounts for its left endpoint. The last chart point is only a right endpoint, so it would otherwise be excluded. The two events at `2*y[-1]` and `2*y[-1]+1` create a singleton-height interval that contributes exactly one intersection at that final vertex.

Now every chart vertex is owned exactly once, while crossings strictly inside segments remain counted normally.

**Sweep all event heights**

`events` is a difference map. A positive delta starts one or more active intersection intervals; a negative delta ends them.

The code sorts event coordinates, adds each delta to `active`, and updates `answer`. Between adjacent event coordinates, the active count is constant, so checking immediately after every change captures the maximum for all possible horizontal line heights.

Several events at the same encoded height are combined in the dictionary before the sweep. Their net delta correctly handles coincident vertices and interval boundaries.

**Why the maximum active count equals intersections**

For any horizontal height, each active encoded segment interval represents one distinct intersection assigned under the endpoint convention. Shared vertices are assigned to one adjacent segment, so they are not duplicated. The last-point singleton covers the one otherwise unowned endpoint.

Conversely, every geometric intersection belongs either to a segment interior or a chart vertex. Interior crossings activate that segment; vertices activate their unique owning interval. Thus `active` is exactly the number of distinct intersection points at the represented height.

Taking its maximum returns the requested value.

**Example intuition**

At a local peak, the incoming segment has the peak as its right endpoint and excludes it, while the outgoing segment has it as its left endpoint and includes it. The horizontal line through the peak counts one intersection.

At a local valley, the same left-included/right-excluded ownership rule again counts the shared point once, even though the vertical interval orientations reverse.

**Why the no-horizontal-segment guarantee matters**

Consecutive heights are different, so a horizontal query line never overlaps an entire chart segment. Every meeting is a point and can be counted through interval activity. Horizontal source segments would require a separate definition of “number of points of intersection,” potentially infinite.

**Why event coordinates are enough**

No segment interval starts or ends between two consecutive sorted event coordinates. The set of active segments is therefore unchanged throughout that open vertical gap. Checking one representative count after each event covers the entire gap as well as the encoded endpoint level. The sweep does not need to test arbitrary real-valued heights individually.

## Complexity detail

Let $N$ be the number of chart points. There are $N-1$ segments plus one final singleton, producing $O(N)$ distinct event keys. Building the map takes expected $O(N)$ time.

Sorting event coordinates costs $O(N\log N)$ and dominates the linear sweep. The event map and sorted key list use $O(N)$ space. Input `y` is not modified.

## Alternatives and edge cases

- **Closed intervals for every segment:** This double-counts shared vertices.
- **Evaluate only integer heights:** The maximum can occur between vertex heights, such as at 1.5, so fractional regions matter.
- **Floating epsilon endpoints:** Doubled integers encode endpoint order exactly without floating-point error.
- **Brute-force candidate heights against all segments:** Testing $O(N)$ height regions with $O(N)$ segments costs $O(N^2)$.
- **Strictly increasing chart:** Every horizontal line within the height range intersects once, and the sweep returns one.
- **Local peaks and valleys:** Endpoint ownership ensures each shared point contributes once.
- **Repeated nonconsecutive heights:** Events combine correctly; only consecutive equality is forbidden.
- **Last vertex:** Its explicit singleton is necessary because all segment right endpoints are excluded.
- **Large height values:** Doubling values up to $10^9$ is safe in Python integer arithmetic.
