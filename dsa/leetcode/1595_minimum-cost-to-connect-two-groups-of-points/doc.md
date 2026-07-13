# Minimum Cost to Connect Two Groups of Points

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1595 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Bit Manipulation, Matrix, Bitmask |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [minimum-cost-to-connect-two-groups-of-points](https://leetcode.com/problems/minimum-cost-to-connect-two-groups-of-points/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/minimum-cost-to-connect-two-groups-of-points/).

### Goal
Connect every point in each of two groups to at least one point in the other
group while minimizing total connection cost.

### Function Contract
**Inputs**

- `cost`: a matrix where `cost[i][j]` is the cost to connect group-one point
  `i` to group-two point `j`.

**Return value**

The minimum total cost needed to satisfy both groups.

### Examples
**Example 1**

- Input: `cost = [[15, 96], [36, 2]]`
- Output: `17`

**Example 2**

- Input: `cost = [[1, 3, 5], [4, 1, 1], [1, 5, 3]]`
- Output: `4`

**Example 3**

- Input: `cost = [[2, 5, 1], [3, 4, 7], [8, 1, 2], [6, 2, 4]]`
- Output: `10`

---

## Solution
### Approach
Use dynamic programming over rows of the first group and a bitmask of which
second-group points have been connected. For each first-group point, try
connecting it to every second-group point. After all first-group points are
processed, add the cheapest missing connection for any second-group point not in
the mask.

### Complexity Analysis
- **Time Complexity**: `O(m * n * 2^n)`, where `n` is the second group size.
- **Space Complexity**: `O(2^n)`.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
