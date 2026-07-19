## General
**Put both times on one minute axis.** Parse each clock time as `60 * hour + minute`. If logout is numerically earlier than login, add $1440$ minutes to logout, representing the next day. The session is then one ordinary half-open interval on a non-wrapping timeline.

**Round inward to complete boundaries.** The first round that can be fully played begins at the first multiple of $15$ not earlier than login:

$$
S = 15\left\lceil\frac{\textit{start}}{15}\right\rceil.
$$

The last usable round ends at the last multiple of $15$ not later than logout:

$$
E = 15\left\lfloor\frac{\textit{end}}{15}\right\rfloor.
$$

When $E \ge S$, the number of complete quarter-hour intervals is $(E-S)/15$. Otherwise there is no full round, so clamp the result at zero. These inward boundaries exclude partial rounds at both ends and handle midnight without separate before/after counts.

## Complexity detail
Parsing two fixed-width strings and performing a fixed number of integer operations takes $O(1)$ time and $O(1)$ space. The legal domain contains only one day's 1,440 minute positions, so a `bounded_domain` certificate replaces meaningless runtime scaling with exhaustive validation of every distinct login/logout pair.

## Alternatives and edge cases
- **Simulate every quarter-hour:** At most 96 rounds exist per day, but direct arithmetic is simpler and constant work.
- **Round login downward:** This incorrectly counts a round that had already started when the player logged in.
- **Round logout upward:** This incorrectly counts a round that was unfinished at logout.
- **Crossing midnight:** Add one day to logout only when its clock value is earlier than login.
- **Short session:** Even a positive-duration session can contain zero complete rounds.
- **Exact boundaries:** A login on a quarter-hour and logout on the following quarter-hour count exactly one round.
