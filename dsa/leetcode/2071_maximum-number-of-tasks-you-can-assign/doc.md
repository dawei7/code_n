# Maximum Number of Tasks You Can Assign

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2071 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Two Pointers, Binary Search, Greedy, Queue, Sorting, Monotonic Queue |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-number-of-tasks-you-can-assign/) |

## Problem Description

### Goal

There are $n$ tasks with individual strength requirements and $m$ workers with individual strengths. A worker can complete a task when the worker's strength is at least its requirement. Each task and each worker may participate in at most one assignment.

Up to `pills` workers may each receive one magical pill. A pill increases that worker's strength by exactly `strength` for the assignment; no worker may take more than one pill. Pills need not all be used.

Choose the assignments and pill recipients to maximize the number of completed tasks. Return that maximum count, including zero when no task can be matched.

### Function Contract

**Inputs**

- `tasks`: an array of $n$ task requirements, where $1 \le n \le 5\cdot10^4$.
- `workers`: an array of $m$ worker strengths, where $1 \le m \le 5\cdot10^4$.
- `pills`: the available pill count, where $0 \le \texttt{pills}\le m$.
- `strength`: the nonnegative strength added by one pill.

Every task requirement, worker strength, and `strength` lies between $0$ and $10^9$. Let $r=\min(n,m)$.

**Return value**

- Return the greatest number of one-to-one task-worker assignments achievable under the pill rules.

### Examples

**Example 1**

- Input: `tasks = [3,2,1], workers = [0,3,3], pills = 1, strength = 1`
- Output: `3`
- Explanation: Boost worker `0` to complete task `1`; the two strength-`3` workers complete requirements `2` and `3`.

**Example 2**

- Input: `tasks = [5,4], workers = [0,0,0], pills = 1, strength = 5`
- Output: `1`
- Explanation: One boosted worker can complete one task, but only one pill is available.

**Example 3**

- Input: `tasks = [10,15,30], workers = [0,10,10,10,10], pills = 3, strength = 10`
- Output: `2`
- Explanation: Two boosted workers can meet requirements `10` and `15`; no worker can reach `30`.

### Required Complexity

- **Time:** $O(n\log n+m\log m+r\log r)$
- **Space:** $O(r)$

<details>
<summary>Approach</summary>

#### General

**Binary-search a monotone assignment count**

Sort both arrays. If $k$ tasks can be assigned, then any smaller number can also be assigned by discarding assignments. To test $k$, only the $k$ easiest tasks and $k$ strongest workers can improve feasibility. Binary-search the greatest feasible $k$ between zero and $r$.

**Match workers while preserving scarce options**

Process the selected workers from weakest to strongest. Before handling a worker, append every still-unconsidered selected task whose requirement is at most `worker + strength` to a deque. These are exactly the remaining tasks this worker could perform with a pill.

If the deque's easiest task requires no pill, assign that front task: spending a pill would be unnecessary, and saving harder tasks cannot hurt stronger later workers. Otherwise a pill is mandatory, so spend one and assign the hardest task at the deque's back. Using the boosted worker on that hardest reachable task preserves easier work for later unboosted assignments. An empty deque or exhausted pill supply makes $k$ infeasible.

The selected tasks and workers are optimal candidates by sorted dominance. At each worker, the no-pill choice consumes the least demanding feasible task, while the pill choice consumes the most demanding task that this weaker worker can rescue. Standard exchange arguments replace any feasible assignment's choice with these choices without reducing what later, stronger workers can do. Thus the predicate accepts exactly feasible counts, and binary search returns the maximum.

#### Complexity detail

Sorting costs $O(n\log n+m\log m)$. One feasibility check processes at most $r$ tasks and workers in $O(r)$ time, and binary search performs $O(\log r)$ checks, for $O(n\log n+m\log m+r\log r)$ total time. A check's deque holds at most $r$ requirements, using $O(r)$ auxiliary space.

#### Alternatives and edge cases

- **Ordered multiset feasibility:** Remove the weakest unboosted candidate or weakest pill-eligible candidate with balanced-tree operations; this is correct but adds a logarithmic factor per assignment.
- **Linear-list front removal:** The same greedy choices remain correct, but repeatedly shifting the candidate list can make a check quadratic.
- **Try every matching:** Exhaustive assignment and pill choices grow combinatorially and are infeasible at the input limits.
- The $k$ easiest tasks, not an arbitrary $k$, must be tested for a candidate count.
- The $k$ strongest workers dominate every other size-$k$ worker subset.
- A pill with `strength == 0` cannot create any new feasible pairing, though it may remain unused.
- Workers that already meet a requirement should not consume scarce pills.
- Zero-strength workers can complete zero-requirement tasks without pills.
- Extra workers or tasks do not force assignments; the answer is at most $r$.

</details>
