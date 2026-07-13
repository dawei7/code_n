# Sort Items by Groups Respecting Dependencies

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1203 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Depth-First Search, Breadth-First Search, Graph Theory, Topological Sort |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [sort-items-by-groups-respecting-dependencies](https://leetcode.com/problems/sort-items-by-groups-respecting-dependencies/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/sort-items-by-groups-respecting-dependencies/).

### Goal
Sort items so every dependency appears before the item that depends on it, while items in the same group remain contiguous in the final order. Items with group `-1` should be treated as their own independent groups. Return an empty list if no valid order exists.

### Function Contract
**Inputs**

- `n`: Number of items labeled `0` through `n - 1`.
- `m`: Number of initial groups.
- `group`: `group[i]` is item `i`'s group, or `-1`.
- `beforeItems`: `beforeItems[i]` lists items that must appear before item `i`.

**Return value**

One valid ordering of all items, or `[]` if impossible.

### Examples
**Example 1**

- Input: `n = 8`, `m = 2`, `group = [-1,-1,1,0,0,1,0,-1]`, `beforeItems = [[],[6],[5],[6],[3,6],[],[],[]]`
- Output: `[6,3,4,1,5,2,0,7]`

**Example 2**

- Input: `n = 8`, `m = 2`, `group = [-1,-1,1,0,0,1,0,-1]`, `beforeItems = [[],[6],[5],[6],[3],[],[4],[]]`
- Output: `[]`

**Example 3**

- Input: `n = 3`, `m = 1`, `group = [0,0,0]`, `beforeItems = [[],[0],[1]]`
- Output: `[0,1,2]`

---

## Solution
### Approach
Assign a fresh group id to every item whose group is `-1`. Build two dependency graphs:

- An item graph for dependencies between individual items.
- A group graph for dependencies that cross group boundaries.

Topologically sort the groups. Also topologically sort items, then bucket sorted items by group. Emit groups in group topological order and append that group's items in item topological order. If either topological sort detects a cycle, return `[]`.

### Complexity Analysis
- **Time Complexity**: `O(n + m + e)`, where `e` is the total number of dependencies.
- **Space Complexity**: `O(n + m + e)`.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
