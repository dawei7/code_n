# Course Schedule II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 210 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Depth-First Search, Breadth-First Search, Graph Theory, Topological Sort |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/course-schedule-ii/) |

## Problem Description
### Goal
There are `num_courses` courses labeled from `0` through `num_courses - 1`. Every prerequisite pair `[course, prerequisite]` requires the second course to occur before the first, and courses can belong to separate dependency groups or have multiple prerequisites.

Return any ordering containing every course exactly once and satisfying all dependency relationships. Several valid orders may exist, and any one is acceptable. If a directed cycle or self-dependency prevents completion of the full course set, return an empty list rather than a partial schedule. Courses with no prerequisites still need to appear somewhere in every successful result.

### Function Contract
**Inputs**

- `num_courses`: courses labeled from zero through `num_courses - 1`
- `prerequisites`: pairs `[course, prerequisite]`

**Return value**

Any valid ordering containing every course, or an empty list when no such ordering exists.

### Examples
**Example 1**

- Input: `2, [[1,0]]`
- Output: `[0,1]`

**Example 2**

- Input contains a directed cycle
- Output: `[]`

**Example 3**

- Input: `3, []`
- Output: any permutation of all three courses
