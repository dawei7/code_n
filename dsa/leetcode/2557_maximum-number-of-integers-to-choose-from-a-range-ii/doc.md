# Maximum Number of Integers to Choose From a Range II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2557 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Binary Search, Greedy, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Maximum Number of Integers to Choose From a Range II](https://leetcode.com/problems/maximum-number-of-integers-to-choose-from-a-range-ii/) |

## Problem Description

### Goal

You are given an integer array `banned`, an upper bound `n`, and a sum limit `maxSum`. Choose any number of distinct integers from the inclusive range $[1,n]$. A value may be chosen at most once, and no value that occurs in `banned` may be included.

The sum of the chosen integers must not exceed `maxSum`. Return the maximum possible number of integers in such a selection. Repeated occurrences of the same banned value still forbid only that one integer; the objective is the number selected, not the number of different valid selections.

### Function Contract

**Inputs**

- `banned`: A list of $m$ forbidden integers, where $1 \le m \le 10^5$ and each value is in $[1,n]$. Duplicate values are permitted.
- `n`: The inclusive upper bound of the candidate range, where $1 \le n \le 10^9$.
- `maxSum`: The largest permitted sum of selected values, where $1 \le \texttt{maxSum} \le 10^{15}$.

**Return value**

- The maximum number of distinct, non-banned integers that can be selected from $[1,n]$ without their sum exceeding `maxSum`.

### Examples

#### Example 1

- **Input:** `banned = [1, 4, 6], n = 6, maxSum = 4`
- **Output:** `1`
- **Explanation:** One valid choice is `3`. No two available positive integers have a total at most `4`.

#### Example 2

- **Input:** `banned = [4, 3, 5, 6], n = 7, maxSum = 18`
- **Output:** `3`
- **Explanation:** The allowed values `1`, `2`, and `7` have total `10`; the only other candidate values are banned.

#### Example 3

- **Input:** `banned = [2, 4], n = 6, maxSum = 12`
- **Output:** `3`
- **Explanation:** Selecting `1`, `3`, and `5` costs `9`. Adding the next allowed value `6` would exceed the budget.
