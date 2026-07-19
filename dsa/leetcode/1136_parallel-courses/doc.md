# Parallel Courses

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1136 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Graph Theory, Topological Sort |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/parallel-courses/) |

## Problem Description

### Goal

There are `n` courses labeled from `1` through `n`. Each unique pair `relations[i] = [prevCourse_i, nextCourse_i]` is a prerequisite relationship: `prevCourse_i` must be completed before `nextCourse_i` can be taken.

During one semester, you may take any number of courses whose prerequisites were all completed in previous semesters. Determine the minimum number of semesters needed to take every course. If the prerequisite relationships make it impossible to complete them all, return `-1`.

### Function Contract

**Inputs**

- `n`: the number of courses, with $1 \le n \le 5000$.
- `relations`: an array of $r$ distinct prerequisite pairs, where $1 \le r \le 5000$.
- Each pair is `[prevCourse_i, nextCourse_i]`, with both labels in $[1,n]$ and `prevCourse_i != nextCourse_i`.

Let $r=\lvert\texttt{relations}\rvert$.

**Return value**

The minimum number of semesters required to take every course, or `-1` when the prerequisite graph contains a cycle that prevents completion.

### Examples

**Example 1**

- Input: `n = 3, relations = [[1, 3], [2, 3]]`
- Output: `2`
- Explanation: Courses `1` and `2` can be taken together first, followed by course `3`.

**Example 2**

- Input: `n = 3, relations = [[1, 2], [2, 3], [3, 1]]`
- Output: `-1`
- Explanation: Each course in the cycle waits for another course in that same cycle.
