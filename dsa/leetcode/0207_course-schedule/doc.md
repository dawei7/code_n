# Course Schedule

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 207 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Depth-First Search, Breadth-First Search, Graph Theory, Topological Sort |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/course-schedule/) |

## Problem Description
### Goal
There are `num_courses` courses labeled from `0` through `num_courses - 1`. Each pair `[course, prerequisite]` states that the prerequisite course must be completed before the listed course can be taken, and a course may depend on several others.

Return `True` when some ordering can complete every course while respecting all prerequisite relationships. Return `False` when a directed dependency cycle, including a self-dependency, makes completion impossible. Courses with no dependencies may appear anywhere permitted by the remaining constraints, and disconnected groups must all be feasible; the task asks only whether an ordering exists, not to return one.

### Function Contract
**Inputs**

- `num_courses`: courses labeled from zero through `num_courses - 1`
- `prerequisites`: pairs `[course, prerequisite]`

**Return value**

`True` when the directed prerequisite graph has an ordering containing every course; otherwise `False`.

### Examples
**Example 1**

- Input: `2, [[1,0]]`
- Output: `True`

**Example 2**

- Input: `2, [[1,0],[0,1]]`
- Output: `False`

**Example 3**

- Input: `3, []`
- Output: `True`
