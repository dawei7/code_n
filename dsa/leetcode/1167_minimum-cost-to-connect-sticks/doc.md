# Minimum Cost to Connect Sticks

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1167 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Greedy, Heap (Priority Queue) |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-cost-to-connect-sticks/) |

## Problem Description

### Goal

You are given an array `sticks` of positive integers, where `sticks[i]` is the length of the $i$-th stick. Choose any two current sticks of lengths $x$ and $y$ and connect them into one stick of length $x+y$.

Each connection costs $x+y$, and the combined stick remains available for later connections. Continue until exactly one stick remains. Different choices change how often each length contributes to later costs, so return the minimum possible total cost of connecting all the original sticks into one.

### Function Contract

**Inputs**

- `sticks`: An array of $n$ positive stick lengths, where $1 \le n \le 10^4$ and $1 \le \texttt{sticks[i]} \le 10^4$.

**Return value**

- The minimum sum of all connection costs needed to leave one stick.

### Examples

**Example 1**

- Input: `sticks = [2,4,3]`
- Output: `14`

Connect lengths `2` and `3` for cost `5`, then connect `5` and `4` for cost `9`; the total is `14`.

**Example 2**

- Input: `sticks = [1,8,3,5]`
- Output: `30`

**Example 3**

- Input: `sticks = [5]`
- Output: `0`

No connection is needed when only one stick exists.
