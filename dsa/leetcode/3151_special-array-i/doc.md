# Special Array I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3151 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/special-array-i/) |

## Problem Description
### Goal
An integer array is **special** when the parity changes at every step between adjacent elements. Equivalently, each neighboring pair must contain one even value and one odd value.

Given `nums`, return whether the entire array is special. An array containing only one value has no adjacent pair that can violate the condition, so it is special.

Only consecutive positions form the pairs considered by this test; values farther apart impose no additional condition.

### Function Contract
**Inputs**

- `nums`: A list of $n$ positive integers, where $1 \le n \le 100$ and $1 \le \texttt{nums[i]} \le 100$.

**Return value**

Return `true` if every adjacent pair in `nums` has different parity; otherwise, return `false`.

### Examples
**Example 1**

- Input: `nums = [1]`
- Output: `true`
- Explanation: A one-element array has no adjacent pair, so no parity violation exists.

**Example 2**

- Input: `nums = [2,1,4]`
- Output: `true`
- Explanation: The pairs `(2,1)` and `(1,4)` each contain one even and one odd value.

**Example 3**

- Input: `nums = [4,3,1,6]`
- Output: `false`
- Explanation: The adjacent values `3` and `1` are both odd.
