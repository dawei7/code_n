## General
**Turn each endpoint into a dynamic-programming state.** Group requests by
their ending point. Let `best[x]` be the greatest earnings possible after
reaching road point `x`. Moving without a passenger preserves the previous
value, so begin each state with `best[x] = best[x - 1]`.

**Evaluate every ride exactly when it becomes available.** For a request
`[start, x, tip]` ending at `x`, the best compatible history is already stored
at `best[start]`. Taking that ride produces
`best[start] + x - start + tip`. Maximize `best[x]` over the carry-forward
choice and every request ending there.

All transitions come from points no later than the current endpoint. By
induction, `best[start]` already represents the optimal compatible sequence
before a considered ride begins. The transition appends that ride without
overlap, including the permitted case where one ride ends exactly at
`start`. Conversely, every valid optimal sequence either takes no ride ending
at `x` or has some final ride ending there, so one of the evaluated choices
reconstructs its value. Thus `best[n]` is optimal.

## Complexity detail
Here $N=n$ is the number of road positions and $R$ is the number of requests.
Creating the endpoint groups takes $O(N+R)$ space. The scan visits $N$ points
and processes each ride once, taking $O(N+R)$ time. The dynamic-programming
array and grouped rides use $O(N+R)$ space.

## Alternatives and edge cases
- **Sort rides plus binary search:** Weighted interval scheduling over rides
  sorted by endpoint takes $O(R\log R)$ time and $O(R)$ space, which can avoid
  scanning unused road points but does not meet the requested linear bound.
- **Compare every pair of rides:** A direct compatibility transition over all
  earlier requests takes $O(R^2)$ time.
- Rides may share an endpoint; a drop-off and pickup at the same point are
  compatible.
- Skipping road segments earns nothing but may be necessary before a later,
  more profitable request.
- Earnings can exceed 32-bit integer range across many rides, so the result
  must retain the platform's wide integer value.
