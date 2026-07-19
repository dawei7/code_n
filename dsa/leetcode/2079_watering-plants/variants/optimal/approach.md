## General
**Count the unavoidable forward progress**

Without refills, reaching each next plant costs one step: river to plant 0, then plant 0 to plant 1, and so on. Add this one step while processing every plant, giving a baseline of $n$ steps.

**Charge only the detour before a dry plant**

Before plant `index`, the gardener is at plant `index - 1`. If the remaining water is too small for the current requirement, returning from coordinate `index - 1` to the river costs `index` steps. Walking from the river to plant `index` costs `index + 1` steps, whereas the baseline already counted the one direct step. The refill therefore contributes exactly `2 * index` additional steps. Reset the remaining water to `capacity`, then water the plant.

**Mirror the mandated refill timing**

Checking capacity immediately before each plant is equivalent to checking the next requirement immediately after the preceding plant. Use strict insufficiency: when the remaining amount equals the next requirement, the plant can be watered completely and no refill is permitted. Since every requirement is at most `capacity`, one refill is always enough.

## Complexity detail
The simulation visits each of the $n$ plant requirements once and performs constant work per plant, for $O(n)$ time. The remaining-water and step counters use $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Simulate every walked coordinate:** Moving a position variable one step at a time is correct, but repeated river trips can make the running time proportional to the answer, which is $O(n^2)$.
- **Prefix-sum refill groups:** Partitioning plants into maximal consecutive groups that fit in one can also works, but it encodes the same greedy simulation with more bookkeeping.
- **Exact remaining water:** Equality is sufficient; refill only when `water < plants[index]`.
- **No refill needed:** The result is simply $n$ when all requirements fit into the initial can cumulatively.
- **Single plant:** Starting at the river and moving to coordinate 0 costs exactly one step.
- **Refill before the final plant:** The return trip still includes walking back out to that plant; the process does not end at the river.
