# Find Lucky Integer in an Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1394 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/find-lucky-integer-in-an-array/) |

## Problem Description

### Goal

An integer is lucky in an array when its numeric value equals the number of times it occurs. For example, `3` is lucky only when the array contains exactly three occurrences of `3`.

Given an integer array `arr`, return the largest lucky integer it contains. Several different values may satisfy the frequency rule at the same time, so the numeric maximum determines the answer. If no array value has frequency equal to itself, return `-1`.

### Function Contract

**Inputs**

- `arr`: an integer array of length $n$, where $1 \le n \le 500$ and $1 \le \texttt{arr[i]} \le 500$.

Let $u$ be the number of distinct values in `arr`.

**Return value**

- The greatest value whose frequency equals that value, or `-1` if no such value exists.

### Examples

**Example 1**

- Input: `arr = [2,2,3,4]`
- Output: `2`

**Example 2**

- Input: `arr = [1,2,2,3,3,3]`
- Output: `3`

**Example 3**

- Input: `arr = [2,2,2,3,3]`
- Output: `-1`
