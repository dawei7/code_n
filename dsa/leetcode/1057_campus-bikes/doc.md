# Campus Bikes

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1057 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Sorting, Heap (Priority Queue) |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [campus-bikes](https://leetcode.com/problems/campus-bikes/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/campus-bikes/).

### Goal
Assign one bike to each worker. The assignment process considers every worker-bike pair by increasing Manhattan distance, breaking ties by smaller worker index and then smaller bike index. When a pair is considered, it is used only if both that worker and that bike are still unassigned.

### Function Contract
**Inputs**

- `workers`: List of worker coordinates `[x, y]`.
- `bikes`: List of bike coordinates `[x, y]`.

**Return value**

List `answer` where `answer[i]` is the index of the bike assigned to worker `i`.

### Examples
**Example 1**

- Input: `workers = [[0, 0], [2, 1]], bikes = [[1, 2], [3, 3]]`
- Output: `[1, 0]`

**Example 2**

- Input: `workers = [[0, 0], [1, 1], [2, 0]], bikes = [[1, 0], [2, 2], [2, 1]]`
- Output: `[0, 2, 1]`

**Example 3**

- Input: `workers = [[0, 0]], bikes = [[2, 3]]`
- Output: `[0]`

---

## Solution
### Approach
Generate all worker-bike pairs with their Manhattan distance, worker index, and bike index. Sort these triples lexicographically. Then scan the sorted list, assigning a bike whenever both the worker and bike are still free.

Because the sort order exactly matches the required tie-breaking order, the first valid pair encountered for each worker is the correct assignment.

### Complexity Analysis
- **Time Complexity**: `O(w * b * log(w * b))`, where `w` is the number of workers and `b` is the number of bikes.
- **Space Complexity**: `O(w * b)` for the candidate pairs.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
