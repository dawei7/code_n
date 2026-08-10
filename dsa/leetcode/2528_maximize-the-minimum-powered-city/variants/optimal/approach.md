## General

**Binary-search a candidate minimum power**

Suppose every city must end with power at least `x`. Ask whether at most `k` additional stations can achieve that target.

Feasibility is monotone:

- if target `x` is feasible, every smaller target is feasible;
- if `x` is infeasible, every larger target is infeasible.

The outer binary search finds the greatest feasible `x`. The main work is an $O(n)$ greedy feasibility check.

**Precompute each city's original power with a difference array**

A station at city `i` contributes to interval

$$
[\max(0,i-r),\min(n-1,i+r)].
$$

Instead of adding `v=stations[i]` separately to every city in that interval, the code uses range-difference updates:

- add `v` at the interval's left endpoint;
- subtract `v` just after its right endpoint.

Taking prefix sums through `accumulate` converts these boundary changes into array `s`, where `s[i]` is city `i`'s original power.

This preprocessing handles all station ranges in $O(n)$ rather than $O(nr)$.

**Sweep cities from left to right inside `check`**

The check uses another difference array `d` for power supplied by newly built stations. Running value `t` is the active added power covering the current city.

At index `i`, `t+=d[i]` applies any scheduled change beginning or ending there. Current power is

`s[i]+t`.

If this already reaches `x`, no new station is needed for city `i`.

If it falls short, deficit is

`dist=x-(s[i]+t)`.

At least `dist` new stations covering city `i` are unavoidable. Each station increases that city's power by exactly one, so no solution can use fewer at this point.

**Place required stations as far right as possible**

A station covers city `i` when its construction city lies between `i-r` and `i+r`. Among legal array indices, the rightmost possible placement is

`j=min(i+r,n-1)`.

Placing all `dist` stations at `j` fixes current city `i` and maximizes their usefulness for cities still to be processed on the right. Any placement farther left would expire no later and could not help a future city more.

This greedy choice never harms already processed cities because they already meet the target and need not be reconsidered.

**Schedule the added coverage interval**

Stations placed at `j` cover

$$
[\max(0,j-r),\min(n-1,j+r)].
$$

The code adds `dist` at `d[left]` and subtracts it at `d[right+1]`. Since `left<=i` during the left-to-right sweep, its start boundary may already have been passed. The source immediately executes `t+=dist` so the new power affects current city and following cities.

The negative event at `right+1` remains in the future and automatically removes this contribution after its range expires.

**Respect the construction budget**

If remaining `k` is below `dist`, current city cannot reach `x`. No later placement can cover a city already being passed more efficiently than one power per station, so the check returns false.

Otherwise, it subtracts `dist` and continues. If every city is processed, the greedy construction uses at most the budget and proves feasibility.

**Why the greedy check is optimal**

At each city, previous decisions are fixed and current active power is known. Any feasible plan must add at least the current deficit using stations that cover this city. Moving those necessary stations to the rightmost legal position preserves their coverage of current city and weakly extends their coverage toward all unprocessed cities.

Therefore, there exists a feasible plan following the greedy choice whenever any feasible plan exists. Induction across city indices proves `check(x)` is exact.

**Binary-search details**

`left=0` is always feasible. `right=1<<40` is safely above any possible city power under the constraints.

The upper midpoint

`(left+right+1)>>1`

prevents stalling while maximizing. A feasible midpoint replaces `left`; an infeasible one makes `right=mid-1`. When the bounds meet, they equal the maximum achievable minimum.

**Trace the objective, not one city's maximum**

The algorithm never tries to maximize total power or the strongest city. It raises deficient cities only as needed for a shared lower bound, which is exactly a max-min optimization.

## Complexity detail

Let $U$ be the binary-search upper bound. Original power preprocessing is $O(n)$. Each feasibility check allocates and scans an $O(n)$ difference array. Binary search performs $O(\log U)$ checks, so total time is $O(n\log U)$.

Here `U=2^40`, so there are at most about 40 checks. This is often expressed as $O(n\log(B+k))$ for a natural base-power bound $B$.

Arrays `s` and the per-check difference array use $O(n)$ space. Recursion is not used.

## Alternatives and edge cases

- **Binary search plus explicit range updates:** Updating every covered city directly makes one check $O(nr)$ and is too slow.
- **`r=0`:** New stations help only their own city; the greedy placement is the current index.
- **`r>=n-1`:** Every station covers every city, so additions raise all powers together.
- **`k=0`:** Feasibility depends solely on precomputed original powers.
- **Zero-station cities:** They are handled through their range-summed power like any other city.
- **Right boundary:** `min(i+r,n-1)` keeps placements inside the array.
- **Exact deficit:** Adding more than needed at current city is never required by the greedy feasibility test.
- **Budget exhaustion:** Return false as soon as a required deficit exceeds remaining `k`.
- **Difference expiration:** The subtraction at `right+1` removes added power at the correct future point.
- **Upper midpoint:** It is essential for a greatest-feasible binary search.
