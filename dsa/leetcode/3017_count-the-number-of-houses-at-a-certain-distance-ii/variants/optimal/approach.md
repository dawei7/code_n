## General

**Expose the cycle and tails.** First order the endpoints so $x\le y$. If $y-x\le1$, the extra road does not improve the original chain, whose distance-$d$ count is simply $2(N-d)$.

Otherwise, houses from $x$ through $y$, together with the extra road, form a cycle of length

$$
C=y-x+1.
$$

There are $L=x-1$ houses in the left tail and $R=N-y$ in the right tail. Count unordered pairs by distance, then multiply every total by two because the required pairs are ordered.

**Pairs confined to one region.** A tail plus its cycle endpoint is a path. At distance $d$, the left path contributes $L+1-d$ pairs when $1\le d\le L$, and the right path contributes $R+1-d$. Within the cycle, every distance below $C/2$ has $C$ unordered pairs. When $C$ is even, its antipodal distance $C/2$ has only $C/2$ pairs.

**Pairs joining a tail to the cycle.** A cycle vertex at cycle distance $c$ from a tail endpoint has two choices, except the unique antipodal vertex of an even cycle. Combining it with tail depth $t$ produces distance $c+t$. For fixed $c$, all tail depths form one consecutive distance interval, so add the multiplicity to that interval in a difference array. Do this independently for both tails.

**Pairs joining the two tails.** A house at left depth $a$ and one at right depth $b$ use the extra road between the endpoints, giving distance $a+1+b$. For each $a$, the possible right depths again create one consecutive interval, so another range addition accounts for all such pairs.

A prefix sum converts the difference array into per-distance cross-region counts. Adding the direct regional counts covers every unordered pair exactly once: both houses lie in one tail path, both lie on the cycle, one lies on a tail and one elsewhere on the cycle, or they lie on opposite tails. Doubling then gives the required ordered counts.

## Complexity detail

Each tail depth and each relevant cycle distance is processed a constant number of times. The final prefix scan also has length $N$, so the total time is $O(N)$. The distance totals and difference array use $O(N)$ space; the returned length-$N$ answer already requires $\Omega(N)$ output space.

## Alternatives and edge cases

- **Breadth-first search from every house:** This directly computes all shortest paths and is useful as an oracle, but costs $O(N^2)$ time on this sparse graph.
- **Evaluate every unordered pair algebraically:** The distance is the minimum of the chain route and the two routes using the added road. Enumerating all pairs remains $O(N^2)$.
- **Coincident or adjacent endpoints:** When $y-x\le1$, the additional road cannot shorten a route, so the ordinary chain formula applies.
- **Reversed endpoints:** Swapping `x` and `y` leaves the undirected graph unchanged; normalizing them avoids duplicated cases.
- **Even cycle:** Antipodal cycle vertices have only one partner direction, so their multiplicity is one rather than two in tail-to-cycle range updates.
- **Unused distances:** The result still has length $N$ and ends with zeros for distances larger than the graph diameter.
