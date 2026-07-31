# Sum of Total Strength of Wizards

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2281 |
| Difficulty | Hard |
| Topics | Array, Stack, Monotonic Stack, Prefix Sum |
| Official Link | [LeetCode](https://leetcode.com/problems/sum-of-total-strength-of-wizards/) |

## Problem Description
### Goal
An army is represented by the 0-indexed array `strength`, where
`strength[i]` is the strength of wizard $i$. Every contiguous, non-empty
subarray describes one group of wizards.

The total strength of a group is the product of its weakest member's strength
and the sum of all strengths in that group. Sum this value over every
contiguous group and return the result modulo $10^9+7$.

### Function Contract
**Inputs**

- `strength`: An integer array of length $n$ containing the individual wizard strengths.

Here, $1 \le n \le 10^5$ and
$1 \le \texttt{strength[i]} \le 10^9$.

**Return value**

The sum, modulo $10^9+7$, of

$$
\min(\text{subarray})\sum(\text{subarray})
$$

over all non-empty contiguous subarrays.

### Examples
**Example 1**

- Input: `strength = [1, 3, 1, 2]`
- Output: `44`

**Example 2**

- Input: `strength = [5, 4, 6]`
- Output: `213`

**Example 3**

- Input: `strength = [7]`
- Output: `49`
