## General

**Represent available choices as gaps between occupied boundaries**

When some seats are occupied, every available seat lies in a gap between two occupied seats, or between a room boundary and the nearest occupied seat.

The solution represents one gap as tuple `(l,r)`:

- `l` and `r` are occupied seats bounding the gap;
- virtual boundary `-1` represents the space before seat 0;
- virtual boundary `n` represents the space after seat `n-1`.

The available seats in the gap are strictly between `l` and `r`.

Initially, no seat is occupied, so one interval `(-1,n)` represents the whole room.

**Best distance within a gap**

Nested function `dist(x)` calculates the maximum closest-person distance obtainable from interval `(l,r)`.

For a leading interval `(-1,r)`, the best seat is 0 and its distance to the person at `r` is `r`. The formula `r-l-1` becomes `r`.

For a trailing interval `(l,n)`, the best seat is `n-1` and its distance is `n-l-1`, again `r-l-1`.

For an internal interval with occupied endpoints, the best seat is the lower midpoint:

$$
\left\lfloor\frac{l+r}{2}\right\rfloor,
$$

and its distance to the nearer endpoint is:

$$
\left\lfloor\frac{r-l}{2}\right\rfloor.
$$

The function returns `(r-l) >> 1` for this case.

**Keep gaps ordered by the seating rule**

`SortedList` uses key:

`(-dist(x), x[0])`.

Negating distance means a gap with larger achievable distance sorts earlier. If distances tie, smaller left boundary sorts earlier. Its selected seat is also smaller, so this enforces the required lowest-seat tie break.

`self.ts[0]` is therefore always the gap containing the next correct seat.

**Choose and split a gap**

`seat()` selects first gap `s=(l,r)`.

For an internal gap, candidate `p=(l+r)>>1` is the lower midpoint, which gives the lowest index when two central seats tie.

Special cases override it:

- if `l==-1`, choose seat 0;
- if `r==n`, choose seat `n-1`.

The chosen gap is removed, and two new gaps `(l,p)` and `(p,r)` are added. Seat `p` becomes their occupied shared boundary.

These intervals may have no empty seat, such as `(-1,0)`. Their distance is zero, so they cannot win while a genuine seat remains. Keeping them simplifies neighbor bookkeeping.

**Maps make leaving a seat efficient**

To remove occupied seat `p`, we need the occupied boundary immediately to its left and right.

The interval maps encode:

- `left[r]=l` for interval `(l,r)`;
- `right[l]=r`.

The two gaps adjacent to occupied `p` are:

- `(left[p],p)`;
- `(p,right[p])`.

`leave(p)` retrieves `l` and `r` in constant dictionary time, removes both gaps from the sorted structure, and adds merged gap `(l,r)`. This exactly makes `p` available again.

**Why add and delete update both structures**

`add(s)` inserts the gap into `ts` and records both boundary relations.

`delete(s)` removes it from `ts` and deletes the matching map entries. Maintaining these updates together ensures the sorted gaps and neighbor maps always describe the same partition of the room.

**Trace the beginning of a room of size 10**

- Initial gap `(-1,10)` chooses seat 0 and splits into `(-1,0)` and `(0,10)`.
- Trailing gap `(0,10)` has best distance 9, so choose seat 9.
- Internal gap `(0,9)` chooses lower midpoint 4 with distance 4.
- Gaps `(0,4)` and `(4,9)` have best distances 2; smaller left boundary wins, so choose seat 2.

If seat 4 leaves, neighboring gaps `(2,4)` and `(4,9)` merge into `(2,9)`. Its best seat is 5.

**Why the structure is correct**

The intervals partition every currently empty seat according to adjacent occupied boundaries. `dist` and the candidate formula find the rule-optimal seat within each interval.

Ordering compares each interval's best possible distance globally, then its smallest candidate seat. Therefore, the first interval yields the required room-wide choice.

Seating splits exactly the affected gap; leaving merges exactly the two affected gaps. By induction over operations, the interval partition and ordering remain correct.

## Complexity detail

Let `q` be the number of operations performed so far. There are `O(q)` occupied boundaries and gaps.

`SortedList` insertion and removal take `O(\log q)` time. `seat` performs one removal and two insertions; `leave` performs two removals and one insertion. Dictionary operations are expected `O(1)`. Each operation is `O(\log q)`, so `q` calls take `O(q\log q)` time.

The sorted gaps and two neighbor maps store `O(q)` entries, giving `O(q)` space.

Room size `n` may be as large as `10^9`, but storage depends only on calls, not on allocating one entry per seat.

## Alternatives and edge cases

- **Store occupied seats and scan every gap on `seat`:** Leaving is easy, but each seating call can take `O(q)` time.

- **Allocate an array of `n` seats:** Impossible when `n` is up to `10^9` and unnecessary for only `10^4` operations.

- **Priority queue with lazy deletion:** It can choose maximum gaps but needs stale-entry handling and neighbor maps. `SortedList` supports direct deletion.

- **Empty room:** Virtual interval `(-1,n)` chooses seat zero.

- **Only trailing space:** The right boundary `n` makes the best seat `n-1`.

- **Only leading space:** The left boundary `-1` makes the best seat zero.

- **Internal odd-length tie:** Lower midpoint from right shift gives the smaller seat.

- **Equal distances in different gaps:** Smaller left boundary yields the lower candidate seat.

- **Leaving an endpoint seat:** One adjacent interval uses a virtual boundary and merges normally.

- **Guaranteed occupied `p`:** Maps contain both neighbors when `leave(p)` is called.

- **Zero-empty-seat intervals:** They remain ordered with distance zero and simplify consistent merging.

- **External dependency:** The implementation relies on `SortedList` supporting a key function and logarithmic updates.
