# Meeting Scheduler

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1229 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Two Pointers, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/meeting-scheduler/) |

## Problem Description

### Goal

Two people each provide a list of time slots during which they are available. A slot `[start, end]` can host a meeting beginning no earlier than `start` and finishing no later than `end`. Within either person's list, the slots do not overlap one another.

Given `slots1`, `slots2`, and a positive meeting `duration`, return the earliest time interval that lasts exactly `duration` and lies within one slot from each person. If no common availability is long enough, return an empty list.

### Function Contract

**Inputs**

- `slots1`: The first person's $n$ nonoverlapping availability intervals, where $1\le n\le10^4$.
- `slots2`: The second person's $m$ nonoverlapping availability intervals, where $1\le m\le10^4$.
- Every slot has two endpoints satisfying $0\le\texttt{start}<\texttt{end}\le10^9$.
- `duration`: The required meeting length, where $1\le\texttt{duration}\le10^6$.

**Return value**

- `[start, start + duration]` for the earliest feasible meeting, or `[]` when none exists.

### Examples

**Example 1**

- Input: `slots1 = [[10,50],[60,120],[140,210]]`, `slots2 = [[0,15],[60,70]]`, `duration = 8`
- Output: `[60,68]`

The first overlap lasts from `10` through `15`, which is too short. The overlap beginning at `60` can host eight time units.

**Example 2**

- Input: `slots1 = [[10,50],[60,120],[140,210]]`, `slots2 = [[0,15],[60,70]]`, `duration = 12`
- Output: `[]`

No shared interval lasts twelve time units.

**Example 3**

- Input: `slots1 = [[1,2]]`, `slots2 = [[3,4]]`, `duration = 1`
- Output: `[]`

### Required Complexity

- **Time:** $O(n\log n+m\log m)$
- **Space:** $O(n+m)$

<details>
<summary>Approach</summary>

#### General

**Put both schedules in chronological order.** Sort each list by interval start. Keeping sorted copies avoids changing the caller's inputs and makes the next possible overlap depend only on one current interval from each schedule.

**Measure the current intersection.** For intervals `[a, b]` and `[c, d]`, the shared portion begins at `max(a, c)` and ends at `min(b, d)`. If `end - start >= duration`, this is the earliest feasible overlap among all unprocessed slots, so return `[start, start + duration]` immediately.

**Discard the interval that ends first.** When the overlap is too short, whichever current interval has the smaller end cannot form a longer overlap with any later interval from the other sorted schedule: those later intervals start no earlier than the current opposing interval. Advance that interval's pointer; on equal ends, advancing either is safe.

Every interval discarded by this rule is proven unable to participate in a feasible earlier meeting. The pointers therefore examine all potentially useful pairs in chronological order, and the first returned intersection has the smallest possible start time. Exhausting either list proves no pair remains.

#### Complexity detail

Sorting costs $O(n\log n+m\log m)$ time, and the two pointers advance at most $n+m$ times. The sorted copies occupy $O(n+m)$ space.

#### Alternatives and edge cases

- **Compare every slot pair:** Testing all $nm$ intersections is correct but quadratic when both schedules are large.
- **Merge all endpoints:** A sweep-line event list can find common availability but uses more state than two pointers.
- **Touching endpoints:** An overlap of zero duration cannot host any positive `duration`.
- **Exact fit:** If `end - start == duration`, return that entire overlap.
- **Unsorted input:** Sorting is required before pointer advancement is valid.
- **Multiple feasible overlaps:** Return immediately at the first one in chronological pointer order.
- **No overlap:** Exhaustion of either schedule returns `[]`.

</details>
