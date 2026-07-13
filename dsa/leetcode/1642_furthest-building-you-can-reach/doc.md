# Furthest Building You Can Reach

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1642 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Greedy, Heap (Priority Queue) |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [furthest-building-you-can-reach](https://leetcode.com/problems/furthest-building-you-can-reach/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/furthest-building-you-can-reach/).

### Goal
Move across buildings from left to right using bricks for climbs and ladders for
some climbs. Return the furthest reachable index.

### Function Contract
**Inputs**

- `heights`: building heights.
- `bricks`: total bricks available.
- `ladders`: total ladders available.

**Return value**

The furthest building index that can be reached.

### Examples
**Example 1**

- Input: `heights = [4, 2, 7, 6, 9, 14, 12], bricks = 5, ladders = 1`
- Output: `4`

**Example 2**

- Input: `heights = [4, 12, 2, 7, 3, 18, 20, 3, 19], bricks = 10, ladders = 2`
- Output: `7`

**Example 3**

- Input: `heights = [14, 3, 19, 3], bricks = 17, ladders = 0`
- Output: `3`

---

## Solution
### Approach
Use ladders for the largest climbs and bricks for smaller climbs. As you scan,
push every positive climb into a min-heap. If the heap size exceeds the number
of ladders, pay bricks for the smallest climb in the heap. When bricks become
negative, the previous building is the furthest reachable.

### Complexity Analysis
- **Time Complexity**: `O(n log l)`, where `l` is the number of ladders.
- **Space Complexity**: `O(l)`.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
