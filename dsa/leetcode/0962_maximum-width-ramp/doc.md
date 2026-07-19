# Maximum Width Ramp

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 962 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Two Pointers, Stack, Monotonic Stack |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [maximum-width-ramp](https://leetcode.com/problems/maximum-width-ramp/) |

## Problem Description

### Goal

In an integer array `nums`, a ramp is a pair of indices `(i, j)` satisfying both $i<j$ and `nums[i] <= nums[j]`. Its width is the distance between those indices, $j-i$.

Choose a valid ramp with the greatest possible width and return that width. The pair may span values between its endpoints; only the endpoint inequality matters. Equality is permitted. If the array contains no pair satisfying the ramp conditions, return `0`.

### Function Contract

**Inputs**

- `nums`: an integer array of length $N$, where $2 \le N \le 5\times10^4$.
- Every value satisfies $0 \le \texttt{nums[i]} \le 5\times10^4$.

**Return value**

Return the maximum value of $j-i$ over all ramps `(i, j)`, or `0` when no ramp exists.

### Examples

**Example 1**

- Input: `nums = [6,0,8,2,1,5]`
- Output: `4`
- Explanation: Indices `(1, 5)` form a ramp because `nums[1] = 0 <= 5 = nums[5]`.

**Example 2**

- Input: `nums = [9,8,1,0,1,9,4,0,4,1]`
- Output: `7`
- Explanation: The equal endpoint values at indices `(2, 9)` form a width-`7` ramp.
