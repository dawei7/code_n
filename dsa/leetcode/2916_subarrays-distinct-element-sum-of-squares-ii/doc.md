# Subarrays Distinct Element Sum of Squares II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2916 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table, Binary Indexed Tree, Segment Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-ii/) |

## Problem Description

### Goal

For every non-empty contiguous subarray of `nums`, count how many different
integer values it contains. The score of that subarray is the square of this
distinct-element count.

Add the scores of all subarrays and return the total modulo
$10^9+7$. Equal values at different positions count as one distinct value
within a particular subarray, while the same position participates in many
different subarrays.

### Function Contract

**Inputs**

- `nums`: A non-empty list of integers.

Let $n=\lvert\texttt{nums}\rvert$. The input satisfies
$1 \le n \le 10^5$ and $1 \le \texttt{nums[i]} \le 10^5$.

**Return value**

- The sum of the squared distinct-element counts over every non-empty
  contiguous subarray, reduced modulo $10^9+7$.

### Examples

**Example 1**

- Input: `nums = [1, 2, 1]`
- Output: `15`
- Explanation: The three length-one subarrays each score $1$. The subarrays
  `[1, 2]`, `[2, 1]`, and `[1, 2, 1]` each contain two distinct values
  and score $4$, so the total is $3 + 3 \cdot 4 = 15$.

**Example 2**

- Input: `nums = [2, 2]`
- Output: `3`
- Explanation: Both singletons and the whole array contain only one distinct
  value, so each of the three subarrays scores $1$.

**Example 3**

- Input: `nums = [1, 2, 3]`
- Output: `20`
- Explanation: The three singletons contribute $3$, the two length-two
  subarrays contribute $2 \cdot 2^2=8$, and the whole array contributes
  $3^2=9$.
