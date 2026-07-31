## General

First separate the coverage supplied for free by the existing bulbs from the coverage that must be purchased with new bulbs. Each positive `lights[i] = v` contributes the inclusive interval from `max(0, i - v)` through `min(n - 1, i + v)`. Add `1` at the left endpoint and `-1` immediately after the right endpoint in a difference array. A prefix sum is positive exactly at positions illuminated by at least one existing bulb, so all initial visibility is computed in linear time even when the intervals are large and overlap heavily.

Now scan the road from left to right. If the current position is already visible, advance one step. Otherwise, let `i` be this first invisible position. Any new radius-one bulb that covers `i` must be placed at `i - 1`, `i`, or `i + 1`, subject to the road boundary. Placing it as far right as possible—at `i + 1` unless `i` is the last position—covers every still-relevant position covered by either earlier choice and extends coverage farthest into the unprocessed suffix. The scan can therefore count one bulb and jump directly past `i`, `i + 1`, and `i + 2`.

For correctness, consider any optimal completion when the scan first reaches an invisible `i`. Replace the bulb that covers `i` with the rightmost legal placement. No position before `i` matters any longer because all of them were already visible, while the replacement reaches at least as far right. The replacement never increases the number of bulbs and leaves an optimal solution for the remaining suffix. Repeating this exchange at every greedy placement proves that the final count is minimum.

## Complexity detail

Building the difference array, taking its prefix sum, and performing the greedy scan each inspect $O(n)$ positions. The total running time is $O(n)$. The difference and visibility arrays use $O(n)$ auxiliary space.

## Alternatives and edge cases

- **Mark every interval cell by cell:** Directly painting each existing bulb's range is simple but can take $O(n^2)$ time when many bulbs have large radii.
- **Check every bulb from every road position:** Testing visibility independently also costs $O(n^2)$ in the worst case and repeats the same interval work.
- **Place at the first invisible position:** This is valid but may cover one fewer future position than placing at `i + 1`, so it can use more bulbs.
- **Difference-array boundary:** Subtract at `right + 1`; the array has length `n + 1`, so an interval ending at `n - 1` remains safe.
- **Already fully visible:** The greedy scan finds no invisible position and returns `0`.
- **One position or an invisible final position:** The same greedy step counts one bulb and advances beyond the road, even though the preferred `i + 1` placement is out of bounds.
