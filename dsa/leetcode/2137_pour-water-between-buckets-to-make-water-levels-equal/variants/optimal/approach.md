## General

The desired common water level is a real number, and transferred water is partially lost. Rather than constructing a sequence of pours, test whether a proposed level `v` is achievable. Feasibility changes monotonically: if all buckets can reach level `v`, they can also reach any lower level by transferring less water or discarding surplus through lossy transfers.

This monotonic boundary is exactly what binary search needs.

**Measure available source water**

For a bucket containing `x >= v` gallons, the amount above the proposed final level is `x - v`. That surplus may be poured out while leaving exactly `v` in the source bucket. The checker adds all such raw surplus to `a`.

It is important that `a` measures water before transfer loss. If one gallon is poured, the source loses the full gallon even though the destination receives less.

**Convert each deficit into required poured water**

For a bucket with `x < v`, its received-water deficit is `v - x`. If the loss is `loss` percent, only

$$
\frac{100-\textit{loss}}{100}
$$

of any poured amount arrives. Delivering a deficit $d$ therefore requires the sources to pour

$$
d\cdot\frac{100}{100-\textit{loss}}.
$$

The exact checker adds `(v - x) * 100 / (100 - loss)` to `b`. Thus `b` is not merely the missing water visible in low buckets; it is the total pre-loss amount that high buckets must release to fill those deficits.

The candidate level is feasible exactly when `a >= b`. If the sources have more than the required amount, they need not pour the extra. If they have less, no rearrangement can overcome the loss.

For buckets `[1,2,7]` with 80 percent loss and candidate level $2$, the high bucket offers $5$ gallons of raw surplus. The first bucket needs to receive $1$ gallon, which requires pouring $1\cdot100/20=5$ gallons. The middle bucket needs nothing, so `a == b` and level $2$ is feasible.

**Establish safe search bounds**

The lower bound `l = 0` is always feasible: no bucket needs to receive water, and all existing water can simply remain or be poured away as needed. The upper bound `r = max(buckets)` cannot be exceeded because transferring water never creates water, and no bucket initially lies above that maximum.

The code maintains `l` as a feasible level and `r` as an upper boundary that need not be feasible. It evaluates `mid = (l + r) / 2`:

- if `check(mid)` is true, the maximum lies at or above `mid`, so `l = mid`;
- otherwise, `mid` is too high, so `r = mid`.

Each decision discards half of the current numeric interval.

**Why feasibility is monotone**

As `v` rises, high buckets have less surplus above it, while low buckets have larger deficits. Some buckets may also move from the source group into the deficit group. None of these changes makes a higher candidate easier. Therefore feasible levels form a prefix interval beginning at zero, and infeasible levels lie above the optimum.

**Stop at the required precision**

The loop continues while `r - l > 1e-5`. On exit, the uncertainty interval has width at most $10^{-5}$. Since `l` remains feasible and the true maximum lies between `l` and `r`, returning `l` is within the accepted tolerance while avoiding an infeasible overestimate.

The method does not need to output individual transfers. The aggregate surplus-versus-requirement equation is sufficient because water is divisible and may be poured between any buckets in arbitrary real amounts.

**Why the aggregate comparison constructs a solution**

If `a >= b`, imagine drawing the required pre-loss amounts for deficient buckets from one combined pool of all source surpluses. Transfers can use fractional amounts and any source may pour to any destination, so the pool can be divided exactly as needed. Each destination receives its deficit after loss, and unused surplus remains in source buckets or is simply not poured. No routing restriction prevents this allocation.

If `a < b`, even pouring every available surplus loses too much water to supply the total deficits. A different ordering of pours cannot improve the fixed retention percentage, so the candidate is impossible.

## Complexity detail

Let $n$ be the number of buckets and let $R=\max(\texttt{buckets})$. One call to `check` scans all $n$ buckets and uses $O(n)$ time. Binary search halves an initial interval of width $R$ until its width is at most $\varepsilon=10^{-5}$. This takes $O(\log(R/\varepsilon))$ iterations. Total time is

$$
O\left(n\log\frac{R}{\varepsilon}\right).
$$

The checker stores only `a`, `b`, and its loop variable. The binary search stores only its two bounds and midpoint. The exact implementation uses $O(1)$ auxiliary space.

All arithmetic involving `v` and the loss ratio is floating point. The tolerance-based contract and stopping condition account for small representation error.

## Alternatives and edge cases

- **Search for a closed-form weighted average:** The set of source and deficit buckets changes with the candidate level, making a single ordinary average insufficient when loss is positive. Binary search handles those changing roles cleanly.
- **Simulate individual pours:** Many valid transfer sequences may realize the same level. Aggregate raw surplus and required pre-loss water avoid unnecessary pair selection.
- **Compare delivered surplus instead:** One may test `a * (100 - loss) / 100` against the unscaled deficits. This is algebraically equivalent to the exact code’s choice to scale deficits upward.
- **No loss:** When `loss = 0`, required poured water equals each deficit. The optimum is the ordinary average water level, and the same checker finds it.
- **Very high loss:** At `loss = 99`, only one percent arrives, so deficits require one hundred times as much source water. The denominator remains positive because loss never reaches 100.
- **One bucket:** No transfer is needed. Every level through that bucket’s amount is feasible, and binary search approaches the original amount.
- **All buckets equal:** Their common value is the maximum answer. Candidates above it create deficits without any source surplus; candidates at it are feasible.
- **All buckets empty:** Both bounds are zero, the loop does not run, and the method returns `0`.
- **Candidate equal to a bucket:** The `x >= v` branch adds zero surplus. Treating equality as a source does not change either total.
- **Extra surplus:** Feasibility requires `a >= b`, not equality, because unused source water need not be transferred.
- **Real-valued transfers:** Fractional deficits and pours are permitted, so floating-point level testing matches the contract.
- **Return the lower bound:** `l` is preserved as feasible, whereas `r` may be the first known infeasible side. Returning `l` respects the feasibility boundary.
- **Input preservation:** The checker only iterates over `buckets` and never changes an amount.
