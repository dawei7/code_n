# Maximum Number of Integers to Choose From a Range I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2554 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Binary Search, Greedy, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Maximum Number of Integers to Choose From a Range I](https://leetcode.com/problems/maximum-number-of-integers-to-choose-from-a-range-i/) |

## Problem Description

### Goal

You are given an integer array `banned`, an upper bound `n`, and a sum limit `maxSum`. Choose integers from the inclusive range $[1,n]$. Each integer may be chosen at most once, and no chosen value may appear anywhere in `banned`.

The sum of all chosen integers must not exceed `maxSum`. Return the largest possible number of chosen integers. Duplicate entries in `banned` do not create additional restrictions, and banned values outside $[1,n]$ have no effect on the available choices.

### Function Contract

**Inputs**

- `banned`: A list of $m$ forbidden integers, where $1 \le m \le 10^4$ and every value lies between $1$ and $10^4$, inclusive.
- `n`: The inclusive upper bound of the candidate range, with $1 \le n \le 10^4$.
- `maxSum`: The maximum permitted sum, with $1 \le \texttt{maxSum} \le 10^9$.

**Return value**

- The maximum number of distinct allowed integers that can be selected without their sum exceeding `maxSum`.

### Examples

**Example 1**

- Input: `banned = [1, 6, 5], n = 5, maxSum = 6`
- Output: `2`
- Explanation: Choosing `2` and `4` uses two allowed values and reaches a sum of `6`.

**Example 2**

- Input: `banned = [1, 2, 3, 4, 5, 6, 7], n = 8, maxSum = 1`
- Output: `0`
- Explanation: Every value small enough for the budget is forbidden.

**Example 3**

- Input: `banned = [11], n = 7, maxSum = 50`
- Output: `7`
- Explanation: The banned value is outside the range, and all values from `1` through `7` sum to `28`.
