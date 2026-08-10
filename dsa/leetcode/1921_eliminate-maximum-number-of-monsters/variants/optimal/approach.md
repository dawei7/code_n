## General

**Turn each moving monster into an integer deadline**

The weapon can fire at integer times $0,1,2,\ldots$: it is ready immediately, then becomes ready once per minute. A monster at distance $d$ moving at speed $s$ reaches the city at real time $d/s$. Firing at minute $i$ is safe only when the shot happens strictly before that arrival:

$$
i < \frac{d}{s}.
$$

The strict inequality matters. If the monster arrives exactly at minute $i$, the rules say the city is lost before the weapon can fire.

The exact solution avoids floating-point arrival times. It computes

$$
t=\left\lfloor\frac{d-1}{s}\right\rfloor
$$

with `(d - 1) // s`. This $t$ is the last integer minute at which that monster can safely be eliminated. To see the equivalence, a shot at integer minute $i$ is safe exactly when $is<d$. Since both sides are integers, this is the same as $is\le d-1$, which is the same as $i\le\lfloor(d-1)/s\rfloor$. The moving-monster story has therefore become a unit-time scheduling problem: every monster is a one-shot job, and $t$ is its inclusive deadline.

**Handle the earliest deadlines first**

The code constructs all deadlines and sorts them:

`times = sorted((d - 1) // s for d, s in zip(dist, speed))`

After sorting, `times[0]` is the most urgent monster, `times[1]` is the next most urgent, and so forth. The monster at sorted index `i` would be the $(i+1)$-st target and would be shot at minute `i`. It can still be shot if `times[i] >= i`. If `times[i] < i`, its last safe minute has already passed, so the code returns `i`: exactly `i` earlier monsters were eliminated at minutes $0$ through $i-1$.

For example, suppose the sorted deadlines are `[0, 2, 2]`. The first target is safely shot at minute $0$. The second is safely shot at minute $1$, and the third at minute $2$. All three are eliminated. By contrast, for `[0, 0, 1, 2]`, index $0$ succeeds, but at index $1$ the next deadline is $0<1$. The second monster reaches the city before the minute-$1$ shot, so only one elimination is possible.

**Why sorting by deadline is optimal**

Consider any schedule that fires at one monster per minute. If it ever shoots a later-deadline monster before an earlier-deadline monster, swap those two shots. The earlier-deadline monster moves to an earlier time, which cannot hurt it. The later-deadline monster moves to the former time of the more urgent monster; because its deadline is at least as large, it is also still safe whenever the earlier-deadline monster was safe there. Repeating such swaps produces sorted-deadline order without reducing the number of successful shots.

Now suppose sorted position $i$ has `times[i] < i`. Among the first $i+1$ most urgent monsters, every deadline is at most `times[i]` and therefore below $i$. There are only $i$ firing slots before minute $i$, namely minutes $0$ through $i-1$, but $i+1$ monsters would need those slots. At least one must reach the city. No different ordering can rescue the schedule. Returning `i` is therefore not merely reporting failure of this chosen order; it is the maximum achievable number.

If the loop never finds a missed deadline, each sorted monster is shot by its own deadline. The function then returns `len(times)`, meaning all monsters can be eliminated.

**Why integer deadlines are safer than division**

Using `d / s` creates floating-point values. The constraints are small enough that common implementations may behave correctly here, but exact integer arithmetic communicates the boundary rule directly and cannot round a value that should be exactly integral. The subtraction by one is not an arbitrary trick: it encodes the “arrival at the same moment is already too late” rule.

## Complexity detail

Let $N$ be the number of monsters.

`zip(dist, speed)` visits the corresponding distance and speed once for each monster, and the generator computes $N$ integer deadlines in $O(N)$ time. Python's `sorted` materializes and sorts those $N$ values in $O(N\log N)$ time. The final scan stops at the first impossible deadline or visits every deadline, costing at most $O(N)$. Sorting dominates, so total time is $O(N\log N)$.

The sorted list contains $N$ deadline integers, requiring $O(N)$ space. Python's sorting implementation may also use $O(N)$ temporary memory in the worst case. The generator itself is lazy, so it does not create a second full deadline list before `sorted` consumes it. The scan uses constant additional scalar state.

## Alternatives and edge cases

- **Floating-point arrival times:** Sorting `d / s` and failing when the arrival time is at most the shot minute follows the same idea, but integer deadlines express the strict boundary exactly and avoid rounding concerns.
- **Min-heap:** All arrival deadlines can be heapified and removed from earliest to latest. This still uses $O(N)$ space and up to $O(N\log N)$ time, with more per-element overhead than sorting a list.
- **Counting deadlines:** Under bounded input values, deadlines could be bucketed and processed by minute. That can avoid comparison sorting, but it depends on the numeric constraints and is less direct than the robust sort.
- **Nearest current distance first:** Distance alone is insufficient because speed changes urgency. A farther but much faster monster may arrive sooner.
- **Fastest speed first:** Speed alone is also insufficient because initial distance matters. The ratio, represented by the exact deadline, is the relevant quantity.
- **Arrival exactly at a firing minute:** If $d$ is divisible by $s$ and the monster arrives at minute $q=d/s$, its last safe shot is $q-1$. The formula `(d - 1) // s` produces exactly that value.
- **Arrival between firing minutes:** If arrival is, for example, $2.5$, minute $2$ is safe and minute $3$ is too late. The deadline formula produces $2$.
- **Several monsters with the same deadline:** Sorting keeps them adjacent. If there are more such urgent monsters than available firing slots, the first index that exceeds that shared deadline correctly detects the unavoidable loss.
- **Monster reachable before minute one:** Any monster with $d\le s$ has deadline $0$. One such monster can be shot immediately; if two or more have deadline $0$, only one can be eliminated before another arrives.
- **One monster:** The weapon is ready at minute $0$, while positive distance guarantees a positive arrival time. Its deadline is at least $0$, so the function returns $1$.
- **All monsters schedulable:** If every sorted deadline satisfies `t >= i`, the loop completes and returns $N$ rather than needing a separate simulation of movement.
