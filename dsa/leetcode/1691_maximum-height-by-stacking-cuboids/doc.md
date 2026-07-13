# Maximum Height by Stacking Cuboids

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1691 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [maximum-height-by-stacking-cuboids](https://leetcode.com/problems/maximum-height-by-stacking-cuboids/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/maximum-height-by-stacking-cuboids/).

### Goal
Each cuboid may be rotated. Stack cuboids so every dimension of an upper cuboid is no larger than the corresponding dimension of the cuboid below it, and maximize total height.

### Function Contract
**Inputs**

- `cuboids`: a list of three-dimensional cuboids.

**Return value**

Return the maximum achievable stack height.

### Examples
**Example 1**

- Input: `cuboids = [[50,45,20],[95,37,53],[45,23,12]]`
- Output: `190`

**Example 2**

- Input: `cuboids = [[38,25,45],[76,35,3]]`
- Output: `76`

**Example 3**

- Input: `cuboids = [[7,11,17],[7,17,11],[11,7,17],[11,17,7],[17,7,11],[17,11,7]]`
- Output: `102`

---

## Solution
### Approach
Sort the three dimensions inside each cuboid so the largest dimension can serve as height without losing generality. Then sort the cuboids lexicographically and run a longest-increasing-subsequence style DP: `dp[i]` is the best height ending with cuboid `i` on top of compatible earlier cuboids.

### Complexity Analysis
- **Time Complexity**: `O(n^2)`
- **Space Complexity**: `O(n)`

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
