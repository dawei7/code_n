# Car Fleet

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 853 |
| Difficulty | Medium |
| Topics | Array, Stack, Sorting, Monotonic Stack |
| Official Link | [LeetCode](https://leetcode.com/problems/car-fleet/) |

## Problem Description
### Goal
There are $n$ cars traveling from distinct starting positions toward mile `target`. Arrays `position` and `speed` give each car's starting mile and constant speed. No car may pass another car. When a faster car catches a car or fleet ahead, they continue together at the minimum speed among their members.

A car fleet is either one car or cars traveling together. A catch that occurs exactly at `target` still joins the cars into one fleet. Return the number of distinct fleets that reach the destination.

### Function Contract
**Inputs**

- `target`: the destination mile, where $0 < \texttt{target} \leq 10^6$.
- `position`: $n$ unique starting positions satisfying $0 \leq \texttt{position[i]} < \texttt{target}$.
- `speed`: $n$ positive speeds paired by index with `position`, where $1 \leq n \leq 10^5$ and $0 < \texttt{speed[i]} \leq 10^6$.

**Return value**

Return the number of car fleets that arrive at `target`.

### Examples
**Example 1**

- Input: `target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]`
- Output: `3`

The cars at positions `10` and `8` meet at the target, the cars at `5` and `3` merge earlier, and the car at `0` remains alone.

**Example 2**

- Input: `target = 10, position = [3], speed = [3]`
- Output: `1`

**Example 3**

- Input: `target = 100, position = [0,2,4], speed = [4,2,1]`
- Output: `1`

The rear cars successively catch the slower car ahead.
