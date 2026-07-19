# Minimum Number of Work Sessions to Finish the Tasks

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1986 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming, Backtracking, Bit Manipulation, Bitmask |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-number-of-work-sessions-to-finish-the-tasks/) |

## Problem Description
### Goal
You must complete `n` tasks whose durations are listed in `tasks`. Work is
divided into sessions, each lasting at most `sessionTime` hours before a break.
Once a task starts, it must finish within that same session; tasks cannot be
split across breaks, although multiple tasks may be completed consecutively in
one session.

The tasks may be performed in any order. Assign every task to a session without
exceeding the per-session time limit, and return the minimum number of sessions
needed. Every individual task is guaranteed to fit within one session.

### Function Contract
**Inputs**

- `tasks`: a list of $N$ positive task durations, where $1 \le N \le 14$ and
  $1 \le \texttt{tasks[i]} \le 10$.
- `sessionTime`: the capacity $S$ of each session, where
  $\max(\texttt{tasks}) \le S \le 15$.

**Return value**

- The minimum number of capacity-$S$ sessions that can contain all tasks,
  assigning each task wholly to exactly one session.

### Examples
**Example 1**

- Input: `tasks = [1, 2, 3], sessionTime = 3`
- Output: `2`

Tasks `1` and `2` share one session, while task `3` uses another.

**Example 2**

- Input: `tasks = [3, 1, 3, 1, 1], sessionTime = 8`
- Output: `2`

Four tasks totaling `8` can share the first session.

**Example 3**

- Input: `tasks = [1, 2, 3, 4, 5], sessionTime = 15`
- Output: `1`

### Required Complexity
- **Time:** $O(N2^N)$
- **Space:** $O(2^N)$

<details>
<summary>Approach</summary>

#### General

**Represent completed tasks with a bitmask**

Assign one bit to every task. A mask records exactly which tasks have already
been scheduled, allowing all execution orders that reach the same completed
set to share one dynamic-programming state. For each mask, store a pair:
the number of sessions opened and the amount of time used in the current
session.

Initialize the empty mask as `(1, 0)`. The first session is available but still
empty; because at least one task exists, this convention makes the final
session count direct.

**Extend a state by one unfinished task**

For every task absent from a mask, place it in the current session when its
duration fits. Otherwise, open one new session and make that task its first
occupant. This produces a candidate pair for the mask with that task added.

Compare candidates lexicographically: fewer sessions is always better, and
among schedules using the same number of sessions, a smaller current load is
better because it leaves at least as much capacity for every future task.

**Why one pair per mask is sufficient**

Consider two schedules that complete the same set of tasks. If one uses fewer
sessions, it dominates immediately. If they use the same number but one has a
smaller current load, every continuation feasible from the fuller session is
also feasible from the emptier one. Therefore the lexicographically smallest
pair preserves an optimal continuation for each mask.

Every full task order appears along some sequence of transitions. Since only
dominated partial schedules are discarded, the pair for the all-task mask has
the globally minimum session count.

#### Complexity detail

There are $2^N$ masks, and each mask considers at most $N$ task transitions,
for $O(N2^N)$ time. The table stores one constant-size pair for every mask,
using $O(2^N)$ space.

#### Alternatives and edge cases

- **Backtracking into explicit sessions:** Place tasks one by one while pruning
  symmetric session loads. This can be effective for $N \le 14$ but retains an
  exponential worst case and requires careful duplicate-state pruning.
- **Enumerate task orders:** Next-fit packing across every permutation is
  correct when minimized over all orders, but costs $O(N! \cdot N)$ time.
- **Enumerate feasible session subsets:** Precompute which masks fit in one
  session and cover the full mask with them. A direct submask transition can
  take $O(3^N)$ time.
- A task whose duration equals `sessionTime` must occupy a session by itself.
- If all task durations sum to at most `sessionTime`, the answer is `1`.
- Equal task durations still represent distinct tasks and therefore distinct
  mask bits.
- The lower bound
  $\left\lceil \sum \texttt{tasks[i]} / \texttt{sessionTime} \right\rceil$
  is useful for reasoning but may be unattainable because tasks cannot split.

</details>
