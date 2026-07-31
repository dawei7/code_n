# Minimum Operations to Make Array Values Equal to K

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3375 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-operations-to-make-array-values-equal-to-k/) |

## Problem Description

### Goal

An integer `h` is valid for the current array when every element strictly greater than `h` has the same value. In one operation, choose such a valid `h` and replace every array element greater than `h` by `h`. The validity test is repeated against the array produced by earlier operations.

Find the fewest operations that make every element equal to `k`. Values may only decrease, so an initial element below `k` makes the target unreachable. Otherwise, choose valid thresholds in descending order to remove the distinct value levels above `k`, including a final reduction to `k` when `k` was not initially present.

### Function Contract

**Inputs**

- `nums`: A list of $n$ integers representing the current array values.
- `k`: The target integer for every array position.

The constraints are $1\leq n\leq100$, $1\leq\texttt{nums[i]}\leq100$, and $1\leq k\leq100$.

**Return value**

- The minimum operation count needed to make every element equal to `k`, or `-1` when this is impossible.

### Examples

**Example 1**

- Input: `nums = [5,2,5,4,5]`, `k = 2`
- Output: `2`
- Explanation: Valid thresholds `4` and then `2` remove the two distinct levels above `k`.

**Example 2**

- Input: `nums = [2,1,2]`, `k = 2`
- Output: `-1`
- Explanation: The value `1` cannot be increased to `2`.

**Example 3**

- Input: `nums = [9,7,5,3]`, `k = 1`
- Output: `4`
- Explanation: Thresholds `7`, `5`, `3`, and `1` remove one distinct level per operation.
