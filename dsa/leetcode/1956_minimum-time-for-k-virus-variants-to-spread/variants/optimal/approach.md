## General
**Turn spreading time into distance**

After $d$ days, a variant has reached exactly the grid points whose Manhattan
distance from its origin is at most $d$. Therefore, at a fixed candidate point,
the first day when `k` variants are present is the $k$-th smallest Manhattan
distance from that point to the $N$ origins.

**Restrict the infinite grid**

An optimal meeting point can be chosen within the origins' axis-aligned
bounding box. If its horizontal coordinate lies left or right of that box,
projecting it to the nearest boundary does not increase its distance to any
origin; the same argument applies vertically. It is therefore sufficient to
enumerate the $XY$ integer points in the bounding box.

For each candidate, compute and sort all $N$ Manhattan distances, then inspect
the value at index `k - 1`. Minimizing that value over all candidates gives a
point reached by `k` variants on the reported day. No earlier day can work,
because every candidate's $k$-th distance is at least this global minimum and
points outside the box cannot improve it.

## Complexity detail
There are $XY$ candidate points. Computing their distance lists takes $O(N)$
per candidate and sorting takes $O(N\log N)$, for $O(XYN\log N)$ time. A
single distance list contains $N$ integers, so the auxiliary space is $O(N)$.
Here $X,Y\le100$ and $N\le50$ under the contract.

## Alternatives and edge cases
- **Transformed-coordinate sweep:** Mapping $(x,y)$ to $(x+y,x-y)$ turns
  Manhattan diamonds into axis-aligned squares. Binary search plus a sweep can
  reduce dependence on the coordinate box, but requires more intricate
  overlap and parity handling.
- **Simulate daily spreading:** Expanding every variant's infected region
  duplicates a rapidly growing amount of state and is unnecessary because
  Manhattan distance gives each arrival day directly.
- Distinct variants that start at the same coordinate already coexist on day
  zero and must be counted separately.
- The answer depends on the `k`-th nearest origin, not necessarily on all $N$
  variants reaching the same point.
- Meeting points are integer grid coordinates; a geometric midpoint with
  fractional coordinates is not a valid candidate.
