# Maximum Increasing Triplet Value

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3073 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Ordered Set |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-increasing-triplet-value/) |

## Problem Description

### Goal

Given an integer array `nums`, choose three indices $(i, j, k)$ whose positions and values are both strictly increasing:

$$
i < j < k
\quad\text{and}\quad
\texttt{nums[i]} < \texttt{nums[j]} < \texttt{nums[k]}.
$$

The value of such a triplet is calculated by `nums[i] - nums[j] + nums[k]`. Return the maximum value over every triplet satisfying both strict inequalities.

The input is guaranteed to contain at least one valid increasing triplet.

### Function Contract

**Inputs**

- `nums`: A list of $n$ integers, where $3 \le n \le 10^5$ and $1 \le \texttt{nums[i]} \le 10^9$.

At least one choice of $(i, j, k)$ satisfies the required index and value ordering.

**Return value**

- The maximum integer value `nums[i] - nums[j] + nums[k]` among all valid increasing triplets.

### Examples

**Example 1**

- Input: `nums = [5, 6, 9]`
- Output: `8`
- Explanation: The only possible triplet uses all three values, and `5 - 6 + 9 = 8`.

**Example 2**

- Input: `nums = [1, 5, 3, 6]`
- Output: `4`
- Explanation: The valid choices have values `(1, 5, 6)` and `(1, 3, 6)`, worth `2` and `4` respectively, so the maximum is `4`.
