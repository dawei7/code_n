# Minimum Initial Energy to Finish Tasks

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1665 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Greedy, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-initial-energy-to-finish-tasks/) |

## Problem Description
### Goal
Each task is described by `[actual, minimum]`. You must have at least `minimum` energy immediately before starting that task, and completing it permanently consumes `actual` energy. For example, a `[10, 12]` task cannot start from 11 energy; starting from 13 leaves 3 afterward.

All tasks must be completed, but their order is yours to choose. Determine the smallest initial energy for which some ordering satisfies every start threshold and energy cost.

### Function Contract
**Inputs**

- `tasks`: an array of $n$ pairs `[actual, minimum]`, where $1 \le n \le 10^5$ and $1 \le \texttt{actual} \le \texttt{minimum} \le 10^4$.

**Return value**

Return the minimum initial energy that permits completion of every task in an optimally chosen order.

### Examples
**Example 1**

- Input: `tasks = [[1, 2], [2, 4], [4, 8]]`
- Output: `8`

Ordering the tasks as `[4, 8]`, `[2, 4]`, `[1, 2]` succeeds from 8.

**Example 2**

- Input: `tasks = [[1, 3], [2, 4], [10, 11], [10, 12], [8, 9]]`
- Output: `32`

**Example 3**

- Input: `tasks = [[1, 7], [2, 8], [3, 9], [4, 10], [5, 11], [6, 12]]`
- Output: `27`

### Required Complexity
- **Time:** $O(n\log n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Measure each task's reserved-energy gap.** The quantity `minimum - actual` is the energy that must remain available beyond the task's own cost when it begins at its threshold. A large gap is restrictive: postponing that task until energy has already been consumed can force a larger starting reserve.

**Order larger gaps first.** Sort tasks by `minimum - actual` in descending order. For two adjacent tasks $A=(a,m)$ and $B=(b,q)$, order $A,B$ requires at least $\max(m,a+q)$ energy at that boundary, while $B,A$ requires $\max(q,b+m)$. When $m-a \ge q-b$, placing $A$ first never makes the former bound larger than the latter. Repeatedly exchanging inverted adjacent pairs therefore transforms an optimal schedule into the sorted order without increasing its required energy.

**Simulate only the necessary top-ups.** Start with zero tracked energy and zero initial reserve. Before each sorted task, if current energy is below its minimum, increase both the initial reserve and current energy by exactly the deficit. Then subtract the actual cost. Each top-up is unavoidable for that fixed prefix, and adding only the deficit keeps the final initial amount minimal for the greedy order.

**Why the result is globally minimal.** The exchange argument proves that some globally optimal schedule follows the gap order. The simulation computes the least energy capable of executing that exact schedule because every added unit responds to a violated threshold and no unnecessary unit is introduced. Its accumulated reserve is therefore the minimum across all task orders.

#### Complexity detail

Sorting $n$ tasks costs $O(n\log n)$ time, and the simulation costs $O(n)$. The sorted task storage and language sorting workspace require $O(n)$ auxiliary space in the worst case.

#### Alternatives and edge cases

- **Backward requirement recurrence:** After sorting by the same gap, process the schedule backward with `required = max(minimum, required + actual)` in the corresponding orientation.
- **Quadratic selection:** Repeatedly scan the unscheduled tasks for the largest gap, then simulate it. This preserves correctness but costs $O(n^2)$ time.
- **Sort by minimum alone:** A high threshold paired with a high actual cost is not equivalent to a high reserved-energy gap and can produce a nonoptimal order.
- **Sort by actual cost alone:** Cost does not capture how much energy must be present before the task begins.
- A single task requires exactly its minimum energy.
- When `actual == minimum` for every task, initial energy must cover the sum of all actual costs.
- Equal-gap tasks may appear in any relative order without changing optimality.
- The answer can exceed every individual minimum because earlier tasks consume energy needed by later tasks.

</details>
