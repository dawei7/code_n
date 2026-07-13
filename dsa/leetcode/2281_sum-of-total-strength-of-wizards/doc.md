# Sum of Total Strength of Wizards

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2281 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Stack, Monotonic Stack, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [sum-of-total-strength-of-wizards](https://leetcode.com/problems/sum-of-total-strength-of-wizards/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/sum-of-total-strength-of-wizards/).

### Goal
For every nonempty contiguous group of wizards, multiply the group's minimum strength by its total strength. Sum these products over all groups and return the result modulo `1,000,000,007`.

### Function Contract
**Inputs**

- `strength`: positive wizard strengths in order.

**Return value**

The sum of all subarray total-strength values modulo `1,000,000,007`.

### Examples
**Example 1**

- Input: `strength = [1, 3, 1, 2]`
- Output: `44`

**Example 2**

- Input: `strength = [5, 4, 6]`
- Output: `213`

**Example 3**

- Input: `strength = [1]`
- Output: `1`

---

## Solution
### Approach
Assign each subarray to one occurrence of its minimum using monotonic-stack boundaries, with one side strict and the other non-strict to handle ties exactly once. For index `i`, all assigned subarrays choose a left endpoint in its boundary range and a right endpoint in the other range. A prefix sum of prefix sums computes the aggregate subarray sums across those endpoint combinations in constant time. Multiply that aggregate by `strength[i]`, sum contributions, and normalize modulo the required constant.

### Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)`

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
