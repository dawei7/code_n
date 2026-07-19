# Daily Temperatures

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 739 |
| Difficulty | Medium |
| Topics | Array, Stack, Monotonic Stack |
| Official Link | [LeetCode](https://leetcode.com/problems/daily-temperatures/) |

## Problem Description
### Goal
Given an array `temperatures` representing consecutive daily temperatures, determine for each day how long you must wait until a future day with a warmer temperature.

Return an array of the same length where `answer[i]` is the smallest positive number of days to a later index `j` with `temperatures[j] > temperatures[i]`. If no future day is strictly warmer, store `0` at that position. An equal temperature does not end the wait.

### Function Contract
**Inputs**

- `temperatures`: an ordered list of daily integer temperatures

**Return value**

- A list of the same length where position $i$ stores the smallest positive $j-i$ with `temperatures[j] > temperatures[i]`, or `0` when no such $j$ exists

### Examples
**Example 1**

- Input: `temperatures = [73,74,75,71,69,72,76,73]`
- Output: `[1,1,4,2,1,1,0,0]`

**Example 2**

- Input: `temperatures = [30,40,50,60]`
- Output: `[1,1,1,0]`

**Example 3**

- Input: `temperatures = [30,60,90]`
- Output: `[1,1,0]`
