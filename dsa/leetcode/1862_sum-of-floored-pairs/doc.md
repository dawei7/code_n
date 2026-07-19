# Sum of Floored Pairs

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1862 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Math, Binary Search, Counting, Enumeration, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/sum-of-floored-pairs/) |

## Problem Description
### Goal
Given a positive integer array `nums`, consider every ordered pair of indices
$(i,j)$, including pairs whose indices are equal. The pair contributes the
integer part of `nums[i] / nums[j]`, equivalently
$\left\lfloor \texttt{nums}[i]/\texttt{nums}[j]\right\rfloor$.

Add the contributions of all $n^2$ ordered pairs. Because this sum can be
large, return its remainder modulo $10^9+7$.

### Function Contract
**Inputs**

- `nums`: an array of $n$ positive integers, where $1 \le n \le 10^5$ and
  every value is at most $10^5$.

Let $U = \max(\texttt{nums})$.

**Return value**

The ordered-pair floor-division sum as an integer modulo $1{,}000{,}000{,}007$.

### Examples
**Example 1**

- Input: `nums = [2,5,9]`
- Output: `10`

**Example 2**

- Input: `nums = [7,7,7,7,7,7,7]`
- Output: `49`

Every ordered pair contributes one.

**Example 3**

- Input: `nums = [1,2,3]`
- Output: `9`
