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

### Required Complexity

- **Time:** $O(n+m)$
- **Space:** $O(n+m)$

<details>
<summary>Approach</summary>

#### General

**Earliest finish as a DAG recurrence**

For each course `v`, its earliest start is the latest finish among all its prerequisites. Therefore its earliest finish equals its own duration plus that maximum; a course without prerequisites simply finishes after its own duration. This is a longest-path dynamic program on a DAG, where course durations are vertex weights.

**Processing prerequisites before dependents**

Build outgoing adjacency lists and indegrees. Initialize each course's finish value to its own duration and enqueue all zero-indegree courses. When a processed course reaches a dependent, use its finish time to improve the dependent's candidate finish, then decrement the dependent's indegree. An indegree of zero proves every prerequisite contribution has arrived, so the dependent can safely enter the queue.

Every feasible schedule must wait for the longest prerequisite chain ending at each course. Conversely, starting each course at the maximum prerequisite finish realizes exactly the computed time because unlimited parallel work is allowed. The maximum finish over all courses is thus both a lower bound on any schedule and an achievable completion time.

#### Complexity detail

Each of the $n$ courses enters the queue once, and each of the $m$ relations is examined once, giving $O(n+m)$ time. The adjacency lists, indegrees, finish values, and queue use $O(n+m)$ space.

#### Alternatives and edge cases

- **Memoized depth-first search:** Computing the longest path from prerequisites gives the same bound, but a long chain risks recursion-depth failure in Python.
- **Repeated edge relaxation:** Relaxing every relation until no value changes is correct for a DAG but may require $O(nm)$ time when edges are ordered against a long chain.
- With no prerequisite relations, every course starts immediately and the answer is `max(time)`, not the sum.
- Multiple prerequisites require the maximum of their finish times because they run in parallel; their durations are not added together.
- Course labels are one-based, whereas `time` and the implementation's graph arrays are zero-based.

</details>
