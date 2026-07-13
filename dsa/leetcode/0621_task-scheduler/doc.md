# Task Scheduler

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 621 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Greedy, Sorting, Heap (Priority Queue), Counting |
| Official Link | [LeetCode](https://leetcode.com/problems/task-scheduler/) |

## Problem Description
### Goal
You are given an array of CPU tasks labeled with uppercase letters from `A` through `Z` and a nonnegative integer `n`. Each CPU interval can either complete one task or remain idle, and the tasks may be completed in any order.

Schedule every task using the minimum number of CPU intervals. Between two tasks with the same label, there must be a gap of at least `n` complete intervals, which may contain other tasks or idle time. Count both working and forced-idle intervals in the returned schedule length.

### Function Contract
**Inputs**

- `tasks`: uppercase task identifiers; each list entry is one required execution
- `n`: the nonnegative cooldown between equal task types

**Return value**

- The minimum schedule length, including any forced idle intervals
- Different task types may run in any order

### Examples
**Example 1**

- Input: `tasks = ["A","A","A","B","B","B"]`, `n = 2`
- Output: `8`

**Example 2**

- Input: `tasks = ["A","A","A","B","B","B"]`, `n = 0`
- Output: `6`

**Example 3**

- Input: `tasks = ["A","A","A","B","B","B"]`, `n = 1`
- Output: `6`

### Required Complexity

- **Time:** $O(T)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Let the most frequent tasks define the skeleton**

Count the 26 task types. Let `maximum` be the largest frequency and let `leaders` be the number of task types attaining it. Place the first `maximum - 1` copies of one leading type at the starts of frames. Consecutive starts must be $n + 1$ intervals apart, so these frames require `(maximum - 1) * (n + 1)` positions.

**Account for the final leading copies**

Every type tied for maximum frequency still has one last copy after those complete frames. Appending the `leaders` final copies gives the frame lower bound `(maximum - 1) * (n + 1) + leaders`.

**Why the task count is the other bound**

No schedule can use fewer intervals than there are tasks. When enough other task types exist to fill every frame gap, the schedule has no idle time and its length is exactly `T = len(tasks)`, which may exceed the frame expression.

**Why the larger bound is achievable**

Arrange the leading task types across the frame boundaries, then place all remaining tasks into the open positions between them. If they fill or overflow the gaps, every interval is a task and length is `T`. If they do not, the unfilled positions are exactly the forced idles represented by the frame bound. Thus `max(T, frame_bound)` is both necessary and attainable.

#### Complexity detail

Counting `T` tasks takes $O(T)$ time. Finding the maximum and its number of ties scans a fixed array of 26 counts. That fixed alphabet uses $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Heap plus cooldown queue:** simulate a greedy schedule by repeatedly running the most frequent available type; it is constructive and correct but costs $O(answer \log K)$ for `K` task types and may step through many idle intervals.
- **Sort the 26 frequencies:** the same frame formula can use sorted counts, but sorting a fixed alphabet adds no practical value.
- With $n = 0$, no idle is required and the answer is always the task count.
- A single task finishes in one interval regardless of cooldown.
- Several types tied for maximum frequency all occupy the final frame and must all be included in `leaders`.
- A large variety of less frequent tasks can eliminate every otherwise idle slot.
- A single repeated type forces exactly `n` idle intervals between consecutive executions.

</details>
