## General

**Assign every shared vertex once.** Treat each segment as including its left
endpoint and excluding its right endpoint. Then a chart vertex belongs to
exactly one adjacent segment. Add the final chart endpoint separately because
no segment starts there.

For an ascending segment from low to high, the intersected height interval is
$[\text{low},\text{high})$. For a descending segment, it is
$(\text{low},\text{high}]$. Double all heights: an exact integer height is
`2 * height`, while adding one represents the open side immediately above
that height. This converts both interval types into ordinary half-open sweep
events without floating-point values.

Add +1 at each interval start and -1 at its end. Represent the final endpoint
as the isolated doubled interval from `2 * y[-1]` to `2 * y[-1] + 1`.
Sweep events in height order; the greatest active count is the desired number
of distinct intersections.

## Complexity detail

There are $O(N)$ event coordinates. Constructing them is linear, sorting them
takes $O(N\log N)$ time, and the sweep is linear. The event map uses $O(N)$
auxiliary space.

## Alternatives and edge cases

- **Test every critical level:** Rescanning all segments at every endpoint and between-height level is correct but costs $O(N^2)$ time.
- **Closed interval per segment:** This double-counts a shared vertex when the horizontal line passes exactly through it.
- **Floating-point offsets:** Small epsilon adjustments are fragile; doubled integer coordinates encode open boundaries exactly.
- **Local maximum or minimum:** Both adjacent segments meet at one geometric point and must contribute one intersection there.
- **Final endpoint:** It needs an explicit isolated event because the half-open segment convention excludes it.
- **Repeated nonadjacent heights:** Their distinct horizontal positions remain separate intersections.
