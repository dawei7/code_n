# Minimum Operations to Collect Elements

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2869 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, Bit Manipulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Minimum Operations to Collect Elements](https://leetcode.com/problems/minimum-operations-to-collect-elements/) |

## Problem Description

### Goal

You are given an array `nums` of positive integers and an integer `k`. One operation removes the last element of the current array and places that value in your collection. Because removal always happens at the end, the values are collected by scanning the original array from right to left.

Determine the minimum number of operations required before the collection contains every integer from $1$ through $k$. Values outside that target range may still have to be removed, and collecting a duplicate target value does not replace any missing value. The input guarantees that all required values can eventually be collected.

### Function Contract

**Inputs**

- `nums`: A nonempty list of positive integers.
- `k`: The inclusive upper bound of the target values that must be collected.

Let $n = \lvert\texttt{nums}\rvert$. The constraints are $1 \le n \le 50$, $1 \le \texttt{nums[i]} \le n$, and $1 \le k \le n$. Every integer in $\{1, 2, \ldots, k\}$ occurs in `nums`.

**Return value**

- The minimum number of removals from the end of `nums` needed to collect all integers from $1$ through $k$.

### Examples

**Example 1**

- Input: `nums = [3,1,5,4,2], k = 2`
- Output: `4`
- Explanation: The removed values are `2`, `4`, `5`, and `1`. At that point both required values, `1` and `2`, have been collected.

**Example 2**

- Input: `nums = [3,1,5,4,2], k = 5`
- Output: `5`
- Explanation: Every array element must be removed before the collection contains all values from `1` through `5`.

**Example 3**

- Input: `nums = [3,2,5,3,1], k = 3`
- Output: `4`
- Explanation: Removing `1`, `3`, `5`, and `2` collects every required value; the irrelevant `5` still counts as an operation.
