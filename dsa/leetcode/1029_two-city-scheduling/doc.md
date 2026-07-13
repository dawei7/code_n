# Two City Scheduling

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1029 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Greedy, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [two-city-scheduling](https://leetcode.com/problems/two-city-scheduling/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/two-city-scheduling/).

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

## Solution
### Approach
Greedy sorting by relative savings.

### Complexity Analysis
- **Time Complexity**: `O(n log n)`
- **Space Complexity**: `O(1)` auxiliary space if sorting in place

### Reference Implementations
<details>
<summary>python</summary>

```python
"""Optimal solution for LeetCode 1029: Two City Scheduling."""


def solve(costs: list[list[int]]) -> int:
    costs.sort(key=lambda cost: cost[0] - cost[1])
    half = len(costs) // 2
    return sum(cost[0] for cost in costs[:half]) + sum(cost[1] for cost in costs[half:])
```
</details>
