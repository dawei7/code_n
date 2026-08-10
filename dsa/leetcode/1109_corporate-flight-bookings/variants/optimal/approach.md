## General

**A booking adds the same value across an inclusive range**

Booking `[first, last, seats]` contributes `seats` to every flight label from `first` through `last`, inclusive. Updating each flight separately would repeat work when ranges are long.

A difference array records only where a contribution begins and where it stops. Later, one prefix sum reconstructs the total active contribution at every flight.

**Translate one-based flight labels to zero-based indices**

The answer list has indices zero through `n - 1`, while flights are labelled one through `n`. Therefore, a booking begins at array index `first - 1`. The update:

`ans[first - 1] += seats`

means that every prefix sum from this point onward includes the booking.

**Cancel immediately after the inclusive endpoint**

The booking must remain active through flight `last` and disappear before flight `last + 1`. In zero-based indexing, flight `last + 1` corresponds to array index `last`. Thus:

`ans[last] -= seats`

marks the cancellation.

When `last == n`, there is no array position after the final flight. The booking should remain active through the end, so no cancellation entry is needed. The guard `if last < n` prevents an out-of-range write and expresses exactly that boundary.

**Accumulate all booking effects**

Updates from different bookings add in the same difference array. Addition is commutative, so input order does not matter and overlapping ranges naturally combine.

`accumulate(ans)` produces prefix sums. At output index `i`, a booking contributes seats exactly when its start update has been encountered but its cancellation has not. That condition is equivalent to:

`first - 1 <= i < last`,

or in flight labels, `first <= i + 1 <= last`. Therefore, each prefix value is precisely the total seats reserved for that flight.

The function converts the accumulator iterator to a list because the contract requires an array result.

**Walk through a concrete overlap**

For bookings `[1,2,10]` and `[2,3,20]` with three flights, the first writes plus ten at index zero and minus ten at index two. The second writes plus twenty at index one and has no cancellation because it ends at flight three.

The difference array is `[10,20,-10]`. Prefix sums are ten, thirty, and twenty. Flight two receives both bookings, while flights one and three receive only their respective range contribution.

**Why the method is correct**

For one booking, its start marker makes the running total increase by seats at the first included flight, and its cancellation makes the running total decrease by the same amount immediately after the last included flight. It therefore contributes exactly on its requested inclusive interval.

Prefix summation is linear, so summing markers for all bookings is equivalent to summing every booking’s individual contribution at each flight. Hence every returned position contains exactly the required total.

This equivalence follows from distributivity: taking a prefix sum after adding all boundary arrays gives the same value as prefix-summing each booking’s boundary array and then adding their per-flight results. The algorithm merely changes the order of additions, not which reservations contribute.

## Complexity detail

Let $B$ be the number of bookings. Recording two constant-time boundary updates per booking costs $O(B)$. Prefix accumulation visits the $n$ flight positions once, costing $O(n)$. Total time is $O(B+n)$.

The difference array and returned result contain $n$ values. In this implementation they share the same underlying list before `accumulate` creates the final list, so peak result-related storage is $O(n)$. Scalar loop variables require constant space.

The algorithm avoids work proportional to the sum of booking-range lengths, which could reach $O(Bn)$ for many full-range bookings.

## Alternatives and edge cases

- **Direct range updates:** Add seats to every covered flight for every booking. It is easy to understand but can require $O(Bn)$ time.
- **Fenwick tree:** Range additions and point queries can solve the problem, but all bookings are known before one final output pass, so a difference array is simpler.
- **Segment tree:** Supports more dynamic query patterns than needed and adds substantial implementation overhead.
- **Booking for one flight:** Start and cancellation are adjacent, so the contribution appears in exactly one prefix value.
- **Booking through flight `n`:** No cancellation slot exists or is needed; the guard skips it.
- **Booking starting at flight one:** The start marker is written at index zero.
- **Overlapping bookings:** Their active contributions add in the prefix total.
- **Identical bookings:** Each input row is a separate reservation and both contributions are counted.
- **Width exactly all flights:** A booking from one through `n` adds once at index zero and remains active to the end.
- **Positive seat counts:** Totals never need special handling for negative reservations; only cancellation markers are negative.
- **Input order:** Boundary additions commute, so sorting bookings is unnecessary.
- **One flight:** Every valid booking covers that flight, and all seat counts accumulate at the sole index.
- **Iterator conversion:** Returning `accumulate(ans)` directly would return an iterator rather than the required list, so `list` is essential.
