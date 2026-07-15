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

### Required Complexity

- **Time:** $O(n+r)$
- **Space:** $O(n+r)$

<details>
<summary>Approach</summary>

#### General

**Model eligibility with in-degrees.** Build a directed adjacency list from every prerequisite to the courses that depend on it. For each course, its in-degree counts prerequisites not yet completed. Courses whose initial in-degree is zero can all be taken in the first semester.

**Process one complete semester at a time.** Put all currently eligible courses in a queue. At the start of each loop, record the queue length: exactly those courses form the present semester, because courses unlocked while processing them cannot be taken until a later semester. Remove that entire layer, count each course as completed, and decrement the in-degree of every dependent course. When a dependent reaches zero, enqueue it for the next layer.

Every valid schedule must place a course after each of its prerequisites. Thus the number of semesters is at least the number of vertices on the longest prerequisite chain. Layered topological processing assigns every course the earliest semester allowed by all incoming relationships, so it meets that lower bound and is minimal.

**Use the processed count to expose cycles.** An acyclic directed graph always has an in-degree-zero course, so the queue processes all `n` courses. If the queue empties early, every remaining subgraph vertex has an unresolved incoming prerequisite; those vertices include a directed cycle. Return `-1` instead of the accumulated layer count.

#### Complexity detail

Building the graph takes $O(n+r)$ time and space. Each course enters and leaves the queue once, and each prerequisite relationship is traversed once, for total time $O(n+r)$. The adjacency list, in-degrees, and queue together use $O(n+r)$ space.

#### Alternatives and edge cases

- **Depth-first longest-path calculation:** Memoized DFS can compute the longest prerequisite chain while detecting recursion-stack cycles in $O(n+r)$ time, but a chain of up to `5000` courses requires care with recursion depth.
- **Repeated eligibility scans:** Rescanning every course after each semester is correct, but a chain makes it spend $O(n^2+r)$ time.
- **Directed cycle:** No member of a cycle can become eligible solely by completing courses outside that cycle, so the result is `-1`.
- **Independent courses:** Courses with no incoming relationships are all taken in the earliest semester, even when they belong to separate graph components.
- **Multiple prerequisites:** A course enters the queue only when its last unresolved prerequisite is completed; reaching one prerequisite is insufficient.
- **Parallel availability:** Every course already in the queue at the start of a layer belongs to the same semester, while newly unlocked courses wait for the next one.

</details>
