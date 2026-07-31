# Find the Power of K-Size Subarrays I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3254 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Sliding Window |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-the-power-of-k-size-subarrays-i/) |

## Problem Description

### Goal

For every contiguous subarray of length \`k\` in \`nums\`, determine its power. A subarray has a valid power only when its elements are consecutive integers arranged in ascending order. Equivalently, each element after the first must be exactly one greater than its predecessor.

When a window meets that condition, its power is its maximum element; because the window is ascending, this is its final element. Otherwise its power is \`-1\`. Return the powers in starting-index order, producing exactly $n-k+1$ results.

### Function Contract

**Inputs**

- \`nums\`: A list of $n$ positive integers, where $1 \le n \le 500$ and $1 \le \texttt{nums[i]} \le 10^5$.
- \`k\`: The required subarray length, where $1 \le k \le n$.

**Return value**

- A list of $n-k+1$ integers; entry \`i\` is the power of \`nums[i:i+k]\`.

### Examples

**Example 1**

- Input: \`nums = [1,2,3,4,3,2,5], k = 3\`
- Output: \`[3,4,-1,-1,-1]\`

The first two windows rise by one at every step. Each remaining window contains a break.

**Example 2**

- Input: \`nums = [2,2,2,2,2], k = 4\`
- Output: \`[-1,-1]\`

Equal neighboring values are not consecutive in ascending order.

**Example 3**

- Input: \`nums = [3,2,3,2,3,2], k = 2\`
- Output: \`[-1,3,-1,3,-1]\`

Only the two windows \`[2,3]\` satisfy the required step.
