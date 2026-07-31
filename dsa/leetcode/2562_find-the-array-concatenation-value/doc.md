# Find the Array Concatenation Value

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2562 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Two Pointers, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Find the Array Concatenation Value](https://leetcode.com/problems/find-the-array-concatenation-value/) |

## Problem Description

### Goal

The concatenation of two positive integers is formed by writing the decimal digits of the second immediately after those of the first; for example, concatenating `15` and `49` produces `1549`. Begin with a concatenation value of zero and a 0-indexed array `nums`.

While at least two elements remain, concatenate the current first element with the current last element, add the result to the total, and remove both elements. If one middle element remains, add it without concatenation. Return the total after the array has been completely consumed.

### Function Contract

**Inputs**

- `nums`: A list of $n$ positive integers, where $1 \le n \le 1000$ and $1 \le \texttt{nums[i]} \le 10^4$.

**Return value**

- The sum of the ordered outer-pair concatenations, plus the unmodified middle value when `nums` has odd length.

### Examples

**Example 1**

- Input: `nums = [7, 52, 2, 4]`
- Output: `596`
- Explanation: The outer pairs produce `74` and `522`, whose sum is `596`.

**Example 2**

- Input: `nums = [5, 14, 13, 8, 12]`
- Output: `673`
- Explanation: The pair values are `512` and `148`, and the middle value `13` is added directly.

**Example 3**

- Input: `nums = [1]`
- Output: `1`
- Explanation: The only element is the unmatched middle value.
