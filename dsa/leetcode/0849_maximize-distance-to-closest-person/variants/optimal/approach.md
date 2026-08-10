## General

**Every empty seat lies in one of three gap types**

Occupied seats divide the row's empty seats into:

- a leading gap before the first occupied seat;
- internal gaps between two occupied seats;
- a trailing gap after the last occupied seat.

The best distance formula differs at the ends because an end gap has a person on only one side. Scanning occupied-seat indices is enough to measure all three types.

**Track first, last, and largest occupied-to-occupied gap**

`first` stores the first occupied index encountered. `last` stores the most recent occupied index. Both begin as `None`.

When a new occupied seat at index `i` is found:

- if `last` exists, `i-last` is the distance between consecutive occupied seats; `d` retains the maximum such distance;
- if `first` is still `None`, set it to `i`;
- update `last=i`.

Only occupied seats matter as boundaries. Runs of zeroes need no per-run counter because their length follows from adjacent occupied indices.

**Leading gap**

If the first occupied seat is at index `first`, seats 0 through `first-1` are empty. Sitting at index 0 maximizes distance within this gap, and the nearest person is `first` seats away.

Thus, the leading candidate is simply `first`.

For `[0,0,1]`, `first=2` and the best leading distance is two.

**Trailing gap**

If the last occupied seat is at index `last`, the final index is `len(seats)-1`. Sitting at that final seat gives distance:

`len(seats) - last - 1`.

For `[1,0,0,0]`, `last=0` and this candidate is three.

**Internal gap**

Suppose consecutive occupied seats are at indices `L` and `R`, with distance `D=R-L`. Any empty seat between them has closest-person distance:

$$
\min(i-L,R-i).
$$

This is maximized at the middle. The best integer distance is:

$$
\left\lfloor\frac{D}{2}\right\rfloor.
$$

Variable `d` stores the largest `D` across all internal gaps, so the best internal candidate is `d // 2`.

If `D` is even, there is one central seat at equal distance from both people. If `D` is odd, the two middle seats have distances differing by direction but the same minimum `\lfloor D/2\rfloor`.

**Take the best of the three categories**

The final return is:

`max(first, len(seats) - last - 1, d // 2)`.

The contract guarantees at least one occupied seat, so `first` and `last` are not `None` after the scan. It also guarantees an empty seat, so at least one category supplies a positive feasible distance.

**Trace the main example**

For `[1,0,0,0,1,0,1]`:

- `first=0`, so leading distance is zero;
- consecutive occupied gaps are 4 and 2, so `d=4` and internal candidate is 2;
- `last=6` in a length-seven row, so trailing distance is zero.

The maximum is two, achieved by sitting at index 2 between occupied indices 0 and 4.

**Why only consecutive occupied seats matter**

Within an internal gap, the closest people to any empty seat are the occupied seats immediately bounding that gap. Any other occupied seat lies even farther outside one boundary and cannot reduce the distance below the nearer boundary.

At a leading or trailing gap, the nearest person is the first or last occupied seat respectively. Therefore, the three formulas consider the true closest person for every possible empty seat.

Every empty seat belongs to exactly one gap category. The computed candidate is the best within that category, so their maximum is the global optimum.

This classification is exhaustive even when a gap contains just one empty seat.

## Complexity detail

Let `n = len(seats)`. The algorithm scans the array once and performs constant work at occupied positions. Time complexity is `O(n)`.

It stores only `first`, `last`, `d`, and loop variables, so auxiliary space is `O(1)`.

No secondary distance array or list of occupied indices is required.

## Alternatives and edge cases

- **Distance array from two passes:** Compute nearest occupied distance from left and right for every seat. It is linear-time but uses `O(n)` space.

- **Store all occupied indices:** Then inspect gaps. It works but the running `first`, `last`, and `d` values are sufficient.

- **Expand from every empty seat:** Searching outward separately can become quadratic.

- **Leading empty run:** Its best seat is index zero, not its midpoint, because no person lies to the left.

- **Trailing empty run:** Its best seat is the final index for the same one-sided reason.

- **Internal even distance:** The exact midpoint achieves `D/2`.

- **Internal odd distance:** Either middle seat achieves `D//2` to its closest person.

- **Adjacent occupied seats:** `D=1` contributes zero internal seating distance because no empty seat lies between them.

- **Only one occupied seat:** `d` remains zero; leading and trailing candidates correctly choose the farther end.

- **Occupied seat at each end:** Only internal gaps can produce the answer.

- **Guaranteed empty seat:** The result is never forced to describe sitting in an occupied position.

- **Input immutability:** The seat array is scanned and not modified.
