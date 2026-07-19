# Check If It Is a Good Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1250 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Math, Number Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/check-if-it-is-a-good-array/) |

## Problem Description

### Goal

You are given an array `nums` of positive integers. You may select a nonempty subset of its values, multiply every selected value by an arbitrary integer, and add the resulting products.

The array is *good* when some choice of subset and integer multipliers produces a sum equal to $1$. Return whether `nums` is good. Multipliers may be positive, negative, or zero; the question concerns existence rather than constructing the subset or coefficients.

### Function Contract

**Inputs**

- `nums`: an array of $n$ positive integers, where $1 \le n \le 10^5$ and $1 \le \texttt{nums[i]} \le 10^9$.
- Let $M = \max(\texttt{nums})$.

**Return value**

- Return `true` if an integer linear combination of selected array values can equal $1$; otherwise return `false`.

### Examples

**Example 1**

- Input: `nums = [12, 5, 7, 23]`
- Output: `true`
- Explanation: The values admit an integer linear combination equal to $1$.

**Example 2**

- Input: `nums = [29, 6, 10]`
- Output: `true`
- Explanation: For example, $29 + 6 - 3 \cdot 10 = 5$ and further integer combinations yield $1$ because the common greatest divisor is $1$.

**Example 3**

- Input: `nums = [3, 6]`
- Output: `false`
- Explanation: Every integer linear combination is divisible by $3$, so it cannot equal $1$.
