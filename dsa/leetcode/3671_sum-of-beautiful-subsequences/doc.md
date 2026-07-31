# Sum of Beautiful Subsequences

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3671 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Binary Indexed Tree, Number Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/sum-of-beautiful-subsequences/) |

## Problem Description
### Goal

Given an integer array `nums`, consider every nonempty subsequence whose selected values are strictly increasing from left to right. Subsequences use increasing indices and are distinguished by their chosen index sets.

For each positive integer $g$, count the qualifying subsequences whose greatest common divisor is exactly $g$. Define the beauty associated with $g$ as that count multiplied by $g$.

Return the sum of these beauty values over all positive $g$, reduced modulo $10^9+7$. Equivalently, add the GCD of every strictly increasing subsequence and apply the modulus.

### Function Contract

**Inputs**

- `nums`: a positive integer array of length $n$, where $1\le n\le10^4$ and $1\le\texttt{nums[i]}\le7\cdot10^4$.

Let $V=\max(\texttt{nums})$, and let $T$ be the sum of the positive-divisor counts of all input values.

**Return value**

Return the sum of the GCDs of all nonempty strictly increasing subsequences, modulo $10^9+7$.

### Examples

**Example 1**

- Input: `nums = [1, 2, 3]`
- Output: `10`
- Five subsequences have GCD `1`, while the singleton subsequences `[2]` and `[3]` contribute `2` and `3`.

**Example 2**

- Input: `nums = [4, 6]`
- Output: `12`
- The singleton GCDs are `4` and `6`, and the pair has GCD `2`.

**Example 3**

- Input: `nums = [3, 2, 1]`
- Output: `6`
- No multi-element subsequence is strictly increasing, so only the three singleton GCDs contribute.
