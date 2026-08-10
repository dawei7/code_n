## General

**A valid trip is a simple path with exactly `k` edges**

Crossing exactly `k` highways visits exactly `k + 1` cities because no city may repeat. If `k >= n`, the trip would require more than `n` distinct cities. The solution immediately returns `-1` in that impossible case.

For remaining cases, the small bound `n <= 15` allows a bitmask to record visited cities.

**Build undirected weighted adjacency**

Each highway `[a, b, cost]` is added as `(b, cost)` in `g[a]` and `(a, cost)` in `g[b]`. A trip can traverse it in either direction with the same toll.

**Define the dynamic-programming state**

`f[mask][j]` is the maximum toll cost of a simple trip that visits exactly the cities whose bits are set in `mask` and ends at city `j`.

Every city can be a starting point. A trip containing only city `i` crosses no highway and costs zero, so the code initializes

`f[1 << i][i] = 0`.

All other states begin at negative infinity, marking them unreachable. This sentinel is important because a real cost may be zero.

**Remove the endpoint to find a predecessor**

To compute a state ending at `j`, the code considers every neighbor `h` of `j` that is also in `mask`. The previous trip must have visited all current cities except `j` and ended at `h`. Its mask is

`mask ^ (1 << j)`.

Because the code enters this transition only when bit `j` is set, XOR removes that bit. Adding highway `h-j` produces the candidate

`f[mask without j][h] + cost`.

Taking the maximum over neighbors gives the best trip for `f[mask][j]`.

The loop processes masks in increasing numeric order. Removing a set bit produces a smaller integer mask, so every predecessor row has already been computed.

**Why the mask prevents repeated cities**

The predecessor mask excludes endpoint `j`, so the prior trip cannot already contain `j`. Adding it visits `j` for the first time. Every transition grows a simple path by one new endpoint.

Conversely, removing the final city from any valid simple trip yields exactly a smaller valid state of this form. The recurrence covers every possible trip order.

**Collect states of exactly the required length**

A mask with `k + 1` set bits represents `k + 1` visited cities and therefore `k` highways. Whenever `i.bit_count() == k + 1`, the solution compares every endpoint state with `ans`.

Unreachable entries remain negative infinity and cannot raise the initial answer `-1`. Toll costs are nonnegative, so every real trip has cost at least zero and replaces `-1`.

The bit-count test sits outside the endpoint-membership branch, so it also examines entries where `j` is not in the mask. Those entries remain negative infinity; the extra comparisons are harmless.

**Why the recurrence is exact**

Every transition appends a real highway to a reachable path, uses a city not previously in the mask, and adds the correct toll. It therefore constructs only valid trips.

For any valid trip ending at `j`, let `h` be its preceding city. Removing `j` gives a valid predecessor state with the remaining mask and endpoint `h`. The recurrence considers highway `h-j` and can reconstruct the trip. By induction on mask size, `f` stores the maximum cost for every state.

Taking the maximum over all endpoints and masks of size `k + 1` therefore yields the maximum valid trip cost.

**Starting city and direction are unrestricted**

All singleton states are initialized, so trips may begin anywhere. Undirected adjacency permits either direction. The same physical path may be represented in reverse, but duplicate representations do not affect a maximum.

**Trace the state growth**

A singleton mask has cost zero at its sole endpoint. A two-city state becomes reachable only if a highway connects them. A three-city state appends a third city to some reachable two-city endpoint, and so on until `k + 1` cities are present.

Disconnected components naturally remain separate because no transition crosses a missing highway.

## Complexity detail

There are `2^n` masks and `n` possible endpoints. For each state, the code can inspect the endpoint's neighbors. In the worst case the graph is dense, giving `O(n)` neighbors and total time `O(2^n n^2)`.

The DP table contains `2^n n` numeric entries, using `O(2^n n)` space. Adjacency adds `O(n + m)`, dominated by the DP bound for the stated range.

With `n <= 15`, exponential subset DP is intentional and feasible.

## Alternatives and edge cases

- **Depth-first enumerate every simple path:** Without memoization, many prefixes with the same visited set and endpoint repeat equivalent future work.
- **DP only by endpoint and length:** It cannot prevent revisiting a city because it forgets which cities were used.
- **Greedily take the largest toll:** A locally expensive highway can lead to a dead end or force revisiting, so it does not guarantee the best exact-length trip.
- **`k >= n`:** More than `n` distinct cities would be required, so the early `-1` is necessary.
- **No trip of the requested length:** All target-size states remain unreachable and `ans` stays `-1`.
- **Zero-cost highways:** A valid trip can have cost zero and must be distinguished from unreachable negative infinity.
- **Start anywhere:** Singleton initialization covers every possible start.
- **Disconnected graph:** Trips remain within one component; the maximum among feasible components wins.
- **Exact length:** Only masks with `k + 1` cities update the answer; shorter trips are not accepted.
- **No repeated city:** Removing and adding endpoint bits enforces first-time visits.
- **Reverse trip:** It may be represented separately but has the same cost.
- **Negative-infinity arithmetic:** Adding a finite toll to an unreachable sentinel remains unusable and never beats a real state.
