## General
**An optimal board may be anchored at a covered dart**

If an optimal circle has covered darts but none lies on its boundary, its
center can move continuously until a covered dart first reaches the boundary,
without immediately losing any covered point. Therefore some optimal placement
has at least one covered dart exactly $r$ from the center. Try every dart as
that boundary anchor. A center for anchor $p$ then lies somewhere on the circle
of radius $r$ around $p$ and can be described by one direction angle $\theta$.

The one-dart case is already covered by initializing the answer to one; no
second boundary point is required.

**Each other dart becomes an interval of valid center directions**

Fix anchor $p$ and another dart $q$. Let $d$ be their distance and let $\phi$
be the direction angle from $p$ to $q$. A candidate center is

$$
c=p+r(\cos\theta,\sin\theta).
$$

Requiring $q$ to lie on or inside the board means

$$
\lVert c-q\rVert^2\le r^2.
$$

After expanding and cancelling $r^2$, this is equivalent to

$$
\cos(\theta-\phi)\ge \frac{d}{2r}.
$$

If $d>2r$, no radius-$r$ circle can cover both darts and $q$ contributes no
interval. Otherwise define

$$
\alpha=\arccos\left(\frac{d}{2r}\right).
$$

Exactly the center angles in the closed interval
$[\phi-\alpha,\phi+\alpha]$ cover $q$. Closed endpoints are important because
darts on the circumference count.

**Find the maximum overlap on a circular angle axis**

Create a start and end event for every valid interval. Angles wrap modulo
$2\pi$, so add both the original interval and a copy shifted by $2\pi$; this
turns boundary-crossing overlap into ordinary overlap somewhere on a line.
The interval width is at most $\pi$, so an interval and its shifted copy cannot
overlap and double-count the same dart.

Sort events by angle, placing starts before ends at equal angles. Begin the
active count at one for the anchor, increment at a start, decrement at an end,
and record the largest count. Start-before-end ordering captures placements
where one interval begins exactly as another ends, correctly including both
boundary darts.

For the fixed anchor, an angle covered by $k$ intervals defines a center that
covers those $k$ darts plus the anchor. Conversely, every board centered at an
angle has exactly the darts whose intervals contain that angle. The sweep thus
finds the best placement with that anchor on the boundary. Since at least one
optimal placement has some covered dart on its boundary and every dart is used
as an anchor, the maximum over all sweeps is the global optimum.

**Control floating-point boundary error**

Distance and inverse-cosine calculations use floating point. Permit a small
tolerance when comparing $d$ with $2r$, and clamp the computed ratio to at
most one before `acos`. These measures preserve mathematically valid diameter
pairs that might otherwise be rejected by a tiny rounding error; they do not
meaningfully enlarge the geometric circle.

## Complexity detail
For each of the $n$ anchors, at most $n-1$ darts generate a constant number of
events. Building them takes $O(n)$ time and sorting them takes
$O(n\log n)$; the sweep itself is linear. Repeating for all anchors gives
$O(n^2\log n)$ time.

Only the event list for one anchor is retained, containing $O(n)$ entries, so
the auxiliary-space bound is $O(n)$.

## Alternatives and edge cases
- **Centers through every point pair:** For each pair within distance $2r$,
  construct its two possible radius-$r$ centers and rescan every dart. This is
  the standard direct geometry method and is correct, but takes $O(n^3)$ time.
- **Enumerate arbitrary grid centers:** Optimal centers need not have integer
  coordinates, so any finite integer grid can miss the answer.
- **One dart:** Return one; any board centered at or near the point covers it.
- **Points farther than the diameter:** They cannot share a board and produce
  no common-center interval.
- **Distance exactly $2r$:** The valid interval collapses to one angle, which
  still represents the unique center halfway between the two darts.
- **Boundary darts:** Use closed intervals and start-before-end event ordering
  so circumference points count.
- **Negative coordinates:** Translation and angle formulas work unchanged.
- **Circular wraparound:** Duplicating intervals with a $2\pi$ shift prevents
  an interval near $-\pi$ from being separated from one near $\pi$.
- **Unique input points:** The contract rules out zero-distance pairs, avoiding
  an undefined direction angle between distinct darts.
