# Minimum Sideway Jumps

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1824 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming, Greedy |
| Official Link | [minimum-sideway-jumps](https://leetcode.com/problems/minimum-sideway-jumps/) |

## Problem Description & Examples
### Goal
A frog starts at point `0` in lane `2` and wants to reach the final point. It may move forward in the same lane unless blocked, or make side jumps at the same point to another unblocked lane. Find the fewest side jumps.

### Function Contract
**Inputs**

- `obstacles`: an array where `obstacles[i]` is the blocked lane at point `i`, or `0` if no lane is blocked.

**Return value**

Return the minimum number of side jumps needed to reach the end.

### Examples
**Example 1**

- Input: `obstacles = [0,1,2,3,0]`
- Output: `2`

**Example 2**

- Input: `obstacles = [0,1,1,3,3,0]`
- Output: `0`

**Example 3**

- Input: `obstacles = [0,2,1,0,3,0]`
- Output: `2`

---

## Underlying Base Algorithm(s)
Keep the minimum side jumps needed to stand in each of the three lanes at the current point. At each position, mark a blocked lane as impossible. Then relax side jumps among the remaining lanes: any unblocked lane can be reached from another unblocked lane with one extra side jump.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)`
