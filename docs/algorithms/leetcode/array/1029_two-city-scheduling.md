# Two City Scheduling

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1029 |
| Difficulty | Medium |
| Topics | Array, Greedy, Sorting |
| Official Link | [two-city-scheduling](https://leetcode.com/problems/two-city-scheduling/) |

## Problem Description & Examples
### Goal
There are `2n` people and two cities. Each person has a cost for city A and city B. Send exactly `n` people to each city with minimum total cost.

### Function Contract
**Inputs**

- `costs`: List[List[int]] where each item is `[costA, costB]`

**Return value**

int - minimum total assignment cost

### Examples
**Example 1**

- Input: `costs = [[10,20],[30,200],[400,50],[30,20]]`
- Output: `110`

**Example 2**

- Input: `costs = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]`
- Output: `1859`

**Example 3**

- Input: `costs = [[515,563],[451,713],[537,709],[343,819],[855,779],[457,60],[650,359],[631,42]]`
- Output: `3086`

---

## Underlying Base Algorithm(s)
Greedy sorting by relative savings.

---

## Complexity Analysis
- **Time Complexity**: `O(n log n)`
- **Space Complexity**: `O(1)` auxiliary space if sorting in place
