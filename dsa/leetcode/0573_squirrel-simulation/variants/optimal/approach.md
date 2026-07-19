## General
**Use tree round trips as a baseline**

After delivering any nut, the squirrel is at the tree. Thus every nut except the first costs twice its Manhattan distance to the tree. Start with that round-trip cost for all nuts.

**Measure the first-trip replacement**

If a nut is collected first, its baseline outbound leg from the tree is replaced by a leg from the squirrel's initial position. Relative to the baseline, choosing that nut saves `tree_distance - squirrel_distance`.

**Choose the greatest saving**

Scan all nuts, add twice each tree distance to the baseline, and track the maximum saving. Subtract that saving from the baseline. The saving may be negative when the squirrel starts farther from every nut than the tree; the least-negative choice still gives the optimum because some nut must be first.

**Why only the first nut affects the choice**

Once the first nut is delivered, every remaining trip starts and ends at the tree, regardless of collection order. Those round-trip costs are fixed. The only variable part of any valid route is which nut replaces its tree-to-nut outbound leg with the initial squirrel-to-nut leg, so maximizing that one saving minimizes the complete route.

## Complexity detail
Each of the `n` nuts requires two constant-time Manhattan distance calculations, giving $O(n)$ time. The baseline and best-saving scalars use $O(1)$ space.

## Alternatives and edge cases
- **Try every first nut and recompute all trips:** is correct but repeats the fixed baseline and takes $O(n^2)$ time.
- **Choose the nut closest to the squirrel:** can be wrong because the tree distance determines how much baseline travel is replaced.
- **One nut:** the route is squirrel to nut to tree.
- **Squirrel at the tree:** every saving is zero and all trips are round trips.
- **Negative saving:** must not be clamped to zero because the squirrel cannot skip the initial trip.
- **Grid dimensions:** bound valid coordinates but do not change Manhattan distance calculations.
- **Collection order after the first:** has no effect on total distance.
