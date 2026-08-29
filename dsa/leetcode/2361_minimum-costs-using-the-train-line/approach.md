## General

**Why one cheapest cost per stop is not enough**

At every stop, a traveler may be on the regular route or the express route. Two paths with the same cost but different current routes are not interchangeable: entering express from regular costs `expressCost`, staying on express costs nothing extra, and moving from express to regular is free. The current route changes the price of future choices.

Dynamic programming therefore keeps two states for every stop:

- `f[i]` is the minimum cost to reach stop `i` while being on the regular route.
- `g[i]` is the minimum cost to reach stop `i` while being on the express route.

Once those two minimum costs are known at stop `i - 1`, the exact path taken before that stop no longer matters. All future charges depend only on the current stop and route. This is the optimal-substructure property that makes the two-state DP complete.

**Base states**

The traveler begins at stop `0` on the regular route for free, so `f[0] = 0`. The solution initializes all entries of `g` to infinity, including `g[0]`. This represents that its state model has not already transferred to express at stop zero.

That choice is slightly different from a formulation that sets `g[0] = expressCost`. Both formulations are equivalent when transitions are written consistently. In the exact code, entering express from `f[0]` while traveling to stop one adds `expressCost` then. In other words, the transfer fee is delayed until the first express segment rather than stored as a reachable express state at stop zero.

**Transition into the regular route**

Suppose `a` is the cost of the current regular segment from stop `i - 1` to stop `i`. The traveler can take it after arriving at the previous stop on either route:

$$
f[i]=\min(f[i-1]+a,\;g[i-1]+a).
$$

No transfer charge appears in the second option because moving from express back to regular is free. Both terms add the same segment cost, but the code retains the explicit alternatives:

```python
f[i] = min(f[i - 1] + a, g[i - 1] + a)
```

This state is the cheapest path whose final segment is regular.

**Transition into the express route**

Let `b` be the express segment's cost. If the traveler was regular at the previous stop, they must pay the transfer fee before using express. If they were already express, no additional transfer is needed:

$$
g[i]=\min(f[i-1]+\textit{expressCost}+b,\;g[i-1]+b).
$$

The transition deliberately considers paying `expressCost` more than once over a complete trip. A path may leave express for regular at no cost and later enter express again; each later regular-to-express transition must pay the fee again.

**Producing the answer for every stop**

The problem counts a stop as reached from either route. Therefore, after computing both states at stop `i`, the output for that stop is

$$
\min(f[i],g[i]).
$$

The implementation stores this at `cost[i - 1]` because the DP arrays include stop zero at index zero, whereas the returned length-$n$ array begins with the answer for stop one.

The loop uses

```python
enumerate(zip(regular, express), 1)
```

so `i` starts at one while `a` and `b` are the paired segment costs from the two zero-indexed Python input arrays. On iteration `i`, those values describe travel from stop `i - 1` to `i`. `zip` is safe because the contract guarantees equal array lengths.

**Why the transitions are exhaustive and correct**

Consider any cheapest path ending on regular at stop `i`. Its last movement must use the regular segment from `i - 1`. Immediately before that segment, the traveler was either regular or express; there is no third route. The two terms defining `f[i]` cover exactly those possibilities, apply the correct transfer rule, and choose their cheaper cost.

The same argument holds for a path ending on express. It must use the express segment, and its previous state is either regular, requiring the fee, or express, not requiring it. Thus the formula for `g[i]` considers every possible final transition and no illegal one.

By induction, assume `f[i-1]` and `g[i-1]` are the true minimum costs for their states. Replacing a prefix in any candidate path with the corresponding minimum prefix cannot make the path more expensive or change the route at the transition point. The formulas therefore produce the true state minima at `i`. The base state is correct, so the claim holds for all stops. Taking the smaller state cost then gives the true route-independent cost requested for each stop.

For the second example, the first express state is obtained from `f[0] + 3 + 7 = 10`. At a later stop, switching freely to regular may make `f` cheaper. If express becomes attractive again, the formula from `f` adds another `3`, faithfully enforcing the repeated-transfer rule.

## Complexity detail

Let $n$ be the number of segments, which is also the length of each input array and the number of requested output entries. The loop processes each paired regular/express segment exactly once and performs a constant number of additions, comparisons, and assignments. Time complexity is $O(n)$.

The arrays `f` and `g` each contain $n+1$ numeric entries, and `cost` contains $n$ entries. Including the returned result, the implementation uses $O(n)$ space, matching the variant manifest. If output storage is excluded from auxiliary-space analysis, the two DP arrays still make auxiliary usage $O(n)$.

Only the previous values of `f` and `g` are needed to compute the next stop. The exact code retains all state values, but it could reduce auxiliary state to two scalars without changing the recurrence.

## Alternatives and edge cases

- **Two scalar DP states:** Keep only the previous regular and express minima and append each answer. This reduces auxiliary state excluding output to $O(1)$ while preserving $O(n)$ time.
- **Shortest path on a layered graph:** Represent each stop-route pair as a vertex and transitions as weighted edges. A general shortest-path algorithm works but obscures the simple left-to-right acyclic structure and adds overhead.
- **Greedy choice of the cheaper current segment:** It can fail because paying the transfer fee now may enable several cheap express segments, while leaving express changes future fees. Both route states must be preserved.
- **One segment:** The result is the smaller of the direct regular cost and `expressCost + express[0]`, exactly as the first transitions compute.
- **Express is always cheaper per segment:** Entering it may still be unattractive for a short prefix because of the fee; the DP includes that fee at the precise entry transition.
- **Switching back to regular:** The `g[i-1] + a` option contains no fee, correctly modeling a free express-to-regular transfer.
- **Re-entering express:** The `f[i-1] + expressCost + b` option charges the fee each time, even if the path used express earlier.
- **Equal state costs:** Either predecessor is valid; only the minimum numeric cost is required, not the actual route.
- **Large totals:** Python integers grow as necessary, so accumulating up to many large segment costs does not overflow.
