## General

**Turn a candidate time into a monotone decision**

By elapsed time $x$, a bus with duration $d$ has completed
$\lfloor x/d\rfloor$ trips. The combined count is therefore

$$
F(x)=\sum_{d\in\texttt{time}}\left\lfloor\frac{x}{d}\right\rfloor.
$$

As $x$ increases, $F(x)$ never decreases. The predicate
$F(x)\ge\texttt{totalTrips}$ is consequently false before some boundary and
true from that boundary onward.

**Binary-search the first feasible time**

Time `1` is the smallest positive candidate. The fastest bus can complete all
required trips alone by
$U=\min(\texttt{time})\cdot\texttt{totalTrips}$, so `U` is a valid upper
bound. Binary-search this inclusive range: keep the midpoint when it is
feasible, otherwise discard it and everything below it.

The maintained interval always contains the first feasible time. A feasible
midpoint cannot prove any larger answer minimal, while an infeasible midpoint
proves that no earlier time works. When the bounds meet, the remaining value
is feasible and every smaller value has been excluded, making it the required
minimum.

## Complexity detail

Let $n=\lvert\texttt{time}\rvert$. Each feasibility check scans at most $n$
buses, and binary search performs $O(\log U)$ checks. Total time is
$O(n\log U)$. The bounds and running trip count use $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Advance time one unit at a time:** Recompute completed trips until the
  target is reached. It is correct but takes $O(nU)$ time in the worst case.
- **Event priority queue:** Repeatedly schedule the bus whose next completion
  occurs first. This takes $O(\texttt{totalTrips}\log n)$ time and becomes
  expensive for a large target.
- With one bus, the answer is its duration multiplied by `totalTrips`.
- Several buses can finish trips at the same instant; all those trips count.
- The answer may be much larger than 32-bit range.
- Reaching more than `totalTrips` at the minimum time is valid.
- The feasibility sum may stop early once it reaches the target.
