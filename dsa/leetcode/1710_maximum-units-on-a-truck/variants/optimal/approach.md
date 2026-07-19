## General
**Prioritize units per occupied slot**

Every box consumes exactly one truck slot, so only its units-per-box value determines its benefit. Sort box types from greatest to least `unitsPerBox`. For each type, load as many boxes as possible: the smaller of its available count and the remaining capacity.

**Why the greedy choice cannot hurt**

Suppose a loading plan uses a lower-value box while a higher-value box remains available. Exchanging those two boxes preserves the box count and never decreases total units. Repeating this exchange transforms an optimal plan into one that exhausts higher-value types before taking lower-value ones. The descending greedy process constructs exactly such a plan.

Stop when capacity becomes zero. If all types are exhausted first, returning the accumulated units is correct because loading fewer than `truckSize` boxes is allowed.

## Complexity detail
Sorting the $t$ box types costs $O(t\log t)$ time and $O(t)$ space for the sorted copy. The subsequent greedy scan visits each type at most once, taking $O(t)$ time and $O(1)$ additional state.

## Alternatives and edge cases
- **Expand every physical box:** materializing one value per box and sorting those values is correct but can use time and space proportional to the total box count rather than the number of types.
- **Max-heap by type value:** repeatedly extracting the best type also takes $O(t\log t)$ time but adds heap machinery without improving the bound.
- **Dynamic programming by capacity:** treating this as general knapsack wastes $O(t\cdot\texttt{truckSize})$ work because every box has identical weight one.
- **Partially used type:** when a type has more boxes than the remaining slots, load only the remaining count.
- **Capacity exceeds supply:** load every available box and return before the nominal capacity is filled.
- **Equal values:** their relative order is irrelevant because exchanging equal-value boxes does not change the result.
- **One slot:** select one box from a type with maximum units per box.
- **Large counts:** multiply the number loaded by its units value instead of iterating over individual boxes.
