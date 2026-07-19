# Two City Scheduling

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1029 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Greedy, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/two-city-scheduling/) |

## Problem Description

### Goal

A company plans to interview `2n` people. For person `i`, `costs[i] = [aCost_i, bCost_i]` gives the price of flying that person to city A and city B, respectively.

Fly every person to exactly one city so that exactly `n` people arrive in city A and exactly `n` arrive in city B. Return the minimum possible total flight cost under this balance requirement.

### Function Contract

**Inputs**

- `costs`: an array containing $N=2n$ pairs `[aCost, bCost]`.
- $2 \le N \le 100$, $N$ is even, and every flight cost is between $1$ and $1000$, inclusive.

**Return value**

- The minimum total cost of assigning exactly $N/2$ people to each city.

### Examples

**Example 1**

- Input: `costs = [[10,20],[30,200],[400,50],[30,20]]`
- Output: `110`
- Explanation: Send the first two people to A for `10 + 30` and the other two to B for `50 + 20`.

**Example 2**

- Input: `costs = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]`
- Output: `1859`

**Example 3**

- Input: `costs = [[515,563],[451,713],[537,709],[343,819],[855,779],[457,60],[650,359],[631,42]]`
- Output: `3086`
