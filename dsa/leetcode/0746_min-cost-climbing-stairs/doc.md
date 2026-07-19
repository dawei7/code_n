# Min Cost Climbing Stairs

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 746 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/min-cost-climbing-stairs/) |

## Problem Description

### Goal

Given an integer array `cost`, `cost[i]` is the price paid when you step on stair `i`. After paying that cost, you may climb either one step or two steps.

You may begin on stair `0` or stair `1`. Return the minimum total cost needed to reach the top of the floor, which lies just beyond the final indexed stair. You do not pay a separate cost for the top itself, and you may choose different one- and two-step moves along the route.

### Function Contract

**Inputs**

- `cost`: a list of non-negative integers, where `cost[i]` is charged when stair `i` is used.

**Return value**

- The minimum cost of reaching the virtual top immediately after the array.

### Examples

**Example 1**

- Input: `cost = [10, 15, 20]`
- Output: `15`
- Explanation: Start on stair `1`, pay `15`, and jump two positions to the top.

**Example 2**

- Input: `cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]`
- Output: `6`
- Explanation: Choosing the inexpensive stairs avoids every cost of `100`.
