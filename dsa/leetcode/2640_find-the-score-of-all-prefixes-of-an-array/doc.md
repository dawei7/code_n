# Find the Score of All Prefixes of an Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2640 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-the-score-of-all-prefixes-of-an-array/) |

## Problem Description

### Goal

For an integer array `arr`, define its conversion array `conver` by setting `conver[i] = arr[i] + max(arr[0..i])`. Thus, each converted value combines the original entry with the largest entry that appears at or before its index. The score of `arr` is the sum of all values in this conversion array.

You are given a 0-indexed positive-integer array `nums` of length $n$. Return an array `ans` of the same length such that `ans[i]` is the score of the prefix `nums[0..i]`. Each prefix retains the conversion values determined by the running maxima at their respective positions.

### Function Contract

**Inputs**

- `nums`: A positive-integer array of length $n$, where $1 \le n \le 10^5$ and $1 \le \texttt{nums[i]} \le 10^9$.

**Return value**

- Return a length-$n$ integer array where entry $i$ is the sum of `nums[j] + max(nums[0..j])` over all $0 \le j \le i$.

### Examples

**Example 1**

- Input: `nums = [2, 3, 7, 5, 10]`
- Output: `[4, 10, 24, 36, 56]`
- Explanation: The conversion array is `[4, 6, 14, 12, 20]`; its successive prefix sums form the answer.

**Example 2**

- Input: `nums = [1, 1, 2, 4, 8, 16]`
- Output: `[2, 4, 8, 16, 32, 64]`
- Explanation: Every new power of two is also the running maximum, while the repeated initial one contributes another two.
