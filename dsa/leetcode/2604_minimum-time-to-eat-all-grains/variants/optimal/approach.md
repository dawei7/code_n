## General

**Binary-search a shared completion time**

All hens move simultaneously, so a proposed time $t$ is feasible when the grains can be divided among hens such that each hen can eat its assigned grains within $t$ seconds.

If time $t$ works, every larger time works by following the same routes and optionally waiting. Feasibility is monotone, so the minimum time is the first true value of a binary search.

The helper `check(t)` greedily tests one time limit after both position arrays are sorted.

**Assign consecutive grains from left to right**

Pointer `j` identifies the leftmost grain not yet assigned. Hens are processed from left to right.

An optimal assignment can give each hen a consecutive block of remaining sorted grains. Crossing assignments are unnecessary: if a left hen goes past a grain assigned to a right hen while that right hen travels back for an earlier grain, exchanging their responsibilities cannot increase the maximum travel distance.

Thus each hen should consume the longest feasible prefix beginning at `grains[j]`. This leaves later hens with only later grains and is maximally helpful.

**Case one: the leftmost grain is left of the hen**

Let hen position be $x$, leftmost remaining grain be $y\le x$, and

$$
d=x-y.
$$

The hen must at least travel distance $d$ to reach $y$. If $d>t$, this hen cannot eat the grain. No later hen can either, because later hens stand at positions at least $x$ and are even farther right. The check returns false immediately.

If $d\le t$, every unassigned grain between $y$ and $x$ is eaten along a trip through that interval. The first `while` advances past all grains `<= x`.

**How far right can that hen also travel?**

Suppose the hen also wants to cover a rightmost grain $z>x$. Let $R=z-x$. Starting at $x$, it must cover the entire interval $[y,z]$.

There are two useful route orders:

- go left first to $y$, return through $x$, then continue to $z$, costing $2d+R$;
- go right first to $z$, return through $x$, then continue to $y$, costing $d+2R$.

The minimum is

$$
d+R+\min(d,R).
$$

Since $z-y=d+R$, the code writes this as

`min(d, grains[j] - x) + grains[j] - y`.

While this cost is at most $t$, the next right grain can join the same hen's consecutive block.

**Case two: every remaining grain is right of the hen**

If $y>x$, the hen need not reverse direction. It can walk right and eat every grain through position $z$ in `z - x` seconds.

The loop therefore advances while `grains[j] - x <= t`.

**Why consuming the longest feasible prefix is safe**

For a fixed hen and leftmost remaining grain, any feasible assignment that stops earlier can be extended to every additional grain satisfying the same route bound without hurting that hen. Removing those grains from later hens only reduces their work.

If the next grain does not fit, assigning an even farther grain to this hen cannot fit either. The pointer stops at the exact greedy boundary.

After all hens, feasibility holds exactly when `j == m`.

**Binary-search bounds**

The upper route bound

`abs(hens[0] - grains[0]) + grains[-1] - grains[0]`

lets the first sorted hen travel to the leftmost grain and across the full grain span, eating everything alone. The code adds one to form exclusive range endpoint `r`, so this guaranteed feasible time is included in `range(r)`.

`bisect_left(..., True, key=check)` finds the first feasible integer time.

**Trace the first example**

With sorted hens `[3,6,7]`, grains `[2,4,7,9]`, and $t=2$:

- hen $3$ reaches grain $2$ with $d=1$ but cannot also cover $4$ within the interval-route bound, so consumes $2$;
- hen $6$ reaches $4$ in two seconds;
- hen $7$ starts on grain $7$ and walks right to $9$ in two seconds.

All grains are assigned, so time two is feasible. A smaller time cannot cover the needed gaps.

## Complexity detail

Let $n$ be the number of hens, $m$ the number of grains, and $C$ the searched time bound. Sorting costs $O(n\log n+m\log m)$. In one check, each hen is visited once and pointer `j` advances at most $m$ times, so cost is $O(n+m)$.

Binary search performs $O(\log C)$ checks. Total time is $O(n\log n+m\log m+(n+m)\log C)$. Python sorting may use $O(n+m)$ temporary memory. Both input arrays are sorted in place.

## Alternatives and edge cases

- **Explicit assignment search:** Distributing grains among hens combinatorially is unnecessary because sorted noncrossing greedy assignment is optimal.
- **Simulate movement per second:** Time coordinates can be huge; route formulas evaluate reach directly.
- **All grains on one side:** Each hen uses a one-direction distance check with no reversal.
- **Hen on a grain:** Eating costs no time, and the grain is consumed by the `<= x` loop.
- **Unreachable leftmost grain:** If the current hen is too far right, every later hen is worse, justifying immediate false.
- **Multiple hens at one position:** They are processed independently and can split consecutive grain blocks.
- **Duplicate grain positions:** Pointer advancement consumes every occurrence at that coordinate.
- **Input mutation:** Both position arrays are sorted.
- **Exclusive search endpoint:** Adding one ensures the constructive all-grains route is present in `range(r)`.
