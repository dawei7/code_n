## General

For a proposed common radius `r`, the question “are all houses covered?” is easy to answer. More importantly, it is monotonic: if radius `r` works, every larger radius also works; if it fails, every smaller radius also fails. The exact solution sorts both position lists, checks a radius with a two-pointer sweep, and binary-searches for the smallest radius whose check succeeds.

**Sort positions to enable one forward sweep**

After sorting, houses are considered left to right and heaters are also considered left to right. Pointer `i` identifies the first house not yet covered. Pointer `j` identifies the current heater under consideration.

For radius `r`, heater `heaters[j]` covers the closed interval

$$
[\texttt{heaters}[j]-r,\ \texttt{heaters}[j]+r].
$$

Call these endpoints `mi` and `mx`.

**Three cases in `check(r)`**

Compare the current house with that heater interval:

1. If `houses[i] < mi`, the house lies left of the current heater's coverage. Every later heater is at least as far right, so its left endpoint is no smaller. No later heater can cover this house. Earlier heaters were already passed because their right coverage ended too early. Return false.
2. If `houses[i] > mx`, the house lies right of the current heater's coverage. This heater cannot cover this house or any later house, so advance `j` and keep the same `i`.
3. Otherwise, `mi <= houses[i] <= mx`. The current house is covered, so advance `i` while retaining the heater, which may cover additional houses.

If all houses are advanced past, return true. If heaters run out first, return false.

Each pointer moves only forward, so one feasibility check is linear rather than testing every house against every heater.

**Why the sweep never skips a possible cover**

When the algorithm advances a heater, its right endpoint is already left of the current house. Because houses are sorted, it cannot help any future house. When it declares a house too far left, all later heaters begin even farther right. These decisions discard only positions that are provably useless, so `check(r)` returns true exactly when radius `r` covers every house.

**Binary-search the first working radius**

The search interval begins at `left = 0` and `right = 1_000_000_000`. The upper bound is sufficient because all coordinates lie from 1 through one billion, so the maximum distance between any house and heater is less than one billion.

While `left < right`, choose floor midpoint

`mid = (left + right) >> 1`.

If `check(mid)` succeeds, `mid` may be the answer, but perhaps a smaller radius works, so set `right = mid`. If it fails, no radius at or below `mid` can work, so set `left = mid + 1`.

The interval always retains the smallest feasible radius and shrinks until both bounds meet. The returned `left` is therefore minimal.

**Trace the first example**

For houses `[1,2,3]` and heater `[2]`, radius zero covers only house `2`, so the check fails. Radius one gives interval `[1,3]`, covering all houses. Binary search eventually identifies one as the first feasible radius.

For houses `[1,5]` and heater `[2]`, the nearest-heater distances are one and three. Radius two fails at house five; radius three covers interval `[-1,5]` and succeeds, so the result is three.

**Relation to nearest-heater distances**

For each house, the minimum radius needed is its distance to the closest heater. A single shared radius must be at least all of those values, so the answer is their maximum. The binary-search predicate tests whether a candidate radius is at least that unknown maximum without explicitly computing each nearest distance.

## Complexity detail

Let $H$ be the number of houses, $T$ the number of heaters, and $C=10^9$ the coordinate search bound.

Sorting costs $O(H\log H+T\log T)$. Each feasibility check costs $O(H+T)$, and binary search performs $O(\log C)$ checks—about 30 under the constraints. Exact total time is

$$
O(H\log H+T\log T+(H+T)\log C).
$$

Because $C$ is a fixed source bound, $\log C$ is constant, and sorting often dominates asymptotically in terms of list sizes. This explains the manifest's simplified sorting-style time bound.

Both lists are sorted in place and therefore mutated. Python's Timsort can use $O(H+T)$ temporary space in the worst case; the `check` function itself uses $O(1)$ extra state. The manifest's $O(T)$ space does not fully describe sorting both arbitrary input lists when $H$ may exceed $T$.

## Alternatives and edge cases

- **Binary-search heaters for each house:** After sorting heaters, find each house's insertion point and compare its nearest left and right heater. This takes $O(T\log T+H\log T)$ time and directly computes the maximum nearest distance.
- **Two-pointer nearest-distance sweep:** Sort both lists and move the heater pointer toward each house's closest heater, achieving linear work after sorting without radius binary search.
- **Test every radius sequentially:** Coordinates reach one billion, so linear search over radius is infeasible.
- **House exactly at a heater:** Radius zero covers it because intervals are closed.
- **Houses outside the heater range:** The first or last heater determines their distance; the sweep's left/right failure logic handles them.
- **Duplicate positions:** Sorting and closed interval comparisons handle duplicates naturally.
- **One heater:** The answer is the larger distance from that heater to the extreme houses.
- **Large coordinate gap:** The one-billion upper bound remains sufficient under the source limits.
- **Input mutation:** Both arrays are reordered by in-place sorting.
- **Common radius:** Different houses may use different heaters, but every heater shares the same binary-searched radius.
