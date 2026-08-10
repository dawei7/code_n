## General

**The two journeys must share the stones without reusing interior ones**

The frog travels from the first stone to the last and then returns. Apart from the endpoint needed to turn around and the first stone needed to finish, an interior stone cannot be used on both directions because each stone may be jumped to at most once.

Since positions are strictly increasing, the useful structure is to distribute interior stones between the outward and return journeys. If one direction takes alternating stones, the other direction can take the stones it skipped. Each direction then usually jumps across one intervening stone.

The exact answer is the largest gap between stones two indices apart, with the first adjacent gap included for the two-stone boundary case:

$$
\max\left(
\texttt{stones}[1]-\texttt{stones}[0],
\max_{i=2}^{n-1}
\bigl(\texttt{stones}[i]-\texttt{stones}[i-2]\bigr)
\right).
$$

The code computes exactly this expression in one scan.

**Why two-index gaps are unavoidable**

Consider any three consecutive stones at positions

$$
\texttt{stones}[i-2]
<
\texttt{stones}[i-1]
<
\texttt{stones}[i].
$$

The middle stone cannot serve both the outward and return routes. At least one direction must get from the region at or left of `stones[i-2]` to the region at or right of `stones[i]` without landing on that middle stone as an intermediate stop for that crossing.

That direction must make a jump whose length is at least

`stones[i]-stones[i-2]`.

Therefore, every legal round trip has cost at least every two-index gap, and hence at least their maximum.

The initial adjacent gap `stones[1]-stones[0]` is also unavoidable at the boundary when there are only two stones. For longer arrays it is no larger than `stones[2]-stones[0]`, but initializing with it makes the formula valid uniformly for the minimum length `n=2`.

**Alternating stones attain the lower bound**

Assign alternating interior stones to the two directions. One way to picture it is:

- travel outward through indices `0,2,4,...`, including the final index when needed;
- return through the unused indices in decreasing order, finally reaching index 0.

Depending on whether the number of stones is odd or even, the final stone may sit next to the last alternating outward stone, and the turn into the return sequence may also be adjacent. Adjacent gaps are bounded by a surrounding two-index gap.

Every non-adjacent jump in this construction connects indices differing by two, so its length is one of the values inspected by the loop. No constructed jump exceeds the computed maximum.

The lower bound said no route can do better than that maximum, while the alternating construction achieves a route no worse than it. The two bounds meet, proving optimality.

**Trace the first sample**

For `stones=[0,2,5,6,7]`, the inspected distances are:

- initial gap $2-0=2$;
- $5-0=5$;
- $6-2=4$;
- $7-5=2$.

The maximum is five.

A matching round trip is

`0 -> 5 -> 7 -> 6 -> 2 -> 0`.

Its jump lengths are 5, 2, 1, 4, and 2, so its cost is five. It visits each interior stone once and realizes the lower bound.

**Why taking every stone in one direction is bad**

If the outward journey used every interior stone, the return would have no unused intermediate stones and would require a direct jump from the final stone to the first. Alternating the stones balances the largest gaps across the two directions.

The goal is a bottleneck minimum: only the largest jump matters. The method does not minimize the total traveled distance or the number of jumps.

**Read the loop**

`ans` starts with the first adjacent gap. For every index `i` from two onward, the code compares the current answer with `stones[i]-stones[i-2]`.

Strictly increasing input means these differences are positive, so absolute values are unnecessary for the forward-position formula. The returned maximum is an integer even though the conceptual return journey travels in decreasing order.

The input array is never changed and no route needs to be explicitly constructed.

## Complexity detail

Let $n$ be the number of stones. The loop visits indices 2 through $n-1$ once, performing constant work at each. Time is $O(n)$.

Only `ans` and the loop index are stored, so auxiliary space is $O(1)$.

Stone positions may reach $10^9$, but every difference stays within that range and fits a 32-bit signed integer. Python arithmetic has no overflow concern.

## Alternatives and edge cases

- **Binary search the allowed cost:** Test whether stones can be assigned to two routes under a candidate maximum. It is more complicated and slower than the direct formula.
- **Explicit alternating route arrays:** They demonstrate achievability but consume $O(n)$ space unnecessarily.
- **Two stones:** The frog must jump directly each way, so the sole gap is the answer.
- **Three stones:** One direction may use the middle stone, while the other jumps directly from first to last; the two-index gap is unavoidable.
- **Uneven spacing:** The formula uses actual coordinate differences, not counts of skipped stones.
- **Endpoint parity:** The alternating construction may use an adjacent jump near the final stone; it remains bounded by the computed maximum.
- **Stone reuse:** Interior stones must be distributed between directions rather than used twice.
- **Strict ordering:** It lets the code subtract positions without `abs`.
- **Bottleneck objective:** A route with longer total distance can still be optimal if its largest jump is minimal.
- **No route construction required:** The lower-bound and matching-construction proof justifies returning only the maximum gap.
