# Parallel Courses III

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2050 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Graph Theory, Topological Sort |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [parallel-courses-iii](https://leetcode.com/problems/parallel-courses-iii/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/parallel-courses-iii/).

### Goal
Courses have durations and prerequisite relations. Any number of available courses can be taken in parallel; find the earliest month when all courses can be completed.

### Function Contract
**Inputs**

- `n`: number of courses labeled `1` through `n`.
- `relations`: prerequisite pairs `[prev, next]`.
- `time`: duration of each course.

**Return value**

Return the minimum total months needed to finish every course.

### Examples
**Example 1**

- Input: `n = 3, relations = [[1,3],[2,3]], time = [3,2,5]`
- Output: `8`

**Example 2**

- Input: `n = 5, relations = [[1,5],[2,5],[3,5],[3,4],[4,5]], time = [1,2,3,4,5]`
- Output: `12`

**Example 3**

- Input: `n = 2, relations = [], time = [5,7]`
- Output: `7`

---

## Solution
### Approach
Run topological DP over the prerequisite DAG. Each course's earliest finish time is its duration plus the maximum earliest finish among its prerequisites. The answer is the maximum finish time.

### Complexity Analysis
- **Time Complexity**: `O(n + relations.length)`
- **Space Complexity**: `O(n + relations.length)`

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
