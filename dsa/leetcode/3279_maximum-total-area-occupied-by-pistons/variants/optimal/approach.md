## General

Each piston follows a triangular wave between zero and `height`. Its position changes linearly with slope plus one while moving up and minus one while moving down. The total area is the sum of positions, so it is also piecewise linear. A maximum of a linear segment occurs at an endpoint; only direction-change times need to be examined.

At time zero, `res` is the sum of all positions. `diff` is the total slope: add one for each upward piston and subtract one for each downward piston.

Dictionary `delta` stores how the total slope changes at future event times within one full period of length `2 * height`.

For an upward piston at `pos`, it reaches the top after `height - pos` seconds. Its slope changes from plus one to minus one, a delta of minus two. It next reaches the bottom at `2 * height - pos`, changing back by plus two.

For a downward piston, it reaches zero after `pos` seconds, changing slope from minus one to plus one, a delta of plus two. It next reaches the top at `height + pos`, changing by minus two.

All pistons have the same period `2 * height`, regardless of phase. Therefore their total repeats after one period, and checking its event points over that interval is sufficient for the maximum over all time.

The sweep sorts event times. Between previous time `pre` and current `cur`, the slope stays `diff`, so the total changes by `(cur - pre) * diff`. The code advances `res` to the event, applies all combined direction changes `d` at that time, and compares the event value with `ans`.

Combining deltas in a dictionary is important when several pistons hit endpoints simultaneously. Their slope changes occur together, while the total position at that instant is evaluated only once.

An event at time zero handles a piston initially at an endpoint and pointing outward. The time advance is zero, then its slope reverses immediately before subsequent motion. This makes the source robust to endpoint directions without a separate branch.

For example two, the sweep reaches time three with positions three, three, three, and six. The summed area fifteen is checked at the corresponding event boundary and becomes the maximum.

**Why no interior second needs checking.** On an interval without a bounce, total area has constant slope. If positive it is greatest at the right endpoint, if negative at the left, and if zero everywhere equal. Event endpoints plus time zero cover all cases.

The construction exactly superposes individual triangular waves; linearity of sums makes their slopes and slope changes additive.

## Complexity detail

Let $n$ be the piston count. Each piston contributes at most two event keys, so building state takes $O(n)$. Sorting at most $2n$ events costs $O(n\log n)$; the sweep is linear.

The event dictionary uses $O(n)$ space. Other state is constant. Positions and summed area can be large, but Python integers handle them exactly.

## Alternatives and edge cases

- **Simulate every second:** The period can be $2\cdot10^6$ and there can be $10^5$ pistons, making direct simulation far too costly.
- **Evaluate every piston at every event:** There are $O(n)$ events and pistons, causing $O(n^2)$ work. Slope deltas update the total in constant time per event.
- **Use trigonometric formulas:** Motion is a triangular, not sinusoidal, wave; piecewise-linear events are exact and simpler.
- **All pistons move up:** Initial slope is positive until the earliest top event, which the sweep reaches directly.
- **All move down:** Time zero may already be the maximum; initializing `ans = res` preserves it.
- **Several simultaneous bounces:** Their deltas sum in one dictionary entry.
- **Piston at zero moving down:** A time-zero plus-two delta turns its effective slope upward.
- **Piston at height moving up:** A time-zero minus-two delta turns it downward.
- **One piston:** Its maximum is `height`, found at its top event or initially.
- **Flat total segment:** Zero total slope means every point on that segment has equal area, and either endpoint represents it.
- **Period endpoint:** The total returns to its time-zero value; including events through the period cannot introduce an unrepresented larger value.
- **Area interpretation:** Each piston's current position equals its area contribution under the stated model, so summing positions is the requested total.
- **Events beyond the first bounce:** Each piston needs exactly two events in one full period. Its later bounces are those same event phases shifted by `2 * height` and cannot create a new total pattern.
- **Slope update ordering:** `res` advances using the old slope up to `cur`, then `diff` changes. Applying the delta first would incorrectly use the post-bounce direction during the interval before the bounce.
- **Initial maximum:** `ans` is initialized before sweeping because a strictly decreasing total can be greatest at time zero, which may not otherwise appear as a positive-time event.
- **Dictionary cancellation:** Opposite slope changes from different pistons at the same time can sum to zero. Keeping the event is harmless; the value is still checked at a legitimate linear-segment boundary.
