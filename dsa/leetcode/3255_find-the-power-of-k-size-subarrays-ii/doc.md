# Find the Power of K-Size Subarrays II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3255 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Sliding Window |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-the-power-of-k-size-subarrays-ii/) |

## Problem Description

### Goal

Examine each contiguous length-\`k\` subarray of \`nums\`. Its power is its maximum element when the subarray consists of consecutive integers sorted in ascending order; this means every adjacent pair differs by exactly $+1$. If any pair is equal, decreases, or jumps by more than one, that window's power is \`-1\`.

Return one power for every possible starting index. The result has length $n-k+1$ and follows the windows from left to right. In a valid window, the last element is necessarily the maximum and is therefore the reported power.

### Function Contract

**Inputs**

- \`nums\`: A list of $n$ positive integers, where $1 \le n \le 10^5$ and $1 \le \texttt{nums[i]} \le 10^6$.
- \`k\`: The exact window length, where $1 \le k \le n$.

**Return value**

- A list of $n-k+1$ powers, with entry \`i\` describing \`nums[i:i+k]\`.

### Examples

#### Example 1

- **Input:** \`nums = [1,2,3,4,3,2,5], k = 3\`
- **Output:** \`[3,4,-1,-1,-1]\`

Only the first two windows are consecutive and ascending.

#### Example 2

- **Input:** \`nums = [2,2,2,2,2], k = 4\`
- **Output:** \`[-1,-1]\`

Repeated values do not satisfy an exact increase of one.

#### Example 3

- **Input:** \`nums = [3,2,3,2,3,2], k = 2\`
- **Output:** \`[-1,3,-1,3,-1]\`

Each \`[2,3]\` window has power 3, while every decreasing pair has power \`-1\`.
