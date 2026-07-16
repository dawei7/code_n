# Minimum Number of Increments on Subarrays to Form a Target Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1526 |
| Difficulty | Hard |
| Topics | Array, Dynamic Programming, Stack, Greedy, Monotonic Stack |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-number-of-increments-on-subarrays-to-form-a-target-array/) |

## Problem Description
### Goal

Start with an integer array of zeros having the same length as a positive `target` array. One operation chooses any nonempty contiguous subarray and increases every selected value by exactly one.

Return the minimum number of operations required to make the initial array equal `target`. Operations may overlap and use different intervals, but no value may be decremented; the input guarantees that the minimum fits in a signed 32-bit integer.

### Function Contract
**Inputs**

- `target`: A list of $n$ positive integers, where $1 \leq n \leq 10^5$.
- Every target height lies between 1 and $10^5$, inclusive.

**Return value**

Return the fewest contiguous-range increment operations that construct `target` from an all-zero array.

### Examples
**Example 1**

- Input: `target = [1, 2, 3, 2, 1]`
- Output: `3`
- Explanation: Increment the whole array, then the middle three entries, then the center entry.

**Example 2**

- Input: `target = [3, 1, 1, 2]`
- Output: `4`
- Explanation: Three layers must start at the first position, and one new layer starts at the final rise.

**Example 3**

- Input: `target = [3, 1, 5, 4, 2]`
- Output: `7`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**View operations as horizontal layers**

Each range increment contributes one unit-height horizontal layer across a contiguous group of columns. At index 0, `target[0]` layers must begin because no earlier column can carry a layer into the array.

Moving from `target[i - 1]` to `target[i]`, existing layers can continue across the boundary up to the smaller height. If the current height is larger, the excess `target[i] - target[i - 1]` cannot come from the left and therefore requires that many new operations starting at or before index `i`; starting them at `i` is sufficient. A drop starts no new layers because surplus layers simply end at the previous index.

**Sum every unavoidable rise**

The minimum is consequently `target[0]` plus every positive adjacent difference. This is a lower bound because each counted layer start needs a distinct operation. It is attainable by extending every layer across as many later columns as their heights permit, so the same count constructs the target.

Only adjacent heights matter. The actual intervals need not be materialized, and overlapping mountains or valleys are handled by starting layers on rises and ending them on drops.

#### Complexity detail

A single left-to-right scan examines each adjacent pair once, giving $O(n)$ time. The running total and previous/current values use $O(1)$ auxiliary space.

The answer may exceed any individual target height because separated rises require independent operations, but the source guarantees the total fits a 32-bit integer.

#### Alternatives and edge cases

- **Per-height run counting:** for each horizontal level, count contiguous positive runs. It proves the layer interpretation but may require $O(nH)$ time for maximum height $H$.
- **Operation-by-operation simulation:** repeatedly decrement positive runs. It is correct but can be much slower than reading boundary rises directly.
- **Monotonic stack:** layers can be opened and closed with a stack, but adjacent positive differences already encode the same information more simply.
- **Single element:** its target value is the number of required one-position increments.
- **Strictly increasing target:** every rise adds, so the answer equals the final height.
- **Strictly decreasing target:** all layers start at index 0, so the answer equals the first height.
- **Flat plateau:** equal adjacent heights reuse all active layers and add no operation.
- **Separated peaks:** each rise after a valley starts additional layers and must be counted independently.

</details>
