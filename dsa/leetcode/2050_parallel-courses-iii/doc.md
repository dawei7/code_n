# Parallel Courses III

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2050 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Graph Theory, Topological Sort |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/parallel-courses-iii/) |

## Problem Description

### Goal

There are $n$ courses labeled from $1$ through $n$. Each pair `[previous, next]` in `relations` means that `previous` must be completed before `next` may begin, and `time[i]` gives the number of months required for course `i + 1`.

A course may start at any time once all its prerequisites are finished, and there is no limit on how many eligible courses can run concurrently. The prerequisite graph is guaranteed to be a directed acyclic graph, so every course can eventually be completed. Determine the minimum number of months needed to finish all courses under an optimal parallel schedule.

### Function Contract

**Inputs**

- `n`: the number of courses, with $1 \le n \le 5 \cdot 10^4$.
- `relations`: up to $5 \cdot 10^4$ unique prerequisite pairs `[previous, next]`, using labels from $1$ through $n$ and forming a directed acyclic graph.
- `time`: an array of length $n$, where `time[i]` is between $1$ and $10^4$ months.

Let $m$ be `relations.length`.

**Return value**

- Return the earliest month by which every course can be completed.

### Examples

**Example 1**

- Input: `n = 3, relations = [[1,3],[2,3]], time = [3,2,5]`
- Output: `8`
- Explanation: Courses `1` and `2` start together. Course `3` waits until month $3$ and then requires five more months.

**Example 2**

- Input: `n = 5, relations = [[1,5],[2,5],[3,5],[3,4],[4,5]], time = [1,2,3,4,5]`
- Output: `12`
- Explanation: The critical sequence is course `3`, then `4`, then `5`, with total duration $3+4+5=12$.
