# Parallel Courses

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1136 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Graph Theory, Topological Sort |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [parallel-courses](https://leetcode.com/problems/parallel-courses/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/parallel-courses/).

### Goal
There are `n` courses and prerequisite relations. Each semester, any number of courses with all prerequisites already completed can be taken. Return the minimum number of semesters needed to finish all courses, or `-1` if a cycle makes completion impossible.

### Function Contract
**Inputs**

- `n`: Number of courses labeled `1` through `n`.
- `relations`: List of `[previous_course, next_course]` prerequisite edges.

**Return value**

Minimum number of semesters to complete every course, or `-1`.

### Examples
**Example 1**

- Input: `n = 3, relations = [[1, 3], [2, 3]]`
- Output: `2`

**Example 2**

- Input: `n = 3, relations = [[1, 2], [2, 3], [3, 1]]`
- Output: `-1`

**Example 3**

- Input: `n = 4, relations = [[1, 2], [1, 3], [3, 4]]`
- Output: `3`

---

## Solution
### Approach
Use topological BFS. Compute indegrees and start with all courses that have indegree `0`; those can be taken in semester `1`. For each semester, process the whole current queue, removing those courses and reducing indegrees of dependent courses.

If all courses are processed, the number of BFS layers is the answer. Otherwise, a cycle prevented some courses from ever reaching indegree `0`.

### Complexity Analysis
- **Time Complexity**: `O(n + r)`, where `r` is the number of relations.
- **Space Complexity**: `O(n + r)` for the graph, indegrees, and queue.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
