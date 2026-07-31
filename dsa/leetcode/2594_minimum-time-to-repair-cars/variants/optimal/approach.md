## General

**Turn a time limit into a capacity test.** Suppose a mechanic has rank $r$ and the available time is $t$. Repairing $x$ cars is possible exactly when $r x^2 \leq t$, so the greatest possible integer $x$ is

$$
\left\lfloor\sqrt{\frac{t}{r}}\right\rfloor.
$$

Summing that quantity over every rank gives the maximum number of cars the whole team can repair by time $t$. Integer square root keeps this test exact even near the largest legal times.

**Binary-search the first feasible time.** The capacity never decreases as $t$ increases. Time zero is a safe lower endpoint, while `min(ranks) * cars * cars` is certainly feasible because the fastest mechanic could repair every car alone. At each midpoint, replace the upper endpoint when the combined capacity reaches `cars`; otherwise discard that midpoint and everything below it. The interval therefore always contains the earliest feasible time and eventually collapses to it.

This returned time is sufficient by the capacity calculation. Its immediate predecessor is insufficient by the first-feasible binary-search invariant, so no smaller answer can repair all cars.

## Complexity detail

Let $m$ be the number of mechanics and $c$ the number of cars. Because every rank is at most 100, the search interval's upper bound is at most $100c^2$, which requires $O(\log c)$ iterations. Each feasibility check scans all $m$ ranks, giving $O(m \log c)$ time. The algorithm stores only a few integer accumulators, so it uses $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Priority-queue scheduling:** Repeatedly assign the next car to the mechanic whose next completion time is smallest. This is correct, but it performs one heap operation per car and costs $O(c \log m)$ time.
- **Floating-point square roots:** Rounding near a perfect square can change a mechanic's capacity by one; integer square root avoids that boundary error.
- **One mechanic:** The result is exactly `ranks[0] * cars * cars`, which also supplies the binary search's universal feasible upper bound.
- **Many simultaneous mechanics:** Capacities must be summed; choosing only the fastest mechanic can substantially overestimate the minimum time.
- **Integer width:** The answer can reach $10^{14}$, so fixed-width implementations need 64-bit arithmetic for time and products.
