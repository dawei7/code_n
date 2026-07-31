## General

**Bound the useful life of every tire**

Let $m$ be the fastest first-lap time among all tire types. Suppose the next
lap on the current tire would take more than
$\texttt{changeTime}+m$ seconds. Changing to a fresh fastest tire before that
lap is strictly quicker. No optimal schedule therefore needs a stint extending
through such a lap.

For each pair `[f, r]`, generate its consecutive lap times
$f,f r,f r^2,\ldots$ only while that bound holds. Record in
`best_stint[k]` the cheapest total time for exactly $k$ consecutive laps on one
tire. Because every ratio is at least $2$, the useful stint length $L$ is
small even at the largest legal values.

**Compose complete stints**

Let `best_total[i]` be the minimum time for the first $i$ laps. If the final
stint has length $k$, its cost is `best_stint[k]`; when earlier laps exist, one
tire change separates the two stints. Trying every useful $k$ gives

$$
D(i)=\min_{1\le k\le\min(i,L)}
\left(D(i-k)+\texttt{changeTime}+B(k)\right).
$$

Initialize `best_total[0]` to `-changeTime`. The recurrence then cancels the
otherwise-added change delay for the first stint, exactly matching the rule
that the race may start on any tire for free.

Every legal schedule partitions into consecutive single-tire stints, and the
precomputation uses the cheapest possible tire for each stint length. The
recurrence considers the final stint of every such partition, so it cannot
miss an optimum. Conversely, every transition represents a valid earlier
schedule, one permitted tire change, and one realizable stint. Its minimum is
therefore both attainable and optimal.

## Complexity detail

Each of the $T$ tire types is extended through at most $L$ useful laps.
Precomputation takes $O(TL)$ time. The dynamic program tries at most $L$ final
stints for each of $N$ lap counts, taking $O(NL)$ time. The two arrays occupy
$O(N+L)$ space.

## Alternatives and edge cases

- **Quadratic partition dynamic programming:** Precompute every possible stint
  length and try all previous split points. It is correct, but takes
  $O(TN+N^2)$ time instead of exploiting geometric degradation.
- **State by tire and wear:** Track the chosen tire type and consecutive-lap
  count after every completed lap. This retains many dominated states and can
  require $O(TN^2)$ work.
- A one-lap race uses the tire with the smallest `f` and pays no change cost.
- Changing to a fresh copy of the same tire type is allowed.
- A very large `changeTime` can make several consecutive laps preferable even
  though their individual times increase.
- Equality at the pruning boundary is harmless: keeping the tire and changing
  are tied for that next lap.
- Intermediate geometric lap times and total race times should use an integer
  type wide enough to avoid overflow.
