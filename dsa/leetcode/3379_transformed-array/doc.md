# Transformed Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3379 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/transformed-array/) |

## Problem Description

### Goal

Treat the integer list `nums` as circular. For every index `i`, independently use `nums[i]` as a signed movement distance starting from `i`: a positive value moves right, a negative value moves left by its absolute value, and zero remains at the same index. Crossing either end wraps around to the other side.

Create a new array of the same length. At position `i`, store the original value found at the destination of that movement. Every lookup must use the unchanged input array rather than values already written to the result, so transformations at different indices do not affect one another.

### Function Contract

**Inputs**

- `nums`: A nonempty list of integers representing both the circular values and the signed jump distances.

The constraints are $1\leq n\leq100$ and $-100\leq\texttt{nums[i]}\leq100$, where $n=\lvert\texttt{nums}\rvert$.

**Return value**

- A list `result` of length $n$ where `result[i] = nums[(i + nums[i]) % n]` under nonnegative circular indexing.

### Examples

**Example 1**

- Input: `nums = [3,-2,1,1]`
- Output: `[1,1,1,3]`
- Explanation: The four destinations are indices `3`, `3`, `3`, and `0`.

**Example 2**

- Input: `nums = [-1,4,-1]`
- Output: `[-1,-1,4]`
- Explanation: Left and oversized right movements wrap to indices `2`, `2`, and `1`.

**Example 3**

- Input: `nums = [0,0,0]`
- Output: `[0,0,0]`
- Explanation: Every zero offset reads the value at its current index.
