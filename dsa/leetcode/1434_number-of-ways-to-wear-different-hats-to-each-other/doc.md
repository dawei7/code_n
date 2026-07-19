# Number of Ways to Wear Different Hats to Each Other

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1434 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Bit Manipulation, Bitmask |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/number-of-ways-to-wear-different-hats-to-each-other/) |

## Problem Description

### Goal

A group of people is choosing hats numbered from `1` through `40`. For each person `i`, `hats[i]` lists exactly the hat numbers that person is willing to wear.

Count the assignments in which every person receives exactly one liked hat and no two people receive the same hat. Two assignments are different when at least one person receives a different hat. Because the count can be large, return it modulo $1{,}000{,}000{,}007$.

### Function Contract

**Inputs**

- `hats`: a list of $p$ preference lists, where $1 \le p \le 10$.
- Each `hats[i]` contains between $1$ and $40$ distinct integers from $1$ through $40$.

**Return value**

- The number of valid one-liked-hat-per-person assignments with all assigned hats distinct, modulo $1{,}000{,}000{,}007$.

### Examples

**Example 1**

- Input: `hats = [[3,4],[4,5],[5]]`
- Output: `1`

**Example 2**

- Input: `hats = [[3,5,1],[3,5]]`
- Output: `4`

**Example 3**

- Input: `hats = [[1,2,3],[2,3,5],[1,3,5]]`
- Output: `11`
