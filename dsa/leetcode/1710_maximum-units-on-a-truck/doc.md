# Maximum Units on a Truck

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1710 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Greedy, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-units-on-a-truck/) |

## Problem Description
### Goal

You must load boxes onto one truck. Each entry in `boxTypes` describes how many boxes of one type are available and how many units each box of that type contains. Boxes within a type have equal value, but boxes from different types may contain different numbers of units.

The truck can carry at most `truckSize` boxes. You may choose any available boxes and do not have to fill the truck when fewer boxes exist. Return the greatest total number of units that can be loaded without exceeding the box-count capacity.

### Function Contract
**Inputs**

- `boxTypes`: a list of $t$ pairs `[numberOfBoxes, unitsPerBox]`
- `truckSize`: the maximum number of boxes the truck can hold
- $1 \le t \le 1000$
- every box count and units-per-box value is between $1$ and $1000$, and $1 \le \texttt{truckSize} \le 10^6$

**Return value**

The maximum total units obtainable by loading at most `truckSize` available boxes.

### Examples
**Example 1**

- Input: `boxTypes = [[1, 3], [2, 2], [3, 1]], truckSize = 4`
- Output: `8`

Load the one three-unit box, both two-unit boxes, and one one-unit box.

**Example 2**

- Input: `boxTypes = [[5, 10], [2, 5], [4, 7], [3, 9]], truckSize = 10`
- Output: `91`

Taking the types in descending units-per-box order fills the truck with the ten most valuable boxes.

**Example 3**

- Input: `boxTypes = [[2, 4], [3, 2]], truckSize = 3`
- Output: `10`

Both four-unit boxes and one two-unit box are optimal.

### Required Complexity

- **Time:** $O(t\log t)$
- **Space:** $O(t)$

<details>
<summary>Approach</summary>

#### General

**Prioritize units per occupied slot**

Every box consumes exactly one truck slot, so only its units-per-box value determines its benefit. Sort box types from greatest to least `unitsPerBox`. For each type, load as many boxes as possible: the smaller of its available count and the remaining capacity.

**Why the greedy choice cannot hurt**

Suppose a loading plan uses a lower-value box while a higher-value box remains available. Exchanging those two boxes preserves the box count and never decreases total units. Repeating this exchange transforms an optimal plan into one that exhausts higher-value types before taking lower-value ones. The descending greedy process constructs exactly such a plan.

Stop when capacity becomes zero. If all types are exhausted first, returning the accumulated units is correct because loading fewer than `truckSize` boxes is allowed.

#### Complexity detail

Sorting the $t$ box types costs $O(t\log t)$ time and $O(t)$ space for the sorted copy. The subsequent greedy scan visits each type at most once, taking $O(t)$ time and $O(1)$ additional state.

#### Alternatives and edge cases

- **Expand every physical box:** materializing one value per box and sorting those values is correct but can use time and space proportional to the total box count rather than the number of types.
- **Max-heap by type value:** repeatedly extracting the best type also takes $O(t\log t)$ time but adds heap machinery without improving the bound.
- **Dynamic programming by capacity:** treating this as general knapsack wastes $O(t\cdot\texttt{truckSize})$ work because every box has identical weight one.
- **Partially used type:** when a type has more boxes than the remaining slots, load only the remaining count.
- **Capacity exceeds supply:** load every available box and return before the nominal capacity is filled.
- **Equal values:** their relative order is irrelevant because exchanging equal-value boxes does not change the result.
- **One slot:** select one box from a type with maximum units per box.
- **Large counts:** multiply the number loaded by its units value instead of iterating over individual boxes.

</details>
