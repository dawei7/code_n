## General

For a proposed elapsed time $x$, a bus whose trip time is $v$ completes

$$
\left\lfloor\frac{x}{v}\right\rfloor
$$

whole trips. Trips that have started but not finished do not count. Since buses operate independently, summing this quantity across all buses gives the total number completed by time $x$.

That total never decreases as $x$ grows. The exact solution uses `bisect_left` as a binary search over possible times to locate the first $x$ whose total reaches `totalTrips`.

**Define the monotone production function**

The key function is

`lambda x: sum(x // v for v in time)`.

For each bus time `v`, integer division counts its completed trips. The generator visits every bus and `sum` combines their independent work.

If time increases from $x$ to $x+1$, no quotient `x // v` can decrease. Therefore the total production function is nondecreasing. All times before some boundary are insufficient, and every time at or after that boundary is sufficient.

This monotonic boundary is what makes binary search valid.

**Choose a guaranteed upper bound**

Let `min(time)` be the duration of the fastest bus. That bus alone can complete `totalTrips` trips in

`mx = min(time) * totalTrips`

time. Other buses can only add more completed trips, so the true minimum is at most `mx`.

Time zero is a natural lower endpoint: it completes zero trips and is insufficient because `totalTrips >= 1`.

**Search a lazy range of times**

`range(mx)` represents integers zero through `mx - 1` without storing them all. For a range beginning at zero with step one, each value equals its positional index.

The call

`bisect_left(range(mx), totalTrips, key=production)`

conceptually examines the nondecreasing sequence

`production(0), production(1), ..., production(mx - 1)`

and returns the first index whose keyed value is at least `totalTrips`.

Because range values equal indices, the returned insertion index is also the corresponding elapsed time.

**Why excluding `mx` from the range is still safe**

Python ranges exclude their stop value, so `range(mx)` does not contain `mx`. If the first sufficient time is smaller than `mx`, `bisect_left` finds that value normally.

If the fastest-bus bound itself is the first sufficient time, then every keyed element inside the range is below the target. `bisect_left` returns the insertion position after all `mx` elements, which is integer `mx`. That return value is exactly the missing boundary time.

Thus the half-open range still represents the closed search interval from zero through `mx` via its possible insertion positions.

**Understand `bisect_left` with a key**

The target `totalTrips` is compared against keyed range elements. The key is applied to candidate times, not to the target.

At each binary-search step, the library evaluates production at a midpoint. If it is below the target, every earlier time is also insufficient and the lower half is discarded. Otherwise the midpoint may be the first sufficient time, so the search keeps it and discards only later candidates.

The “left” variant returns the earliest position meeting the threshold, not merely any sufficient time.

**Why the returned time is minimal**

Let $T$ be the returned insertion position. Binary search guarantees every represented time below $T$ has production below `totalTrips`, while the boundary at $T$ has production at least the target. The upper-bound argument covers the special returned endpoint `mx`.

So $T$ is sufficient and $T-1$ is insufficient whenever $T>0$. This is exactly the definition of the minimum required time.

For `time = [1,2,3]` and five trips, production at two is $2+1+0=3$, while production at three is $3+1+1=5$. The first threshold crossing is three.

**Why simultaneous completions are handled naturally**

Several buses may finish trips at the same time. The production sum includes every quotient independently, so all completions at the boundary are counted. The requirement says “at least” the target, so overshooting on that time is allowed.

## Complexity detail

Let $n$ be the number of buses and $U=\min(\texttt{time})\cdot\texttt{totalTrips}$. Binary search performs $O(\log U)$ key evaluations. Each evaluation scans all $n$ bus times and performs integer division, so total time is $O(n\log U)$.

`range(mx)` is a constant-size range object rather than an array of $U$ integers. The generator inside `sum` is consumed lazily. Apart from scalar binary-search state, auxiliary space is $O(1)$.

The manifest's $O(n\log U)$ time and $O(1)$ space match the exact implementation.

## Alternatives and edge cases

- **Explicit binary-search loop:** Maintain `left` and `right` and test midpoints manually. It has the same bound and may be more portable than keyed `bisect_left`.
- **Use a slower-bus upper bound:** `max(time) * totalTrips` is also safe but creates a wider search interval than the fastest-bus bound.
- **Simulate completion events:** A heap can generate trips chronologically but may process up to `totalTrips` events, far too many at $10^7$.
- **One bus:** The answer is exactly its trip time times `totalTrips`, and the insertion-at-`mx` behavior handles it.
- **One required trip:** Binary search finds the fastest bus's first completion.
- **Equal bus times:** Their quotient contributions add, correctly representing parallel work.
- **More than the target:** A time is feasible as soon as the sum is at least the target; exact equality is unnecessary.
- **Time zero:** It is included as a candidate production value but can never satisfy a positive target.
- **Half-open range:** If the answer equals `mx`, the returned insertion position is still `mx` even though it is not an element.
- **Large upper bound:** The lazy range avoids allocating memory proportional to time.
- **No overflow in Python:** Products and trip totals may be large, but Python integers expand automatically.
- **Input preservation:** The bus-time list is only scanned and never sorted or modified.
- **No early cutoff:** The exact lambda sums every bus even after reaching the target; an explicit predicate could stop early to improve constants.
