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
