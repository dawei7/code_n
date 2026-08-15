# Sum of Variable Length Subarrays

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/sum-of-variable-length-subarrays/) |
| Frontend ID | 3427 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

For every index `i` in the integer array `nums`, define a contiguous subarray that ends at `i`. Its starting index is `max(0, i - nums[i])`, so the value stored at the endpoint determines how far the subarray reaches to the left, with index `0` acting as a boundary.

Add every element of the subarray defined for index `0`, then do the same for index `1`, and continue through the final index. Elements may contribute multiple times because the defined subarrays can overlap. Return the total of all these subarray sums.

### Function Contract

**Inputs**

- `nums`: An integer array of length $n$, where $1 \le n \le 100$ and $1 \le \texttt{nums[i]} \le 1000$.

**Return value**

Return the sum of the $n$ variable-length subarray sums.

### Examples

#### Example 1

- **Input:** `nums = [2,3,1]`
- **Output:** `11`
- **Explanation:** The defined subarrays are `[2]`, `[2,3]`, and `[3,1]`, whose sums are `2`, `5`, and `4`.

#### Example 2

- **Input:** `nums = [3,1,1,2]`
- **Output:** `13`
- **Explanation:** The four subarray sums are `3`, `4`, `2`, and `4`.
