# Map of Highest Peak

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1765 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Breadth-First Search, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [map-of-highest-peak](https://leetcode.com/problems/map-of-highest-peak/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/map-of-highest-peak/).

### Goal
Assign a non-negative height to every cell so all water cells have height `0`, neighboring cells differ by at most `1`, and the maximum height is as large as possible.

### Function Contract
**Inputs**

- `isWater`: a binary matrix where `1` marks water and `0` marks land.

**Return value**

Return a height matrix satisfying the rules and maximizing the highest land height.

### Examples
**Example 1**

- Input: `isWater = [[0,1],[0,0]]`
- Output: `[[1,0],[2,1]]`

**Example 2**

- Input: `isWater = [[0,0,1],[1,0,0],[0,0,0]]`
- Output: `[[1,1,0],[0,1,1],[1,2,2]]`

**Example 3**

- Input: `isWater = [[1]]`
- Output: `[[0]]`

---

## Solution
### Approach
Run multi-source BFS from every water cell at height `0`. Each unvisited neighbor receives height `current + 1` the first time it is reached. BFS distance from the nearest water cell gives the maximum valid height assignment.

### Complexity Analysis
- **Time Complexity**: `O(m * n)`
- **Space Complexity**: `O(m * n)`

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
