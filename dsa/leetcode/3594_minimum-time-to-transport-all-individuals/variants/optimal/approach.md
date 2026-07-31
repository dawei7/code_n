## General

At every moment when the boat is ready at the base, the future is determined by two values: the bitmask of people still at the base and the current environmental stage. The precise history is irrelevant. Treat each such pair as a graph vertex.

From state `(mask, stage)`, choose any nonempty submask `group` of at most `k` people. Its forward duration is the largest neutral time in `group` multiplied by `mul[stage]`; precomputing the largest time for every submask makes this lookup constant-time. Advance the stage by the floored duration and remove `group` from `mask`.

If the remaining mask is zero, that forward trip reaches a terminal state. Otherwise, the boat must return. Every person outside the remaining mask is currently at the destination and is a legal returner, including people delivered on earlier trips. For each possible returner, add that person's stage-adjusted return duration, advance the stage again, and put the returner's bit back into the base mask. This combined forward-and-return choice is one directed edge between base-ready states.

Every edge duration is positive. The state graph contains cycles because a return can recreate an earlier mask at a different or identical stage, so ordinary acyclic subset DP is invalid. Dijkstra's algorithm settles states in increasing elapsed time; the first settled zero-mask state is therefore the globally minimum completion time.

When `k == 1` and more than one person exists, every nonfinal forward traveler must immediately return with the only boat, so the instance is impossible.

## Complexity detail

Let $n$ be the number of people and $m$ the number of stages. There are

$$
V = m2^n
$$

mask-stage states. Across all masks, enumerating forward submasks is bounded by $3^n$. A forward choice can pair with at most $n$ destination returners, so the number of generated transitions is $E = O(mn3^n)$. Binary-heap Dijkstra consequently takes

$$
O\bigl(mn3^n\log(m2^n)\bigr)
$$

time. The distance table and subset-maximum table use $O(m2^n)$ space. Because a standard duplicate-entry heap can retain stale improvements, the conservative worst-case auxiliary-space bound is $O(E)=O(mn3^n)$; transitions themselves are generated lazily rather than stored as adjacency lists.

Adding a tiny tolerance before converting a mathematically integral floating duration to an integer prevents binary representation error from advancing one stage too few.

## Alternatives and edge cases

- **Boat-side state graph:** Modeling forward and return crossings as separate vertices is also correct, but doubles the state dimension and exposes more intermediate states; combining a mandatory return into one edge is smaller.
- **Subset DP without shortest paths:** Masks can repeat after returns, so there is no topological order and a one-pass recurrence can miss cheaper cyclic routes.
- **Breadth-first search:** It minimizes the number of trips, not the weighted elapsed time; stage multipliers make edge durations unequal.
- **Greedy fastest returner:** The quickest immediate return can lead to a worse future stage, so every person at the destination must remain eligible.
- **Final crossing:** Once the base mask becomes zero, no return trip is taken.
- **Capacity one:** More than one person is impossible, while a singleton finishes in one forward trip.
- **Stage advancement:** Apply $\lfloor d\rfloor \bmod m$ after each direction separately, using the newly reached stage for the return.
- **Floating comparison:** Expected answers require tolerance-based comparison, while distance relaxations still compare the accumulated values directly.
